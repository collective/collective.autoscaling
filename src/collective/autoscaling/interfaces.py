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
    is_enabled = schema.Bool(
        title=_(u"Enabled"),
        description=_(u"Enable autoscaling."),
        required=False,
        default=True
    )

    image_max_height = schema.Int(
        title=_(u"Maximum Image Height"),
        description=_(u"Higher images will be down sampled."),
        required=False,
        min=1,
        default=800
    )

    image_max_width = schema.Int(
        title=_(u"Maximum Image Width"),
        description=_(u"Wider images will be down sampled."),
        required=False,
        min=1,
        default=1200
    )

    show_message = schema.Bool(
        title=_(u"Show message to user"),
        description=_(u"Show message when an image has been down sampled."),
        required=False,
        default=False
    )
