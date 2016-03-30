# -*- coding: utf-8 -*-

from plone import api

from collective.autoscaling.interfaces import ICollectiveAutoscalingSettings


def get_autoscaling_settings(name):
    setting = api.portal.get_registry_record(name,
                                             ICollectiveAutoscalingSettings)
    return setting
