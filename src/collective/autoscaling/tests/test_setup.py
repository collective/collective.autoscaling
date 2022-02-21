# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from collective.autoscaling.testing import COLLECTIVE_AUTOSCALING_INTEGRATION_TESTING  # noqa
from Products.CMFPlone.utils import get_installer

import unittest


class TestSetup(unittest.TestCase):
    """Test that collective.autoscaling is properly installed."""

    layer = COLLECTIVE_AUTOSCALING_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = get_installer(self.portal, self.layer['request'])

    def test_product_installed(self):
        """Test if collective.autoscaling is installed."""
        self.assertTrue(self.installer.is_product_installed(
            'collective.autoscaling'))

    def test_browserlayer(self):
        """Test that ICollectiveAutoscalingLayer is registered."""
        from collective.autoscaling.interfaces import (
            ICollectiveAutoscalingLayer)
        from plone.browserlayer import utils
        self.assertIn(ICollectiveAutoscalingLayer, utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = COLLECTIVE_AUTOSCALING_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.installer = get_installer(self.portal, self.layer["request"])
        self.installer.uninstall_product('collective.autoscaling')

    def test_product_uninstalled(self):
        """Test if collective.autoscaling is cleanly uninstalled."""
        self.assertFalse(self.installer.is_product_installed(
            'collective.autoscaling'))

    def test_browserlayer_removed(self):
        """Test that ICollectiveAutoscalingLayer is removed."""
        from collective.autoscaling.interfaces import (
            ICollectiveAutoscalingLayer)
        from plone.browserlayer import utils
        self.assertNotIn(ICollectiveAutoscalingLayer, utils.registered_layers())
