# -*- coding: utf-8 -*-

from cStringIO import StringIO
from plone import api
from plone.app.imagecropping.interfaces import IImageCroppingUtils
from zope.i18n import translate
import PIL.Image
import logging

from collective.autoscaling import _
from collective.autoscaling.interfaces import ICollectiveAutoscalingLayer
from collective.autoscaling.interfaces import ICollectiveAutoscalingSettings

logger = logging.getLogger('collective.autoscaling')


def get_autoscaling_settings(name):
    setting = api.portal.get_registry_record(name,
                                             ICollectiveAutoscalingSettings)
    return setting


def get_max_size():
    width = get_autoscaling_settings('image_max_width')
    height = get_autoscaling_settings('image_max_height')
    return width, height


def handle_max_image_size(obj, event):
    request = event.object.REQUEST
    if not ICollectiveAutoscalingLayer.providedBy(request):
        return

    enabled = get_autoscaling_settings('is_enabled')
    if not enabled:
        return

    croputils = IImageCroppingUtils(obj)
    imageFieldsNames = croputils.image_field_names()
    if not imageFieldsNames:
        return

    resized = 0
    for imageFieldName in imageFieldsNames:
        imageField = croputils.get_image_field(imageFieldName)
        original_file = StringIO(imageField.data)
        image = PIL.Image.open(original_file)

        maxWidth, maxHeight = get_max_size()
        width, height = image.size
        if maxHeight > height and maxWidth > width:
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

    if resized == 0:
        return

    obj.reindexObject()
    logger.debug('{} images resized for object {}'.format(resized,
                                                          obj.absolute_url()))

    show_message = get_autoscaling_settings('show_message')
    if show_message:
        if resized > 1:
            msgid = _(u'images_have_been_resized',
                      default=u'${nb} images have been resized on this content.',
                      mapping={u'nb': resized})
            message = translate(msgid, context=request)
            api.portal.show_message(message=message,
                                    request=request,
                                    type='info')
        else:
            message = _('One image has been resized on this content.')
            api.portal.show_message(message=message,
                                    request=request,
                                    type='info')
