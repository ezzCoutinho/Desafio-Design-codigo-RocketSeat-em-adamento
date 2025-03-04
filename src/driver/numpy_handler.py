from numpy import mean
from typing import List
from src.driver.interface.driver_handler_interface import DriverHandlerInterface

class NumpyHandler(DriverHandlerInterface):
  def __init__(self):
    self.__mean = mean
  
  def calculate_mean(self, numbers: List[float]) -> float:
    return self.__mean(numbers)