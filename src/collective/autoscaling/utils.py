from collective.autoscaling.interfaces import ICollectiveAutoscalingSettings
from plone import api
from plone.behavior.interfaces import IBehaviorAssignable
from plone.namedfile.interfaces import IImage
from zope.schema import getFieldsInOrder


def get_all_fields(obj):
    type_info = obj.getTypeInfo()
    if type_info is None:
        return
    schema = type_info.lookupSchema()
    yield from getFieldsInOrder(schema)
    behavior_assignable = IBehaviorAssignable(obj)
    if behavior_assignable:
        for behavior in behavior_assignable.enumerateBehaviors():
            yield from getFieldsInOrder(behavior.interface)


def get_image_fields(obj):
    for fieldname, field in get_all_fields(obj):
        value = getattr(obj, fieldname, None)
        if value and IImage.providedBy(value):
            yield fieldname


def get_autoscaling_settings(name):
    setting = api.portal.get_registry_record(name, ICollectiveAutoscalingSettings)
    return setting
