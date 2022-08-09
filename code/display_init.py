import os
import busio
import displayio
import terminalio
import adafruit_displayio_ssd1306
from adafruit_display_text import label
import microcontroller
import board
import time

WIDTH = 128
HEIGHT = 64
CENTER_X = int(WIDTH/2)
CENTER_Y = int(HEIGHT/2)

displayio.release_displays()

SDA = board.GP12
SCL = board.GP13
i2c = busio.I2C(SCL, SDA)

if(i2c.try_lock()):
    print("i2c.scan(): " + str(i2c.scan()))
    i2c.unlock()
print()

display_bus = displayio.I2CDisplay(i2c, device_address=60)
display = adafruit_displayio_ssd1306.SSD1306(display_bus, width=128, height=64)

time.sleep(0.5)
splash = displayio.Group()
display.auto_refresh = True
display.show(splash)

def display_init():
    image_file = open("./4.bmp", "rb")
    image = displayio.OnDiskBitmap(image_file)
    image_sprite1 = displayio.TileGrid(image, pixel_shader=getattr(image, 'pixel_shader', displayio.ColorConverter()))

    
    splash.append(image_sprite1)
    time.sleep(1)
    color_bitmap = displayio.Bitmap(128, 64, 1) # 全屏白色
    color_palette = displayio.Palette(1)
    color_palette[0] = 0x000000 # 白色
    bg_sprite = displayio.TileGrid(color_bitmap, pixel_shader=color_palette, x=0, y= 0)
    splash.append(bg_sprite)

def call_show_map(text1,text2,text3,text4,text5,text6,text7,text8,text9):
    text_area_top_left = label.Label(terminalio.FONT, text=text9)
    text_area_top_left.anchor_point = (0.5, 0.0)
    text_area_top_left.anchored_position = (WIDTH/6, 0)

    text_area_top_middle = label.Label(terminalio.FONT, text=text8)
    text_area_top_middle.anchor_point = (0.5, 0.0)
    text_area_top_middle.anchored_position = (WIDTH / 2, 0)

    text_area_top_right = label.Label(terminalio.FONT, text=text7)
    text_area_top_right.anchor_point = (0.5, 0.0)
    text_area_top_right.anchored_position = ((WIDTH/6)*5, 0)

    text_area_middle_left = label.Label(terminalio.FONT, text=text6)
    text_area_middle_left.anchor_point = (0.5, 0.5)
    text_area_middle_left.anchored_position = (WIDTH/6, HEIGHT / 2)

    text_area_middle_middle = label.Label(terminalio.FONT, text=text5)
    text_area_middle_middle.anchor_point = (0.5, 0.5)
    text_area_middle_middle.anchored_position = (WIDTH / 2, HEIGHT / 2)

    text_area_middle_right = label.Label(terminalio.FONT, text=text4)
    text_area_middle_right.anchor_point = (0.5, 0.5)
    text_area_middle_right.anchored_position = ((WIDTH/6)*5, HEIGHT / 2)

    text_area_bottom_left = label.Label(terminalio.FONT, text=text3)
    text_area_bottom_left.anchor_point = (0.5, 1.0)
    text_area_bottom_left.anchored_position = (WIDTH/6, HEIGHT)

    text_area_bottom_middle = label.Label(terminalio.FONT, text=text2)
    text_area_bottom_middle.anchor_point = (0.5, 1.0)
    text_area_bottom_middle.anchored_position = (WIDTH / 2, HEIGHT)

    text_area_bottom_right = label.Label(terminalio.FONT, text=text1)
    text_area_bottom_right.anchor_point = (0.5, 1.0)
    text_area_bottom_right.anchored_position = ((WIDTH/6)*5, HEIGHT)

    text_group = displayio.Group()
    text_group.append(text_area_top_middle)
    text_group.append(text_area_top_left)
    text_group.append(text_area_top_right)
    text_group.append(text_area_middle_middle)
    text_group.append(text_area_middle_left)
    text_group.append(text_area_middle_right)
    text_group.append(text_area_bottom_middle)
    text_group.append(text_area_bottom_left)
    text_group.append(text_area_bottom_right)

    display.show(text_group)
