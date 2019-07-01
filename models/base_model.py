#!/usr/bin/python3
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
        return ("[{}] ({}) {}".format(self.__class__.__name__, self.id,
                                      self.__dict__))

    def save(self):
        """
        updates the public instance attribute updated_at with the current
        datetime
        """
        self.updated_at = datetime.datetime.now()
        models.storage.save()



    def to_dict(self):
        dic = {}
        olddic = self.__dict__
        for key in olddic:
            if key == 'created_at' or key == 'updated_at':
                dic[key] = olddic[key].isoformat()
            else:
                dic[key] = olddic[key]
        dic['__class__'] = self.__class__.__name__
        return dic
