#!/usr/bin/python3
from models.base_model import BaseModel

my_model = BaseModel()
my_model.name = "Holberton"
my_model.my_number = 89
print(my_model.id)
print(my_model)
print(type(my_model.created_at))
print("--")
my_model_j = my_model.to_dict()
print(my_model_j)
print("JSON of my_model:")
for k in my_model_j.keys():
    print("\t{}: ({}) - {}".format(k, type(my_model_j[k]), my_model_j[k]))

print("--")
my_new_model = BaseModel(**my_model_j)
print(my_new_model.id)
print(my_new_model)
print(type(my_new_model.created_at))

print("--")
print(my_model is my_new_model)
