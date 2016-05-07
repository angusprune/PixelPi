import ws2801
from pprint import pprint
import time

leds = ws2801.WS2801_Chain(300)

leds.cycle()

leds.set_off()