import board
import neopixel
from adafruit_pixel_framebuf import PixelFramebuffer
from adafruit_pixel_framebuf import VERTICAL

pixel_pin = board.GP1
pixel_width = 32
pixel_height = 8

pixels = neopixel.NeoPixel(
    pixel_pin,
    pixel_width * pixel_height,
    brightness=0.1,
    auto_write=False,
)

pixel_framebuf = PixelFramebuffer(
    pixels,
    32,
    8,
    orientation=VERTICAL,
    rotation=2
)

#Letters are 5 pixels wide with 1 space in between them
display_text = "Ho Ho Ho    Merry Christmas!"
text_size = len(display_text) * 6

while True:
    for i in range(pixel_width, -text_size, -1):
        pixel_framebuf.fill(0x000000)
        pixel_framebuf.text(display_text, i, 0, 0xFF0000)
        pixel_framebuf.display()
