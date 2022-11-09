from app import db
from flask_login import UserMixin
from sqlalchemy.orm import relationship

class User(db.Model, UserMixin):
# class User(db.Model):
    __tablename__ = "user"

    email = db.Column(db.String(255), nullable=False, primary_key=True, unique=True)
    password = db.Column(db.String(255), nullable=False)

    predictions = relationship("Prediction", back_populates="user")

    def get_id(self):
        return self.email