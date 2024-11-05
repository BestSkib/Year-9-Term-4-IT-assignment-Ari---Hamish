from machine import Pin, ADC, PWM
import time 


buzzer = PWM(Pin(15))


def play_tone(frequency, duration):
    
    buzzer.freq(frequency)
   
    buzzer.duty_u16(200)
    
    time.sleep(duration)
    
    buzzer.duty_u16(0)

led = Pin(1, Pin.OUT)



play_tone(392, 0.5)  # G4 - 392 Hz
led.toggle()
time.sleep(0.1)

play_tone(392, 0.5)  # G4 - 392 Hz
led.toggle()
time.sleep(0.1)

play_tone(392, 0.5)  # G4 - 392 Hz
led.toggle()
time.sleep(0.1)

play_tone(311, 0.35)  # Eb4 - 311 Hz
led.toggle()
time.sleep(0.1)

play_tone(466, 0.15)  # Bb4 - 466 Hz
led.toggle()
time.sleep(0.1)

play_tone(392, 0.5)  # G4 - 392 Hz
led.toggle()
time.sleep(0.1)

play_tone(311, 0.35)  # Eb4 - 311 Hz
led.toggle()
time.sleep(0.1)

play_tone(466, 0.15)  # Bb4 - 466 Hz
led.toggle()
time.sleep(0.1)

play_tone(392, 0.5)  # G4 - 392 Hz
led.toggle()
time.sleep(0.3)

#second phrase
play_tone(587, 0.5)  # D5 - 587 Hz
led.toggle()
time.sleep(0.1)

play_tone(587, 0.5)  # D5 - 587 Hz
led.toggle()
time.sleep(0.1)

play_tone(587, 0.5)  # D5 - 587 Hz
led.toggle()
time.sleep(0.1)

play_tone(622, 0.35)  # Eb5 - 622 Hz
led.toggle()
time.sleep(0.1)

play_tone(466, 0.15)  # Bb4 - 466 Hz
led.toggle()
time.sleep(0.1)

play_tone(370, 0.5)  # Fs4 - 466 Hz
led.toggle()
time.sleep(0.1)

play_tone(311, 0.35)  # Eb4 - 311 Hz
led.toggle()
time.sleep(0.1)

play_tone(466, 0.15)  # Bb4 - 466 Hz
led.toggle()
time.sleep(0.1)

play_tone(392, 0.5)  # G4 - 392 Hz
led.toggle()
time.sleep(0.3)

# Middle section
play_tone(784, 0.5)  # G5 - 587 Hz
led.toggle()
time.sleep(0.1)

play_tone(392, 0.15)  # G4 - 392 Hz
led.toggle()
time.sleep(0.15)

play_tone(392, 0.15)  # G4 - 392 Hz
led.toggle()
time.sleep(0.15)

play_tone(784, 0.5)  # G5 - 587 Hz
led.toggle()
time.sleep(0.1)

play_tone(466, 0.15)  # Bb4 - 466 Hz
led.toggle()
time.sleep(0.1)

play_tone(370, 0.5)  # Fs4 - 466 Hz
led.toggle()
time.sleep(0.1)

play_tone(311, 0.35)  # Eb4 - 311 Hz
led.toggle()
time.sleep(0.1)

play_tone(466, 0.15)  # Bb4 - 466 Hz
led.toggle()
time.sleep(0.1)

play_tone(392, 0.5)  # G4 - 392 Hz
led.toggle()
time.sleep(0.3)


# Clean up by deactivating the PWM
buzzer.deinit()









    

    
