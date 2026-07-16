#NUMPY

import numpy as np
arr_1d = np.array([1, 2, 3, 4, 5])
print("1D array:",arr_1d)
arr_2d = np.array([[1, 2, 3, 4, 5],[6, 7, 8, 9, 10]])
print("2D array:\n",arr_2d)


py_list = [1,2,3]
print(py_list)
print("Python List Multiplication", py_list * 2)    #Python List Multiplication [1, 2, 3, 1, 2, 3]
print("Python Array Multiplication", arr_1d*2)      #Python Array Multiplication [ 2  4  6  8 10]


a = np.array([[2,4],[5,6]])
b = np.array([[5,6],[7,8]])
print("Python Array Multiplication with another array\n", a*b)      # multiplies corresponding elements. not like matrix multiplication.


# Time efficient
import time
start = time.time()
c = [i*2 for i in range(10)]
print("\n List Operation Time:", time.time() - start)
start = time.time()
d = np.arange(10) * 2
print("\n Numpy Operation Time:", time.time() - start)



# Creating array from scratch

zeroes = np.zeros((3,4))
print("zeros array:\n", zeroes)
ones = np.ones((4,3))
print("ones array:\n", ones)
full = np.full((2,2),7)
print("full array (constant value)\n", full)
random = np.random.random((2,3))
print("random array:\n", random)
sequence = np.arange(1,10,2)
print("sequence array :\n", sequence)


# Vector
vector = np.array([2,3,4])
print("Vector:",vector)

# Matrix
matrix = np.array([[2,4,6],
[3,5,7]])
print("Matrix:\n",matrix)

# Tensor
tensor = np.array([[[1,2],[3,4]],[[5,6],[7,8]],[[9,10],[11,12]]])
print("Tensor:\n",tensor)



# Properties
print("Shape", vector.shape , matrix.shape, tensor.shape)
print("Dimension",vector.ndim, matrix.ndim,tensor.ndim)
print("Size", vector.size,matrix.size, tensor.size)
print("Datatype", vector.dtype,matrix.dtype, tensor.dtype)


# array reshaping
e = np.arange(12)
print("OG array : \n", e)
e_reshaped = e.reshape((3,4))
print("Reshaped array : \n", e_reshaped)
e_flattened = e_reshaped.flatten()
print("Flattened array : \n", e_flattened)
""" ravel returns view instead of copy. flatten returns copy"""
e_raveled = e_reshaped.ravel()
print("Raveled array : \n", e_raveled)

# Transpose
e_reshaped_transpose = e_reshaped.T
print("Transposed array : \n", e_reshaped_transpose)



"""numpy array ops"""
# Indexing and Slicing
f = np.arange(1,11,1)
print("Basic Slicing :", f[2:7])
print("With step value :", f[2:7:2])
print("Negative Indexing :", f[-3])

f_2d = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(f_2d)
print("Specific Element : 2nd Row 3rd colm :" ,f_2d[1,2])
print("Specific Element : 1st Row 1st colm :" ,f_2d[0,0])
print("Entire Row :", f_2d[2])
print("Entire column :", f_2d[:,2])

# Sorting
unsorted = np.array([5,4,6,2,8,1,5,5,8,6,3,7,9])
print("Unsorted Array :", unsorted)
print("Sorted Array :", np.sort(unsorted))
g_2d_unsorted = np.array([[9,4,6],[1,8,7],[3,5,2]])
print("sorted 2d array by colm :\n", np.sort(g_2d_unsorted, axis=0))
print("sorted 2d array by row :\n", np.sort(g_2d_unsorted, axis=1 ))

# Filtering
h = np.array([1,2,3,4,5,6,7,8,9,10])
even_h = h[h%2==0]
print("whole array",h)
print("filtered even no array",even_h)

mask = h > 5        # filter using mask
print("no.s greater than 5 in array",h[mask])

# Fancy indexing vs np.where()
indices = [0,2,4]
print("using index",h[indices])   # Fancy indexing
where_result = np.where(h>5)
print("NP where", h[where_result])  # np.where() similar to mask
""" np.where(condition,true,false) """
condn_array = np.where(h > 5,h * 2, h*4)
print(condn_array)      # check the result

