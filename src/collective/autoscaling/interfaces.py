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
        title=_("Enabled"),
        description=_("Enable autoscaling."),
        required=False,
        default=True,
    )

    image_max_height = schema.Int(
        title=_("Maximum Image Height"),
        description=_("Higher images will be down sampled."),
        required=False,
        min=1,
        default=800,
    )

    image_max_width = schema.Int(
        title=_("Maximum Image Width"),
        description=_("Wider images will be down sampled."),
        required=False,
        min=1,
        default=1200,
    )

    image_quality = schema.Int(
        title=_("JPEG Quality"),
        description=_(
            "Set Quality for JPEG format; lower value saves space at expense of quality."
        ),
        required=False,
        min=75,
        default=95,
    )

    show_message = schema.Bool(
        title=_("Show message to user"),
        description=_("Show message when an image has been down sampled."),
        required=False,
        default=False,
    )
