#!/usr/bin/env python3
"""Original soft-upbeat bed. Synthesized in numpy; no samples, no downloads."""
from __future__ import annotations

import math
import wave
from pathlib import Path

import numpy as np

SR = 44100
RNG = np.random.default_rng(20261113)  # deterministic original piece


def midi(n: float) -> float:
    return 440.0 * (2.0 ** ((n - 69) / 12.0))


def env_adsr(n, attack=0.01, decay=0.12, sustain=0.35, release=0.25, sr=SR):
    a = max(1, int(attack * sr))
    d = max(1, int(decay * sr))
    r = max(1, int(release * sr))
    s = max(0, n - a - d - r)
    e = np.concatenate(
        [
            np.linspace(0, 1, a, endpoint=False),
            np.linspace(1, sustain, d, endpoint=False),
            np.full(s, sustain, dtype=np.float64),
            np.linspace(sustain, 0, r, endpoint=True) if r else np.array([], dtype=np.float64),
        ]
    )
    if len(e) < n:
        e = np.pad(e, (0, n - len(e)))
    return e[:n]


def fade_io(x, fin=1.0, fout=1.6, sr=SR):
    n = len(x)
    a = min(n, int(fin * sr))
    b = min(n, int(fout * sr))
    if a:
        x[:a] *= np.linspace(0, 1, a)
    if b:
        x[-b:] *= np.linspace(1, 0, b)
    return x


def osc(freq, n, kind="sine", phase=0.0):
    t = (np.arange(n) / SR) * (2 * np.pi * freq) + phase
    if kind == "sine":
        return np.sin(t)
    if kind == "tri":
        # band-limited-ish triangle via 7 odd harmonics
        y = np.zeros(n)
        for k, sgn in enumerate((1, -1, 1, -1, 1, -1, 1), start=1):
            odd = 2 * k - 1
            y += sgn * np.sin(odd * t) / (odd * odd)
        return y * (8 / np.pi**2)
    if kind == "sqsoft":
        y = np.zeros(n)
        for odd in (1, 3, 5, 7):
            y += np.sin(odd * t) / odd
        return y * (4 / np.pi) * 0.35
    raise ValueError(kind)


def noise_burst(n, decay=0.04):
    y = RNG.normal(0, 1, n)
    # simple 1-pole highpass-ish by differencing, then decay
    y = np.concatenate([[0], np.diff(y)])
    e = np.exp(-np.arange(n) / (decay * SR))
    return y * e


def lowpass(x, cutoff=1800, sr=SR):
    # one-pole
    rc = 1 / (2 * math.pi * cutoff)
    a = 1 / (rc * sr + 1)
    y = np.empty_like(x)
    acc = 0.0
    for i, s in enumerate(x):
        acc += a * (s - acc)
        y[i] = acc
    return y


