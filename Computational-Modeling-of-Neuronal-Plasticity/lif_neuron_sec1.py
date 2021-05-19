import pint
import numpy as np
import matplotlib.pyplot as plt

# Section 1

def lif_voltage(si, V_0, V_thres, V_reset, E_leak, R_m, I_ext, τ_mem, T, Δt):
    """
        Simulate a simple Leaky Integrate-and-Fire Neuron without synaptic input,
        but with external current.
    """
    steps = int(T / Δt)
    V = np.zeros(steps) * si.mV
    V[0] = V_0

    for i in range(1, steps):
        V[i] = Δt * (E_leak - V[i-1] + R_m * I_ext) / τ_mem + V[i-1]
        if V[i] >= V_thres:
            V[i] = V_reset
    
    ts = np.arange(0, T.to(si.ms).magnitude, Δt.magnitude)

    return ts, V

def plot_lif(si, title, ts, V):
    """
        Plot of voltage over time
    """
    plt.title(title)
    plt.xlabel("time [ms]")
    plt.ylabel("V [mV]")
    plt.plot(ts, V)
