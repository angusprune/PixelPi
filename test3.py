import ws2801
from pprint import pprint
import time

leds = ws2801.WS2801_Chain()



leds.all_on()
leds.write()
pprint(leds.ics)

leds.set_blue()
leds.write()
pprint(leds.ics)

leds.all_off()
leds.write()
pprint(leds.ics)

leds.cycle()