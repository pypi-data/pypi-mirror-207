import json
from typing import Dict, List, Literal, Union
from urllib.parse import parse_qs
from wsgiref.types import WSGIEnvironment


class Uplink:
  def __init__(self, environ: WSGIEnvironment):
    self.__environ = environ

  @property
  def method(self) -> Literal['GET', 'POST', 'PUT', 'PATCH', 'DELETE']:
    return self.__environ['REQUEST_METHOD']

  @property
  def query(self) -> Dict[str, List[str]]:
    return parse_qs(self.__environ['QUERY_STRING'])

  @property
  def body(self) -> Union[str, Dict, List[Dict]]:
    c_length = int(self.__environ['CONTENT_LENGTH'])
    c_type = self.__environ['CONTENT_TYPE']
    c_data = self.__environ['wsgi.input'].read(c_length).decode()

    match c_type:
      case 'application/json':
        return json.loads(c_data)
      case _:
        return c_data
