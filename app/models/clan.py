from .db import db
from sqlalchemy.sql import func


class Clan(db.Model):
    __tablename__ = 'clans'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40), nullable=False, unique=True)
    owner_user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False, unique=True)
    created_at = db.Column(db.DateTime, server_default=func.now())
    updated_at = db.Column(db.DateTime, onupdate=func.now())

    owner = db.relationship("User", back_populates="owned_clan", cascade="all, delete")
    members = db.relationship("User", back_populates="member_of_clan", cascade="all, delete")
    clan_messages = db.relationship("Message", back_populates="clan", cascade="all, delete")



    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'owner_user_id': self.owner_user_id,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }
