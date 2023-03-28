import time
import tkinter as tk
from PIL import ImageTk, Image
import pyautogui
from mss import mss
import ctypes
import keyboard


def take_screenshot():
    screen_capture = ScreenCapture()
    screen_capture.mainloop()


class ScreenCapture(tk.Tk):
    def __init__(self):
        super().__init__()

        with mss() as sct:
            bbox = (0, 0, self.winfo_screenwidth(), self.winfo_screenheight())
            self.full_screenshot = sct.grab(bbox)
            self.full_screenshot = Image.frombytes("RGB", self.full_screenshot.size, self.full_screenshot.bgra, "raw",
                                                   "BGRX")

        self.photoimage = ImageTk.PhotoImage(self.full_screenshot)

        self.overrideredirect(True)
        self.attributes('-alpha', 1, '-topmost', True)
        self.geometry("{0}x{1}+0+0".format(self.winfo_screenwidth(), self.winfo_screenheight()))

        self.canvas = tk.Canvas(self, bg='white', highlightthickness=0)
        self.canvas.pack(fill='both', expand=True)

        self.canvas.create_image(0, 0, image=self.photoimage, anchor=tk.NW)

        self.start_x, self.start_y = None, None
        self.end_x, self.end_y = None, None
        self.click_count = 0

        self.canvas.bind('<Button-1>', self.on_click)
        self.canvas.bind('<B1-Motion>', self.on_drag)
        self.canvas.bind('<ButtonRelease-1>', self.on_release)

        self.update()
        ctypes.windll.user32.SetForegroundWindow(self.winfo_id())


    def on_click(self, event):
        self.start_x, self.start_y = event.x, event.y

    def on_drag(self, event):
        self.canvas.delete('selected_area')
        self.end_x, self.end_y = event.x, event.y
        self.canvas.create_rectangle(self.start_x, self.start_y, self.end_x, self.end_y,
                                     outline='black', width=2, tags='selected_area')

    def on_release(self, event):
        self.attributes('-alpha', 0)
        self.update()

        bbox = (self.start_x, self.start_y, self.end_x, self.end_y)
        cropped_image = self.full_screenshot.crop(bbox)

        self.destroy()
        cropped_image.show()


keyboard.add_hotkey('ctrl+shift+s', take_screenshot)

# Wait for events
keyboard.wait()
