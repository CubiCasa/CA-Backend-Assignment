from sqlalchemy import Column, Integer, String, DateTime, Enum, ForeignKey, Float
from sqlalchemy.dialects.postgresql import ARRAY, UUID
from sqlalchemy.orm import relationship
from sqlalchemy_serializer import SerializerMixin
import uuid

from app.base.base_model import BaseModel
from app.base.constants import UserTypes, Genders


class User(BaseModel, SerializerMixin):
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
        jobs = ARRAY string
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
        jobs (array): Jobs array
    """

    __tablename__ = 'users'
    serialize_rules = ('-password',)

    id = Column(UUID(as_uuid=True), primary_key=True)
    username = Column(String(255), unique=True)
    password = Column(String(255))
    first_name = Column(String(255))
    last_name = Column(String(255))
    email = Column(String(255))
    address = Column(String(255), nullable=True)
    school_name = Column(String(255), nullable=True)
    user_type = Column(Enum(UserTypes))
    gender = Column(Enum(Genders))
    user_school_performances = relationship("UserSchoolPerformance")
    jobs = Column(ARRAY(String))

    def __init__(self, username: str = None, password: str = None, first_name: str = None, last_name: str = None,
                 email: str = None, address: str = None, school_name: str = None, user_type: UserTypes = None,
                 gender: Genders = None) -> None:
        """ The constructor for User class.
        Parameters:
            username (str): User's username
            password (str): User's password
        """
        super().__init__()
        self.id = uuid.uuid4()
        self.username = username
        if password:
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
            'username': self.username,
        }

        return data

    def __repr__(self) -> str:
        return '<User %r>' % (self.username)


class UserSchoolPerformance(BaseModel, SerializerMixin):
    """ User performance's model class.
        Column:
            id = (Integer, primary_key=True)
            user_id = (Integer, ForeignKey('user.id'))
            math = (Integer, nullable=True)
            physics = (Integer, nullable=True)
            chemistry = (Integer, nullable=True)
            biology = (Integer, nullable=True)
            literature = (Integer, nullable=True)
            history = (Integer, nullable=True)
            geography = (Integer, nullable=True)
            phylosophy = (Integer, nullable=True)
            art = (Integer, nullable=True)
            foreign_language = (Integer, nullable=True)
        Attributes:
            id = (number): User performance: id
            user_id = (number): User performance: user id
            math = (number): User performance: math
            physics = (number): User performance: physics
            chemistry = (number): User performance: chemistry
            biology = (number): User performance: biology
            literature = (number): User performance: literature
            history = (number): User performance: history
            geography = (number): User performance: geography
            phylosophy = (number): User performance: phylosophy
            art = (number): User performance: art
            foreign_language = (number): User performance: foreign_language
        """

    __tablename__ = 'user_school_performances'

    id = Column(UUID(as_uuid=True), primary_key=True)
    user_id = Column(UUID(as_uuid=True), ForeignKey('users.id'))
    math = Column(Float, nullable=True)
    physics = Column(Float, nullable=True)
    chemistry = Column(Float, nullable=True)
    biology = Column(Float, nullable=True)
    literature = Column(Float, nullable=True)
    history = Column(Float, nullable=True)
    geography = Column(Float, nullable=True)
    phylosophy = Column(Float, nullable=True)
    art = Column(Float, nullable=True)
    foreign_language = Column(Float, nullable=True)

    def __init__(self, user_id: int = None, math: int = None, physics: int = None, chemistry: int = None,
                 biology: int = None, literature: int = None, history: int = None, geography: int = None,
                 phylosophy: int = None, art: int = None, foreign_language: int = None) -> None:
        """ The constructor for User class.
        Parameters:
            username (str): User's username
            password (str): User's password
        """
        super().__init__()
        self.id = uuid.uuid4()
        self.user_id = user_id
        self.math = math
        self.physics = physics
        self.chemistry = chemistry
        self.biology = biology
        self.literature = literature
        self.history = history
        self.geography = geography
        self.phylosophy = phylosophy
        self.art = art
        self.foreign_language = foreign_language

    def serialize(self) -> dict:
        """Serialize the object attributes values into a dictionary.
        Returns:
           dict: a dictionary containing the attributes values
        """

        data = {
            'id': self.id,
        }

        return data

    def __repr__(self) -> str:
        return '<UserSchoolPerformance %r>' % (self.id)