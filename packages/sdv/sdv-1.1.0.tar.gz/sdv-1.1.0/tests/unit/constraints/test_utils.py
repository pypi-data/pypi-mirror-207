"""Tests for the sdv.constraints.utils module."""
from datetime import datetime
from decimal import Decimal

import numpy as np
import pandas as pd

from sdv.constraints.utils import (
    _cast_to_type, cast_to_datetime64, compute_nans_column, get_nan_component_value, logit,
    matches_datetime_format, revert_nans_columns, sigmoid)
from sdv.utils import get_datetime_format, is_datetime_type


def test_is_datetime_type_with_datetime_series():
    """Test the ``is_datetime_type`` function when a datetime series is passed.

    Expect to return True when a datetime series is passed.

    Input:
    - A pandas.Series of type `datetime64[ns]`
    Output:
    - True
    """
    # Setup
    data = pd.Series([
        pd.to_datetime('2020-01-01'),
        pd.to_datetime('2020-01-02'),
        pd.to_datetime('2020-01-03')
    ],
    )

    # Run
    is_datetime = is_datetime_type(data)

    # Assert
    assert is_datetime


def test_is_datetime_type_with_datetime():
    """Test the ``is_datetime_type`` function when a datetime is passed.

    Expect to return True when a datetime variable is passed.

    Input:
    - datetime.Datetime
    Output:
    - True
    """
    # Setup
    data = datetime(2020, 1, 1)

    # Run
    is_datetime = is_datetime_type(data)

    # Assert
    assert is_datetime


def test_is_datetime_type_with_pandas_datetime():
    """Test the ``is_datetime_type`` function when a pandas.datetime is passed.

    Expect to return True when a datetime variable is passed.

    Input:
    - pandas.Datetime
    Output:
    - True
    """
    # Setup
    data = pd.to_datetime('2020-01-01')

    # Run
    is_datetime = is_datetime_type(data)

    # Assert
    assert is_datetime


def test_is_datetime_type_with_int():
    """Test the ``is_datetime_type`` function when an int is passed.

    Expect to return False when an int variable is passed.

    Input:
    - int
    Output:
    - False
    """
    # Setup
    data = 2

    # Run
    is_datetime = is_datetime_type(data)

    # Assert
    assert is_datetime is False


def test_is_datetime_type_with_datetime_str():
    """Test the ``is_datetime_type`` function when an valid datetime string is passed.

    Expect to return True when a valid string representing datetime is passed.

    Input:
    - string
    Output:
    - True
    """
    # Setup
    value = '2021-02-02'

    # Run
    is_datetime = is_datetime_type(value)

    # Assert
    assert is_datetime


def test_is_datetime_type_with_invalid_str():
    """Test the ``is_datetime_type`` function when an invalid string is passed.

    Expect to return False when an invalid string is passed.

    Input:
    - string
    Output:
    - False
    """
    # Setup
    value = 'abcd'

    # Run
    is_datetime = is_datetime_type(value)

    # Assert
    assert is_datetime is False


def test_is_datetime_type_with_string():
    """Test the ``is_datetime_type`` function when a string is passed.

    Expect to return False when a string variable is passed.

    Input:
    - string
    Output:
    - False
    """
    # Setup
    data = 'test'

    # Run
    is_datetime = is_datetime_type(data)

    # Assert
    assert is_datetime is False


def test_is_datetime_type_with_int_series():
    """Test the ``is_datetime_type`` function when an int series is passed.

    Expect to return False when an int series variable is passed.

    Input:
    -  pd.Series of type int
    Output:
    - False
    """
    # Setup
    data = pd.Series([1, 2, 3, 4])

    # Run
    is_datetime = is_datetime_type(data)

    # Assert
    assert is_datetime is False


def test__cast_to_type():
    """Test the ``_cast_to_type`` function.

    Given ``pd.Series``, ``np.array`` or just a numeric value, it should
    cast it to the given ``type``.

    Input:
        - pd.Series
        - np.array
        - numeric
        - Type
    Output:
        The values should be casted to the expected ``type``.
    """
    # Setup
    value = 88
    series = pd.Series([1, 2, 3])
    array = np.array([1, 2, 3])

    # Run
    res_value = _cast_to_type(value, float)
    res_series = _cast_to_type(series, float)
    res_array = _cast_to_type(array, float)

    # Assert
    assert isinstance(res_value, float)
    assert res_series.dtype == float
    assert res_array.dtype == float


def test_logit():
    """Test the ``logit`` function.

    Setup:
        - Compute ``expected_res`` with the ``high`` and ``low`` values.
    Input:
        - ``data`` a number.
        - ``low`` and ``high`` numbers.
    Output:
        The result of the scaled logit.
    """
    # Setup
    high, low = 100, 49
    _data = (88 - low) / (high - low)
    _data = Decimal(_data) * Decimal(0.95) + Decimal(0.025)
    _data = float(_data)
    expected_res = np.log(_data / (1.0 - _data))

    data = 88

    # Run
    res = logit(data, low, high)

    # Assert

    assert res == expected_res


