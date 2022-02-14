from datetime import datetime
from doom.database import db
from doom.database import Column
from doom.database import PkModel
from doom.database import relationship
from doom.database import reference_col
from doom.extensions import bcrypt


class User(PkModel):
    """A user of the app."""

    __tablename__ = "users"
    username = Column(db.String(80), unique=True, nullable=False)
    password = Column(db.LargeBinary(128), nullable=True)
    active = Column(db.Boolean(), default=True)
    created_at = Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __init__(self, username, password=None, **kwargs):
        """Create instance."""
        super().__init__(username=username, **kwargs)
        if password:
            self.set_password(password)
        else:
            self.password = None

    def set_password(self, password):
        """Set password."""
        self.password = bcrypt.generate_password_hash(password).decode('utf-8')

    def check_password(self, value):
        """Check password."""
        return bcrypt.check_password_hash(self.password, value)
