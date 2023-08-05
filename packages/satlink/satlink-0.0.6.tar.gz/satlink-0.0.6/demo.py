from src.satlink import Satellite, Uplink, Downlink


sat = Satellite()


@sat.datalink("/")
def index(uplink: Uplink, downlink: Downlink):
    return downlink.text("Hello, Earth!")


sat.transmit()
