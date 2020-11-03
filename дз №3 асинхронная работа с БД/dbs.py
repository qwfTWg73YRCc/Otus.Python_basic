from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session, relationship

ENGINE = create_engine("postgresql://postgres:postgres@localhost/postgres")
Base = declarative_base(bind=ENGINE)

session_factory = sessionmaker(bind=ENGINE)
Session = scoped_session(session_factory)


class User(Base):

    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String(32), unique=True)
    username = Column(String(32), unique=True)
    email = Column(String(50), unique=True)
    posts = relationship("Post", back_populates="author")


class Post(Base):

    __tablename__ = "posts"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey(User.id), nullable=False)
    title = Column(String(256), nullable=False)
    body = Column(String(256), nullable=False)
    author = relationship(User, back_populates="posts")


def make_migrations():
    Base.metadata.create_all()
    session = Session()
    session.close()

