from pokemon.db import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from sqlalchemy.exc import IntegrityError

from pokemon.db import db

from pokemon.utils.logger import configure_logger

logger = logging.getLogger(__name__)

class User(UserMixin, db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=True)
    password_hash = db.Column(db.String(128), nullable=False)

    def set_password(self, password):
        """Hashes and sets the user's password."""
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        """Checks the provided password against the stored hash."""
        return check_password_hash(self.password_hash, password)

    def to_dict(self):
        """Serializes the user object to a dictionary."""
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email
        }