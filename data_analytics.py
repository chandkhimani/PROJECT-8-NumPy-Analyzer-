import numpy as np


class DataAnalytics:

    # =================================================
    # CONSTRUCTOR
    # =================================================
    def __init__(self, array=None):
        self.__array = array

    # =================================================
    # GET / SET ARRAY
    # =================================================
    def get_array(self):
        return self.__array

    def set_array(self, array):
        self.__array = np.array(array)

    # =================================================
    # DISPLAY ARRAY
    # =================================================
    def display_array(self):
        self.__validate_array()

        print("\nCurrent Array:")
        print(self.__array)

        print(f"\nDimensions : {self.__array.ndim}D")
        print(f"Shape      : {self.__array.shape}")
        print(f"Data Type  : {self.__array.dtype}")

    # =================================================
    # PRIVATE VALIDATION METHOD
    # =================================================
    def __validate_array(self):
        if self.__array is None:
            raise ValueError(
                "No array has been created. Please create an array first."
            )

    # =================================================
    # CLASS METHOD
    # =================================================
    @classmethod
    def create_from_values(cls, values, shape=None):

        array = np.array(values)

        if shape is not None:
            try:
                array = array.reshape(shape)

            except ValueError:
                raise ValueError(
                    "The given values cannot be reshaped "
                    "into the specified shape."
                )

        return cls(array)

    # =================================================
    # INDEXING
    # =================================================
    def get_element(self, indices):

        self.__validate_array()

        try:
            return self.__array[indices]

        except (IndexError, TypeError):
            raise IndexError(
                "Invalid index or index is out of range."
            )

    # =================================================
    # SLICING
    # =================================================
    def slice_array(self, slices):

        self.__validate_array()

        try:
            return self.__array[slices]

        except (IndexError, TypeError):
            raise IndexError(
                "Invalid slicing operation."
            )

    # =================================================
    # MATHEMATICAL OPERATIONS
    # =================================================
    def mathematical_operation(self, second_array, operation):

        self.__validate_array()

        second_array = np.array(second_array)

        if self.__array.shape != second_array.shape:
            raise ValueError(
                "Both arrays must have the same shape."
            )

        if operation == "add":

            return self.__array + second_array

        elif operation == "subtract":

            return self.__array - second_array

        elif operation == "multiply":

            return self.__array * second_array

        elif operation == "divide":

            if np.any(second_array == 0):
                raise ValueError(
                    "Division by zero is not allowed."
                )

            return self.__array / second_array

        else:

            raise ValueError(
                "Invalid mathematical operation."
            )

    # =================================================
    # DOT PRODUCT
    # =================================================
    def dot_product(self, second_array):

        self.__validate_array()

        second_array = np.array(second_array)

        if self.__array.ndim != 2:
            raise ValueError(
                "Dot product requires the current array to be 2D."
            )

        if second_array.ndim != 2:
            raise ValueError(
                "Dot product requires the second array to be 2D."
            )

        if self.__array.shape[1] != second_array.shape[0]:
            raise ValueError(
                "Arrays have incompatible dimensions for dot product."
            )

        return np.dot(self.__array, second_array)

    # =================================================
    # MATRIX MULTIPLICATION
    # =================================================
    def matrix_multiplication(self, second_array):

        self.__validate_array()

        second_array = np.array(second_array)

        if self.__array.ndim != 2:
            raise ValueError(
                "Matrix multiplication requires the current array to be 2D."
            )

        if second_array.ndim != 2:
            raise ValueError(
                "Matrix multiplication requires the second array to be 2D."
            )

        if self.__array.shape[1] != second_array.shape[0]:
            raise ValueError(
                "Arrays have incompatible dimensions for matrix multiplication."
            )

        return np.matmul(self.__array, second_array)

    # =================================================
    # COMBINE / CONCATENATE ARRAYS
    # =================================================
    def combine_arrays(self, second_array, axis=0):

        self.__validate_array()

        second_array = np.array(second_array)

        if self.__array.ndim != second_array.ndim:
            raise ValueError(
                "Both arrays must have the same number of dimensions."
            )

        if axis < 0 or axis >= self.__array.ndim:
            raise ValueError(
                "Invalid axis."
            )

        for dimension in range(self.__array.ndim):

            if dimension != axis:

                if (
                    self.__array.shape[dimension]
                    != second_array.shape[dimension]
                ):
                    raise ValueError(
                        "Array dimensions are incompatible for combining."
                    )

        return np.concatenate(
            (self.__array, second_array),
            axis=axis
        )

    # =================================================
    # SPLIT ARRAY
    # =================================================
    def split_array(self, sections, axis=0):

        self.__validate_array()

        if sections <= 0:
            raise ValueError(
                "Number of sections must be greater than 0."
            )

        if axis < 0 or axis >= self.__array.ndim:
            raise ValueError(
                "Invalid axis."
            )

        return np.array_split(
            self.__array,
            sections,
            axis=axis
        )

    # =================================================
    # SEARCH
    # =================================================
    def search_value(self, value):

        self.__validate_array()

        return np.where(
            self.__array == value
        )

    # =================================================
    # SORT
    # =================================================
    def sort_array(self, descending=False):

        self.__validate_array()

        # Flatten array for consistent sorting
        flattened_array = self.__array.flatten()

        sorted_array = np.sort(
            flattened_array
        )

        if descending:
            return sorted_array[::-1]

        return sorted_array

    # =================================================
    # FILTER
    # =================================================
    def filter_array(self, condition, value):

        self.__validate_array()

        if not self.is_valid_condition(condition):
            raise ValueError(
                "Invalid condition. "
                "Use >, <, >=, <=, == or !=."
            )

        if condition == ">":

            return self.__array[
                self.__array > value
            ]

        elif condition == "<":

            return self.__array[
                self.__array < value
            ]

        elif condition == ">=":

            return self.__array[
                self.__array >= value
            ]

        elif condition == "<=":

            return self.__array[
                self.__array <= value
            ]

        elif condition == "==":

            return self.__array[
                self.__array == value
            ]

        elif condition == "!=":

            return self.__array[
                self.__array != value
            ]

    # =================================================
    # STATIC METHOD
    # =================================================
    @staticmethod
    def is_valid_condition(condition):

        return condition in [
            ">",
            "<",
            ">=",
            "<=",
            "==",
            "!="
        ]

    # =================================================
    # SUM
    # =================================================
    def calculate_sum(self):

        self.__validate_array()

        return np.sum(
            self.__array
        )

    # =================================================
    # MEAN
    # =================================================
    def calculate_mean(self):

        self.__validate_array()

        return np.mean(
            self.__array
        )

    # =================================================
    # MEDIAN
    # =================================================
    def calculate_median(self):

        self.__validate_array()

        return np.median(
            self.__array
        )

    # =================================================
    # STANDARD DEVIATION
    # =================================================
    def calculate_standard_deviation(self):

        self.__validate_array()

        return np.std(
            self.__array
        )

    # =================================================
    # VARIANCE
    # =================================================
    def calculate_variance(self):

        self.__validate_array()

        return np.var(
            self.__array
        )

    # =================================================
    # MINIMUM
    # =================================================
    def calculate_minimum(self):

        self.__validate_array()

        return np.min(
            self.__array
        )

    # =================================================
    # MAXIMUM
    # =================================================
    def calculate_maximum(self):

        self.__validate_array()

        return np.max(
            self.__array
        )

    # =================================================
    # PERCENTILE
    # =================================================
    def calculate_percentile(self, percentile):

        self.__validate_array()

        if percentile < 0 or percentile > 100:
            raise ValueError(
                "Percentile must be between 0 and 100."
            )

        return np.percentile(
            self.__array,
            percentile
        )

    # =================================================
    # CORRELATION COEFFICIENT
    # =================================================
    def calculate_correlation(self, second_array):

        self.__validate_array()

        second_array = np.array(
            second_array
        )

        if self.__array.ndim != 1:
            raise ValueError(
                "Correlation requires the current array to be 1D."
            )

        if second_array.ndim != 1:
            raise ValueError(
                "Correlation requires the second array to be 1D."
            )

        if self.__array.size != second_array.size:
            raise ValueError(
                "Both arrays must contain the same number of values."
            )

        if self.__array.size < 2:
            raise ValueError(
                "At least two values are required."
            )

        # Check for constant arrays
        if (
            np.std(self.__array) == 0
            or np.std(second_array) == 0
        ):
            raise ValueError(
                "Correlation cannot be calculated "
                "when an array has constant values."
            )

        return np.corrcoef(
            self.__array,
            second_array
        )[0, 1]