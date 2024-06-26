from kivy.app import App
from kivy.lang import Builder
from kivy.uix.image import Image
from kivy.core.image import Image as CoreImage
from kivy.properties import BooleanProperty
from PIL import ImageOps
from PIL import Image as PImage

import io
from pathlib import Path


kv = """
<MirrorImage>:
    keep_ratio: True
    allow_stretch: True

BoxLayout:
    orientation: 'vertical'
    Label:
        size_hint_y: None
        height: 48
        text: 'Mirror Image Test'
    MirrorImage:
        id: mi
        source:'back_image.png'  # replace with your image
    ToggleButton:
        size_hint_y: None
        height: 48
        text: 'Mirror'
        on_release: mi.mirror = False if self.state == 'normal' else True
"""


class MirrorImage(Image):
    mirror = BooleanProperty(False
)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.mirror_image = None
        self.previous_filename = None
        self.extension = {'.jpg': {'format': 'jpeg', 'ext': 'jpg'},
                          '.png': {'format': 'png', 'ext': 'png'}}
        # expand with required formats, see: https://pillow.readthedocs.io/en/stable/handbook/image-file-formats.html

    def on_source(self, *args):
        if not self.source or self.source == self.previous_filename: # if source is '' or same as previous
            return
        self.previous_filename = self.source  # else create texture
        with PImage.open(self.source) as im:
            mirror_image = ImageOps.flip(im)
        output = io.BytesIO()
        ext = Path(self.source).suffix
        mirror_image.save(output, format=self.extension[ext]['format'])
        output.seek(0)
        self.mirror_image = CoreImage(output, ext=self.extension[ext]['ext'])

    def on_mirror(self, *args):
        if self.mirror:
            self.texture = self.mirror_image.texture
        else:
            self.reload()

class MirrorImageApp(App):
    def build(self):
        return Builder.load_string(kv)


MirrorImageApp().run()