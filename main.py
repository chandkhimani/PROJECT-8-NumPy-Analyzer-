import numpy as np
from data_analytics import DataAnalytics


# =====================================================
# HELPER FUNCTION: CONVERT USER INPUT TO NUMPY VALUES
# =====================================================
def convert_value(value):
    try:
        # Integer check
        if "." not in value:
            return int(value)

        # Decimal check
        return float(value)

    except ValueError:
        raise ValueError(
            f"'{value}' is not a valid number."
        )


# =====================================================
# GET VALUES FROM USER
# =====================================================
def get_values():

    values = input(
        "Enter numbers separated by spaces: "
    ).strip()

    if not values:
        raise ValueError(
            "Please enter at least one number."
        )

    return [
        convert_value(value)
        for value in values.split()
    ]


# =====================================================
# GET SECOND ARRAY
# =====================================================
def get_second_array():

    values = get_values()

    return np.array(values)


# =====================================================
# GET ARRAY WITH SHAPE
# =====================================================
def get_array_with_shape(shape):

    total_values = int(np.prod(shape))

    values = input(
        f"Enter {total_values} numbers separated by spaces: "
    ).strip()

    if not values:
        raise ValueError(
            "Please enter the required values."
        )

    values = [
        convert_value(value)
        for value in values.split()
    ]

    if len(values) != total_values:
        raise ValueError(
            f"Expected {total_values} values, "
            f"but received {len(values)}."
        )

    return np.array(values).reshape(shape)


