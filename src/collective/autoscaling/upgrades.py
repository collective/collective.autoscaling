# -*- coding: utf-8 -*-

from plone import api

PROFILEID = "profile-collective.autoscaling:default"


def reload_registry(context):
    portal_setup = api.portal.get_tool("portal_setup")
    portal_setup.runImportStepFromProfile(PROFILEID, "plone.app.registry")
