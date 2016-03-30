# -*- coding: utf-8 -*-

from Products.CMFDefault.formlib.schema import SchemaAdapterBase
from Products.CMFPlone.interfaces import IPloneSiteRoot
from plone.app.controlpanel.form import ControlPanelForm
from plone.registry.interfaces import IRegistry
from zope.component import adapts
from zope.component import getUtility
from zope.formlib import form
from zope.interface import implements

from collective.autoscaling import _
from collective.autoscaling.interfaces import ICollectiveAutoscalingSettings


class AutoscalingControlPanelAdapter(SchemaAdapterBase):

    adapts(IPloneSiteRoot)
    implements(ICollectiveAutoscalingSettings)

    def __init__(self, context):
        super(AutoscalingControlPanelAdapter, self).__init__(context)
        registry = getUtility(IRegistry)
        self.settings = registry.forInterface(ICollectiveAutoscalingSettings, False)

    def getIsEnabled(self):
        return self.settings.is_enabled

    def setIsEnabled(self, value):
        self.settings.is_enabled = value

    is_enabled = property(getIsEnabled, setIsEnabled)

    def getImageMaxHeight(self):
        return self.settings.image_max_height

    def setImageMaxHeight(self, value):
        self.settings.image_max_height = value

    image_max_height = property(getImageMaxHeight, setImageMaxHeight)

    def getImageMaxWidth(self):
        return self.settings.image_max_width

    def setImageMaxWidth(self, value):
        self.settings.image_max_width = value

    image_max_width = property(getImageMaxWidth, setImageMaxWidth)

    def getShowMessage(self):
        return self.settings.show_message

    def setShowMessage(self, value):
        self.settings.show_message = value

    show_message = property(getShowMessage, setShowMessage)


class AutoscalingControlPanel(ControlPanelForm):

    label = _("Autoscaling settings")
    description = _("Lets you change the settings of images autoscaling feature")
    form_fields = form.FormFields(ICollectiveAutoscalingSettings)
