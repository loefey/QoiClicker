import time
import threading
import pyautogui
import keyboard

autoclicker_enabled = False

def autoclicker():
    while True:
        if autoclicker_enabled:
            pyautogui.click()
        time.sleep(0.1)

def toggle_autoclicker():
    global autoclicker_enabled
    autoclicker_enabled = not autoclicker_enabled
    print(f"Autoclicker {'enabled' if autoclicker_enabled else 'disabled'}")

def stop_program():
    global autoclicker_enabled
    autoclicker_enabled = False

autoclicker_thread = threading.Thread(target=autoclicker)

def hotkey_listener():
    toggle_hotkey = "ctrl+alt+a" # Change this to change the hotkey
    keyboard.add_hotkey(toggle_hotkey, toggle_autoclicker)
    print(f"Press '{toggle_hotkey}' to toggle autoclicker")
    keyboard.wait()

try:
    autoclicker_thread.start()
    hotkey_listener_thread = threading.Thread(target=hotkey_listener)
    hotkey_listener_thread.start()

except KeyboardInterrupt:
    autoclicker_enabled = False

finally:
    autoclicker_thread.join()
