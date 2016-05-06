import ws2801
from pprint import pprint

leds = ws2801.WS2801_Chain()



leds.all_on()
leds.write()

leds.set_blue()
leds.write()

pprint(leds)
