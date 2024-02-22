import ctypes
from ctypes import wintypes
from image_reader import recognize_japanese_text
from overlay import create_overlay
from image_extractor import take_screenshot
from furigana import to_hiragana
from gpt import generate_response

byref = ctypes.byref
user32 = ctypes.windll.user32
MOD_CONTROL = 0x0002
VK_F1 = 0x70
WM_HOTKEY = 0x0312

HOTKEYS = {
    1: (MOD_CONTROL, VK_F1)
}

def register_hotkeys():
    for id, (mod, key) in HOTKEYS.items():
        if not user32.RegisterHotKey(None, id, mod, key):
            raise ValueError(f"Unable to register hotkey: {mod}, {key}")

def main():
    image_data, top_left_coords = take_screenshot()
    recognized_text = recognize_japanese_text(image_data)
    gpt = generate_response(recognized_text)
    create_overlay(image_data, gpt, top_left_coords)

def listen_for_hotkey():
    try:
        msg = wintypes.MSG()
        while user32.GetMessageA(byref(msg), None, 0, 0) != 0:
            if msg.message == WM_HOTKEY:
                main()
            user32.TranslateMessage(byref(msg))
            user32.DispatchMessageA(byref(msg))

    finally:
        for id in HOTKEYS:
            user32.UnregisterHotKey(None, id)

if __name__ == "__main__":
    register_hotkeys()
    listen_for_hotkey()
