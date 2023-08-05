from dataclasses import dataclass
from typing import Callable
from .uplink import Uplink
from .downlink import Downlink


@dataclass
class Datalink:
  route: str
  handler: Callable[[Uplink, Downlink], Downlink]

  def match(self, path: str):
    path = path[:-1] if path.endswith('/') and path != "/" else path
    return True if path == self.route else False
