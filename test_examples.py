# Test examples for Programmers club.

import numpy as np
import pytest
import examples
from examples import inc, wav_selector, telluric_mask, division


def test_pass_inc():
    assert inc(10) == 11

@pytest.mark.xfail()
def test_inc():
    # This will fail
    assert inc(3) == 5

def test_raising_error():
    # This will raise an error but not fail.
    with pytest.raises(ZeroDivisionError):
        division(1, 0)

@pytest.mark.xfail()
def test_not_raising_error():
    # This will fail because error will not be raised.
    with pytest.raises(ZeroDivisionError):
        division(1, 2)


# Test using hypothesis
from hypothesis import given, example, assume
import hypothesis.strategies as st
from math import isnan





# Property based testing. Hypothesis basic examples.
@given(st.integers(), st.integers())
def test_ints_are_commutative(x, y):
    assert x + y == y + x

@given(x=st.integers(), y=st.integers())
def test_ints_cancel(x, y):
    assert (x + y) - y == x

@given(st.lists(st.integers()))
def test_reversing_twice_gives_same_list(xs):
    # This will generate lists of arbitrary length (usually between 0 and
    # 100 elements) whose elements are integers.
    ys = list(xs)
    ys.reverse()
    ys.reverse()
    assert xs == ys

@given(st.tuples(st.booleans(), st.text()))
def test_look_tuples_work_too(t):
    # A tuple is generated as the one you provided, with the corresponding
    # types in those positions.
    assert len(t) == 2
    assert isinstance(t[0], bool)
    assert isinstance(t[1], str)


# My own examples:
@given(st.lists(st.floats(allow_infinity=False), min_size=1), st.floats(), st.floats())
#@given(st.lists(st.floats()), st.floats(), st.floats())
@example([1, 2, 3, 4], 2, 5)
def test_wav_selector(wav, xmin, xmax):
    assume(not isnan(xmin))  # Allows you to avoid wasting test that do not meet your assumptions
    assume(not isnan(xmax))
    wav = np.asarray(wav)
    flux = wav + 2   # not important

    new_wav, new_flux = wav_selector(wav, flux, xmin, xmax)

    assert np.all(new_wav > xmin)   # Every value left is above the minimum
    assert np.all(new_wav < xmax)    # Every value left is below the max
    assert len(new_wav) == len(new_flux)


@given(st.lists(st.floats(min_value=0, max_value=2, allow_infinity=False), min_size=100, max_size=101),
       st.sampled_from([0.98, 0.95]))
def test_telluric_mask_properties(flux, limit):
    flux = np.asarray(flux)
    mask = telluric_mask(flux, limit)
    assert np.all(flux[mask] > limit)  # Test that 1 masked values are all above limit
    assert np.all(flux[~mask] <= limit)  # Test that 0 masked values are all below limit.


@pytest.mark.parametrize('limit', [0.9, 0.95, 0.98])
def test_telluric_mask_with_parameters(limit):
    flux = np.array([0.99, 0.981, 0.9, 0.8, 0.91, 0.94, 0.96, 0.98, 0.99, 0.991])  # Bad test example (antipattern)

    mask = telluric_mask(flux, limit)
    assert np.all(flux[mask] > limit)
    assert np.all(flux[~mask] <= limit)
    assert len(flux[mask]) < len(flux)
