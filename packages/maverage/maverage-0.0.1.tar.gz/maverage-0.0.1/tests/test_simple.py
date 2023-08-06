'''Tests for the `Simple` moving average class.'''
# pylint: disable=redefined-outer-name
import pytest

from maverage import Simple


@pytest.fixture()
def sma():
    """Create the Simple object sma to be used in tests."""
    simple = Simple(3)
    return simple


@pytest.mark.parametrize('test_input', [0, -1, 'string', 1.5, 2.0, None])
def test_invalid_size_argument(test_input):
    """Tests the __init__ method with invalid size arguments."""
    with pytest.raises(ValueError):
        Simple(test_input)


def test_moving_average(sma):
    """Input values and check the results."""
    sma.input(1)
    assert sma.average==1

    sma.input(2)
    assert sma.average==1.5

    sma.input(3)
    assert sma.average==2

    sma.input(4)
    # Do not check sma.average this time to show it is not necessary.

    sma.input(5)
    assert sma.average==4


def test_chaining(sma):
    """Test that the input method allows for chaining the average property for immediate use."""
    val = sma.input(1)
    assert val is sma

    assert sma.input(2).average==1.5
