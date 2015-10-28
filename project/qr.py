__author__ = 'Dennis'

import qrcode
import qrcode.image.svg

class qr(object):
    def create_qr(self, reisid):
        factory = qrcode.image.svg.SvgPathImage
        img = qrcode.make(reisid, image_factory=factory)
        filename = str(reisid) + ".svg"
        img.save("qrcodes/" + filename)



