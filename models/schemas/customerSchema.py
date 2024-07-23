from flask import request, jsonify
from services import customerService #dont import the individual function, import the module as a whole
from marshmallow import ValidationError
from marshmallow import ValidationError, fields
from . import ma


class CustomerSchema(ma.Schema):
    id = fields.Integer(required = False)
    customer_name = fields.String(required = True)
    email = fields.String(required = True)
    phone = fields.String(required = True)

    class Meta:
        fields = ('id', "customer_name", "email", "phone")

customer_schema = CustomerSchema()
customers_schema = CustomerSchema(many = True)