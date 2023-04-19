from PIL import Image
import pyglet
import win32gui
import win32con
import io
from pyglet.gl import glClearColor

def create_overlay(image_data, recognized_words, offset=(0, 0)):
    image = Image.open(io.BytesIO(image_data))
    width, height = image.size

    custom_title = "Pyglet Overlay"
    window = pyglet.window.Window(width, height, style=pyglet.window.Window.WINDOW_STYLE_BORDERLESS, caption=custom_title)

    hwnd = win32gui.FindWindow(None, custom_title)
    win32gui.SetWindowPos(hwnd, win32con.HWND_TOPMOST, offset[0], offset[1], width, height, 0)

    glClearColor(0, 0, 0, 0)

    labels = []
    for word, coords, avg_symbol_height in recognized_words:
        x = coords[0].x
        y = height - coords[0].y
        font_size = int(avg_symbol_height)
        if font_size < 1:
            font_size = 1
        label = pyglet.text.Label(
            word,
            font_size=font_size,
            x=x,
            y=y,
            anchor_x="left",
            anchor_y="top",
            color=(255, 255, 255, 255),
        )
        labels.append(label)

    @window.event
    def on_draw():
        window.clear()
        for label in labels:
            label.draw()

    @window.event
    def on_key_press(symbol, _modifiers):
        if symbol == pyglet.window.key.ESCAPE:
            window.close()

    pyglet.app.run()