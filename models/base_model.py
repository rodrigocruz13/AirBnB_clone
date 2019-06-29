#!/usr/bin/python3
import uuid
import datetime

class BaseModel():
    """
    BaseModel class, parent of other classes
    """

    def __init__(self):
        """
        This class manage id attribute in all classes and helps to avoid
        duplicating the same code. So it will be in charge of counting
        the # of objects.
        Attributes:
        id (str): [pub] id of object
        created_at (datetime): [pub] - creation time
        updated_at (datetime): [pub] - modification time
        """

        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()

    def __str__(self):
        return ("[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__))

    def save(self):
        """
        """
        self.updated_at = datetime.datetime.now()


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
