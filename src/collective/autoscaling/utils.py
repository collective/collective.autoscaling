# -*- coding: utf-8 -*-

from plone import api
from plone.behavior.interfaces import IBehaviorAssignable
from plone.namedfile.interfaces import IImage
from zope.schema import getFieldsInOrder

from collective.autoscaling.interfaces import ICollectiveAutoscalingSettings


def get_all_fields(obj):
    type_info = obj.getTypeInfo()
    if type_info is None:
        return
    schema = type_info.lookupSchema()
    for field in getFieldsInOrder(schema):
        yield field
    behavior_assignable = IBehaviorAssignable(obj)
    if behavior_assignable:
        for behavior in behavior_assignable.enumerateBehaviors():
            for field in getFieldsInOrder(behavior.interface):
                yield field


def get_image_fields(obj):
    for fieldname, field in get_all_fields(obj):
        value = getattr(obj, fieldname, None)
        if value and IImage.providedBy(value):
            yield fieldname


def get_autoscaling_settings(name):
    setting = api.portal.get_registry_record(name,
                                             ICollectiveAutoscalingSettings)
    return setting
