from typing import Dict, List
from pytest import raises
from src.calculator.calculator_4 import Calculator4

class MockDriverHandler():
  def __init__(self, body: Dict) -> None:
    self.json = body

  def calculate_mean(self, numbers: List[float]) -> float:
    return 1

class MockDriverHandlerError():  
  def calculate_mean(self, numbers: List[float]) -> float:
    return 1000000 

def test_calculate_with_variance_error():
  mock_request = MockDriverHandler(body={"number": [1, 2, 3, 4, 5]})
  calculator = Calculator4(MockDriverHandlerError())

  with raises(Exception) as excinfo:
    assert calculator.calculate(mock_request) == "body mal formatado!"
  assert str(excinfo.value) == "body mal formatado!"

def test_calculate():
  mock_request = MockDriverHandler(body={"numbers": [10, 20, 30, 40, 50]})
  calculator = Calculator4(mock_request)
  formated_response = calculator.calculate(mock_request)
  print(formated_response)