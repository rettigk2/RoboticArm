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
servo_length = len(fingers)
for i in range(0,servo_length):
	kit.servo[i].angle=100
	# kit.servo[1].angle=degree
	# time.sleep(0.01)

time.sleep(0.5)


while True:	
	time.sleep(0.5)
	for i in range(0,servo_length):
		inputangle = float(input("Enter Servo Angle for : "))
		kit.servo[i].angle=inputangle

output_pin = output_pins.get(GPIO.model, None)
if output_pin is None:
    raise Exception('PWM not supported on this board')


