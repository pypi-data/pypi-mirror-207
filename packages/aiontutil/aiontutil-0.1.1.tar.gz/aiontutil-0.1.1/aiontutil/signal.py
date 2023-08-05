import numpy as np
import scipy as sp


def get_freq_amp(x: np.ndarray, fs: int):
    """
    Examples
    --------
    >>> n_secs = 5
    >>> fs = 256
    >>> true_freqs = np.array([11, 23, 31, 41])
    >>> true_amps = np.array([13, 29, 37, 43])
    >>> t = np.linspace(0, n_secs, n_secs * fs, endpoint=False)
    >>> x = (np.sin(2 * np.pi * t[..., np.newaxis] * true_freqs) * true_amps).sum(1)
    >>> freq, amps = get_freq_amp(x=x, fs=fs)
    """
    if np.ndim(x) == 1:
        x = x.reshape(1, -1)
    n = x.shape[-1]
    freq = sp.fft.fftfreq(n, d=1 / fs)
    fhat = sp.fft.fft(x)
    amp = 2 * np.abs(fhat) / n
    amp[..., 0] = 0
    return freq[: n // 2].copy(), amp[..., : n // 2].copy()
