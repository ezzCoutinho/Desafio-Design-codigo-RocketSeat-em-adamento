from abc import ABC, abstractmethod
from typing import List

class DriverHandlerInterface(ABC):

  @abstractmethod
  def calculate_mean(self, driver_id: str):
    pass