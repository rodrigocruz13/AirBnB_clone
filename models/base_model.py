#!/usr/bin/python3

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
    import uuid
    self.id = uuid.uuid4()    //Formato fecha
    self.id2 = str(self.id)      //Formato Texto
    import datetime as dt
    self.created_at = dt.datetime.now()
    self.updated_at = self.created_at
    
    @classmethod
    def __str_(self)_
    print("[{}] ({}) {}".format(self.__class__.name, self.id, self.__dict__))
    
    @classmethod
    def save(self):
    """ Class method
    """
    self.updated_at = dt.datetime.now()

    @classmethod
    def to_dict(self):
    """Class method
    """
    d = []

    for key,val in self.__dict__():
    d.update(key, value)
    return d
