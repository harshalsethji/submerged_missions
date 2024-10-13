from hub import *
import runloop
import distance_sensor
import motor
import time

async def garbage_can():
    for i in range(4):


        while distance_sensor.distance(port.B) >= 250 or distance_sensor.distance(port.B) == -1:
            distance = distance_sensor.distance(port.B)
            print(distance)
            print("Moving")
            motor.run(port.A, -100)
            motor.run(port.E, 100)
            time.sleep(0.1)

        distance = distance_sensor.distance(port.B)
        print(distance)
        motor.run(port.A, 0)
        motor.run(port.E, 0)
        print("turn")

        motor.run(port.A, 100)
        motor.run(port.E, 100)
        time.sleep(1.5)
        motor.run(port.A, 0)
        motor.run(port.E, 0)


        for i in range(5):
            motor.run(port.D, -50)
            time.sleep(0.5)
            print("lowering the arm")
        
        print("moving forward")
        motor.run(port.D, 0)
        motor.run(port.A, -100)
        motor.run(port.E, 100)
        time.sleep(distance / 125)
        motor.run(port.A, 0)
        motor.run(port.E, 0)


        for i in range(5):
            motor.run(port.D, 50)
            time.sleep(0.5)
            print("raising the arm")

        motor.run(port.D, 0)

        print("moving back")
        motor.run(port.A, 100)
        motor.run(port.E, -100)
        time.sleep(distance / 150)
        motor.run(port.A, 0)
        motor.run(port.E, 0)

        print("turn")
        motor.run(port.A, -100)
        motor.run(port.E, -100)
        time.sleep(1.5)
        motor.run(port.A, 0)
        motor.run(port.E, 0)

async def main():
    await light_matrix.write("Hi!")
    await garbage_can()

runloop.run(main())
