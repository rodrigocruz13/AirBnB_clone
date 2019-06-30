#!/usr/bin/python3
from models import storage
from models.base_model import BaseModel

all_objs = storage.all()
print("-- Reloaded objects --")
for obj_id in all_objs.keys():
    obj = all_objs[obj_id]
    print(obj)

print("-- Create a new object --")
my_model = BaseModel()
print("created")
my_model.name = "Holberton"
print("holberton add")
my_model.my_number = 89
print("89 add")
my_model.save()
print("save done")
print(my_model)
