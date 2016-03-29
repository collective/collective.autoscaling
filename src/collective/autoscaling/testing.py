# -*- coding: utf-8 -*-
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import collective.autoscaling


class CollectiveAutoscalingLayer(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        self.loadZCML(package=collective.autoscaling)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'collective.autoscaling:default')


COLLECTIVE_AUTOSCALING_FIXTURE = CollectiveAutoscalingLayer()


COLLECTIVE_AUTOSCALING_INTEGRATION_TESTING = IntegrationTesting(
    bases=(COLLECTIVE_AUTOSCALING_FIXTURE,),
    name='CollectiveAutoscalingLayer:IntegrationTesting'
)


COLLECTIVE_AUTOSCALING_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(COLLECTIVE_AUTOSCALING_FIXTURE,),
    name='CollectiveAutoscalingLayer:FunctionalTesting'
)


COLLECTIVE_AUTOSCALING_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        COLLECTIVE_AUTOSCALING_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE
    ),
    name='CollectiveAutoscalingLayer:AcceptanceTesting'
)