def render(duration: float, path: Path):
    n = int(round(duration * SR))
    mix = np.zeros(n, dtype=np.float64)

    bpm = 102.0
    beat = 60.0 / bpm
    bar = beat * 4

    # I–V–vi–IV in C major, but voiced a bit higher and airy
    # C3 G3 A3 F3 roots, plus open triads
    chords = [
        [48, 52, 55, 60, 64],  # C
        [47, 50, 55, 59, 67],  # G
        [45, 48, 52, 60, 64],  # Am
        [41, 45, 48, 60, 65],  # F
    ]

    # --- warm pad (held chords) ---
    t0 = 0.0
    ci = 0
    while t0 < duration + bar:
        start = int(t0 * SR)
        length = int(bar * SR)
        if start >= n:
            break
        take = min(length, n - start)
        chord = chords[ci % 4]
        chunk = np.zeros(take)
        for i, m in enumerate(chord):
            det = 1 + (0.0015 if i % 2 == 0 else -0.0015)
            chunk += osc(midi(m) * det, take, "sine", phase=i * 0.3) * (0.22 if i < 3 else 0.16)
            chunk += osc(midi(m) * 2 * det, take, "sine") * 0.04
        chunk *= env_adsr(take, 0.18, 0.2, 0.7, 0.35)
        mix[start : start + take] += chunk * 0.28
        t0 += bar
        ci += 1

    # --- soft plucks on the beat (upbeat pulse) ---
    pluck_pat = [0, 1, 2, 2.5, 3]  # beats in the bar
    t0 = 0.0
    ci = 0
    while t0 < duration + bar:
        chord = chords[ci % 4]
        for hit in pluck_pat:
            start = int((t0 + hit * beat) * SR)
            if start >= n:
                break
            length = int(0.55 * SR)
            take = min(length, n - start)
            chunk = np.zeros(take)
            # alternate root and fifth-ish
            notes = chord[:3] if hit in (0, 2, 3) else chord[2:]
            for i, m in enumerate(notes):
                chunk += osc(midi(m + 12), take, "tri", phase=i) * (0.55 / (i + 1))
            chunk *= env_adsr(take, 0.004, 0.08, 0.18, 0.32)
            mix[start : start + take] += chunk * 0.22
        t0 += bar
        ci += 1

    # --- light bass on downbeats ---
    roots = [48, 47, 45, 41]
    t0 = 0.0
    ci = 0
    while t0 < duration + bar:
        start = int(t0 * SR)
        if start >= n:
            break
        length = int(1.6 * beat * SR)
        take = min(length, n - start)
        m = roots[ci % 4]
        chunk = osc(midi(m), take, "sine") * 0.7 + osc(midi(m) * 2, take, "sine") * 0.15
        chunk *= env_adsr(take, 0.01, 0.12, 0.45, 0.4)
        mix[start : start + take] += chunk * 0.26
        # offbeat ghost
        g = int((t0 + 2 * beat) * SR)
        if g < n:
            take2 = min(int(0.7 * beat * SR), n - g)
            chunk2 = osc(midi(m), take2, "sine") * env_adsr(take2, 0.01, 0.08, 0.25, 0.25)
            mix[g : g + take2] += chunk2 * 0.12
        t0 += bar
        ci += 1

    # --- simple major pentatonic melody, sparse and cheerful ---
    # C major pentatonic around C5: 72 74 76 79 81 84
    motif = [
        (0.0, 76, 0.75),
        (1.0, 79, 0.5),
        (1.5, 81, 0.5),
        (2.5, 79, 0.5),
        (3.0, 76, 0.9),
        (4.0, 74, 0.5),
        (4.5, 72, 0.5),
        (5.5, 74, 0.5),
        (6.0, 76, 0.75),
        (7.0, 72, 1.1),
        (8.0, 79, 0.75),
        (9.0, 81, 0.5),
        (9.5, 84, 0.5),
        (10.5, 81, 0.5),
        (11.0, 79, 0.9),
        (12.0, 76, 0.5),
        (12.5, 74, 0.5),
        (13.5, 76, 0.5),
        (14.0, 72, 1.4),
    ]
    loop = 8 * beat  # 2 bars? Wait motif spans 16 beats = 4 bars
    motif_len = 16 * beat
    rep = 0
    while True:
        base = rep * motif_len
        if base >= duration:
            break
        for off, note, dur in motif:
            start = int((base + off * beat) * SR)
            if start >= n:
                break
            length = int((dur * beat + 0.05) * SR)
            take = min(length, n - start)
            # soft flute-ish: sine + slight 2nd
            vib = np.sin(2 * np.pi * 4.5 * np.arange(take) / SR) * 0.0018
            # frequency modulation via phase increment is heavier; slight vibrato via adding
            chunk = osc(midi(note), take, "sine") + 0.18 * osc(midi(note) * 2, take, "sine")
            # cheap vibrato by mixing a detuned copy
            chunk = chunk * 0.85 + osc(midi(note) * (1 + 0.002), take, "sine") * 0.15
            chunk *= env_adsr(take, 0.02, 0.08, 0.55, 0.28)
            # leave first half-bar of first loop almost pad-only (gentle entry)
            amp = 0.16 if base + off * beat >= 1.5 else 0.06
            mix[start : start + take] += chunk * amp
        rep += 1

    # --- very soft percussion: kick (sine thump) + finger snap noise ---
    t = 0.0
    beat_i = 0
    while t < duration:
        start = int(t * SR)
        if start >= n:
            break
        # kick on 1 and 3
        if beat_i % 2 == 0:
            length = int(0.22 * SR)
            take = min(length, n - start)
            tt = np.arange(take) / SR
            freq = 110 * np.exp(-tt * 18) + 42
            phase = np.cumsum(2 * np.pi * freq / SR)
            kick = np.sin(phase) * np.exp(-tt * 10)
            mix[start : start + take] += kick * 0.22
        # snap on 2 and 4
        else:
            length = int(0.09 * SR)
            take = min(length, n - start)
            snap = noise_burst(take, decay=0.035)
            # tiny high sine tick
            snap += 0.25 * osc(3200, take, "sine") * np.exp(-np.arange(take) / (0.015 * SR))
            mix[start : start + take] += snap * 0.07
        # light shaker every 8th
        sh_start = int((t + beat * 0.5) * SR)
        if sh_start < n:
            take = min(int(0.06 * SR), n - sh_start)
            sh = noise_burst(take, decay=0.03) * 0.035
            mix[sh_start : sh_start + take] += sh
        t += beat
        beat_i += 1

    # gentle bus processing
    # soft clip / tanh
    mix = np.tanh(mix * 1.15)
    # very mild high cut via simple downsample-ish average (cheap lowpass)
    # 3-tap moving average twice
    k = np.array([0.25, 0.5, 0.25])
    mix = np.convolve(mix, k, mode="same")
    mix = np.convolve(mix, k, mode="same")

    mix = fade_io(mix, fin=0.85, fout=1.5)

    peak = np.max(np.abs(mix)) or 1.0
    # target peak around -14 dBFS so it sits quietly under a talking-head-less product video
    target = 10 ** (-14 / 20)
    mix = mix / peak * target

    # safety
    mix = np.clip(mix, -0.95, 0.95)
    pcm = (mix * 32767).astype(np.int16)
    path.parent.mkdir(parents=True, exist_ok=True)
    with wave.open(str(path), "wb") as w:
        w.setnchannels(1)
        w.setsampwidth(2)
        w.setframerate(SR)
        w.writeframes(pcm.tobytes())
    print(f"wrote {path}  dur={len(mix)/SR:.3f}s  peak={peak:.3f}  rms={np.sqrt(np.mean(mix**2)):.4f}")


if __name__ == "__main__":
    # a little longer than the longer reel; mux with -shortest
    render(20.5, Path("/tmp/bh_audio/bed_20s.wav"))
