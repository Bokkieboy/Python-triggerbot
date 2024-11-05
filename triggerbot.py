import time
import random
from pynput.mouse import Controller as MouseController, Button
from pynput.keyboard import Controller as KeyboardController
from PIL import ImageGrab
from Quartz import CGEventSourceKeyState, kCGEventSourceStateHIDSystemState

# Initialize mouse and keyboard controllers
mouse = MouseController()
keyboard = KeyboardController()

# Function to get the color of the center pixel
def get_center_pixel_color():
    screen = ImageGrab.grab()
    width, height = screen.size
    center_pixel = screen.getpixel((width // 2, height // 2))
    return center_pixel

# Function to check if Caps Lock is active
def is_caps_lock_on():
    return CGEventSourceKeyState(kCGEventSourceStateHIDSystemState, 0x39)  # 0x39 is the key code for Caps Lock

# Function to check if Shift is active
def shift_on():
    return CGEventSourceKeyState(kCGEventSourceStateHIDSystemState, 0x10)  # 0x10 is the key code for Shift

# Main function to monitor pixel color and click if color changes
def monitor_pixel():
    previous_color = get_center_pixel_color()
    while True:
        # Only activate if Caps Lock is on
        if shift_on():
            current_color = get_center_pixel_color()
            if current_color != previous_color:
                time.sleep(random.uniform(0.1, 0.3)) # Random delay to act like a human
                mouse.click(Button.left)
                previous_color = current_color
            time.sleep(1)  # Adjust the delay as needed

# Start the monitoring in a try-except to handle keyboard interrupts gracefully
try:
    print("Monitoring started. Press Ctrl+C to stop.")
    monitor_pixel()
except KeyboardInterrupt:
    print("Monitoring stopped.")