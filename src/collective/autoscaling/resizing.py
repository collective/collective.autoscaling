# -*- coding: utf-8 -*-

from cStringIO import StringIO
import PIL.Image
import logging

from collective.autoscaling.utils import get_autoscaling_settings
from collective.autoscaling.utils import get_image_fields

logger = logging.getLogger('collective.autoscaling')


def get_max_size():
    width = get_autoscaling_settings('image_max_width')
    height = get_autoscaling_settings('image_max_height')
    return width, height


def scale_images(obj, request):
    imageFieldsNames = get_image_fields(obj)
    if not imageFieldsNames:
        return 0

    resized = 0
    for imageFieldName in imageFieldsNames:
        imageField = getattr(obj, imageFieldName)
        original_file = StringIO(imageField.data)
        image = PIL.Image.open(original_file)

        maxWidth, maxHeight = get_max_size()
        width, height = image.size
        if maxHeight >= height and maxWidth >= width:
            # No need to resize
            continue

        image_format = image.format or 'PNG'
        maxsize = (maxWidth, maxHeight)
        image.thumbnail(maxsize)
        cropped_image_file = StringIO()
        image.save(cropped_image_file, image_format, quality=100)
        cropped_image_file.seek(0)
        imageField.data = cropped_image_file.getvalue()
        resized += 1

    if resized > 0:
        obj.reindexObject()
        logger.debug('{} images resized for object {}'.format(resized,
                                                              obj.absolute_url()))

    return resized
