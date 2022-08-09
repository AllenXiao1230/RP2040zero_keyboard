"""
    Code adapted from the following sources:
    MACROPAD Hotkey (https://learn.adafruit.com/macropad-hotkeys/project-code)
    Pico Four Keypad  (https://learn.adafruit.com/pico-four-key-macropad/code-the-four-keypad)
"""
import board
import keypad
import usb_hid
import digitalio
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.consumer_control import ConsumerControl
from adafruit_hid.consumer_control_code import ConsumerControlCode
import time
import neopixel
import rainbowio
import rotaryio


pixel_pin = board.GP0
num_pixels = 9

pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.3, auto_write=False)

def rainbow_cycle(wait):
    for j in range(255):
        for i in range(num_pixels):
            rc_index = (i * 256 // num_pixels) + j
            pixels[i] = rainbowio.colorwheel(rc_index & 255)
        pixels.show()
        #time.sleep(wait)
    
def breath(r,g,b):
    color=(r,g,b)
    pixels.fill(color)
    pixels.show()
    time.sleep(0.05)

kpd = Keyboard(usb_hid.devices)
keyboard_layout = KeyboardLayoutUS(kpd)

button = digitalio.DigitalInOut(board.GP9)
button.direction = digitalio.Direction.INPUT
button.pull = digitalio.Pull.UP

encoder = rotaryio.IncrementalEncoder(board.GP11, board.GP10)

cc = ConsumerControl(usb_hid.devices)


last_position = encoder.position

# define keys for 4x4 v1
keys = keypad.KeyMatrix(
    row_pins=(board.GP14, board.GP15, board.GP26),
    column_pins=(board.GP27, board.GP28, board.GP2),
    columns_to_anodes=True,
)


keymap = [
    ("Select all", [Keycode.LEFT_CONTROL, Keycode.A]),
    ("Cut", [Keycode.LEFT_CONTROL, Keycode.X]),
    ("Copy", [Keycode.LEFT_CONTROL, Keycode.C]),
    ("Paste", [Keycode.LEFT_CONTROL, Keycode.V]),
    ("Hello World", "open"),
    ("Cut", [Keycode.LEFT_CONTROL, Keycode.X]),
    ("Copy", [Keycode.LEFT_CONTROL, Keycode.C]),
    ("Paste", [Keycode.LEFT_CONTROL, Keycode.V]),
    ("Select all", [Keycode.LEFT_CONTROL, Keycode.A]),
    ("Cut", [Keycode.LEFT_CONTROL, Keycode.X]),
    ("Copy", [Keycode.LEFT_CONTROL, Keycode.C]),
    ("Paste", [Keycode.LEFT_CONTROL, Keycode.V]),
    ("Select all", [Keycode.LEFT_CONTROL, Keycode.A]),
    ("Cut", [Keycode.LEFT_CONTROL, Keycode.X]),
    ("Copy", [Keycode.LEFT_CONTROL, Keycode.C]),
    ("Paste", [Keycode.LEFT_CONTROL, Keycode.V])
]

print("keymap:")
for key in keymap:
    print("\t", key[0])

def open():
    keyboard = Keyboard(usb_hid.devices)
    keyboard_layout = KeyboardLayoutUS(keyboard)

    time.sleep(2.5)

    keyboard.send(Keycode.WINDOWS, Keycode.R)
    time.sleep(0.5)

    keyboard_layout.write('cmd.exe /k "start https://www.youtube.com/watch?v=dQw4w9WgXcQ" && exit')
    keyboard.send(Keycode.ENTER)
    
def rgb_mode_switch():
    if rgb_mode == 'rainbow':
        rgb_mode = 'breath'
    else:
        rgb_mode = 'rainbow'
    
rgb_mode = 'rainbow'
i=0
pd='p'

white={'r':255,'g':100,'b':104}
rr=white['r']
gg=white['g']
bb=white['b']
r=255
g=255
b=255
while True:
    
    current_position = encoder.position
    position_change = current_position - last_position
    if position_change > 0:
        for _ in range(position_change):
            cc.send(ConsumerControlCode.VOLUME_INCREMENT)
        print(current_position)
    elif position_change < 0:
        for _ in range(-position_change):
            cc.send(ConsumerControlCode.VOLUME_DECREMENT)
        print(current_position)
    last_position = current_position
    
    if button.value==0:
        print("Button pressed.")
        cc.send(ConsumerControlCode.MUTE)
        
    
    #rainbow_cycle(0.005)
    if i == 30:
        pd = 'd'
    elif i == 0:
        pd = 'p'
    
    if pd == 'p':
        i+=1
    elif pd == 'd':
        i-=1
    
    pixels.brightness=i/100
    breath(r,g,b)
    
    key_event = keys.events.get()
    if key_event:  
        if key_event.pressed:
            print(keymap[key_event.key_number][0])
            sequence = keymap[key_event.key_number][1]
            for item in sequence:
                print(item)
                if isinstance(item, int):
                    if item >= 0:
                        kpd.press(item)
                    else:
                        kpdrelease(-item)
                elif item == "o":
                    open()
                
        else:
            # Release any still-pressed modifier keys
            for item in sequence:
                if isinstance(item, int) and item >= 0:
                    kpd.release(item)
