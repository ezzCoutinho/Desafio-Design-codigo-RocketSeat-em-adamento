from flask import Blueprint, jsonify, request
from src.main.factories.calculator4_factory import calculator4_factory
from src.errors.error_controller import handle_errors

calc_route_bp = Blueprint("calc_routes", __name__)

@calc_route_bp.route("/calculator/4", methods=["POST"])
def calculator():
  try:
    calc = calculator4_factory()
    response = calc.calculate(request)
    print(response)
    return jsonify(response), 200
  except Exception as e:
    response = handle_errors(e)
    return jsonify(response["body"]), response['status_code']