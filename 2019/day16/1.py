#!/usr/bin/env python3


def fft(signal, phases):
    pattern = [0, 1, 0, -1]
    
    for _ in range(phases):
        new_signal = []
        for k in range(len(signal)):
            a = 0
            for i, s in enumerate(signal):
                p = pattern[(((i + 1) // (k + 1)) % len(pattern))]
                a += s * p
            new_signal.append(abs(a) % 10)
        signal = new_signal

    return signal


data = [int(i) for i in list(open("input").read().strip())]
print("".join(str(s) for s in fft(data, 100)[:8]))
