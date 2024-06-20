from flask import Flask, render_template
import RPi.GPIO as GPIO
import time


switch_pins = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]


def diag():
    print("// Lamp Control System Diagnostics")
    print("Initializing...")
    GPIO.setmode(GPIO.BCM)
    for pin in switch_pins:
        GPIO.setup(pin, GPIO.OUT)
        GPIO.output(pin, GPIO.HIGH)  # Reset the state of all switches
    
    # turn off all switches

    for pin in switch_pins:
        GPIO.output(pin, GPIO.LOW)
        time.sleep(1)
        GPIO.output(pin, GPIO.HIGH)
        time.sleep(1)

    for i in range(0, 10):
        for pin in switch_pins:
            GPIO.output(pin, GPIO.LOW)
        time.sleep(1)
        for pin in switch_pins:
            GPIO.output(pin, GPIO.HIGH)
        time.sleep(1)

    while True :
        pin = int(input("Enter the pin number to test: "))
        GPIO.output(pin, GPIO.HIGH)



if __name__ == "__main__":
    diag()
    print("System Initialized !")
    print("Diagnostics Completed !")
    print("Ready to run the main program")
    print("Exiting...")