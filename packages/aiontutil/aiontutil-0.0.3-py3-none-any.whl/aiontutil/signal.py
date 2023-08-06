import numpy as np
import scipy as sp
from scipy import stats


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


def get_rmeds(x: np.ndarray, axis=-1):
    """
    Examples
    --------
    >>> rmeds = get_rmeds(np.random.randn(10, 1024))
    """
    x = x.copy()
    if np.ndim(x) == 1:
        x = x[np.newaxis, ...]
    return np.sqrt(np.median(x**2, axis=axis))


def get_rms(x: np.ndarray, axis=-1):
    """
    Examples
    --------
    >>> rms = get_rms(np.random.randn(10, 1024))
    """
    x = x.copy()
    if np.ndim(x) == 1:
        x = x[np.newaxis, ...]
    return np.sqrt(np.mean(x**2, axis=axis))


def get_zcr(x: np.ndarray, axis=-1):
    """
    Examples
    --------
    >>> zcr = get_zcr(np.random.randn(10, 1024))
    """
    x = x.copy()
    if np.ndim(x) == 1:
        x = x[np.newaxis, ...]
    zc = np.abs(np.diff(np.sign(x), axis=axis)).sum(axis) / 2
    return zc / x.shape[1]


name_dict = {
    "entropy": stats.entropy,
    "kurtosis": stats.kurtosis,
    "mad": stats.median_abs_deviation,
    "mean": np.mean,
    "median": np.median,
    "rmeds": get_rmeds,
    "rms": get_rms,
    "skew": stats.skew,
    "std": np.std,
    "zcr": get_zcr,
}


def get_feature(x: np.ndarray, name: str):
    """
    Examples
    --------
    >>> n_samples = 4
    >>> n_size = 1024
    >>> x = np.random.randn(n_samples, n_size)
    >>> entropy = get_feature(x, name='entropy')
    """
    x = x.copy()
    if np.ndim(x) == 1:
        x = x[np.newaxis, ...]

    func = name_dict.get(name)
    if not func:
        raise TypeError("Unsupported provided name.")
    return func(x, axis=1)


def get_spectral_feature(
    x: np.ndarray,
    fs: int,
    freq_intervals: np.ndarray,
    name: str,
):
    """
    Get features from spectra.

    Examples
    --------
    >>> n_samples = 10
    >>> fs = 1024
    >>> x = np.random.randn(n_samples, fs)
    >>> features = get_spectral_feature(
    ... x=x,
    ... fs=fs,
    ... freq_intervals=[[50, 70], [110, 130]],
    ... name='entropy',
    ... )
    >>> features.shape
    (10, 2)
    """
    x = x.copy()
    if np.ndim(x) == 1:
        x = x[np.newaxis, ...]

    func = name_dict.get(name)
    if not func:
        raise TypeError("Unsupported provided name.")

    freq, amps = get_freq_amp(x=x, fs=fs)

    feats = []
    for interval in freq_intervals:
        start = interval[0]
        end = interval[-1]
        cond = np.where((start < freq) & (freq < end))[0]

        partial_feats = get_feature(x=amps[..., cond], name=name)
        feats.append(partial_feats)
    feats = np.array(feats).T
    return feats
