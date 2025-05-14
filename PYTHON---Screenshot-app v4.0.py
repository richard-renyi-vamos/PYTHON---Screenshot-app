import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import pyautogui
from datetime import datetime
from PIL import ImageGrab
import keyboard
import os
import webbrowser
import winsound

class ScreenshotApp:
    def __init__(self, master):
        self.master = master
        master.title("Screenshot App")

        # Default values
        self.hotkey = "F12"
        self.save_dir = os.getcwd()
        self.capture_full_screen = tk.BooleanVar(value=True)
        self.image_format = tk.StringVar(value="png")

        # GUI Layout
        self.label = tk.Label(master, text="Press the hotkey or click 'Take Screenshot'")
        self.label.pack(pady=5)

        self.take_screenshot_button = tk.Button(master, text="Take Screenshot", command=self.take_screenshot)
        self.take_screenshot_button.pack(pady=5)

        self.hotkey_label = tk.Label(master, text="Assign Hotkey (e.g., F12):")
        self.hotkey_label.pack()
        self.hotkey_entry = tk.Entry(master)
        self.hotkey_entry.pack()
        self.assign_hotkey_button = tk.Button(master, text="Assign Hotkey", command=self.assign_hotkey)
        self.assign_hotkey_button.pack(pady=5)

        self.select_dir_button = tk.Button(master, text="Select Save Directory", command=self.select_directory)
        self.select_dir_button.pack(pady=5)

        self.checkbox = tk.Checkbutton(master, text="Capture Full Screen", variable=self.capture_full_screen)
        self.checkbox.pack(pady=5)

        self.format_label = tk.Label(master, text="Image Format:")
        self.format_label.pack()
        self.format_dropdown = ttk.Combobox(master, textvariable=self.image_format, values=["png", "jpg"], state="readonly")
        self.format_dropdown.pack()

        self.quit_button = tk.Button(master, text="Quit", command=master.quit)
        self.quit_button.pack(pady=5)

    def take_screenshot(self):
        now = datetime.now()
        timestamp = now.strftime("%Y-%m-%d_%H-%M-%S")
        filename = f"screenshot_{timestamp}.{self.image_format.get()}"
        filepath = os.path.join(self.save_dir, filename)

        if self.capture_full_screen.get():
            screenshot = pyautogui.screenshot()
        else:
            self.label.config(text="Drag to select region...")
            screenshot = ImageGrab.grab(bbox=pyautogui.prompt("Enter region as x1,y1,x2,y2"))

        try:
            screenshot.save(filepath)
            winsound.MessageBeep()
            self.label.config(text=f"Screenshot saved: {filepath}")
            webbrowser.open(filepath)  # Automatically open the screenshot
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def assign_hotkey(self):
        keyboard.unhook_all()
        hotkey = self.hotkey_entry.get()
        if not hotkey:
            messagebox.showwarning("Input Needed", "Please enter a hotkey.")
            return

        try:
            keyboard.add_hotkey(hotkey, self.take_screenshot)
            self.hotkey = hotkey
            self.label.config(text=f"Hotkey {hotkey} assigned successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to assign hotkey: {e}")

    def select_directory(self):
        directory = filedialog.askdirectory()
        if directory:
            self.save_dir = directory
            self.label.config(text=f"Save directory set to: {directory}")

def main():
    root = tk.Tk()
    app = ScreenshotApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
