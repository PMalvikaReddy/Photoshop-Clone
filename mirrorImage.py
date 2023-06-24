from PIL import Image

with Image.open("hands.jpg") as im1:
    im2=im1.transpose(Image.FLIP_LEFT_RIGHT)
    image_merged=Image.new('RGB',(im1.width+im2.width,im1.height))
    image_merged.paste(im1,(0,0))
    image_merged.paste(im2,(im1.width,0))
    image_merged.show()