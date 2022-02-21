======================
collective.autoscaling
======================

.. image:: https://github.com/collective/collective.autoscaling/actions/workflows/plone-package-test.yml/badge.svg
    :target: https://github.com/collective/collective.autoscaling/actions/workflows/plone-package-test.yml
    :alt: CI Status


This package allows automatic scaling of too large images in Plone sites.
Images can be either Image content type or any Image field on content types.

This is totally transparent to the user (except if you choose to show message).

There is also a view (``@@resize-images``) that you can call to scale existing images (under the context of your choice), for example :

 - http://localhost:8080/plone/@@resize-images
 - http://localhost:8080/plone/folder/subfolder/@@resize-images


Settings
--------

- Enable automatic scaling (yes / no)
- Maximum height at which images will be automatically resized (in pixels)
- Maximum width at which images will be automatically resized (in pixels)
- JPEG quality
- Show information message to user when images have been resized (yes / no)


Use case
--------

1. You configure collective.autoscaling to have images with maximum size of height 800px / width 1200px.
2. One of your user uploads a really big image : height 2000px / width 4000px.
3. This image will be resized to height 600px / width 1200px (aspect ratio is of course preserved).


Limitations
-----------

This add-on works only with Dexterity content types.

It has been developed on Plone 4.3, but works with Plone 5 and Plone 6 too.
Current branch is tested on Python 3.x / Plone 5.2.x & Plone 6.0.x.


Translations
------------

This product has been translated into

- English
- French
- Norwegian
- Portuguese


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
