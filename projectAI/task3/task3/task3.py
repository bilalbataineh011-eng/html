import numpy as np
#part 1
a = np.zeros((2,2))
b = np.ones((1,2))
c = np.full((2,2), 7)
d = np.eye(2)
e = np.random.random((2,2))
print("a:\n", a)
print("b:\n", b)
print("c:\n", c)
print("d:\n", d)
print("e:\n", e)
x = np.array([[1,2],[3,4]])
print(np.sum(x))
print(np.sum(x, axis=0))
print(np.sum(x, axis=1))
print(*30*"-")
#part 2

def get_array(arr):
    arr_min=np.min(arr)
    arr_max=np.max(arr)
    arr_mean=np.mean(arr)
    arr_median=np.median(arr)
    print("Minimum=", arr_min)
    print("Maximum=", arr_max)
    print("Mean=", arr_mean)
    print("Median=", arr_median)
    return arr_min, arr_max, arr_mean, arr_median
random_array=np.random.random(10)
print("Random array:", random_array)
get_array(random_array)
#part 3
print(30*"-")
#part 3.1
print("1. Sum of all elements in the array")
myarray=np.arange(-1,5,0.25).reshape(3,8)
print("My array:\n", myarray)

print("Total sum:", np.sum(myarray))

#part 3.2
print("2. Sum of each row in the array")
row_sums = np.sum(myarray, axis=1) 
for i in range(len(row_sums)):
    print("Sum of row", i, ":", row_sums[i])

#part 3.3
print("3. Sum of each column in the array")
col_sums = np.sum(myarray, axis=0) 
for j in range(len(col_sums)):
    print("Sum of column", j, ":", col_sums[j])

#part 3.4
print("4. Find the maximum of all element in the array")
print("Maximum element:", np.max(myarray))

#part 3.5
print("5. Find the minimum of all elements in each row")
row_mins = np.min(myarray, axis=1) 
for i in range(len(row_mins)):
    print("Minimum element in row", i, ":", row_mins[i])

#part 3.6
print("6. Find the mean of all elements in each row")
row_means = np.mean(myarray, axis=1) 
for i in range(len(row_means)):
    print("Mean element in row", i, ":", row_means[i])

#part 3.7
print("7. Find the standard deviation column wise")
col_stds = np.std(myarray, axis=0) 
for j in range(len(col_stds)):
    print("Standard deviation in column", j, ":", col_stds[j])

#part 4
print(*30*"-")

A= np.arange(8, 28).reshape(4, 5)
B= np.full(20, 5).reshape(2,5,2)
C= np.arange(30,50,2).reshape(5,2)
D= np.array([12,22,-12,-22,200])
E= np.random.rand(4)
print("1. Calculate the cube of A vector and print the result.")
cube_A= A**3
print("Cube of A:\n", cube_A)
print("2. Perform C-B and store the result in a new array named by your name.")
Bilal= C-B
print("C-B:\n", Bilal)
print("3. A dot D")
AdotD= np.dot(A,D)
print("A dot D:\n", AdotD)

print("4. Multiply E by 5 and print the result")
NewE=E*5
print("E multiplied by 5:\n", NewE)
print("5. Slicing and dot product of A and C")
slicedA=A[1:3, 1:4]
slicedC=C[0:3, :]
slicedAdotD= np.dot(slicedA, slicedC)
print("Dot product of sliced A and C:\n", slicedAdotD)

