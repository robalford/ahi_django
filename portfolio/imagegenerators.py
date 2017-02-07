from imagekit import ImageSpec, register
from imagekit.processors import ResizeToFill, SmartResize


class Landscape(ImageSpec):
    processors = [SmartResize(1200, 700)]
    format = 'JPEG'
    options = {'quality': 80}


class Portrait(ImageSpec):
    processors = [SmartResize(500, 700)]
    format = 'JPEG'
    options = {'quality': 80}


class Thumbnail(ImageSpec):
    processors = [ResizeToFill(100, 50)]
    format = 'JPEG'
    options = {'quality': 60}

register.generator('portfolio:landscape', Landscape)
register.generator('portfolio:portrait', Portrait)
register.generator('portfolio:thumbnail', Thumbnail)
