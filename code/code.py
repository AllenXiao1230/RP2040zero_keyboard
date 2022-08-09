#======================================
#mode_home
link1_home='https://www.netflix.com/browse'
link2_home='https://www.youtube.com/'
link3_home='https://www.facebook.com/'
link4_home='D:\WYI'
link5_home='d:\Desktop\LINE.lnk'
link6_home=''
link8_home=''
link9_home=''

text1_home='NF'
text2_home='YT'
text3_home='FB'
text4_home='WYI'
text5_home='LINE'
text6_home='6'
text8_home='8'
text9_home='9'

#======================================
#mode_comp
link1_comp='https://www.netflix.com/browse'
link2_comp='https://www.youtube.com/'
link3_comp='https://www.facebook.com/'
link4_comp='D:\WYI'
link5_comp='d:\Desktop\LINE.lnk'
link6_comp=''
link8_comp=''
link9_comp=''


text1_comp='NF'
text2_comp='YT'
text3_comp='FB'
text4_comp='WYI'
text5_comp='LINE'
text6_comp='6'
text8_comp='8'
text9_comp='9'
#======================================

mode = 'home'

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
import rainbowio
import rotaryio
from adafruit_display_text import label
import terminalio

from display_init import *


kpd = Keyboard(usb_hid.devices)
keyboard_layout = KeyboardLayoutUS(kpd)



#======================================
def linkf1():
    kpd.send(Keycode.WINDOWS, Keycode.R)
    time.sleep(1)
    if mode == 'home':
        keyboard_layout.write('cmd.exe /k "start {}" && exit'.format(link1_home))
    else:
        keyboard_layout.write('cmd.exe /k "start {}" && exit'.format(link1_comp))
    kpd.send(Keycode.ENTER)
    
def linkf2():
    kpd.send(Keycode.WINDOWS, Keycode.R)
    time.sleep(1)
    if mode == 'home':
        keyboard_layout.write('cmd.exe /k "start {}" && exit'.format(link2_home))
    else:
        keyboard_layout.write('cmd.exe /k "start {}" && exit'.format(link2_comp))
    kpd.send(Keycode.ENTER)
    
def linkf3():
    kpd.send(Keycode.WINDOWS, Keycode.R)
    time.sleep(1)
    if mode == 'home':
        keyboard_layout.write('cmd.exe /k "start {}" && exit'.format(link3_home))
    else:
        keyboard_layout.write('cmd.exe /k "start {}" && exit'.format(link3_comp))
    kpd.send(Keycode.ENTER)
    
def linkf4():
    kpd.send(Keycode.WINDOWS, Keycode.R)
    time.sleep(1)
    if mode == 'home':
        keyboard_layout.write('cmd.exe /k "start {}" && exit'.format(link4_home))
    else:
        keyboard_layout.write('cmd.exe /k "start {}" && exit'.format(link4_comp))
    kpd.send(Keycode.ENTER)
    
def linkf5():
    kpd.send(Keycode.WINDOWS, Keycode.R)
    time.sleep(1)
    if mode == 'home':
        keyboard_layout.write('cmd.exe /k "start {}" && exit'.format(link5_home))
    else:
        keyboard_layout.write('cmd.exe /k "start {}" && exit'.format(link5_comp))
    kpd.send(Keycode.ENTER)
    
def linkf6():
    kpd.send(Keycode.WINDOWS, Keycode.R)
    time.sleep(1)
    if mode == 'home':
        keyboard_layout.write('cmd.exe /k "start {}" && exit'.format(link6_home))
    else:
        keyboard_layout.write('cmd.exe /k "start {}" && exit'.format(link6_comp))
    kpd.send(Keycode.ENTER)
    
def linkf7():
    global mode
    if mode == 'comp':
        mode='home'
        mi='HOME'
        call_show_map(text1_home,text2_home,text3_home,text4_home,text5_home,text6_home,mi,text8_home,text9_home)
        print('sth')
    elif mode == 'home':
        mode='comp'
        mi='COMP'
        call_show_map(text1_comp,text2_comp,text3_comp,text4_comp,text5_comp,text6_comp,mi,text8_comp,text9_comp)
        print('stc')
        
def linkf8():
    kpd.send(Keycode.WINDOWS, Keycode.R)
    time.sleep(1)
    if mode == 'home':
        keyboard_layout.write('cmd.exe /k "start {}" && exit'.format(link8_home))
    else:
        keyboard_layout.write('cmd.exe /k "start {}" && exit'.format(link8_comp))
    kpd.send(Keycode.ENTER)

def linkf9():
    kpd.send(Keycode.WINDOWS, Keycode.R)
    time.sleep(1)
    if mode == 'home':
        keyboard_layout.write('cmd.exe /k "start {}" && exit'.format(link9_home))
    else:
        keyboard_layout.write('cmd.exe /k "start {}" && exit'.format(link9_comp))
    kpd.send(Keycode.ENTER)
#======================================
display_init()
mi='HOME'
call_show_map(text1_home,text2_home,text3_home,text4_home,text5_home,text6_home,mi,text8_home,text9_home)

button = digitalio.DigitalInOut(board.GP9)
button.direction = digitalio.Direction.INPUT
button.pull = digitalio.Pull.UP

encoder = rotaryio.IncrementalEncoder(board.GP11, board.GP10)

cc = ConsumerControl(usb_hid.devices)

last_position = encoder.position
button_state = None
# define keys for 4x4 v1
keys = keypad.KeyMatrix(
    row_pins=(board.GP14, board.GP15, board.GP26),
    column_pins=(board.GP27, board.GP28, board.GP29),
    columns_to_anodes=True,
)


keymap = [
    ("bt1", "a"),
    ("bt2", "b"),
    ("bt3", "c"),
    ("bt4", "d"),
    ("bt5", "e"),
    ("bt6", "f"),
    ("bt7", "g"),
    ("bt8", "h"),
    ("bt9", "i")
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
    if not button.value and button_state is None:
        button_state = "pressed"
    if button.value and button_state == "pressed":
        print("Button pressed.")
        cc.send(ConsumerControlCode.MUTE)
        button_state = None
        

    
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
                elif item == "a":
                    linkf1()
                elif item == "b":
                    linkf2()
                elif item == "c":
                    linkf3()
                elif item == "d":
                    linkf4()
                elif item == "e":
                    linkf5()
                elif item == "f":
                    linkf6()
                elif item == "g":
                    linkf7()
                elif item == "h":
                    linkf8()
                elif item == "i":
                    linkf9()
                
        else:
            # Release any still-pressed modifier keys
            for item in sequence:
                if isinstance(item, int) and item >= 0:
                    kpd.release(item)


