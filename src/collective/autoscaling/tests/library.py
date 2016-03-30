# -*- coding: utf-8 -*-

from cStringIO import StringIO
from plone import api
from plone.app.robotframework.remote import RemoteLibrary
import PIL.Image


class Image(RemoteLibrary):

    def image_dimensions_of(self, image_url):
        """
        Returns image dimensions
        """
        portal = api.portal.get()
        image = portal.restrictedTraverse(image_url)
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
