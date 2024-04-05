'''
Rotation Example
================
This example rotates a button using PushMatrix and PopMatrix. You should see
a static button with the words 'hello world' rotated at a 45 degree angle.
'''


from kivy.app import App
from kivy.lang import Builder
from kivy.graphics import *

kv = '''
FloatLayout:      
    Image:
        source: 'back_image.png'
        size_hint: 1, 0.3
        pos_hint: {'center_x': .5, 'center_y': .5}
'''


class RotationApp(App):
    def build(self):
        root = Builder.load_string(kv)
        btn = root.children[0]
        with btn.canvas.before:
            PushMatrix()
            rotate = Rotate(angle=180)
        with btn.canvas.after:
            PopMatrix()
        # def update_rotate(w, center):
        #     rotate.origin = center
        btn.bind(center=update_rotate)
        return root

RotationApp().run()