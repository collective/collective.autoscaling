from plone.base.interfaces import INonInstallable
from zope.interface import implementer


@implementer(INonInstallable)
class HiddenProfiles:
    def getNonInstallableProfiles(self):
        """Hide unwanted profiles from site-creation and quickinstaller."""
        return [
            "collective.autoscaling:testing",
            "collective.autoscaling:uninstall",
        ]
