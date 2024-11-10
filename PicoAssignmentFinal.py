from machine import Pin, ADC, PWM
import time 


potentiometer = ADC(Pin(26))  # Potentiometer connected to GPIO 26
led1 = PWM(Pin(15))            # First LED connected to GPIO 15
led2 = PWM(Pin(14))            # Second LED connected to GPIO 14
buzzer = PWM(Pin(16))          # Buzzer connected to GPIO 16

# Set PWM frequency for the LEDs and buzzer
led1.freq(1000)  # Ensures LEDs don't flicker
led2.freq(1000)  # Ensures LED don't flicker
buzzer.freq(1000)  # Controls pitch


while True:
    # Reads potentiometer value
    pot_value = potentiometer.read_u16()

    # Calculate the LED brightness
    led1_brightness = pot_value  # Brightness of LED1 based on potentiometer
    led2_brightness = 65535 - pot_value  # Brightness of LED2 inversely related to LED1

    # Set LED brightness based on Potential meter
    led1.duty_u16(led1_brightness)  # Sets duty cycle for LED1 (Brightness)
    led2.duty_u16(led2_brightness)  # Sets duty cycle for LED2 (Brightness)
    
    # Set buzzer frequency based on potentiometer value
    if pot_value < 21845:  # Less than 1/3 of max
        buzzer.freq(1000)  
    elif pot_value < 43690: # Between 1/3 and 2/3
        buzzer.freq(1500)  
    else:
        buzzer.freq(2000)  # Over 2/3

    buzzer.duty_u16(32768)  # 50% duty cycle (volume) for the buzzer

    # Small delay to smooth the loop
    time.sleep(0.1)

# The program will go on forever unless it is stopped
