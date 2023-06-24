from PIL import Image

def GreyScaleFilter(img):
    size=width,height=img.size
    for x in range(width):
        for y in range(height):
            r,g,b=img.getpixel((x,y))
            avg=(r+g+b)/3
            img.putpixel((x,y),(int(avg),int(avg),int(avg)))
    img.show()
    imageSave(img)

def RedFilter(img):
    size=width,height=img.size
    for x in range(width):
        for y in range(height):
            r,g,b=img.getpixel((x,y))
            avg=(r+g+b)/3
            if(r<128):
                r=2*avg
            else:
                r=255    
            img.putpixel((x,y),(int(r),int(g),int(b)))
    img.show()
    imageSave(img)

def YellowFilter(img):
    size=width,height=img.size
    for x in range(width):
        for y in range(height):
            r,g,b=img.getpixel((x,y))
            avg=(r+g+b)/3
            if(r<128):
                r=2*avg
            else:
                r=255 
            if(g<128):
                g=2*avg
            else:
                g=255       
            img.putpixel((x,y),(int(r),int(g),int(b)))
    img.show()
    imageSave(img)

def MirrorImage(img1):
    img2=img1.transpose(Image.FLIP_LEFT_RIGHT)
    image_merged=Image.new('RGB',(img1.width+img2.width,img1.height))
    image_merged.paste(img1,(0,0))
    image_merged.paste(img2,(img1.width,0))
    image_merged.show()
    imageSave(image_merged)

def imageSave(imagee):
    ans=input("Do you want to save the image(y/n)?")
    if ans=='y':
        imagee.save("newImage.png","PNG")
    else:
        exit()