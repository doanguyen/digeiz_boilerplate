"""Digeiz models declaration"""
from datetime import datetime

from digeiz_api.extensions import db


class BaseModelMixin:
    """Provides datetime mixin for faster model declaration"""

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow,
        nullable=False,
        comment="Automatic store the creation time of the object",
    )
    updated_at = db.Column(
        db.DateTime,
        default=None,
        onupdate=datetime.utcnow,
        comment="Automatic store the update time of the object",
    )


class Account(db.Model, BaseModelMixin):
    """Model describes customers"""

    username = db.Column(
        db.String(50), unique=True, index=True, comment="Unique username"
    )
    email = db.Column(db.String, index=True, unique=True, comment="User unique email")
    phone = db.Column(db.String, comment="User telephone number")
    name = db.Column(db.String, comment="User full name")
    dob = db.Column(db.Date, nullable=True)

    def __str__(self):  # pragma: no cover
        return self.username

    # Relationship
    malls = db.relationship("Mall", cascade="all, delete", backref="account", lazy=True)


class Mall(db.Model, BaseModelMixin):
    """Model describes a real Mall entity"""

    name = db.Column(db.String(128), nullable=False, index=True, unique=True)
    location = db.Column(db.String, comment="The mall location in detail")
    province = db.Column(db.String, comment="The mall province. I.e: Isere")
    city = db.Column(db.String, comment="The mall city. I.e: Grenoble")
    country = db.Column(
        db.String,
        comment="The mall's country. Should match the country_code. I.e: France",
    )
    country_code = db.Column(
        db.String,
        comment="The two-letter country code corresponds to the country. I.e: FR",
    )
    latitude = db.Column(
        db.Float, comment="The latitude of the mall's location. I.e: 42.12"
    )
    longitude = db.Column(
        db.Float, comment="The longitude of the mall's location. I.e: -22.43"
    )
    account_id = db.Column(
        db.Integer, db.ForeignKey("account.id", ondelete="CASCADE"), nullable=False
    )

    # Relationship
    units = db.relationship("Unit", backref="mall")

    def __str__(self):  # pragma: no cover
        return self.name


class Unit(db.Model, BaseModelMixin):
    """Model describes a store belong to a Mall"""

    name = db.Column(db.String(128), nullable=False, index=True, unique=True)

    mall_id = db.Column(db.Integer, db.ForeignKey("mall.id"), nullable=False)

    def __str__(self):  # pragma: no cover
        return self.name