def test_sigmoid():
    """Test the ``sigmoid`` function.

    Setup:
        - Compute ``expected_res`` with the ``high`` and ``low`` values.
    Input:
        - ``data`` a number.
        - ``low`` and ``high`` numbers.
    Output:
        The result of sigmoid.
    """
    # Setup
    high, low = 100, 49
    _data = data = 1.1064708752806303

    _data = 1 / (1 + np.exp(-data))
    _data = (Decimal(_data) - Decimal(0.025)) / Decimal(0.95)
    _data = float(_data)
    expected_res = _data * (high - low) + low

    # Run
    res = sigmoid(data, low, high)

    # Assert
    assert res == expected_res


def test_cast_to_datetime64():
    """Test the ``cast_to_datetime64`` function.

    Setup:
        - String value representing a datetime
        - List value with a ``np.nan`` and string values.
        - pd.Series with datetime values.
    Output:
        - A single np.datetime64
        - A list of np.datetime64
        - A series of np.datetime64
    """
    # Setup
    string_value = '2021-02-02'
    list_value = [np.nan, '2021-02-02']
    series_value = pd.Series(['2021-02-02'])

    # Run
    string_out = cast_to_datetime64(string_value)
    list_out = cast_to_datetime64(list_value)
    series_out = cast_to_datetime64(series_value)

    # Assert
    expected_string_output = np.datetime64('2021-02-02')
    expected_series_output = pd.Series(np.datetime64('2021-02-02'))
    expected_list_output = np.array([np.datetime64('NaT'), '2021-02-02'], dtype='datetime64[ns]')
    np.testing.assert_array_equal(expected_list_output, list_out)
    pd.testing.assert_series_equal(expected_series_output, series_out)
    assert expected_string_output == string_out


def test_get_datetime_format():
    """Test the ``get_datetime_format``.

    Setup:
        - string value representing datetime.
        - list of values with a datetime.
        - series with a datetime.

    Output:
        - The expected output is the format of the datetime representation.
    """
    # Setup
    string_value = '2021-02-02'
    list_value = [np.nan, '2021-02-02']
    series_value = pd.Series(['2021-02-02T12:10:59'])

    # Run
    string_out = get_datetime_format(string_value)
    list_out = get_datetime_format(list_value)
    series_out = get_datetime_format(series_value)

    # Assert
    expected_output = '%Y-%m-%d'
    assert string_out == expected_output
    assert list_out == expected_output
    assert series_out == '%Y-%m-%dT%H:%M:%S'


def test_matches_datetime_format():
    """Test the ``matches_datetime_format`` method.

    If the provided datetime string matches the format, then it should return True.

    Input:
        - Datetime string that matches the format

    Output:
        - True
    """
    # Run
    result = matches_datetime_format('1/1/2020', '%m/%d/%Y')

    # Assert
    assert result is True


def test_matches_datetime_format_does_not_match():
    """Test the ``matches_datetime_format`` method.

    If the provided datetime string does not match the format, then it should return False.

    Input:
        - Datetime string that does not match the format

    Output:
        - False
    """
    # Run
    result = matches_datetime_format('1-1-2020', '%m/%d/%Y')

    # Assert
    assert result is False


def test_matches_datetime_format_bad_value():
    """Test the ``matches_datetime_format`` method.

    If the provided value is not a string, then it should return False.

    Input:
        - int and a datetime format

    Output:
        - False
    """
    # Run
    result = matches_datetime_format(10, '%m/%d/%Y')

    # Assert
    assert result is False


def test_get_nan_component_value():
    """Test the ``get_nan_component_value`` method."""
    # Setup
    row = pd.Series([np.nan, 2, np.nan, 4], index=['a', 'b', 'c', 'd'])

    # Run
    result = get_nan_component_value(row)

    # Assert
    assert result == 'a, c'


def test_compute_nans_columns():
    """Test the ``compute_nans_columns`` method."""
    # Setup
    data = pd.DataFrame({
        'a': [1, np.nan, 3, np.nan], 'b': [np.nan, 2, 3, np.nan], 'c': [1, np.nan, 3, np.nan]
    })

    # Run
    output = compute_nans_column(data, ['a', 'b', 'c'])
    expected_output = pd.Series(['b', 'a, c', 'None', 'a, b, c'], name='a#b#c.nan_component')

    # Assert
    pd.testing.assert_series_equal(output, expected_output)


def test_compute_nans_columns_without_nan():
    """Test the ``compute_nans_columns`` method when there are no nans."""
    # Setup
    data = pd.DataFrame({
        'a': [1, 2, 3, 2], 'b': [2.5, 2, 3, 2.5], 'c': [1, 2, 3, 2]
    })

    # Run
    output = compute_nans_column(data, ['a', 'b', 'c'])

    # Assert
    assert output is None


def test_revert_nans_columns():
    """Test the ``revert_nans_columns`` method."""
    # Setup
    data = pd.DataFrame({
        'a': [1, 2, 3, 2], 'b': [2.5, 2, 3, 2.5], 'c': [1, 2, 3, 2],
        'a#b#c.nan_component': ['b', 'a, c', 'None', 'a, b, c']
    })
    nan_column_name = 'a#b#c.nan_component'

    # Run
    result = revert_nans_columns(data, nan_column_name)

    expected_data = pd.DataFrame({
        'a': [1, np.nan, 3, np.nan], 'b': [np.nan, 2, 3, np.nan],
        'c': [1, np.nan, 3, np.nan]
    })

    # Assert
    pd.testing.assert_frame_equal(result, expected_data)
