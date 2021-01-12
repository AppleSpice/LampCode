import RPi.GPIO as GPIO

ledPin = 11
buttonPin = 12
ledState = False

def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(ledPin, GPIO.OUT)
    GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO. PUD_UP)

def buttonEvent(channel):
    global ledState
    print ('ButtonEvent GPIO%d' %channel)
    ledState = not ledState
    if ledState:
        print ('LIght on')
    else:
        print('LIGHT OFF now')
    GPIO.output(ledPin, ledState)

def loop():
    GPIO.add_event_detect(buttonPin, GPIO.FALLING,callback = buttonEvent,bouncetime=300)
    while True:
      pass

def destroy():
    GPIO.cleanup()
    print ('GPIO Pins cleared')

if __name__ == '__main__':
    print ('We starting')
    setup()
    try:
        loop()
    except KeyboardInterrupt:
        destroy()