"""
Models definition
"""
import datetime
import pytz
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class BaseModel(db.Model):
    """
    Base data model for all objects
    """
    __abstract__ = True

    def __repr__(self):
        """
        Define a base way to print models
        """
        return '%s(%s)' % (self.__class__.__name__, {
            column: value for column, value in self.__dict__.items()
        })

    def json(self):
        """
        Define a base way to jsonify models, dealing with datetime objects
        """
        data = {}
        for column, value in self.__dict__.items():
            if isinstance(value, datetime.date):
                data[column] = value.replace(tzinfo=pytz.UTC).astimezone(
                    tz=ist_tz).strftime('%Y-%m-%d %H:%M:%S')
            else:
                data[column] = value

        data.pop('_sa_instance_state', None)
        return data


class Group(BaseModel, db.Model):
    """
    Model for the Group table
    """
    __tablename__ = 'group'
    id = db.Column(db.VARCHAR(128), primary_key=True, unique=True)
    name = db.Column(db.VARCHAR(512))
    content_id = db.Column(db.VARCHAR(128))
    tenant_id = db.Column(db.VARCHAR(8))

    def __init__(self, id, name, content_id, tenant_id):
        self.id = id
        self.name = name
        self.content_id = content_id
        self.tenant_id = tenant_id


class User(BaseModel, db.Model):
    """
    Model for the User table
    """
    __tablename__ = 'user'
    id = db.Column(db.VARCHAR(128), primary_key=True)
    group_id = db.Column(
        db.VARCHAR(128), db.ForeignKey('group.id'))
    email_id = db.Column(db.VARCHAR(128))
    current_run_time = db.Column(db.FLOAT)
    is_paused = db.Column(db.BOOLEAN)

    def __init__(self, id, group_id, email_id,
                 current_run_time, is_paused):
        self.id = id
        self.group_id = group_id
        self.email_id = email_id
        self.current_run_time = current_run_time
        self.is_paused = is_paused
