.. This README is meant for consumption by humans and pypi. Pypi can render rst files so please do not use Sphinx features.
   If you want to learn more about writing documentation, please check out: http://docs.plone.org/about/documentation_styleguide_addons.html
   This text does not appear on pypi or github. It is a comment.

==============================================================================
collective.autoscaling
==============================================================================

This package allows automatic scaling of too large images in Plone sites.
Images can be either Image content type or any Image field on content types.

This is totally transparent to the user (except if you choose to show message).


Settings
--------

- Enabled (yes / no)
- Maximum height at which images will be automatically resized (in pixels)
- Maximum width at which images will be automatically resized (in pixels)
- Show information message to user when images have been resized (yes / no)


Examples
--------

1. You configure collective.autoscaling to have images with maximum size of height 800px / width 1200px.
2. You upload a big image : height 2000px / width 4000px.
3. It will be resized to height 600px / width 1200px (aspect ratio is of course preserved).


Limitations
-----------

This add-on works only with Dexterity content types.

It has been developed on Plone 4.3.7.


Translations
------------

This product has been translated into

- English
- French


Installation
------------

Install collective.autoscaling by adding it to your buildout::

    [buildout]

    ...

    eggs =
        collective.autoscaling


and then running ``bin/buildout``


Contribute
----------

- Issue Tracker: https://github.com/collective/collective.autoscaling/issues
- Source Code: https://github.com/collective/collective.autoscaling


License
-------

The project is licensed under the GPLv2.
