import RPi.GPIO as GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
class InputHandler:
    def __init__(self, topPins, botPins):
        self.topPins = topPins
        self.botPins = botPins
        for i in topPins:
            GPIO.setup(i, GPIO.IN)
        for i in botPins:
            GPIO.setup(i, GPIO.IN)
    def checkInput(self):
        while True:
            for i in range(len(self.topPins)):
                state = 0
                while GPIO.input(self.topPins[i]):
                    state = GPIO.input(self.botPins[i])
                if state == 1:
                    return i
GPIO.cleanup()