from PIL import Image
from PIL import ImageFilter
from PIL import ImageEnhance
def Show(img):
    img.show()
def Crop_Image(img):
    x=int(input("enter the x-coordinate dimension: "))
    y=int(input("enter the y-coordinate dimension: "))
    crop_img = img.resize([x,y])
    crop_img.show()
    imageSave(crop_img)
def Blur_Image(img):
    blurImg = img.filter(filter=ImageFilter.BoxBlur(4))
    blurImg.show()
    imageSave(blurImg)
def Image_Rotate(img):
    ImgRotate = img.transpose(Image.Transpose.ROTATE_90)
    ImgRotate.show()
    imageSave(ImgRotate)
def Adjust_Brightness(img):
    enh = ImageEnhance.Contrast(img)
    enh.enhance(1.5).show()
    imageSave(enh)
def Adjust_Contrast(img):
    ImgContrast=ImageEnhance.Contrast(img)
    ImgContrast.enhance(3.2).show()
    imageSave(ImgContrast)
def imageSave(imagee):
    ans=input("Do you want to save the image(y/n)?")
    if ans=='y':
        imagee.save("newImage.png","PNG")
    else:
        exit()
    
