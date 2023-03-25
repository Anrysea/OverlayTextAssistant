import pyglet
import win32gui
import win32con
from pyglet import shapes
from pyglet.gl import glClearColor
from pyglet.window import Window, key

config = pyglet.gl.Config(double_buffer=True)
custom_title = "Pyglet Overlay"
window = Window(300, 100, config=config, style=Window.WINDOW_STYLE_BORDERLESS, caption=custom_title)
window.set_location(100, 100)

hwnd = win32gui.FindWindow(None, custom_title)
win32gui.SetWindowPos(hwnd, win32con.HWND_TOPMOST, 100, 100, 300, 100, 0)

batch = pyglet.graphics.Batch()
background = shapes.Rectangle(0, 0, 300, 100, color=(0, 0, 0, 128), batch=batch)

label = pyglet.text.Label(
    "Hello, World!",
    font_size=14,
    x=window.width // 2,
    y=window.height // 2,
    anchor_x="center",
    anchor_y="center",
    batch=batch,
)

@window.event
def on_draw():
    window.clear()
    glClearColor(0, 0, 0, 0)
    batch.draw()

@window.event
def on_key_press(symbol, modifiers):
    if symbol == key.ESCAPE:
        window.close()

pyglet.app.run()
