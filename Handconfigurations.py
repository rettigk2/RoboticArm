# SDA = pin.SDA_1
# SCL = pin.SCL_1
# SDA_1 = pin.SDA
# SCL_1 = pin.SCL

from adafruit_servokit import ServoKit
import board
import busio
import RPi.GPIO as GPIO
import time

# On the Jetson Nano
# Bus 0 (pins 28,27) is board SCL_1, SDA_1 in the jetson board definition file
# Bus 1 (pins 5, 3) is board SCL, SDA in the jetson definition file
# Default is to Bus 1; We are using Bus 0, so we need to construct the busio first ...


print("Initializing Servos")
i2c_bus0=(busio.I2C(board.SCL_1, board.SDA_1))
print("Initializing ServoKit")
kit = ServoKit(channels=16)
# kit[0] is the bottom servo
# kit[1] is the top servo
print("Done initializing")

fingers = [0, 1, 2, 3, 4, 5]
hand = len(fingers)

for i in range(0,hand):
	kit.servo[i].angle=100 #set default hand position

time.sleep(0.5)


while True:	
	time.sleep(0.5)
	position = input("Enter hand positions: \n 1. Closed Hand \n 2. Middle Finger \n 3. Open Hand \n")
	if position == "Closed Hand":
		kit.servo[0].angle = 25
		kit.servo[1].angle = 30
		kit.servo[2].angle = 20
		kit.servo[3].angle = 20
		kit.servo[4].angle = 20
		kit.servo[5].angle = 20
		print("\nOpen Hand Position\n")
	elif position == "Middle Finger":
		kit.servo[0].angle = 30
		kit.servo[1].angle = 170
		kit.servo[2].angle = 30
		kit.servo[3].angle = 180
		kit.servo[4].angle = 30
		kit.servo[5].angle = 30
		print("\nMiddle Finger Position\n")
	elif position == "Open Hand":
		kit.servo[0].angle = 175
		kit.servo[1].angle = 175
		kit.servo[2].angle = 175
		kit.servo[3].angle = 175
		kit.servo[4].angle = 175
		kit.servo[5].angle = 175
		print("\nMiddle Finger Position\n")
	else:
		print("\nError: input one of the options, they are case sensitive \n")
	

output_pin = output_pins.get(GPIO.model, None)
if output_pin is None:
    raise Exception('PWM not supported on this board')


# middle finger = 30, 170, 30, 180, 30, 30
# closed hand = 25, 30, 20, 20, 20, 20

