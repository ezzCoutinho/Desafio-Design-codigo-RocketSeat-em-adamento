from flask import request as FlaskRequest
from typing import Dict, List
from src.driver.interface.driver_handler_interface import DriverHandlerInterface
from src.errors.http_unprocessable_entity import HttpUnprocessableEntity

class Calculator4:
  def __init__(self, driver_handler: DriverHandlerInterface):
    self.__driver_handler = driver_handler

  def calculate(self, request: FlaskRequest) -> Dict: # type: ignore
    body = request.json
    input_data = self.__validate_body(body)

    mean = self.__calculate_mean(input_data)

    formated_response = self.__formated_response(mean)
    return formated_response

  def __calculate_mean(self, numbers: List[float]) -> float:
    mean = self.__driver_handler.calculate_mean(numbers)
    return mean

  def __validate_body(self, body: Dict) -> List[float]:
    if "numbers" not in body:
      raise HttpUnprocessableEntity("body mal formatado!")
    
    input_data = body["numbers"]
    return [float(i) for i in input_data]
  
  def __formated_response(self, mean: float) -> Dict:
    return {
      "data": {
        "Calculator": 4,
        "media": mean,
        "Success": True
    } }