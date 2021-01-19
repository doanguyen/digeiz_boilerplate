from flask import request, jsonify
from flask.views import MethodView
from marshmallow import ValidationError

from digeiz_api.extensions import db
from digeiz_api.models import Account
from digeiz_api.schemas import AccountSchema, MallSchema


class AccountAPI(MethodView):
    """List/Create accounts
    endpoint: /api/accounts
    methods: [GET, POST]
    """

    def get(self):
        """Get list of accounts without paginations
        :return List[Account] without pagination
        """
        all_accounts = Account.query.all()
        schema = AccountSchema(many=True)
        return schema.jsonify(all_accounts)

    def post(self):
        """Create an account
        :return Account which is created
        :raise ValidationError
        """
        schema = AccountSchema()
        try:
            account = schema.load(request.json)
        except ValidationError as e:
            return jsonify({"errors": e.messages}), 400
        acc = schema.create_instance(account)
        db.session.add(acc)
        return account, 201


class SingleAccountAPI(MethodView):
    """Modify a single Account
    endpoint: /api/accounts/<id:>
    methods: [GET/PUT/PATCH/DELETE]
    """

    def get(self, pk: int):
        """Get single account
        :return Account with corresonding pk
        :raise Notfound
        """
        schema = AccountSchema()
        account = Account.query.get(pk)
        if not account:
            return jsonify({"error": ["Account not found"]}), 404
        return schema.jsonify(account), 200

    def put(self, pk: int):
        """Update an account by the id
        :return Account which is updated
        :raise Notfound
        """
        schema = AccountSchema()
        account = Account.query.get(pk)
        if not account:
            return jsonify({"error": ["Account not found"]}), 404
        serialized = schema.dump(request.json)
        account.query.update(serialized)
        db.session.commit()
        return serialized, 200

    patch = put

    def delete(self, pk: int):
        """Delete an account by the id
        :return empty json object {}
        :raise Notfound
        """
        account = Account.query.get(
            pk
        )  # The .delete() method does not cascade, so we get first
        if not account:
            return jsonify({"error": ["Account not found"]}), 404
        db.session.delete(account)
        db.session.commit()
        return {}


class AccountMallsAPI(MethodView):
    """List/Create malls from an account
    endpoint: /api/accounts/<id>/malls
    methods: [GET, POST]
    """

    def get(self, pk: int):
        """Get list of all malls from an account without paginations
        :return List[Mall] without pagination
        """
        account = Account.query.get(pk)
        if not account:
            return {}, 404
        schema = MallSchema(many=True)
        return schema.jsonify(account.malls)

    def post(self, pk: int):
        """Create a mall from provided account
        :return Mall which is created
        :raise ValidationError
        """
        account = Account.query.get(pk)
        if not account:
            return {"errors": ["Account not found"]}, 404
        schema = MallSchema()
        try:
            mall = schema.load(request.json)
        except ValidationError as e:
            return jsonify({"errors": e.messages}), 400
        mall_instance = schema.create_instance(mall)
        account.malls.append(mall_instance)
        db.session.commit()
        return mall, 201


account_malls_api = AccountMallsAPI.as_view("account_malls")
