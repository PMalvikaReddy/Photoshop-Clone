from PIL import Image

class class1:
    def rotateR(self):
        Image = self.im.transpose(Image.Transpose.ROTATE_180)
        Image.show()