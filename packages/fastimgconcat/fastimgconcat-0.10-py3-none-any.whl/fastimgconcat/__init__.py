import sys
import numpy as np


# create empty numpy arrays as module variables

temparrays = sys.modules[__name__]
temparrays.vertical = np.array([], dtype=np.uint8)
temparrays.horizontal = np.array([], dtype=np.uint8)


def adjust_array_size_vertical(arrays: list[np.array]) -> None:
    """
    Resizes the `temparrays.vertical` numpy array to the required size if it
    is not already the same size as the sum of the arrays' heights and the
    maximum width of the arrays in `arrays`, along with the same data type
    as the arrays.

    Parameters:
        arrays (list[np.array]): A list of numpy arrays.

    Returns:
        None.
    """
    allshapes = sum([y.shape[0] for y in arrays])
    allshapesmax = max([y.shape[1] for y in arrays])

    shapeneeded = allshapes, allshapesmax, *arrays[0].shape[2:]
    if (temparrays.vertical.shape != shapeneeded) or (
        temparrays.vertical.dtype.name != arrays[0].dtype.name
    ):
        temparrays.vertical = np.zeros(shapeneeded, dtype=arrays[0].dtype)


def fastconcat_vertical(arrays: list[np.array], checkarraysize: bool = True) -> None:
    """
    Concatenates the numpy arrays in `arrays` vertically and stores the result
    in `temparrays.vertical`. The `temparrays.vertical` numpy array must be
    resized prior to calling this function if its size is not adequate to
    accommodate the resulting concatenation.

    Parameters:
        arrays (list[np.array]): A list of numpy arrays to be concatenated.
        checkarraysize (bool): If True, the `adjust_array_size_vertical()`
        function is called to resize the `temparrays.vertical` numpy array to
        the required size before concatenation. Default is True.

    Returns:
        None.
    """
    if checkarraysize:
        adjust_array_size_vertical(arrays)

    starting1 = 0
    ending = 0
    ending1 = 0
    for a in arrays:
        ending = ending + a.shape[1]
        ending1 = ending1 + a.shape[0]
        temparrays.vertical[starting1:ending1, 0 : a.shape[1]] = a

        starting1 = ending1


def adjust_array_size_horizontal(arrays: list[np.array]) -> None:
    """
    Resizes the `temparrays.horizontal` numpy array to the required size if it
    is not already the same size as the sum of the arrays' widths and the
    maximum height of the arrays in `arrays`, along with the same data type
    as the arrays.

    Parameters:
        arrays (list[np.array]): A list of numpy arrays.

    Returns:
        None.
    """
    allshapes = sum([y.shape[1] for y in arrays])
    allshapesmax = max([y.shape[0] for y in arrays])
    shapeneeded = allshapesmax, allshapes, *arrays[0].shape[2:]
    if (temparrays.horizontal.shape != shapeneeded) or (
        temparrays.horizontal.dtype.name != arrays[0].dtype.name
    ):
        temparrays.horizontal = np.zeros(shapeneeded, dtype=arrays[0].dtype)


def fastconcat_horizontal(arrays: list[np.array], checkarraysize: bool = True) -> None:
    """
    The fastconcat_horizontal function concatenates a list of NumPy arrays horizontally and stores the resulting array in a global variable temparrays.horizontal.

    Parameters:
        arrays: A list of NumPy arrays to concatenate horizontally.
        checkarraysize (default True): A boolean indicating whether to check if the size of the concatenated array matches the size of the existing temparrays.horizontal array.

    Returns:
        None
    The function first checks if checkarraysize is True. If so, it calls the adjust_array_size_horizontal function to ensure that temparrays.horizontal is large enough to accommodate the concatenated arrays.
    Next, the function iterates through the input arrays and computes the total height (ending) and width (ending1) of the concatenated array. It then copies each array in arrays to the appropriate slice of temparrays.horizontal, starting at starting1 and ending at ending1.
    The function returns None. The concatenated array can be accessed as temparrays.horizontal after the function has completed.

    """
    if checkarraysize:
        adjust_array_size_horizontal(arrays)
    starting1 = 0
    ending = 0
    ending1 = 0
    for a in arrays:
        ending = ending + a.shape[0]
        ending1 = ending1 + a.shape[1]
        temparrays.horizontal[0 : a.shape[0], starting1:ending1] = a
        starting1 = ending1
