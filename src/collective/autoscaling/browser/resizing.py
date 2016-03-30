# -*- coding: UTF-8 -*-

from Products.Five import BrowserView
from plone import api

from collective.autoscaling.resizing import scale_images


class ResizingView(BrowserView):

    def __call__(self):
        context = self.context
        request = self.request
        result = []
        totalResized = 0
        catalog = api.portal.get_tool(name='portal_catalog')
        folder_path = '/'.join(context.getPhysicalPath())
        brains = catalog(Language="",
                         show_inactive=True,
                         path={'query': folder_path,
                               'depth': -1})
        for brain in brains:
            obj = brain.getObject()
            resized = scale_images(obj, request)
            if resized > 0:
                totalResized += resized
                result.append(' - {} images resized for object {}'.format(resized,
                                                                          obj.absolute_url()))
        if not result:
            result.append("Nothing has to be done.")
        else:
            result.append('Finished to resize {} images.'.format(totalResized))
        result.insert(0, "Scaling every images under folder {}.".format(context.absolute_url()))
        return '\n'.join(result)