# =====================================================
# MAIN FUNCTION
# =====================================================
def main():

    print("=" * 55)
    print("              NUMPY ANALYZER")
    print("=" * 55)

    analyzer = DataAnalytics()

    while True:

        print("\nMAIN MENU")
        print("-" * 35)
        print("1. Create a NumPy Array")
        print("2. Display Current Array")
        print("3. Indexing and Slicing")
        print("4. Perform Mathematical Operations")
        print("5. Combine or Split Arrays")
        print("6. Search, Sort and Filter")
        print("7. Aggregates and Statistics")
        print("8. Exit")
        print("-" * 35)

        choice = input(
            "Enter your choice: "
        ).strip()

        # =================================================
        # OPTION 1: CREATE NUMPY ARRAY
        # =================================================
        if choice == "1":

            print("\nCREATE NUMPY ARRAY")
            print("-" * 35)
            print("1. Create 1D Array")
            print("2. Create 2D Array")
            print("3. Create 3D Array")

            array_choice = input(
                "Choose array type: "
            ).strip()

            try:

                # -----------------------------------------
                # 1D ARRAY
                # -----------------------------------------
                if array_choice == "1":

                    values = get_values()

                    array = np.array(values)

                    analyzer.set_array(array)

                # -----------------------------------------
                # 2D ARRAY
                # -----------------------------------------
                elif array_choice == "2":

                    rows = int(
                        input("Enter number of rows: ")
                    )

                    columns = int(
                        input("Enter number of columns: ")
                    )

                    if rows <= 0 or columns <= 0:
                        raise ValueError(
                            "Rows and columns must be greater than 0."
                        )

                    array = get_array_with_shape(
                        (rows, columns)
                    )

                    analyzer.set_array(array)

                # -----------------------------------------
                # 3D ARRAY
                # -----------------------------------------
                elif array_choice == "3":

                    depth = int(
                        input("Enter depth: ")
                    )

                    rows = int(
                        input("Enter number of rows: ")
                    )

                    columns = int(
                        input("Enter number of columns: ")
                    )

                    if (
                        depth <= 0
                        or rows <= 0
                        or columns <= 0
                    ):
                        raise ValueError(
                            "Depth, rows and columns "
                            "must be greater than 0."
                        )

                    array = get_array_with_shape(
                        (depth, rows, columns)
                    )

                    analyzer.set_array(array)

                else:

                    print(
                        "Invalid array type. "
                        "Please choose 1, 2 or 3."
                    )

                    continue

                print(
                    "\nArray created successfully!"
                )

                analyzer.display_array()

            except (ValueError, TypeError) as e:

                print(f"\nError: {e}")

        # =================================================
        # OPTION 2: DISPLAY CURRENT ARRAY
        # =================================================
        elif choice == "2":

            try:

                analyzer.display_array()

            except ValueError as e:

                print(f"\nError: {e}")

        # =================================================
        # OPTION 3: INDEXING AND SLICING
        # =================================================
        elif choice == "3":

            print("\nINDEXING AND SLICING")
            print("-" * 35)
            print("1. Get Element")
            print("2. Slice Array")

            sub_choice = input(
                "Enter your choice: "
            ).strip()

            try:

                current_array = analyzer.get_array()

                if current_array is None:
                    raise ValueError(
                        "Please create an array first."
                    )

                # -----------------------------------------
                # GET ELEMENT
                # -----------------------------------------
                if sub_choice == "1":

                    print(
                        f"\nCurrent Array Dimensions: "
                        f"{current_array.ndim}D"
                    )

                    # 1D
                    if current_array.ndim == 1:

                        index = int(
                            input("Enter index: ")
                        )

                        result = analyzer.get_element(
                            index
                        )

                    # 2D
                    elif current_array.ndim == 2:

                        row = int(
                            input("Enter row index: ")
                        )

                        column = int(
                            input("Enter column index: ")
                        )

                        result = analyzer.get_element(
                            (row, column)
                        )

                    # 3D
                    elif current_array.ndim == 3:

                        depth = int(
                            input("Enter depth index: ")
                        )

                        row = int(
                            input("Enter row index: ")
                        )

                        column = int(
                            input("Enter column index: ")
                        )

                        result = analyzer.get_element(
                            (depth, row, column)
                        )

                    else:
                        raise ValueError(
                            "Unsupported array dimension."
                        )

                    print("\nSelected Element:")
                    print(result)

                # -----------------------------------------
                # SLICE ARRAY
                # -----------------------------------------
                elif sub_choice == "2":

                    # 1D SLICING
                    if current_array.ndim == 1:

                        start = int(
                            input("Enter start index: ")
                        )

                        end = int(
                            input("Enter end index: ")
                        )

                        result = analyzer.slice_array(
                            slice(start, end)
                        )

                    # 2D SLICING
                    elif current_array.ndim == 2:

                        print(
                            "\nExample: "
                            "Rows 0:2 and Columns 1:3"
                        )

                        row_start = int(
                            input("Enter row start: ")
                        )

                        row_end = int(
                            input("Enter row end: ")
                        )

                        column_start = int(
                            input("Enter column start: ")
                        )

                        column_end = int(
                            input("Enter column end: ")
                        )

                        result = analyzer.slice_array(
                            (
                                slice(
                                    row_start,
                                    row_end
                                ),
                                slice(
                                    column_start,
                                    column_end
                                )
                            )
                        )

                    # 3D SLICING
                    elif current_array.ndim == 3:

                        print(
                            "\nExample: "
                            "Depth 0:2, Rows 0:2, "
                            "Columns 0:2"
                        )

                        depth_start = int(
                            input("Enter depth start: ")
                        )

                        depth_end = int(
                            input("Enter depth end: ")
                        )

                        row_start = int(
                            input("Enter row start: ")
                        )

                        row_end = int(
                            input("Enter row end: ")
                        )

                        column_start = int(
                            input("Enter column start: ")
                        )

                        column_end = int(
                            input("Enter column end: ")
                        )

                        result = analyzer.slice_array(
                            (
                                slice(
                                    depth_start,
                                    depth_end
                                ),
                                slice(
                                    row_start,
                                    row_end
                                ),
                                slice(
                                    column_start,
                                    column_end
                                )
                            )
                        )

                    else:
                        raise ValueError(
                            "Unsupported array dimension."
                        )

                    print("\nSliced Array:")
                    print(result)

                else:

                    print(
                        "Invalid choice."
                    )

            except (
                ValueError,
                IndexError,
                TypeError
            ) as e:

                print(f"\nError: {e}")

        # =================================================
        # OPTION 4: MATHEMATICAL OPERATIONS
        # =================================================
        elif choice == "4":

            print("\nMATHEMATICAL OPERATIONS")
            print("-" * 35)
            print("1. Addition")
            print("2. Subtraction")
            print("3. Multiplication")
            print("4. Division")
            print("5. Dot Product")
            print("6. Matrix Multiplication")

            operation_choice = input(
                "Enter your choice: "
            ).strip()

            try:

                # -----------------------------------------
                # BASIC OPERATIONS
                # -----------------------------------------
                if operation_choice in [
                    "1",
                    "2",
                    "3",
                    "4"
                ]:

                    second_array = get_second_array()

                    operation_map = {
                        "1": "add",
                        "2": "subtract",
                        "3": "multiply",
                        "4": "divide"
                    }

                    operation = operation_map[
                        operation_choice
                    ]

                    result = analyzer.mathematical_operation(
                        second_array,
                        operation
                    )

                    print("\nResult:")
                    print(result)

                # -----------------------------------------
                # DOT PRODUCT / MATRIX MULTIPLICATION
                # -----------------------------------------
                elif operation_choice in [
                    "5",
                    "6"
                ]:

                    print(
                        "\nEnter second 2D array"
                    )

                    rows = int(
                        input("Enter number of rows: ")
                    )

                    columns = int(
                        input("Enter number of columns: ")
                    )

                    if rows <= 0 or columns <= 0:
                        raise ValueError(
                            "Rows and columns must be greater than 0."
                        )

                    second_array = get_array_with_shape(
                        (rows, columns)
                    )

                    if operation_choice == "5":

                        result = analyzer.dot_product(
                            second_array
                        )

                    else:

                        result = analyzer.matrix_multiplication(
                            second_array
                        )

                    print("\nResult:")
                    print(result)

                else:

                    print(
                        "Invalid operation choice."
                    )

            except (
                ValueError,
                TypeError
            ) as e:

                print(f"\nError: {e}")

        # =================================================
        # OPTION 5: COMBINE / SPLIT
        # =================================================
        elif choice == "5":

            print("\nCOMBINE / SPLIT ARRAYS")
            print("-" * 35)
            print("1. Combine Arrays")
            print("2. Split Array")

            sub_choice = input(
                "Enter your choice: "
            ).strip()

            try:

                current_array = analyzer.get_array()

                if current_array is None:
                    raise ValueError(
                        "Please create an array first."
                    )

                # -----------------------------------------
                # COMBINE
                # -----------------------------------------
                if sub_choice == "1":

                    print(
                        "\nCurrent Array Shape:"
                    )

                    print(
                        current_array.shape
                    )

                    axis = int(
                        input(
                            f"Enter axis "
                            f"(0 to {current_array.ndim - 1}): "
                        )
                    )

                    if (
                        axis < 0
                        or axis >= current_array.ndim
                    ):
                        raise ValueError(
                            "Invalid axis."
                        )

                    print(
                        "\nEnter shape of second array."
                    )

                    shape_values = []

                    for dimension in range(
                        current_array.ndim
                    ):

                        value = int(
                            input(
                                f"Enter size for "
                                f"dimension {dimension}: "
                            )
                        )

                        if value <= 0:
                            raise ValueError(
                                "Shape values must be greater than 0."
                            )

                        shape_values.append(value)

                    second_array = get_array_with_shape(
                        tuple(shape_values)
                    )

                    result = analyzer.combine_arrays(
                        second_array,
                        axis
                    )

                    print(
                        "\nArrays Combined Successfully!"
                    )

                    print("\nResult:")
                    print(result)

                    print("\nNew Shape:")
                    print(result.shape)

                # -----------------------------------------
                # SPLIT
                # -----------------------------------------
                elif sub_choice == "2":

                    print(
                        "\nCurrent Array Shape:"
                    )

                    print(
                        current_array.shape
                    )

                    sections = int(
                        input(
                            "Enter number of sections: "
                        )
                    )

                    axis = int(
                        input(
                            f"Enter axis "
                            f"(0 to {current_array.ndim - 1}): "
                        )
                    )

                    result = analyzer.split_array(
                        sections,
                        axis
                    )

                    print(
                        "\nArray Split Successfully!"
                    )

                    for index, part in enumerate(
                        result,
                        start=1
                    ):

                        print(
                            f"\nPart {index}:"
                        )

                        print(part)

                else:

                    print(
                        "Invalid choice."
                    )

            except (
                ValueError,
                TypeError
            ) as e:

                print(f"\nError: {e}")

        # =================================================
        # OPTION 6: SEARCH / SORT / FILTER
        # =================================================
        elif choice == "6":

            print("\nSEARCH / SORT / FILTER")
            print("-" * 35)
            print("1. Search Value")
            print("2. Sort Ascending")
            print("3. Sort Descending")
            print("4. Filter Array")

            sub_choice = input(
                "Enter your choice: "
            ).strip()

            try:

                current_array = analyzer.get_array()

                if current_array is None:
                    raise ValueError(
                        "Please create an array first."
                    )

                # -----------------------------------------
                # SEARCH
                # -----------------------------------------
                if sub_choice == "1":

                    value = convert_value(
                        input(
                            "Enter value to search: "
                        )
                    )

                    positions = analyzer.search_value(
                        value
                    )

                    if len(positions[0]) == 0:

                        print(
                            "\nValue not found in the array."
                        )

                    else:

                        print(
                            "\nValue found at position(s):"
                        )

                        print(positions)

                # -----------------------------------------
                # ASCENDING
                # -----------------------------------------
                elif sub_choice == "2":

                    result = analyzer.sort_array(
                        descending=False
                    )

                    print(
                        "\nArray Sorted in "
                        "Ascending Order:"
                    )

                    print(result)

                # -----------------------------------------
                # DESCENDING
                # -----------------------------------------
                elif sub_choice == "3":

                    result = analyzer.sort_array(
                        descending=True
                    )

                    print(
                        "\nArray Sorted in "
                        "Descending Order:"
                    )

                    print(result)

                # -----------------------------------------
                # FILTER
                # -----------------------------------------
                elif sub_choice == "4":

                    print(
                        "\nAvailable Conditions:"
                    )

                    print(
                        ">   Greater than"
                    )

                    print(
                        "<   Less than"
                    )

                    print(
                        ">=  Greater than or equal to"
                    )

                    print(
                        "<=  Less than or equal to"
                    )

                    print(
                        "==  Equal to"
                    )

                    print(
                        "!=  Not equal to"
                    )

                    condition = input(
                        "Enter condition: "
                    ).strip()

                    if not analyzer.is_valid_condition(
                        condition
                    ):
                        raise ValueError(
                            "Invalid condition."
                        )

                    value = convert_value(
                        input(
                            "Enter comparison value: "
                        )
                    )

                    result = analyzer.filter_array(
                        condition,
                        value
                    )

                    print(
                        "\nFiltered Array:"
                    )

                    print(result)

                else:

                    print(
                        "Invalid choice."
                    )

            except (
                ValueError,
                TypeError
            ) as e:

                print(f"\nError: {e}")

        # =================================================
        # OPTION 7: AGGREGATES / STATISTICS
        # =================================================
        elif choice == "7":

            print(
                "\nAGGREGATES AND STATISTICS"
            )

            print("-" * 35)

            print("1. Sum")
            print("2. Mean")
            print("3. Median")
            print("4. Standard Deviation")
            print("5. Variance")
            print("6. Minimum")
            print("7. Maximum")
            print("8. Percentile")
            print("9. Correlation Coefficient")

            sub_choice = input(
                "Enter your choice: "
            ).strip()

            try:

                current_array = analyzer.get_array()

                if current_array is None:
                    raise ValueError(
                        "Please create an array first."
                    )

                # -----------------------------------------
                # SUM
                # -----------------------------------------
                if sub_choice == "1":

                    result = analyzer.calculate_sum()

                    print("\nSum:")
                    print(result)

                # -----------------------------------------
                # MEAN
                # -----------------------------------------
                elif sub_choice == "2":

                    result = analyzer.calculate_mean()

                    print("\nMean:")
                    print(result)

                # -----------------------------------------
                # MEDIAN
                # -----------------------------------------
                elif sub_choice == "3":

                    result = analyzer.calculate_median()

                    print("\nMedian:")
                    print(result)

                # -----------------------------------------
                # STANDARD DEVIATION
                # -----------------------------------------
                elif sub_choice == "4":

                    result = (
                        analyzer
                        .calculate_standard_deviation()
                    )

                    print(
                        "\nStandard Deviation:"
                    )

                    print(result)

                # -----------------------------------------
                # VARIANCE
                # -----------------------------------------
                elif sub_choice == "5":

                    result = (
                        analyzer
                        .calculate_variance()
                    )

                    print("\nVariance:")
                    print(result)

                # -----------------------------------------
                # MINIMUM
                # -----------------------------------------
                elif sub_choice == "6":

                    result = (
                        analyzer
                        .calculate_minimum()
                    )

                    print("\nMinimum:")
                    print(result)

                # -----------------------------------------
                # MAXIMUM
                # -----------------------------------------
                elif sub_choice == "7":

                    result = (
                        analyzer
                        .calculate_maximum()
                    )

                    print("\nMaximum:")
                    print(result)

                # -----------------------------------------
                # PERCENTILE
                # -----------------------------------------
                elif sub_choice == "8":

                    percentile = float(
                        input(
                            "Enter percentile (0-100): "
                        )
                    )

                    result = (
                        analyzer
                        .calculate_percentile(
                            percentile
                        )
                    )

                    print(
                        f"\n{percentile}th Percentile:"
                    )

                    print(result)

                # -----------------------------------------
                # CORRELATION
                # -----------------------------------------
                elif sub_choice == "9":

                    print(
                        "\nEnter second 1D array "
                        "for correlation."
                    )

                    second_array = get_second_array()

                    result = (
                        analyzer
                        .calculate_correlation(
                            second_array
                        )
                    )

                    print(
                        "\nCorrelation Coefficient:"
                    )

                    print(result)

                else:

                    print(
                        "Invalid choice."
                    )

            except (
                ValueError,
                TypeError
            ) as e:

                print(f"\nError: {e}")

        # =================================================
        # OPTION 8: EXIT
        # =================================================
        elif choice == "8":

            print("\n" + "=" * 55)
            print(
                "Thank you for using NumPy Analyzer!"
            )
            print("=" * 55)

            break

        # =================================================
        # INVALID MAIN MENU CHOICE
        # =================================================
        else:

            print(
                "\nInvalid choice. "
                "Please enter a number from 1 to 8."
            )


# =====================================================
# PROGRAM START
# =====================================================
if __name__ == "__main__":
    main()