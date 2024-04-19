
import tkinter as tk
from tkinter import filedialog
import pyautogui
from datetime import datetime
from PIL import ImageGrab
import keyboard

class ScreenshotApp:
    def __init__(self, master):
        self.master = master
        master.title("Screenshot App")
        
        # Create GUI elements
        self.label = tk.Label(master, text="Press the hotkey or click 'Take Screenshot'")
        self.label.pack()
        
        self.take_screenshot_button = tk.Button(master, text="Take Screenshot", command=self.take_screenshot)
        self.take_screenshot_button.pack()
        
        self.hotkey_label = tk.Label(master, text="Assign Hotkey (e.g., F12):")
        self.hotkey_label.pack()
        
        self.hotkey_entry = tk.Entry(master)
        self.hotkey_entry.pack()
        
        self.assign_hotkey_button = tk.Button(master, text="Assign Hotkey", command=self.assign_hotkey)
        self.assign_hotkey_button.pack()
        
        self.quit_button = tk.Button(master, text="Quit", command=master.quit)
        self.quit_button.pack()
        
        # Default hotkey
        self.hotkey = "F12"
        
    def take_screenshot(self):
        # Get the current datetime to use in the screenshot filename
        now = datetime.now()
        timestamp = now.strftime("%Y-%m-%d_%H-%M-%S")
        
        # Capture the screenshot
        screenshot = pyautogui.screenshot()
        
        # Save the screenshot to disk
        screenshot.save(f"screenshot_{timestamp}.png")
        self.label.config(text="Screenshot saved successfully!")
        
    def assign_hotkey(self):
        # Remove any existing hotkey
        keyboard.unhook_all()
        
        # Get the hotkey from the entry field
        hotkey = self.hotkey_entry.get()
        
        # Assign the new hotkey
        keyboard.add_hotkey(hotkey, self.take_screenshot)
        self.hotkey = hotkey
        self.label.config(text=f"Hotkey {hotkey} assigned successfully!")

def main():
    root = tk.Tk()
    app = ScreenshotApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
