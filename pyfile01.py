# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 11:04:51 2024

@author: 33553904
"""

print("My first python file/script/recipe")

#This is my first comment

import pandas

file = pandas.read_csv("country_data.csv")

print(file.info())

print(file)

print(file.describe())

file = pandas.read_csv("iris.csv")

print(file.info())

print(file)

print(file.describe())

file = pandas.read_csv("insurance_data.csv" , skiprows=5)

print(file)

file = pandas.read_csv("diab_data.csv")

columns_names = ["A","B","C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N"]

file = pandas.read_csv("housing_data.csv", names=columns_names)

print("WHAT HAPPENDED")


