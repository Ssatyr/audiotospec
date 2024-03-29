import librosa
import numpy as np


def griffin_lim_generator(
        spectrogram,
        iterations=10,
        approximated_signal=None,
        stft_kwargs={},
        istft_kwargs={}):
    """
    Implements the basic Griffin Lim algorithm.

    Returns a generator that outputs the approximated signal at the various iterations.
    :param spectrogram: The Spectrogram from which reconstruction should begin
    :param iterations: The number of iterations you want to perform reconstruction with.
    :param approximated_signal: if you want to begin with an existing approximated signal
    :param stft_kwargs: The arguments to pass to STFT as defined by the librosa
    implementation of these functions.
    :param istft_kwargs: The arguments to pass to ISTFT as defined by the librosa
    implementation of these functions.
    :return generator:  This is a generator of approximated signals at each iteration of
    the griffin lim algorithm
    """
    _M = spectrogram
    for k in range(iterations):
        if approximated_signal is None:
            _P = np.random.randn(*_M.shape)
        else:
            _D = librosa.stft(approximated_signal, **stft_kwargs)
            _P = np.angle(_D)

        _D = _M * np.exp(1j * _P)
        approximated_signal = librosa.istft(_D, **istft_kwargs)
        yield approximated_signal


def gla(spectrogram,
        iterations=10,
        approximated_signal=None,
        stft_kwargs={},
        istft_kwargs={}):
    """
    Implements the basic Griffin Lim algorithm.

    Returns a generator that outputs the approximated signal at the various iterations.
    :param spectrogram: The Spectrogram from which reconstruction should begin
    :param iterations: The number of iterations you want to perform reconstruction with.
    :param approximated_signal: if you want to begin with an existing approximated signal
    :param stft_kwargs: The arguments to pass to STFT and ISTFT as defined by the librosa
    implementation of these functions.
    :param istft_kwargs: The arguments to pass to ISTFT as defined by the librosa
    implementation of these functions.
    :return approximated_signal:
    """
    generator = griffin_lim_generator(spectrogram, iterations, approximated_signal, stft_kwargs, istft_kwargs)
    for approximated_signal in generator:
        pass
    return approximated_signal