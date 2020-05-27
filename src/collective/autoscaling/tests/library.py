# -*- coding: utf-8 -*-

import sys
if (sys.version_info > (3, 0)):
    from io import BytesIO as _io
else:
    from cStringIO import StringIO as _io
    
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
        imageFile = _io(data)
        image = PIL.Image.open(imageFile)
        image_size = image.size
        image.close()
        imageFile.close()
        return image_size

    def delete_image(self, image_url):
        """
        Deletes image
        """
        portal = api.portal.get()
        image = portal.restrictedTraverse(image_url)
        api.content.delete(image)
