#!/usr/bin/env python3

"""DB module
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from sqlalchemy.orm.exc import NoResultFound
from user import Base, User


class DB:
    """DB class
    """

    def __init__(self) -> None:
        """Initialize a new DB instance
        """
        self._engine = create_engine("sqlite:///a.db", echo=True)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """Memoized session object
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email, hashed_password):
        """
        returns a User object. The method should save the user to the database
        """
        user = User(email=email, hashed_password=hashed_password)

        # Add user to db
        self._session.add(user)
        try:
            self._session.commit()
        except Exception as e:
            self._session.rollback()
            print(e)

        return user

    def find_user_by(self, **kwargs):
        """
        takes in keyword and returns the first row found in the users table
        """
        self._session

        user = self.__session.query(User).filter_by(**kwargs).first()
        if not user:
            raise NoResultFound
        return user

    def update_user(self, user_id, **kwargs):
        """
         method that takes as argument a required user_id integer and arbitrary
         keyword arguments, and returns None
        """

        self._session
        user = self.find_user_by(id=user_id)
        if user:
            if kwargs:
                for attr, v in kwargs.items():
                    if hasattr(user, attr):
                        setattr(user, attr, v)
                    else:
                        raise ValueError

                # Add user to db
                self.__session.add(user)
                try:
                    self.__session.commit()
                except Exception as e:
                    self.__session.rollback()
                    print(e)

                return None