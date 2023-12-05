class Runner():
    def __init__(self, block_width, num_pixels, start_position) -> None:
        self.block_width = block_width
        self.num_pixels = num_pixels
        self.start_position = start_position
        self.current_position = start_position

    def start_runner(self):
        pixels[self.start_position:self.start_position + self.block_width] = [(255, 0, 0)]*self.block_width
        

    def step_runner(self, pixels):
        if self.current_position < self.num_pixels - self.block_width:
            pixels[self.current_position] = (0, 0, 0)
            pixels[self.current_position + self.block_width] = (255, 0, 0)
            self.current_position += 1
        else:
            pixels[-(self.block_width + 1):] = [(0, 0, 0)]*(self.block_width+1)
            self.current_position = 0
            pixels[:self.block_width] = [(255, 0, 0)]*self.block_width

import board
import neopixel
import time
num_pixels = 300
pixels = neopixel.NeoPixel(board.GP1, num_pixels)
pixels.brightness = 0.5

block_width = 20
num_runners = 5
runners = []

for i in range(num_runners):
    runners.append(Runner(block_width, num_pixels, (num_pixels//num_runners)*i))

for runner in runners:
    runner.start_runner()

while True:
    for runner in runners:
        runner.step_runner(pixels)