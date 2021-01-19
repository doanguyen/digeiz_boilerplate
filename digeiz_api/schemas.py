from typing import Dict

from marshmallow import fields
from marshmallow.fields import Field

from digeiz_api.extensions import ma
from digeiz_api.models import Account, Mall, Unit


class MallSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Mall

    def create_instance(self, data: Dict, **kwargs) -> Mall:
        """Create mall instance with validated data"""
        data.pop("units", None)
        return Mall(**data)


class AccountSchema(ma.SQLAlchemySchema):
    id: Field = fields.Integer(dump_only=True)  # Enforced dump, don't allows to write
    email: Field = fields.Email(required=True)
    username: Field = fields.String(required=True)
    name: Field = fields.String(required=True)
    phone: Field = fields.String()
    dob: Field = fields.Date()
    malls: Field = ma.List(ma.Nested(MallSchema), dump_only=True)

    class Meta:
        model = Account

    def create_instance(self, data, **kwargs) -> Account:
        """Create account instance with validated data"""
        data.pop("malls", None)
        return Account(**data)


class UnitSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Unit
