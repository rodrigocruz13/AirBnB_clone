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

        self.updated_at = self.created_at


    def __str__(self):
        return ("[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__))

    def save(self):
        """ Class method
        """
        self.updated_at = datetime.datetime.now()


    def to_dict(self):
        """Class method
        """
        """d = {'id' : self.id, 'created_at' : self.created_at,
             'updated at' : self.updated_at}"""
        dic = self.__dict__
        dic['__class__'] = self.__class__.__name__
        return dic
