#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 11:08:59 2024

@author: yadir
"""

import numpy as np

print("\n")
python_list = [1,2,3,6,8,9]
array=np.array(python_list)
print(array)
print("\n")

matriz1 = np.zeros(10,dtype=int)
print(matriz1)

print("\n")
matriz2 = np.ones((3,5),dtype=float)
print(matriz2)

print("\n")
matriz3 = np.arange(0,100,10)
print(matriz3)

print("\n")
random_generator = np.random.RandomState(10)
matriz4 = random_generator.rand(3,3)
print(matriz4)

print("\n")
matriz5 = random_generator.randint(0,10,(3,3))
print(matriz5)

#Indexing - slicing'


print("\n")
one_de_array = np.arange(10)
print(one_de_array)

print("\n")
print(one_de_array[:5])

print("\n")
print(one_de_array[::5])

print("\n")
print(one_de_array[1::5])

print("\n")
lista_indices = [1,2,-3]
print(one_de_array[lista_indices])

print("\n")
randor_generator = np.random.RandomState(10)
two_de_array = randor_generator.randint(0,10,(3,4))
print(two_de_array)

print("\n")
randor_generator_seed = np.random.default_rng(40)
print(randor_generator_seed.integers(0,10,(3,4)))


print("\n")
randor_generator_seed = np.random.default_rng(40)
low=0
high=10
size=(3,4)

print(randor_generator_seed.integers(low,high,size))

#Vectorizacion
print("\n")
a = np.array([0,3,5])
b = np.array([1,2,3])

print(a+b)

print("\n")
a=np.array([0,3,5])
b=5
print(a+b)

print("\n")
a=np.ones((3,3))
b=np.array([1,2,3])
print(a+b)
