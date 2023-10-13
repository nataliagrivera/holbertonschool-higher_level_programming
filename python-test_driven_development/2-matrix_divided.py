def matrix_divided(matrix, div):
    # Check if matrix is a list of lists containing integers or floats
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix) or \
            not all(isinstance(element, (int, float)) for row in matrix for element in row):
        raise TypeError('matrix must be a matrix (list of lists) of integers/floats')
    
    # Check if each row of the matrix has the same size as the first row
    if len(set(len(row) for row in matrix)) > 1:
        raise TypeError('Each row of the matrix must have the same size')
    
    # Check if div is a number (integer or float) and not equal to 0
    if not isinstance(div, (int, float)):
        raise TypeError('div must be a number')
    if div == 0:
        raise ZeroDivisionError('division by zero')
    
    # Divide all elements of the matrix by div and round to 2 decimal places
    new_matrix = [[round(element / div, 2) for element in row] for row in matrix]
    
    return new_matrix
