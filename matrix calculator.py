import numpy as np

last = 1
while last != 0:
    print("Which operation do you want to perform? Type the number corresponding to the operation:")
    print("1: Sum\n2: Multiplication\n3: Subtraction\n4: Division\n5: Transpose of matrices\n6: Trace of matrices")
    
    try:
        opp = int(input("Enter your choice: "))
        if opp not in range(1, 7):
            raise ValueError("Invalid choice.")
    except ValueError as e:
        print(e)
        continue
    
    try:
        a = int(input("Enter number of rows for matrix 1: "))
        b = int(input("Enter number of columns for matrix 1: "))
        print("Enter elements for matrix 1:")
        elements1 = [int(input(f"Element {i+1}: ")) for i in range(a * b)]
        matrix1 = np.array(elements1).reshape(a, b)
    except ValueError:
        print("Invalid input for matrix 1 dimensions or elements. Please try again.")
        continue

    try:
        f = int(input("Enter number of rows for matrix 2: "))
        j = int(input("Enter number of columns for matrix 2: "))
        print("Enter elements for matrix 2:")
        elements2 = [int(input(f"Element {i+1}: ")) for i in range(f * j)]
        matrix2 = np.array(elements2).reshape(f, j)
    except ValueError:
        print("Invalid input for matrix 2 dimensions or elements. Please try again.")
        continue

    try:
        if opp == 1:
            result = np.add(matrix1, matrix2)
            print("Sum of the matrices is:\n", result)
        elif opp == 2:
            if b != f:
                raise ValueError("Matrix multiplication is not possible with the given dimensions.")
            result = np.matmul(matrix1, matrix2)
            print("Multiplication of the matrices is:\n", result)
        elif opp == 3:
            result = np.subtract(matrix1, matrix2)
            print("Subtraction of the matrices is:\n", result)
        elif opp == 4:
            result = np.divide(matrix1, matrix2)
            print("Division of the matrices is:\n", result)
        elif opp == 5:
            transpose1 = np.transpose(matrix1)
            transpose2 = np.transpose(matrix2)
            print("Transpose of matrix 1:\n", transpose1)
            print("Transpose of matrix 2:\n", transpose2)
        elif opp == 6:
            trace1 = np.trace(matrix1)
            trace2 = np.trace(matrix2)
            print("Trace of matrix 1:", trace1)
            print("Trace of matrix 2:", trace2)
    except ValueError as e:
        print(f"Error in performing operation: {e}")
        continue

    last = input("Do you want to perform another operation? Type '1' for Yes, '0' for No: ")
    if last != '1':
        break

print("\nThanks for using the program!")
