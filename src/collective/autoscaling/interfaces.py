# -*- coding: utf-8 -*-

from zope import schema
from zope.interface import Interface
from zope.publisher.interfaces.browser import IDefaultBrowserLayer

from collective.autoscaling import _


class ICollectiveAutoscalingLayer(IDefaultBrowserLayer):
    """Marker interface that defines a browser layer."""


class ICollectiveAutoscalingSettings(Interface):
    """
    Settings for collective.autoscaling
    """
    image_max_height = schema.Int(
        title=_(u"Images maximum height"),
        description=_(u"Maximum height at which images will be automatically resized."),
        required=False,
        default=800
    )

    image_max_width = schema.Int(
        title=_(u"Images maximum width"),
        description=_(u"Maximum width at which images will be automatically resized."),
        required=False,
        default=1200
    )
