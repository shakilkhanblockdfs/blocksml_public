import tensorflow as tf
import torch
import numpy as np
import pandas as pd

# We can specify the datatype in tensor constuctor itself
a = torch.tensor([7, 4, 3, 2, 6], dtype=torch.int64)
# a = torch.tensor([2.2])
print(a)
print(a.dtype)

a = torch.FloatTensor([0, 1, 2, 3])  # Creating explicit float tensor type
print(a)
print(a.type)
print(a.dtype)

# Change the tensor type from int to float
a = torch.tensor([1, 2, 3, 4])
a = a.type(torch.FloatTensor)
print(a.size())    # Gives the number of elements in tensor

print(a.ndimension())  # Gives the dimension or rank of a tensor
#################################

# convert a tensor from one dimention to multiple dimension

a = torch.tensor([1, 2, 3, 4, 5])
a_new = a.view(5, 1)  # New numer of rows and columns

# If we dont know the number of elements we can use -1 and depending on column torch will deduce automatically.
a_new = a.view(-1, 1)

#################################

# Convert numpy array to pytorch array and vice-versa

numpy_array = np.array([0, 1, 2, 3, 4])
torch_tensor = torch.from_numpy(numpy_array)
back_to_numpy = torch_tensor.numpy()

#################################
# convert a Panda series to torch

pandas_series = pd.Series([0.1, 2, 0, 10.1])
pandas_to_torch = torch.from_numpy(pandas_series.values)

#################################

# To return a list from the tensor

this_tensor = torch.tensor([0, 1, 2, 3])
torch_to_list = this_tensor.tolist()
print(torch_to_list)
print(type(torch_to_list))

#################################

# Vector addition in tensor

u = torch.tensor([0, 1])
v = torch.tensor([2, 4])
print(u+v)  # new tensor with 2,5

u = torch.tensor([1,3])
print(u*2)  # returns 2,6

# We can add a number to tensor as well
u = u+1
print(u)  # this will give 2,4
#################################

# product of two tensors

u = torch.tensor([0, 1])
v = torch.tensor([2, 4])
print(u*v)                     # the product is product of first numner and product of second number
                               ## [0,4]


