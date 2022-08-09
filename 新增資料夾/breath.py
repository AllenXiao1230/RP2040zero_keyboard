import time
import board
import neopixel

# 定義RGB控制引腳，必須選擇 D10, D12, D18 或者 D21
pixel_pin = board.GP0
# 串聯RGB燈珠的數量
num_pixels = 9
# 定義RGB數據順序：RGB 或者 GRB
COLOR_ORDER = neopixel.GRB

pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.5, auto_write=False, pixel_order=COLOR_ORDER)

while True:
    
    for i in range(10,255):
        color=(i,i,i)
        pixels.fill(color)
        pixels.show()
        time.sleep(0.01)
        
        
    for i in range(255,5,-1):
        color=(i,i,i)
        pixels.fill(color)
        pixels.show()
        time.sleep(0.01)
        
        
        
