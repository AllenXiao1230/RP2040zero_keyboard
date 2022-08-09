import time
import board
import neopixel

# 定義RGB控制引腳，必須選擇 D10, D12, D18 或者 D21
pixel_pin = board.GP0
# 串聯RGB燈珠的數量
num_pixels = 9
# 定義RGB數據順序：RGB 或者 GRB
COLOR_ORDER = neopixel.GRB

pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.3, auto_write=False, pixel_order=COLOR_ORDER)

def wheel(pos):
    if pos < 0 or pos > 255:
        r = g = b = 0
    elif pos < 85:
        r = int(pos * 3)
        g = int(255 - pos * 3)
        b = 0
    elif pos < 170:
        pos -= 85
        r = int(255 - pos * 3)
        g = 0
        b = int(pos * 3)
    else:
        pos -= 170
        r = 0
        g = int(pos * 3)
        b = int(255 - pos * 3)
    return (r, g, b) if COLOR_ORDER in (neopixel.RGB, neopixel.GRB) else (r, g, b, 0)

def rainbow(wait):
    for j in range(255):
        for i in range(num_pixels):
            pixel_index = (i * 256 // num_pixels) + j
            pixels[8-i] = wheel(pixel_index & 255)
        pixels.show()
        time.sleep(wait)

while True:
    rainbow(0.005)  # 彩虹 