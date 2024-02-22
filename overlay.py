from PIL import Image
import pyglet
import win32gui
import win32con
import io
from pyglet.gl import glClearColor

def create_overlay(image_data, recognized_text, offset=(0, 0)):
    image = Image.open(io.BytesIO(image_data))
    width, height = image.size

    custom_title = "Pyglet Overlay"
    window = pyglet.window.Window(width, height, style=pyglet.window.Window.WINDOW_STYLE_BORDERLESS,
                                  caption=custom_title)

    hwnd = win32gui.FindWindow(None, custom_title)
    win32gui.SetWindowPos(hwnd, win32con.HWND_TOPMOST, offset[0], offset[1], width, height, 0)
    glClearColor(0, 0, 0, 0)

    font_size = 20
    document = pyglet.text.decode_text(recognized_text)
    document.set_style(0, len(recognized_text), dict(color=(255, 255, 255, 255), font_size=font_size))
    layout = pyglet.text.layout.TextLayout(document, width, height, multiline=True, wrap_lines=True)

    # Уменьшение размера шрифта, пока текст не уместится
    while layout.content_height > height and font_size > 6:
        font_size -= 1
        document.set_style(0, len(recognized_text), dict(color=(255, 255, 255, 255), font_size=font_size))
        layout = pyglet.text.layout.TextLayout(document, width, height, multiline=True, wrap_lines=True)

    @window.event
    def on_draw():
        window.clear()
        layout.draw()

    @window.event
    def on_key_press(symbol, _modifiers):
        if symbol == pyglet.window.key.ESCAPE:
            window.close()

    pyglet.app.run()