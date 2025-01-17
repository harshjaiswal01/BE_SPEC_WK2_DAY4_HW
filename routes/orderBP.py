from flask import Blueprint
from controllers.orderController import add_order, order_items, order_tracking

order_blueprint = Blueprint('order_bp', __name__)

order_blueprint.route('/', methods=['POST'])(add_order)
order_blueprint.route('/<int:id>/items', methods=['GET'])(order_items)
order_blueprint.route('/<int:id>/tracking', methods=['GET'])(order_tracking)