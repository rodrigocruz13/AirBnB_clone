#!/usr/bin/python3
""" Module that define the class BaseModel, the base of all proyect
"""
import uuid
import datetime
import models


class BaseModel():
    """
    BaseModel class, parent of other classes
    """

    def __init__(self, *args, **kwargs):
        """
        This class manage id attribute in all classes and helps to avoid
        duplicating the same code. So it will be in charge of counting
        the # of objects.
        *args: not used
        **kwargs: the imput dictionary to create a instance with this info
        Atributes:
        id (str): [pub] id of object
        created_at (datetime): [pub] - creation time
        updated_at (datetime): [pub] - modification time (the same when an
                                       instace is created)
        """

        if kwargs:
            create = {}
            for k in kwargs:
                if k != '__class__':
                    if k == 'created_at' or k == 'updated_at':
                        create[k] = datetime.datetime.strptime
                        (kwargs[k], "%Y-%m-%dT%H:%M:%S.%f")
                    else:
                        create[k] = kwargs[k]

            for key, value in create.items():
                setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()
            models.storage.new(self)

    def __str__(self):
        """
        Returns a formated output of the class
        """
        s_cn = self.__class__.__name__
        s_id = self.id
        s_di = self.__dict__
        return ("[{}] ({}) {}".format(s_cn, s_id, s_di))

    def save(self):
        """
        updates the public instance attribute updated_at with the current
        datetime
        """
        self.updated_at = datetime.datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        Returns a dict with all keys/values of __dict__ of the instance:
        - by using self.__dict__, only instance attributes set will be returned
        - a key __class__ must be added to this dictionary with the class name
        of the object
        - created_at and updated_at must be converted to string object in ISO
        format: --format: %Y-%m-%dT%H:%M:%S.%f (ex: 2017-06-14T22:31:03.285259)
        ---you can use isoformat() of datetime object
        """

        dic = {}
        olddic = self.__dict__
        for key in olddic:
            if key == 'created_at' or key == 'updated_at':
                dic[key] = olddic[key].isoformat()
            else:
                dic[key] = olddic[key]
        dic['__class__'] = self.__class__.__name__
        return dic
