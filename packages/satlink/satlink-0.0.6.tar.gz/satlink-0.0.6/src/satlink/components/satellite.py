from typing import Callable, List
from wsgiref.simple_server import make_server
from wsgiref.types import StartResponse, WSGIEnvironment
from .datalink import Datalink
from .uplink import Uplink
from .downlink import Downlink


class Satellite:
  def __init__(self, port = 3000, hostname = 'localhost'):
    self.__server = make_server(hostname, port, lambda e, s: self.__router(e, s))
    self.__datalinks: List[Datalink] = []
    self.__hostname = hostname
    self.__port = port
  
  def transmit(self):
    try:
      print(f'Transmitting on http://{self.__hostname}:{self.__port}')
      self.__server.serve_forever()
    except KeyboardInterrupt:
      print('\nTransmission terminated')

  def __router(self, environ: WSGIEnvironment, start_response: StartResponse):
    downlink = Downlink(start_response)

    for datalink in self.__datalinks:
      if datalink.match(environ['PATH_INFO']):
        uplink = Uplink(environ)
        return datalink.handler(uplink, downlink)
      
    return downlink.status(404).json({'error': 'Houston, we have a problem!'})
  
  def datalink(self, route: str):
    def inner(handler: Callable[[Uplink, Downlink], Downlink]):
      self.__datalinks.append(Datalink(route, handler))

    return inner
