import numpy as nmp
import matplotlib.pyplot as pll

def plot_sine_wave(frequency=1, amplitude=1, phase=0, duration=1, sampling_rate=1000):
    t = nmp.linspace(0, duration, int(sampling_rate*duration), endpoint=False)
    y = amplitude * nmp.sin(2 * nmp.pi * frequency * t + phase)

    pll.figure(figsize=(10, 4))
    pll.plot(t, y, label=f'{frequency} Hz Sine Wave')
    pll.title("Sine Wave")
    pll.xlabel("Time (s)")
    pll.ylabel("Amplitude")
    pll.grid(True)
    pll.legend()
    pll.show()

if __name__ == "__main__":
    plot_sine_wave(frequency=1)