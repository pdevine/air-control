import pyglet.gl
from pyglet.graphics import draw
from pyglet.window import mouse

class DisplayObject(object):
    def __init__(self):
        pass

    def update(self, tick):
        pass

    def draw(self):
        pass

class Path(DisplayObject):
    def __init__(self):
        self.dragging = False
        self.coords = []

    def draw(self):
        vertices = len(self.coords) / 2
        draw(vertices, pyglet.gl.GL_POINTS, ('v2i', tuple(self.coords)))

    def update(self, tick):
        pass

    def handle_mouse_down(self, x, y, button, modifiers):
        if button == mouse.LEFT:
            self.coords = []
            self.dragging = True

    def handle_mouse_drag(self, x, y, dx, dy, buttons, modifiers):
        if self.dragging:
            self.coords.append(x)
            self.coords.append(y)

    def handle_mouse_up(self, x, y, button, modifiers):
        self.dragging = False

class Airplane(DisplayObject):
    def __init__(self, batch=None):
        pass

if __name__ == '__main__':
    from pyglet import window
    from pyglet import clock
    from pyglet.graphics import draw

    win = window.Window(width=800, height=600)

    p = Path()
    objs = [p]

    @win.event
    def on_mouse_press(x, y, button, modifiers):
        p.handle_mouse_down(x, y, button, modifiers)

    @win.event
    def on_mouse_release(x, y, button, modifiers):
        p.handle_mouse_up(x, y, button, modifiers)

    @win.event
    def on_mouse_drag(x, y, dx, dy, button, modifiers):
        p.handle_mouse_drag(x, y, dx, dy, button, modifiers)

    while not win.has_exit:
        win.dispatch_events()
        tick = clock.tick()

        [obj.update(tick) for obj in objs]

        win.clear()


        [obj.draw() for obj in objs]

        win.flip()


