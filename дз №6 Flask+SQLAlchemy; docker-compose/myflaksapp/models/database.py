from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()  # если app не передан, то он не инициализируется
# нам нужно инициалихировать его позже.
# Поэтому:

__all__ = [
    "db",
]