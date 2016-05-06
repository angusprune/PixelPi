import ws2801

leds = ws2801.WS2801_Chain()

leds.set_blue()
leds.write()

leds.all_on()
leds.write()

