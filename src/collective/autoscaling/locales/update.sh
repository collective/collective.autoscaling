#!/bin/bash
# Run it with ``make i18n``, which installs i18ndude in .venv and puts it in $PATH.
#
# For every language you want to translate into you need a
# locales/[language]/LC_MESSAGES/collective.autoscaling.po
# (e.g. locales/de/LC_MESSAGES/collective.autoscaling.po)

domain=collective.autoscaling

i18ndude rebuild-pot --pot $domain.pot --create $domain ../
i18ndude sync --pot $domain.pot */LC_MESSAGES/$domain.po
