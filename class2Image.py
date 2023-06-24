from PIL import Image

class class2:
    def __init__(self,img):
        self.img=img
    def greyscale(self,im):
        self.im = self.im.convert("L")
        self.im.show()