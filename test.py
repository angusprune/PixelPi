import spidev
from colors import *

spi = spidev.SpiDev()

num_leds = 20
PIXEL_SIZE = 3

gamma = bytearray(256)

for i in range(256):
    gamma[i] = int(pow(float(i) / 255.0, 2.5) * 255.0)

def all_on():
    pixel_output = bytearray(num_leds * PIXEL_SIZE + 3)
    for led in range(num_leds):
        pixel_output[led * PIXEL_SIZE:] = filter_pixel(WHITE, 1)
    spi.writebytes(pixel_output)
    spi.flush()

def filter_pixel(input_pixel, brightness):
    output_pixel = bytearray(PIXEL_SIZE)

    input_pixel[0] = int(brightness * input_pixel[0])
    input_pixel[1] = int(brightness * input_pixel[1])
    input_pixel[2] = int(brightness * input_pixel[2])

    output_pixel[0] = gamma[input_pixel[0]]
    output_pixel[1] = gamma[input_pixel[1]]
    output_pixel[2] = gamma[input_pixel[2]]
    return output_pixel




all_on()