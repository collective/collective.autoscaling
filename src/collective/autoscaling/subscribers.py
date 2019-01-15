# -*- coding: utf-8 -*-

from plone import api
from zope.i18n import translate

from collective.autoscaling import _
from collective.autoscaling.interfaces import ICollectiveAutoscalingLayer
from collective.autoscaling.resizing import scale_images
from collective.autoscaling.utils import get_autoscaling_settings


def handle_max_image_size(obj, event):
    request = getattr(event.object, 'REQUEST', None)
    if not ICollectiveAutoscalingLayer.providedBy(request):
        return

    enabled = get_autoscaling_settings('is_enabled')
    if not enabled:
        return

    resized = scale_images(obj, request)
    if resized == 0:
        return

    show_message = get_autoscaling_settings('show_message')
    if show_message:
        if resized > 1:
            msgid = _(u'images_have_been_resized',
                      default=u'${nb} images were down sampled on this content.',
                      mapping={u'nb': resized})
            message = translate(msgid, context=request)
            api.portal.show_message(message=message,
                                    request=request,
                                    type='info')
        elif resized == 1:
            message = _('One image was down sampled on this content.')
            api.portal.show_message(message=message,
                                    request=request,
                                    type='info')
