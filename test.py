import spidev
import argparse
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
    spi.write(pixel_output)
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

parser = argparse.ArgumentParser(add_help=True, version='1.0', prog='pixelpi.py')
subparsers = parser.add_subparsers(help='sub command help?')
common_parser = argparse.ArgumentParser(add_help=False)
common_parser.add_argument('--chip', action='store', dest='chip_type', default='WS2801',
                           choices=['WS2801', 'LPD8806', 'LPD6803', 'SM16716'],
                           help='Specify chip type LPD6803, LPD8806, WS2801 or SM16716')
common_parser.add_argument('--verbose', action='store_true', dest='verbose', default=True, help='enable verbose mode')
common_parser.add_argument('--spi_dev', action='store', dest='spi_dev_name', required=False, default='/dev/spidev0.0',
                           help='Set the SPI device descriptor')
common_parser.add_argument('--refresh_rate', action='store', dest='refresh_rate', required=False, default=500, type=int,
                           help='Set the refresh rate in ms (default 500ms)')
parser_strip = subparsers.add_parser('strip', parents=[common_parser],
                                     help='Stip Mode - Display an image using POV and a LED strip')
parser_strip.set_defaults(func=strip)
parser_strip.add_argument('--filename', action='store', dest='filename', required=False,
                          help='Specify the image file eg: hello.png')
parser_strip.add_argument('--array_height', action='store', dest='array_height', required=True, type=int, default='7',
                          help='Set the Y dimension of your pixel array (height)')
parser_array = subparsers.add_parser('array', parents=[common_parser],
                                     help='Array Mode - Display an image on a pixel array')
parser_array.set_defaults(func=array)
parser_array.add_argument('--filename', action='store', dest='filename', required=False,
                          help='Specify the image file eg: hello.png')
parser_array.add_argument('--array_width', action='store', dest='array_width', required=True, type=int, default='7',
                          help='Set the X dimension of your pixel array (width)')
parser_array.add_argument('--array_height', action='store', dest='array_height', required=True, type=int, default='7',
                          help='Set the Y dimension of your pixel array (height)')
parser_pixelinvaders = subparsers.add_parser('pixelinvaders', parents=[common_parser],
                                             help='Pixelinvaders Mode - setup pixelpi as a Pixelinvaders slave')
parser_pixelinvaders.set_defaults(func=pixelinvaders)
parser_pixelinvaders.add_argument('--udp-ip', action='store', dest='UDP_IP', required=True,
                                  help='Used for PixelInvaders mode, listening address')
parser_pixelinvaders.add_argument('--udp-port', action='store', dest='UDP_PORT', required=True, default=6803, type=int,
                                  help='Used for PixelInvaders mode, listening port')
parser_fade = subparsers.add_parser('fade', parents=[common_parser], help='Fade Mode - Fade colors on all LEDs')
parser_fade.set_defaults(func=fade)
parser_fade.add_argument('--num_leds', action='store', dest='num_leds', required=True, default=50, type=int,
                         help='Set the  number of LEDs in the string')
parser_chase = subparsers.add_parser('chase', parents=[common_parser], help='Chase Mode - Chase display test mode')
parser_chase.set_defaults(func=chase)
parser_chase.add_argument('--num_leds', action='store', dest='num_leds', required=True, default=50, type=int,
                          help='Set the  number of LEDs in the string')
parser_pan = subparsers.add_parser('pan', parents=[common_parser], help='Pan Mode - Pan an image across an array')
parser_pan.set_defaults(func=pan)
parser_pan.add_argument('--filename', action='store', dest='filename', required=False,
                        help='Specify the image file eg: hello.png')
parser_pan.add_argument('--array_width', action='store', dest='array_width', required=True, type=int, default='7',
                        help='Set the X dimension of your pixel array (width)')
parser_pan.add_argument('--array_height', action='store', dest='array_height', required=True, type=int, default='7',
                        help='Set the Y dimension of your pixel array (height)')
parser_all_on = subparsers.add_parser('all_on', parents=[common_parser], help='All On Mode - Turn all LEDs On')
parser_all_on.set_defaults(func=all_on)
parser_all_on.add_argument('--num_leds', action='store', dest='num_leds', required=True, default=50, type=int,
                           help='Set the  number of LEDs in the string')
parser_all_off = subparsers.add_parser('all_off', parents=[common_parser], help='All Off Mode - Turn all LEDs Off')
parser_all_off.set_defaults(func=all_off)
parser_all_off.add_argument('--num_leds', action='store', dest='num_leds', required=True, default=50, type=int,
                            help='Set the  number of LEDs in the string')
args = parser.parse_args()




all_on()