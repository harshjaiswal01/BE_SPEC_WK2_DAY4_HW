from services import orderService
from database import db #need db be to serve incoming data to db
from models.customer import Customer #need this to creat Customer Objects
from sqlalchemy import select, delete, func
from marshmallow import fields, ValidationError
from flask import Flask, jsonify, request
from models.schemas.orderSchema import order_schema, orders_schema
from models.schemas.productSchema import product_schema, products_schema


def add_order():

    order_data = request.json
    new_order, error = orderService.add_order(order_data)

    if error:
        return error, 404
    
    return jsonify({f"Message":"New Order Placed", "Order ID":new_order.id}),201

def order_items(id):
    products, error = orderService.order_items(id)
    if error:
        return jsonify(error), 400
    return products_schema.jsonify(products)

def order_tracking(id):
    tracking, error = orderService.order_tracking(id)
    if error:
        return error, 400  
    return tracking
