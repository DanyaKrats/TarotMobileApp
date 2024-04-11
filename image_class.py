from kivy.app import App
from kivy.lang import Builder
from kivy.uix.image import Image
from kivy.core.image import Image as CoreImage
from kivy.properties import BooleanProperty
from PIL import ImageOps
from PIL import Image as PImage

import io
from pathlib import Path

class MirrorImage(Image):
    mirror = BooleanProperty(False
)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.mirror_image = None
        self.previous_filename = None
        self.extension = {'.jpg': {'format': 'jpeg', 'ext': 'jpg'},
                          '.png': {'format': 'png', 'ext': 'png'}}

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


kv = """
MirrorImage:
    id: mi
    source:'back_image.png'  # replace with your image
"""
image:MirrorImage = Builder.load_string(kv)
