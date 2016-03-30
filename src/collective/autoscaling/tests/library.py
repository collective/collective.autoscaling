# -*- coding: utf-8 -*-

from cStringIO import StringIO
from plone import api
from plone.app.robotframework.remote import RemoteLibrary
from plone.namedfile.file import NamedBlobImage
import PIL.Image


class Image(RemoteLibrary):

    def image_dimensions_of(self, image_url):
        """
        Returns image dimensions
        """
        portal = api.portal.get()
        image = portal.restrictedTraverse(image_url)
        if isinstance(image, NamedBlobImage):
            data = image.data
        else:
            data = image.image.data
        imageFile = StringIO(data)
        image = PIL.Image.open(imageFile)
        return image.size

    def delete_image(self, image_url):
        """
        Deletes image
        """
        portal = api.portal.get()
        image = portal.restrictedTraverse(image_url)
        api.content.delete(image)
