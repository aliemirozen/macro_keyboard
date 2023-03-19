import time
import board
import digitalio
import usb_hid
from adafruit_hid.keycode import Keycode
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.consumer_control import ConsumerControl
from adafruit_hid.consumer_control_code import ConsumerControlCode

cc = ConsumerControl(usb_hid.devices)

keyboard = Keyboard(usb_hid.devices)

write_text = KeyboardLayoutUS(keyboard)

buttons = [board.GP0, board.GP2,board.GP4,board.GP6,board.GP8,board.GP10]
key = [digitalio.DigitalInOut(pin_name) for pin_name in buttons]
for x in range(0,len(buttons)):
    key[x].direction = digitalio.Direction.INPUT
    key[x].pull = digitalio.Pull.DOWN

while True:
    
    if key[0].value:
        keyboard.send(Keycode.GUI, Keycode.C)
        time.sleep(0.1)
        #Kopyalama komutu
        
    if key[2].value:
        keyboard.send(Keycode.GUI, Keycode.V)
        time.sleep(0.1)
        #Yapıştırma komutu
        
    if key[4].value:
        keyboard.send(Keycode.GUI, Keycode.X)
        time.sleep(0.3)
        #Kesme komutu

    if key[6].value:
        keyboard.send(Keycode.GUI, Keycode.K, Keycode.C)
        time.sleep(0.1)
        #Visual Studio da seçilenleri yorum satırı yapma komutu

    if key[8].value:
        keyboard.send(Keycode.GUI, Keycode.K, Keycode.U)
        time.sleep(0.1)
        #Visual Studio da seçilen yorum satırlarını normal satırlara çevirme komutu
        
    if key[10].value:
        keyboard.send(Keycode.GUI, Keycode.Z)
        time.sleep(0.3)
        #Geri alma komutu
        
    time.sleep(0.1)

#-----------------------------------------------------------------------------------

#Yapılabilecek Örnek Komutlar:

#1) cc.send(ConsumerControlCode.VOLUME_DECREMENT) ---> Ses Yükseltme Komutu.

#2) cc.send(ConsumerControlCode.VOLUME_INCREMENT) ---> Ses Kısma Komutu.

#3) cc.send(ConsumerControlCode.MUTE) ---> Ses Kapatma Komutu.

#4) cc.send(ConsumerControlCode.PLAY_PAUSE) ---> Başlat-Durdur Komutu.

#5) write_text.write('aliemirozen') ---> Tuş Basıldığında "aliemirozen" yazdırır.

#6)
#keyboard.send(Keycode.GUI, Keycode.SPACE)
#time.sleep(0.3)
#write_text.write('Whatsapp\n')
#time.sleep(3)
#keyboard.send(Keycode.GUI, Keycode.F)
#time.sleep(2)
#write_text.write('aliemirozen\n')
#time.sleep(2)
#write_text.write('Selam\n')
# Bu kod whatsapp a girerek kişi aramasına "aliemirozen" yazıyor ve aliemirozen kişisine "Selam" mesajı iletiyor.
