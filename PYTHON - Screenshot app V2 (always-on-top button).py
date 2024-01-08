import pyautogui
import tkinter as tk

def take_screenshot():
    screenshot = pyautogui.screenshot()
    screenshot.save('screenshot.png')
    print("Screenshot taken and saved as 'screenshot.png'")

def toggle_always_on_top():
    root.attributes('-topmost', not root.attributes('-topmost'))

root = tk.Tk()
root.title("Screenshot Taker")

screenshot_button = tk.Button(root, text="Take Screenshot", command=take_screenshot)
screenshot_button.pack(padx=10, pady=5)

always_on_top_button = tk.Button(root, text="Toggle Always On Top", command=toggle_always_on_top)
always_on_top_button.pack(padx=10, pady=5)

root.mainloop()
