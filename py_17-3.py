Python 3.14.2 (tags/v3.14.2:df79316, Dec  5 2025, 17:18:21) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
import pandas as pd
df=pd.read_csv("C:/Users/karun/OneDrive/Desktop/python/Book1.csv")
df
   COURSE  MARKS
0      OS   17.0
1  PYTHON   17.5
2     IVC   16.0
df.shape
(3, 2)
len(df)
3
df.head(2)
   COURSE  MARKS
0      OS   17.0
1  PYTHON   17.5
import os
print(os.listdir("C:/Users/karun/OneDrive/Desktop/python"))
['age.py', 'basic_try_except.py', 'Book1.csv', 'catching_exception_object.py', 'COUNT WORDS.PY', 'divisible by 7.py', 'FAB1.PY', 'FAB2.PY', 'fac.py', 'FAC1.PY', 'factorial.py', 'fib.py', 'handling_multiple_exceptions_in_one_line.py', 'handling_specific_exception.py', 'largest.py', 'LIST.py', 'maximum value.py', 'multiple_except_blocks.py', 'p1.py', 'p10.py', 'p12-3.py', 'p1_05.py', 'p2_05.py', 'p3_5.py', 'p4_17.py', 'p5_19.py', 'py_10-3.py', 'py_17-3.py', 'raising_an_exception.py', 'rectangle.py', 'SET.py', 'si2.py', 'simple_caluclator.py', 'statistics.py', 'sum.py', 'temperature_convertor.py', 'try_except_with_file_handling.py', 'TUPLE.py', 'user_defined_exception_py.py', 'using_else_block.py', 'using_final_blocks.py']
import os
os.rename("reshape","py.shape")
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    os.rename("reshape","py.shape")
FileNotFoundError: [WinError 2] The system cannot find the file specified: 'reshape' -> 'py.shape'
os.rename("p1.txt","txt.py")
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    os.rename("p1.txt","txt.py")
FileNotFoundError: [WinError 2] The system cannot find the file specified: 'p1.txt' -> 'txt.py'
os.rename("C:/Users/karun/OneDrive/Desktop/python/p1.txt","p2.txt")
os.copy("p2.txt","C:/Users/karun/OneDrive/Desktop/python/reshape.py")
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    os.copy("p2.txt","C:/Users/karun/OneDrive/Desktop/python/reshape.py")
AttributeError: module 'os' has no attribute 'copy'
import shutil
shutil.copy("p2.txt","C:/Users/karun/OneDrive/Desktop/python/reshape.py")
'C:/Users/karun/OneDrive/Desktop/python/reshape.py'
shutil.move("p2.txt","C:/Users/karun/OneDrive/Desktop/python/reshape.py")
'C:/Users/karun/OneDrive/Desktop/python/reshape.py'
import numpy as np
array_Id=np.array([1,2,3,4,5])
print("ID Array:")
ID Array:
print(array_Id)
[1 2 3 4 5]

===================================================== RESTART: C:/Users/karun/OneDrive/Desktop/python/creating_a_1D_numpy_array.py =====================================================
1D Array:
[1 2 3 4 5]
array_2d=array_1d.reshape(2,3)
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    array_2d=array_1d.reshape(2,3)
NameError: name 'array_1d' is not defined. Did you mean: 'array_1D'?
array_2d=array_1D.reshape(2,3)
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    array_2d=array_1D.reshape(2,3)
ValueError: cannot reshape array of size 5 into shape (2,3)

============================================================= RESTART: C:/Users/karun/OneDrive/Desktop/python/reshaping.py =============================================================
Traceback (most recent call last):
  File "C:/Users/karun/OneDrive/Desktop/python/reshaping.py", line 1, in <module>
    array_2d=array_1d.reshape(2,2)
NameError: name 'array_1d' is not defined

============================================================= RESTART: C:/Users/karun/OneDrive/Desktop/python/reshaping.py =============================================================
Traceback (most recent call last):
  File "C:/Users/karun/OneDrive/Desktop/python/reshaping.py", line 1, in <module>
    array_2d=array_1D.reshape(2,2)
NameError: name 'array_1D' is not defined
array_1d=np.array([1,2,3,4,5,6])
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    array_1d=np.array([1,2,3,4,5,6])
NameError: name 'np' is not defined
import numpy as np
array_1d=np.array([1,2,3,4,5,6])
array_2d=array_1d.reshape(2,3)
print(array_2d)
[[1 2 3]
 [4 5 6]]
print("/n elements at position(1,2):",array_2d([1,2])

      print("/n elements at position(1,2):",array_2d[1,2])
      
SyntaxError: '(' was never closed
print("/n elements at position(1,2):",array_2d[1,2])
      
/n elements at position(1,2): 6
>>> array_2d[0,1]=10
...       
>>> print("\n modified array(after changing element at position(0,1)to 10):",array_2d)
...       

 modified array(after changing element at position(0,1)to 10): [[ 1 10  3]
 [ 4  5  6]]
>>> array_sum=np.sum(array_2d)
...       
>>> print(sum of all elements in the array:",array_sum)
...       
SyntaxError: unterminated string literal (detected at line 1)
>>> print("sum of all elements in the array:",array_sum)
...       
sum of all elements in the array: 29
>>> import numpy as np
>>> matrix_A=np.array([[1,2],[3,4]])
>>> matrix_B=np.array([[7,9],[9,5]])
>>> matrix_sum=np.add(matrix_A,matrix_B)
>>> print("matrix addition(A+B):",matrix_sum)
matrix addition(A+B): [[ 8 11]
 [12  9]]
>>> matrix_dot_elementwise=np.multiply(matrix_A,matrix_B)
>>> print("matrix multiplication(A*B):",matrix_dot_product)
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    print("matrix multiplication(A*B):",matrix_dot_product)
NameError: name 'matrix_dot_product' is not defined
>>> print("elementwise matrix multiplication(A*B):",matrix_dot_product)
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    print("elementwise matrix multiplication(A*B):",matrix_dot_product)
NameError: name 'matrix_dot_product' is not defined
>>> print("elementwise matrix multiplication(A*B):",matrix_dot_elementwise)
...       
elementwise matrix multiplication(A*B): [[ 7 18]
 [27 20]]
>>> matrix_dot_product=np.dot(matrix_A,matrix_B)
>>> print("matrix dot product(A.B):",matrix_dot_product)
matrix dot product(A.B): [[25 19]
 [57 47]]
>>> matrix_transpose=np.transpose(matrix_A)
>>> print("transpose of matrix A:",matrix_transpose)
transpose of matrix A: [[1 3]
 [2 4]]
