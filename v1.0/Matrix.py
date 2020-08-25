# Matrix Mathematics Library v1.0.0
# Author: Amy Burnett
# Date:   August 25 2020
##########################################################################

from random import seed 
from random import random 

##########################################################################
# Global Vars 

SINGLE_ROW = 0
SINGLE_COL = 1

##########################################################################

class Matrix: 

    ######################################################################
    # CREATION
    ######################################################################
    
    # Ctor 
    # Constructs a (rows x cols) matrix 
    # filled with fill_val 
    # if fill_val is not given, matrix is filled with 
    # zero values 
    def __init__ (self, rows, cols, fill_val = 0):

        # Ensure given rows and columns are valid 
        if(rows <= 0 or cols <= 0):
            print (rows + " x " + cols + " is not a valid dimension")
            print ("Rows/Cols must be an integer larger than 0")
            return None

        # Renaming instance methods for a cleaner interface  
        self.add = self._instance_add 
        self.subtract = self._instance_subtract 
        self.multiply = self._instance_multiply 
        self.map = self._instance_map

        self.rows = rows
        self.cols = cols

        # initialize matrix data
        self.data = []
        for i in range(rows):
            self.data += [[]]
            for j in range(cols):
                self.data[i] += [fill_val]

    ######################################################################
    # DATA MANIPULATION
    ######################################################################

    # Fills the matrix with random values 
    # in the range of [low,high] with an optional seed
    # seed is defaulted to 1 
    # if low, high isnt specified, then random numbers are 
    # floating points numbers from 0 to 1 
    def randomize (self, low = 0, high = 1, seed_value = 1):
        # Ensure user entered valid values 
        if low >= high: 
            print (f"in matrix.randomize() - incorrect random value range ({low},{high})")
            return 

        seed(seed_value)
        for i in range(self.rows):
            for j in range(self.cols):
                self.data[i][j] = low + (random() * (high - low))

    ######################################################################

    # Converts single column or single row matrices to arrays 
    def to_array (self):
        # Ensure matrix can be simplified down to an array
        # - only one column or one row
        if(self.rows != 1 and self.cols != 1):
            print("In matrix.to_array()")
            print("   this matrix cannot be converted to an array")
            print("   must have 1 row or 1 column only")
            return None
        
        # Convert to array 
        # 1 row
        if(self.rows == 1):
            return self.data[0];

        # 1 column
        elif (self.cols == 1):
            arr = []

            for i in range(self.rows):
                arr += [self.data[i][0]]

            return arr
    
    ######################################################################

    # Converts and returns an array into a matrix 
    # the array is converted from a single row to a single column by default
    # use Const SINGLE_ROW/SINGLE_COLUMN
    @staticmethod
    def from_array(arr, type):

        # Ensure given arr exists and is valid 
        if (not isinstance(arr, list)):
            print("In Matrix.from_array()")
            print("   Cannot convert to Matrix")
            print("   an array can only be converted to a matrix")
            return None

        # Single Column Format 
        if (type == SINGLE_COL):
            # Create matrix 
            matrix = Matrix(len(arr), 1)

            # Add data to matrix 
            for i in range(matrix.rows):
                matrix.data[i][0] = arr[i]
            
            return matrix
        
        
        # Single Row Format
        elif (type == SINGLE_ROW):
             # Create matrix 
             matrix = Matrix(1, len(arr))

             # Add data to matrix 
             for i in range(matrix.cols):
                 matrix.data[0][i] = arr[i]
             
             return matrix

        # Wrong format 
        return None 
        
    ######################################################################
    # MATHEMATICS 
    ######################################################################
    
    # Adds a scalar or another matrix to this matrix 
    # Note: this matrix is affected while the other is not
    def _instance_add(self, other):
        # ElementWise Addition
        if(isinstance(other, Matrix)):

            # Ensure matrices have the same dimensions
            if (other.rows != self.rows or other.cols != self.cols):
                print("matrices must have the same dimensions")
                print("to preform elementwise addition")
                print("this: " + str(self.rows) + "x" + str(self.cols))
                print("other: " + str(other.rows) + "x" + (other.cols))
                return

            # Add cooresponding elements to this matrix
            for i in range(self.rows):
                for j in range(self.cols):
                    self.data[i][j] += other.data[i][j]

        # Scalar Addition
        else:
            for i in range(self.rows):
                for j in range(self.cols):
                    self.data[i][j] += other

    ######################################################################

    # subtract a scalar or another matrix to this matrix 
    # Note: this matrix is affected while the other is not
    def _instance_subtract(self, other):
        # ElementWise subtract
        if(isinstance(other, Matrix)):

            # Ensure matrices have the same dimensions
            if (other.rows != self.rows or other.cols != self.cols):
                print("matrices must have the same dimensions")
                print("to preform elementwise subtract")
                print("this: " + str(self.rows) + "x" + str(self.cols))
                print("other: " + str(other.rows) + "x" + (other.cols))
                return

            # subtract cooresponding elements to this matrix
            for i in range(self.rows):
                for j in range(self.cols):
                    self.data[i][j] -= other.data[i][j]

        # Scalar subtract
        else:
            for i in range(self.rows):
                for j in range(self.cols):
                    self.data[i][j] -= other

    ######################################################################

    # multiply a scalar or another matrix to this matrix 
    # Note: this matrix is affected while the other is not
    def _instance_multiply(self, other):
        # ElementWise subtract
        if(isinstance(other, Matrix)):

            # Ensure matrices have the same dimensions
            if (other.rows != self.rows or other.cols != self.cols):
                print("matrices must have the same dimensions")
                print("to preform elementwise multiply")
                print("this: " + str(self.rows) + "x" + str(self.cols))
                print("other: " + str(other.rows) + "x" + (other.cols))
                return

            # multiply cooresponding elements to this matrix
            for i in range(self.rows):
                for j in range(self.cols):
                    self.data[i][j] *= other.data[i][j]

        # Scalar multiply
        else:
            for i in range(self.rows):
                for j in range(self.cols):
                    self.data[i][j] *= other

    ######################################################################

    # Tests if a given matrix equals this matrix
    def _instance_equals(self, other):
        # Ensure that given matrix matches the dimensions of this matrix 
        if(other.rows != self.rows or other.cols != self.cols):
            return False

        # Ensure data matches 
        for i in range(self.rows):
            for j in range(self.cols):
                # Returns false if elements are not equal
                if(self.data[i][j] != other.data[i][j]):
                    return False
        return True
    
    # Applies a given function to each element of this matrix
    def _instance_map(self, f):
        for i in range(self.rows):
            for j in range(self.cols):
                # pass through function
                self.data[i][j] = f(self.data[i][j])
                
    ######################################################################
    # STATIC METHODS
    ######################################################################
    

    # Adds a scalar or another matrix to a given matrix 
    # first parameter must be a matrix  
    # Note: none of the matrices are modified 
    @staticmethod
    def add(a, b):

        # Ensure a is a matrix 
        if (not isinstance(a, Matrix)):
            print("In Matrix.add()")
            print(f"   {a} is not a matrix")

        # ElementWise Addition
        if(isinstance(b, Matrix)):

            # Ensure matrices have the same dimensions
            if (b.rows != a.rows or b.cols != a.cols):
                print("matrices must have the same dimensions")
                print("to preform elementwise addition")
                print("a: " + str(a.rows) + "x" + str(a.cols))
                print("b: " + str(b.rows) + "x" + (b.cols))
                return None

            c = Matrix(a.rows, a.cols)

            # Add matrices together and store in third matrix 
            for i in range(a.rows):
                for j in range(a.cols):
                    c.data[i][j] = a.data[i][j] + b.data[i][j]

            return c

        # Scalar Addition
        else:
            c = Matrix(a.rows, a.cols)

            # add scalar to each matrix element and store in c 
            for i in range(a.rows):
                for j in range(a.cols):
                    c.data[i][j] = a.data[i][j] + b
            
            return c

    ######################################################################

    # subtracts a scalar or another matrix to a given matrix 
    # first parameter must be a matrix  
    # order is a - b
    # Note: none of the matrices are modified 
    @staticmethod
    def subtract(a, b):

        # Ensure a is a matrix 
        if (not isinstance(a, Matrix)):
            print("In Matrix.subtract()")
            print(f"   {a} is not a matrix")

        # ElementWise 
        if(isinstance(b, Matrix)):

            # Ensure matrices have the same dimensions
            if (b.rows != a.rows or b.cols != a.cols):
                print("matrices must have the same dimensions")
                print("to preform elementwise subtract")
                print("a: " + str(a.rows) + "x" + str(a.cols))
                print("b: " + str(b.rows) + "x" + (b.cols))
                return None

            c = Matrix(a.rows, a.cols)

            # Add matrices together and store in third matrix 
            for i in range(a.rows):
                for j in range(a.cols):
                    c.data[i][j] = a.data[i][j] - b.data[i][j]

            return c

        # Scalar 
        else:
            c = Matrix(a.rows, a.cols)

            # add scalar to each matrix element and store in c 
            for i in range(a.rows):
                for j in range(a.cols):
                    c.data[i][j] = a.data[i][j] - b
            
            return c

    ######################################################################

    # multiply a scalar or another matrix to a given matrix 
    # first parameter must be a matrix  
    # Note: none of the matrices are modified 
    @staticmethod
    def multiply(a, b):

        # Ensure a is a matrix 
        if (not isinstance(a, Matrix)):
            print("In Matrix.multiply()")
            print(f"   {a} is not a matrix")

        # ElementWise 
        if(isinstance(b, Matrix)):

            # Ensure matrices have the same dimensions
            if (b.rows != a.rows or b.cols != a.cols):
                print("matrices must have the same dimensions")
                print("to preform elementwise subtract")
                print("a: " + str(a.rows) + "x" + str(a.cols))
                print("b: " + str(b.rows) + "x" + (b.cols))
                return None

            c = Matrix(a.rows, a.cols)

            # Add matrices together and store in third matrix 
            for i in range(a.rows):
                for j in range(a.cols):
                    c.data[i][j] = a.data[i][j] * b.data[i][j]

            return c

        # Scalar 
        else:
            c = Matrix(a.rows, a.cols)

            # add scalar to each matrix element and store in c 
            for i in range(a.rows):
                for j in range(a.cols):
                    c.data[i][j] = a.data[i][j] * b
            
            return c

    ######################################################################

    # Multiplies two given matrices together 
    # Using the matrix product method
    @staticmethod
    def dot(a, b):
        # Ensure given are matrices 
        if(isinstance(a, Matrix) and isinstance(b, Matrix)):

            # Ensure Matrix Multiplication can be applied
            # - Columns of 'a' must equal rows of 'b'
            if(a.cols == b.rows):

                # Create Product matrix
                # - with rows of 'a' and columns of 'b'
                product = Matrix(a.rows, b.cols)

                # Each row of 'a' multiplied by each column of 'b'
                for i in range(a.rows):
                    for j in range(b.cols):

                        # dot-product
                        # each elem in 'a's row are
                        # multiplied by cooresponding elements in 'b's column
                        # and added together 
                        for elem in range(a.cols):
                            product.data[i][j] += a.data[i][elem] * b.data[elem][j]

                return product
        return None

    ######################################################################

    # Returns given matrix transposed
    # -Rows become columns 
    # -Columns become rows
    @staticmethod
    def transpose(m):
        # Create new transposed matrix
        transposedMatrix = Matrix(m.cols, m.rows)
        # Copy Transposed Data
        for i in range(m.rows):
            for j in range(m.cols):
                transposedMatrix.data[j][i] = m.data[i][j]
        return transposedMatrix

    ######################################################################

    # Applies a given function to elements of a given matrix
    # returns a new matrix of the application
    # Note: original matrix is unnaffected
    @staticmethod 
    def map(m, fn):
        matrix = Matrix(m.rows, m.cols)
        for i in range(m.rows):
            for j in range(m.cols):
                # pass through function
                matrix.data[i][j] = fn(m.data[i][j])
        return matrix

    ######################################################################

    # Returns a copy of the given matrix
    @staticmethod
    def copy(matrix):
        
        # Creates new matrix 
        newMatrix = Matrix(matrix.rows, matrix.cols)

        # Copy data to new matrix 
        for i in range(matrix.rows):
            for j in range(matrix.cols):
                newMatrix.data[i][j] = matrix.data[i][j]
        return newMatrix


    ######################################################################
    # DISPLAYING
    ######################################################################
    

    def to_string (self):
        output = ""
        for i in range(self.rows):
            for j in range(self.cols):
                output += str(self.data[i][j]) + " "
            output += "\n"
        return output

    ######################################################################


    # Prints the matrix in a row/column format
    def print (self):
        print (self.to_string())

##########################################################################



