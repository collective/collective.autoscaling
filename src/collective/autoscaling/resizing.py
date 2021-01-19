# -*- coding: utf-8 -*-

import sys
if (sys.version_info > (3, 0)):
    from io import BytesIO as _io
else:
    from cStringIO import StringIO as _io

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
        original_file = _io(imageField.data)
        try:
            image = PIL.Image.open(original_file)
        except Exception as e:
            original_file.close()
            logger.debug("autoscaling {} : {}".format(imageField, e))
            continue
            
        maxWidth, maxHeight = get_max_size()
        width, height = image.size
        if maxHeight >= height and maxWidth >= width:
            # No need to resize
            continue

        image_format = image.format or 'PNG'
        maxsize = (maxWidth, maxHeight)
        quality = get_autoscaling_settings('image_quality')
        image.thumbnail(maxsize)
        scaled_image_file = _io()

        image.save(scaled_image_file, image_format, quality=quality)
        image.close()
        original_file.close()
        scaled_image_file.seek(0)
        imageField.data = scaled_image_file.getvalue()
        scaled_image_file.close()
        resized += 1

    if resized > 0:
        obj.reindexObject()
        logger.debug('{} images resized for object {}'.format(resized,
                                                              obj.absolute_url()))

    return resized
