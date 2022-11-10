from sqlalchemy import Column, Integer, String, Boolean, DateTime, SmallInteger, Enum
from sqlalchemy import inspect
from sqlalchemy_serializer import SerializerMixin

from app.base.constants import UserTypes, Genders
from app.database import db


class Model:
    created_at = Column(DateTime())
    updated_at = Column(DateTime())

    def serialize(self) -> dict:
        """Serialize the object attributes values into a dictionary."""

        return {}

    def remove_session(self):
        """Removes an object from the session its current session."""

        session = inspect(self).session
        if session:
            session.expunge(self)


class User(db.Model, Model, SerializerMixin):
    """ User's model class.
    Column:
        id = (String(36), primary_key=True)
        username = (String(255), unique=True)
        password = (String(255))
        first_name = (String(255))
        last_name = (String(255))
        email = (String(255))
        address = (String(255), nullable=True)
        school_name = (String(255), nullable=True)
        user_type = (Enum(UserTypes))
        gender = (Enum(Genders))
    Attributes:
        username (str): User's username
        password (str): User's password
        first_name (str): User's first name
        last_name (str): User's last name
        email (str): User's email
        address (str): User's address
        school_name (str): User's school_name
        user_type (str): User's user_type
        gender (str): User's gender
    """

    __tablename__ = 'users'

    id = Column(String(36), primary_key=True)
    username = Column(String(255), unique=True)
    password = Column(String(255))
    first_name = Column(String(255))
    last_name = Column(String(255))
    email = Column(String(255))
    address = Column(String(255), nullable=True)
    school_name = Column(String(255), nullable=True)
    user_type = Column(Enum(UserTypes))
    gender = Column(Enum(Genders))

    def __init__(self, username: str = None, password: str = None, first_name: str = None,
                 last_name: str = None, email: str = None, address: str = None, school_name: str = None,
                 user_type: str = None, gender: str = None) -> None:
        """ The constructor for User class.
        Parameters:
            username (str): User's username
            password (str): User's password
        """
        self.username = username
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.address = address
        self.school_name = school_name
        self.user_type = user_type
        self.gender = gender

    def serialize(self) -> dict:
        """Serialize the object attributes values into a dictionary.
        Returns:
           dict: a dictionary containing the attributes values
        """

        data = {
            'id': self.id,
            'username': self.username
        }

        return data

    def __repr__(self) -> str:
        return '<User %r>' % (self.username)
