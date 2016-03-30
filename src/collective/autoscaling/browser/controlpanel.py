# -*- coding: utf-8 -*-

from plone.app.registry.browser.controlpanel import ControlPanelFormWrapper
from plone.app.registry.browser.controlpanel import RegistryEditForm
from plone.z3cform import layout
from z3c.form import form

from collective.autoscaling import _
from collective.autoscaling.interfaces import ICollectiveAutoscalingSettings


class SettingsEditForm(RegistryEditForm):

    label = _("Autoscaling settings")
    description = _("Lets you change the settings of images autoscaling feature.")
    form.extends(RegistryEditForm)
    schema = ICollectiveAutoscalingSettings


AutoscalingControlPanel = layout.wrap_form(SettingsEditForm,
                                           ControlPanelFormWrapper)
