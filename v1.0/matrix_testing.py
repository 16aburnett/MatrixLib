# Unit Testing for my matrix library 
# Author: Amy Burnett
# Date:   August 25 2020

from Matrix1.0 import Matrix 
from Matrix1.0 import SINGLE_COL
from Matrix1.0 import SINGLE_ROW

##########################################################################
# testing functions 

def test (test_name, actual, expected):
    print (test_name, end=" - ")
    if actual == expected:
        print ("SUCCESS")
        return True
    else:
        print ("FAILED")
        print ("Actual:   ")
        print ("---------------")
        print (actual)
        print ("---------------")
        print ("Expected: ")
        print ("---------------")
        print (expected)
        print ("---------------")
        return False

def test_constructor():
    print ("============================")
    print ("Testing Constructor")

    # constructing a simple 3x3 matrix 
    a = Matrix(3,3)
    if not test("   Creating 3x3 Matrix", a.to_string(), "0 0 0 \n0 0 0 \n0 0 0 \n"):
        return False
    
    # constructing a 3x3 matrix filled with 7s 
    a = Matrix(3,3,7)
    if not test("   Creating 3x3 Matrix filled with 7", a.to_string(), "7 7 7 \n7 7 7 \n7 7 7 \n"):
        return False

    return True


def test_randomize():
    print ("============================")
    print ("Testing Randomize")

    # Ensure simple randomize call works 
    a = Matrix(3,3)
    a.randomize()
    if not test("   Filling with random numbers with default range", a.to_string(), "0.13436424411240122 0.8474337369372327 0.763774618976614 \n0.2550690257394217 0.49543508709194095 0.4494910647887381 \n0.651592972722763 0.7887233511355132 0.0938595867742349 \n"):
        return False
    
    return True

def test_to_array():
    print ("============================")
    print ("Testing to_array")

    # Ensure single column matrix works
    a = Matrix(3,1)
    arr = a.to_array()
    if not test("   Converting Single Column Matrix to Array", arr, [0,0,0]):
        return False
        
    # Ensure single row matrix works
    a = Matrix(1,4)
    arr = a.to_array()
    if not test("   Converting Single Row Matrix to Array", arr, [0,0,0,0]):
        return False

    return True

def test_from_array():
    print ("============================")
    print ("Testing from_array")

    # Ensure array to single row matrix 
    a = [1,2,3,4]
    matrix = Matrix.from_array(a,SINGLE_ROW)
    if not test("   Array to Single Row Matrix", matrix.to_string(), "1 2 3 4 \n"):
        return False
        
    # Ensure array to single column matrix 
    matrix = Matrix.from_array(a,SINGLE_COL)
    if not test("   Array to Single Column Matrix", matrix.to_string(), "1 \n2 \n3 \n4 \n"):
        return False

    return True

def test_add():
    print ("============================")
    print ("Testing addition")

    # Matrix plus matrix 
    a = Matrix(3,3)
    a.data = [[1,2,3],[4,5,6],[7,8,9]]
    b = Matrix(3,3)
    b.data = [[5,6,7],[8,9,10],[11,12,13]]
    a.add(b)
    if not test("   Matrix plus Matrix", a.to_string(), "6 8 10 \n12 14 16 \n18 20 22 \n"):
        return False
        
    # Matrix plus matrix static 
    a = Matrix(3,3)
    a.data = [[1,2,3],[4,5,6],[7,8,9]]
    b = Matrix(3,3)
    b.data = [[5,6,7],[8,9,10],[11,12,13]]
    c = Matrix.add(a,b)
    if not test("   Matrix plus Matrix (static method)", c.to_string(), "6 8 10 \n12 14 16 \n18 20 22 \n"):
        return False

    # Matrix plus scalar
    a = Matrix(3,3)
    a.data = [[1,2,3],[4,5,6],[7,8,9]]
    a.add(7)
    if not test("   Matrix plus scalar", a.to_string(), "8 9 10 \n11 12 13 \n14 15 16 \n"):
        return False

    # Matrix plus scalar static
    a = Matrix(3,3)
    a.data = [[1,2,3],[4,5,6],[7,8,9]]
    b = Matrix.add(a, 7)
    if not test("   Matrix plus scalar (static method)", b.to_string(), "8 9 10 \n11 12 13 \n14 15 16 \n"):
        return False

    return True

