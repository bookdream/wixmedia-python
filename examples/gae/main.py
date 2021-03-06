# -*- encoding: UTF-8 -*-

from django.template.loader import render_to_string
import webapp2
from wix import media


class RenderImagesHandler(webapp2.RequestHandler):
    def get(self):

        # Image id's can be fetched from datastore ...
        image_ids = [
            'wixmedia-samples/images/6f113c0b2b274ee68a125263ce1b0b44/cat.jpg',
            'wixmedia-samples/images/b0f7a02a37a341d9bbb68c3dfbdcf887/dog.jpg',
            'wixmedia-samples/images/cdf1ba9ec9554baca147db1cb6e011ec/parrot.jpg'
        ]

        context = {
            'thumbnail_urls': [RenderImagesHandler.create_image_thumbnail_url(image_id) for image_id in image_ids]
        }

        self.response.headers['Content-Type'] = 'text/html'
        self.response.out.write(render_to_string('example.html', context))

    @staticmethod
    def create_image_thumbnail_url(image_id):
        client = media.Client()
        image  = client.get_image_from_id(image_id)

        return image.fill(width=120, height=120).unsharp().quality().get_url()


app = webapp2.WSGIApplication([
    ('/', RenderImagesHandler),
], debug=True)