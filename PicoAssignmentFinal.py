from machine import Pin, ADC, PWM
import time 

# Initialize the potentiometer, two LEDs, and buzzer
potentiometer = ADC(Pin(26))  # Potentiometer connected to GPIO 26
led1 = PWM(Pin(15))            # First LED connected to GPIO 15
led2 = PWM(Pin(14))            # Second LED connected to GPIO 14
buzzer = PWM(Pin(16))          # Buzzer connected to GPIO 16

# Set PWM frequency for the LEDs and buzzer
led1.freq(1000)  # 1 kHz frequency for LED PWM - Controls Brightness
led2.freq(1000)  # 1 kHz frequency for LED PWM - Controls Brightness
buzzer.freq(1000)  # Initial frequency for the buzzer - Controls Volume

# Main loop
while True:
    # Read the potentiometer value (0-65535), and display to terminal
    pot_value = potentiometer.read_u16()

    # Calculate the LED brightness
    led1_brightness = pot_value  # Brightness of LED1 based on potentiometer
    led2_brightness = 65535 - pot_value  # Brightness of LED2 inversely related to LED1

    # Set LED brightness based on calculated values (0-65535)
    led1.duty_u16(led1_brightness)  # Set duty cycle for LED1
    led2.duty_u16(led2_brightness)  # Set duty cycle for LED2

    # Set buzzer frequency based on potentiometer value
    if pot_value < 21845:  # Less than 1/3 of max
        buzzer.freq(1000)  # Tune A
    elif pot_value < 43690:  # Between 1/3 and 2/3
        buzzer.freq(1500)  # Tune B
    else:
        buzzer.freq(2000)  # Tune C

    buzzer.duty_u16(32768)  # 50% duty cycle for the buzzer

    # Small delay to smooth the loop
    time.sleep(0.1)

# Note: The program will run indefinitely. To stop it, you'll need to interrupt it.