def test_subtract():
    print ("============================")
    print ("Testing subtraction")

    # Matrix minus matrix 
    a = Matrix(3,3)
    a.data = [[1,2,3],[4,5,6],[7,8,9]]
    b = Matrix(3,3)
    b.data = [[5,6,7],[8,9,10],[11,12,13]]
    b.subtract(a)
    if not test("   Matrix minus Matrix", b.to_string(), "4 4 4 \n4 4 4 \n4 4 4 \n"):
        return False
        

    # Matrix minus matrix static method 
    a = Matrix(3,3)
    a.data = [[1,2,3],[4,5,6],[7,8,9]]
    b = Matrix(3,3)
    b.data = [[5,6,7],[8,9,10],[11,12,13]]
    c = Matrix.subtract(b,a)
    if not test("   Matrix minus Matrix (static method)", c.to_string(), "4 4 4 \n4 4 4 \n4 4 4 \n"):
        return False

    # Matrix minus scalar
    a = Matrix(3,3)
    a.data = [[1,2,3],[4,5,6],[7,8,9]]
    a.subtract(7)
    if not test("   Matrix plus scalar", a.to_string(), "-6 -5 -4 \n-3 -2 -1 \n0 1 2 \n"):
        return False

    # Matrix minus scalar static 
    a = Matrix(3,3)
    a.data = [[1,2,3],[4,5,6],[7,8,9]]
    b = Matrix.subtract(a, 7)
    if not test("   Matrix plus scalar (static method)", b.to_string(), "-6 -5 -4 \n-3 -2 -1 \n0 1 2 \n"):
        return False

    return True


def test_multiply():
    print ("============================")
    print ("Testing Multiplication")

    # Matrix times matrix 
    a = Matrix(3,3)
    a.data = [[1,2,3],[4,5,6],[7,8,9]]
    b = Matrix(3,3,2)
    b.multiply(a)
    if not test("   Matrix times Matrix", b.to_string(), "2 4 6 \n8 10 12 \n14 16 18 \n"):
        return False
        

    # Matrix times matrix static method 
    a = Matrix(3,3)
    a.data = [[1,2,3],[4,5,6],[7,8,9]]
    b = Matrix(3,3,2)
    c = Matrix.multiply(b,a)
    if not test("   Matrix times Matrix (static method)", c.to_string(), "2 4 6 \n8 10 12 \n14 16 18 \n"):
        return False

    # Matrix times scalar
    a = Matrix(3,3)
    a.data = [[1,2,3],[4,5,6],[7,8,9]]
    a.multiply(2)
    if not test("   Matrix times scalar", a.to_string(), "2 4 6 \n8 10 12 \n14 16 18 \n"):
        return False

    # Matrix times scalar static 
    a = Matrix(3,3)
    a.data = [[1,2,3],[4,5,6],[7,8,9]]
    b = Matrix.multiply(a, 2)
    if not test("   Matrix times scalar (static method)", b.to_string(), "2 4 6 \n8 10 12 \n14 16 18 \n"):
        return False

    return True


def test_dot():
    print ("============================")
    print ("Testing Dot Product")
        
    # dot product
    a = Matrix(3,3)
    a.data = [[1,2,3],[4,5,6],[7,8,9]]
    b = Matrix.copy(a)
    c = Matrix.dot(a,b)
    if not test("   Dot product (static method)", c.to_string(), "30 36 42 \n66 81 96 \n102 126 150 \n"):
        return False

    return True


def test_map():
    print ("============================")
    print ("Testing Map")
        
    # maping matrix 
    a = Matrix(3,3)
    a.data = [[1,2,3],[4,5,6],[7,8,9]]
    a.map(lambda a : a + 7)
    if not test("   Map (a -> a + 7)", a.to_string(), "8 9 10 \n11 12 13 \n14 15 16 \n"):
        return False

    # maping matrix static
    a = Matrix(3,3)
    a.data = [[1,2,3],[4,5,6],[7,8,9]]
    b = Matrix.map(a, lambda a : a + 7)
    if not test("   Map (a -> a + 7) (static method)", b.to_string(), "8 9 10 \n11 12 13 \n14 15 16 \n"):
        return False

    return True



def test_transpose():
    print ("============================")
    print ("Testing Transpose")

    # transpose matrix static
    a = Matrix(3,3)
    a.data = [[1,2,3],[4,5,6],[7,8,9]]
    b = Matrix.transpose(a)
    if not test("   Matrix Transpose", b.to_string(), "1 4 7 \n2 5 8 \n3 6 9 \n"):
        return False

    return True

##########################################################################
# Active tests 

test_constructor()
test_randomize()
test_to_array()
test_from_array()
test_add()
test_subtract()
test_multiply()
test_dot()
test_map()
test_transpose()



# work on a system that tests all
# and keeps track of correct without exiting early 
# maybe add a normalize function 

# add static functions for add, sub, mult 
# add a divide func? just for fun? 
# fun?


# functionality for adding a list to a matrix ? 