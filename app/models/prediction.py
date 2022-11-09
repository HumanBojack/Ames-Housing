from app import db
from app.models import User
from sqlalchemy.orm import relationship

class Prediction(db.Model):
    __tablename__ = "prediction"

    id = db.Column(db.Integer, primary_key=True, unique=True)
    user_id = db.Column(db.ForeignKey(User.email, ondelete="CASCADE"), nullable=False, index=True)

    year_remod_add = db.Column(db.Integer, nullable=False)
    overall_qual = db.Column(db.Integer, nullable=False)
    bsmtfin_sf_1 = db.Column(db.Integer, nullable=False)
    gr_liv_area = db.Column(db.Integer, nullable=False)
    house_area = db.Column(db.Integer, nullable=False)
    fireplaces = db.Column(db.Integer, nullable=False)
    year_built = db.Column(db.Integer, nullable=False)

    neighborhood = db.Column(db.String(100), nullable=False)
    kitchen_qual = db.Column(db.String(100), nullable=False)
    bsmt_qual = db.Column(db.String(100))

    predicted_price = db.Column(db.Integer, nullable=False)

    user = relationship("User", back_populates="predictions")

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()