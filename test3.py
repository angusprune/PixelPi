import ws2801
from pprint import pprint

leds = ws2801.WS2801_Chain()

leds.set_blue()
leds.write()

leds.all_on()
leds.write()
pprint(leds)
