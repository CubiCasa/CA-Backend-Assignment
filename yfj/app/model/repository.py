"""It contains Repository generic class."""

from abc import ABC, abstractmethod

from sqlalchemy import desc, and_

from app.base.base_model import BaseModel
from app.database import db


class Repository(ABC):
    """This class implements the common methods used
    for all specific repositories classes. The subclasses
    of it can provide the implementation of these methods.
    """

    def __init__(self, model_class):
        self.__model_class = model_class
        self.session = db.session

    def get(self, model_id: any) -> BaseModel:
        """Retrieve a model register from database by its id.
        Parameters:
           model_id (int): Id of the model to be retrieved.
        Returns:
           Model: a model object.
        """

        return self.session.query(self.__model_class).filter(
            and_(self.__model_class.id == model_id, self.__model_class.deleted_at == None)).first()

    def get_all(self) -> list:
        """Retrieves a list of all elements in the database.
        Returns:
           list: a list of model objects.
        """

        return self.session.query(self.__model_class).filter(
            and_(self.__model_class.deleted_at == None)).order_by(desc(self.__model_class.id))

    def save(self, model: BaseModel) -> None:
        """Saves a model in the database.
        Parameters:
           model (Model): A model object.
        """

        self.session.add(model)
        self.session.commit()

    def update(self, model: BaseModel) -> None:
        """Update a existent model register in the database.
        Parameters:
           model (Model): A model object.
        """

        self.session.commit()

    def delete(self, model: BaseModel) -> bool:
        """Delete a existent model register in the database.
        Parameters:
           model (Model): A model object.
        Returns:
           int: the a model id that was deleted.
        """
        model.deleted_at = db.func.now()
        self.session.commit()

        return True

    @abstractmethod
    def is_invalid(self, model: BaseModel) -> list:
        """Checks if a given model object is valid.
        Parameters:
            model (Model): The model object.
            editing (bool): Indicates whether the validation is for an editing.
        Returns:
            list: A list containing the fields errors.
        """

        return []
