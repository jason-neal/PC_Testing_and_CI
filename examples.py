
"""Some example functions for testing and to show plugin linting."""

import numpy as np

# Pytest example function
def inc(x):
    """Increment"""
    return x + 1

def division(a, b):
    if b==0:
        raise ZeroDivisionError("b cannot be zero.")
    else:
       return a / b


# Wavelength select
def wav_selector(wav, flux, wav_min, wav_max):
    """Wavelenght selector between wav_min, wav_max.

    Returns as numpy arrays.
    """
    wav = np.asarray(wav)
    flux = np.asarray(flux)

    mask = (wav > wav_min) & (wav < wav_max)
    wav_sel = wav[mask]
    flux_sel = flux[mask]
    return [wav_sel, flux_sel]


## Telluric masking
def telluric_mask(flux, limit=0.98):
    """Create mask of telluic lines.

    Parameters
    ----------
    flux: numpy.ndarray
        Spectrum transmission flux.
    limit: float

    Returns
    -------
    mask: numpy.ndarray of bools
        Mask absortion lines to 0.
    """

    mask = flux > limit

    return mask


# Mypy type-hinting
def type_hint_test(x: float, y: int) -> int:
    # Mypy checks the types for consistency.
    # Should fail here as float + int will return a float.
    # Does this statically (doesn't run the code)
    return x + y
