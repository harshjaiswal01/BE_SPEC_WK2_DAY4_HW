from services import productService
from database import db #need db be to serve incoming data to db
from models.customer import Customer #need this to creat Customer Objects
from sqlalchemy import select, delete, func
from marshmallow import fields, ValidationError
from flask import Flask, jsonify, request
from models.schemas.productSchema import product_schema, products_schema

def add_product():
    product_data = request.json
    new_product, error = productService.add_product(product_data)

    if error:
        return error, 400
    
    return new_product, 201

def get_products():
    productz = productService.get_products()
    return productz, 201

def get_product(id):
    product, error = productService.get_product(id)
    if error:
        return error, 400

    return product, 201

def update_product(id):
    product_data = request.json
    updated_product, error = productService.update_product(id, product_data)

    if error:
        return error, 400
    
    return updated_product, 201

def delete_product(id):
    deletion, error = productService.delete_product(id)

    if error:
        return error, 400
    return deletion, 201