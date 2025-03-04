from typing import Dict
from src.errors.http_unprocessable_entity import HttpUnprocessableEntity

def handle_errors(error: Exception) -> Dict:
  if isinstance(error, (HttpUnprocessableEntity)):
    return {
      'status_code': error.status_code,
      'body': {
        'errors': [{
          'title': error.name,
          'detail': error.message
        }]
      }
    }
  
  return {
      'status_code': 500,
      'body': {
        'errors': [{
          'title': 'Internal Server Error',
          'detail': str(error)
        }]
      }
    }