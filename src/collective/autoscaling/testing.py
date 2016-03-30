# -*- coding: utf-8 -*-

from plone.app.robotframework.autologin import AutoLogin
from plone.app.robotframework.content import Content
from plone.app.robotframework.genericsetup import GenericSetup
from plone.app.robotframework.i18n import I18N
from plone.app.robotframework.mailhost import MockMailHost
from plone.app.robotframework.quickinstaller import QuickInstaller
from plone.app.robotframework.remote import RemoteLibraryLayer
from plone.app.robotframework.server import Zope2ServerRemote
from plone.app.robotframework.users import Users
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import PloneSandboxLayer
from plone.app.testing import TEST_USER_ID
from plone.app.testing import applyProfile
from plone.app.testing import login
from plone.app.testing import setRoles
from plone.testing import z2

from collective.autoscaling.tests.library import Image
import collective.autoscaling


class CollectiveAutoscalingLayer(PloneSandboxLayer):

    def setUpZope(self, app, configurationContext):
        self.loadZCML('testing.zcml', package=collective.autoscaling)
        z2.installProduct(app, 'Products.DateRecurringIndex')

    def tearDownZope(self, app):
        z2.uninstallProduct(app, 'Products.DateRecurringIndex')

    def setUpPloneSite(self, portal):
        portal.acl_users.userFolderAddUser('admin',
                                           'secret',
                                           ['Manager'],
                                           [])
        login(portal, 'admin')
        portal.portal_workflow.setDefaultChain('one_state_workflow')
        applyProfile(portal, 'collective.autoscaling:testing')
        setRoles(portal, TEST_USER_ID, ['Manager'])
        portal.invokeFactory(
            "Folder",
            id="test-folder",
            title=u"Test Folder"
        )


IMAGE_LIBRARY_FIXTURE = RemoteLibraryLayer(
    bases=(PLONE_FIXTURE,),
    libraries=(AutoLogin, QuickInstaller, GenericSetup,
               Content, Users, I18N, MockMailHost,
               Zope2ServerRemote, Image),
    name="ImageRemoteLibrary:RobotRemote"
)


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
        IMAGE_LIBRARY_FIXTURE,
        COLLECTIVE_AUTOSCALING_FIXTURE,
        z2.ZSERVER_FIXTURE
    ),
    name='CollectiveAutoscalingLayer:AcceptanceTesting'
)