# Merging arrays
m = np.array([1,2,3])
n = np.array([4,5,6])
combined = m + n
print(combined) # sum
merge = np.concatenate((m,n))
print(merge)    #merge

# Array compatibility
o = np.array([7,8,9])
print("Compatibility shapes check :", m.shape == n.shape)

# Adding and removing data from array
og = np.array([[1,2],[3,4]])
"""adding new rows"""
new_row = np.array([[5,6]])
og_with_new_row = np.vstack((og,new_row))
print("og:",og)
print("og_with_new_row:",og_with_new_row)
"""adding new columns"""
new_col = np.array([[7],[8]])
og_with_new_col = np.hstack((og,new_col))
print("og_with_new_col",og_with_new_col)
"""deleting a element"""
t = np.array([1,2,3,4,5])
deleted = np.delete(t,2)     #deletes the 2nd element
print("array t after deletion:", deleted)
k = np.delete(og,[0,0]) #removes the element in the 1st row and 1st column
print("og",og)

print("og after deletion",k)


# Real World Data

# data structure : [rest_id,2022,2023,2024,2025]
sales_data = np.array([
        [1, 150000, 180000, 220000, 250000],  # Paradise Biryani
        [2, 120000, 140000, 160000, 110000],  # Beijing Bites
        [3, 200000, 230000, 260000, 300000],  # Pizza Hub
        [4, 180000, 210000, 250000, 270000],  # Burger Point
        [5, 160000, 185000, 205000, 230000]   # Chai Point
])
print("Zomato sales analysis \n","\n Sales data shape",sales_data.shape,"\n Sample data for 1st 3 restaurent \n",sales_data[:3])
print("Sample data for all restaurant without the rest id \n",sales_data[:,1:])
print("Sample data for all restaurant without the rest id and without sales in 2022 \n",sales_data[:,2:])
# Total sale per year
print(np.sum(sales_data,axis=0))
yearly_total = np.sum(sales_data[:,1:],axis=0)
print(yearly_total)
# Min sales
min_sales1 = np.min(sales_data[:,1:], axis=0)   # per year
min_sales2 = np.min(sales_data[:,1:], axis=1)   # per restaurant
print(min_sales1)
print(min_sales2)
# Max sales
max_sales1 = np.max(sales_data[:,1:], axis=0)   # per year
max_sales2 = np.max(sales_data[:,1:], axis=1)   # per restaurant
print(max_sales1)
print(max_sales2)
# Avg sales
avg_sales1 = np.mean(sales_data[:,1:], axis=0)   # per year
avg_sales2 = np.mean(sales_data[:,1:], axis=1)   # per restaurant
print(avg_sales1)
print(avg_sales2)
monthly_avg = sales_data[:,1:] /12
print(monthly_avg)
# Cumulative sales
cumsum1 = np.cumsum(sales_data[:,1:],axis=0)
cumsum2 = np.cumsum(sales_data[:,1:],axis=1)
print(cumsum1)      #year
print(cumsum2)      #restaurant
import matplotlib.pyplot as plt     # JUST TO PLOT THE DATA
plt.figure(figsize=(8,6))
plt.plot(np.mean(cumsum1,axis=0))
plt.title("Avg Cumulative sales across all restaurants")
plt.xlabel("years")
plt.ylabel("sales")
plt.grid(True)
plt.show()

# Vector Addition
vector1 = np.array([1,2,3,4,5])
vector2 = np.array([6,7,8,9,10])
print("Vector Addition : \n", vector1 + vector2)
print("Vector Multiplication : \n", vector1 * vector2)
print("Dot Product : \n", np.dot(vector1,vector2))
print("Angle btw the vectors : \n", np.arccos(np.dot(vector1,vector2) / (np.linalg.norm(vector1) * np.linalg.norm(vector2))))
angle = np.arccos(np.dot(vector1,vector2) / (np.linalg.norm(vector1) * np.linalg.norm(vector2)))
print(angle)

# Vectorise
restaurant_types = np.array(['biryani','chinese','pizza','burger','cafe'])
vectorized_upper = np.vectorize(str.upper)
print(vectorized_upper(restaurant_types))

