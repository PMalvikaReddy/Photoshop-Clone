from PIL import Image
# # img=Image.open( "lion.jpg")
# with Image.open("lion.jpg") as im:
def rainbowFunction(im):
    size=width,height=im.size
    for x in range(width):
        for y in range(int(height/7)):
            r,g,b=im.getpixel((x,y))
            avg=(r+g+b)/3
            if(avg<128):
                r=2*avg
                g=0
                b=0
            else:
                r=255
                g=2*avg-255
                b=2*avg-255
            im.putpixel((x,y),(int(r),int(g),int(b)))
    for x in range(width):
        for y in range(int(height/7),int(2*height/7)):
            r,g,b=im.getpixel((x,y))
            avg=(r+g+b)/3
            if(avg<128):
                r=2*avg
                g=0.8*avg
                b=0
            else:
                r=255
                g=1.2*avg-51
                b=2*avg-255
            im.putpixel((x,y),(int(r),int(g),int(b)))
    for x in range(width):
        for y in range(int(2*height/7),int(3*height/7)):
            r,g,b=im.getpixel((x,y))
            avg=(r+g+b)/3
            if(avg<128):
                r=2*avg
                g=2*avg
                b=0
            else:
                r=255
                g=255
                b=2*avg-255
            im.putpixel((x,y),(int(r),int(g),int(b)))
    for x in range(width):
        for y in range(int(2*height/7),int(3*height/7)):
            r,g,b=im.getpixel((x,y))
            avg=(r+g+b)/3
            if(avg<128):
                r=2*avg
                g=2*avg
                b=0
            else:
                r=255
                g=255
                b=2*avg-255
            im.putpixel((x,y),(int(r),int(g),int(b)))
    for x in range(width):
        for y in range(int(3*height/7),int(4*height/7)):
            r,g,b=im.getpixel((x,y))
            avg=(r+g+b)/3
            if(avg<128):
                r=0
                g=2*avg
                b=0
            else:
                r=2*avg-255
                g=255
                b=2*avg-255
            im.putpixel((x,y),(int(r),int(g),int(b)))
    for x in range(width):
        for y in range(int(4*height/7),int(5*height/7)):
            r,g,b=im.getpixel((x,y))
            avg=(r+g+b)/3
            if(avg<128):
                r=0
                g=0
                b=2*avg
            else:
                r=2*avg-255
                g=2*avg-255
                b=255
            im.putpixel((x,y),(int(r),int(g),int(b)))
    for x in range(width):
        for y in range(int(5*height/7),int(6*height/7)):
            r,g,b=im.getpixel((x,y))
            avg=(r+g+b)/3
            if(avg<128):
                r=0.8*avg
                g=0
                b=2*avg
            else:
                r=1.2*avg-51
                g=2*avg-255
                b=255
            im.putpixel((x,y),(int(r),int(g),int(b)))
    for x in range(width):
        for y in range(int(6*height/7),int(7*height/7)):
            r,g,b=im.getpixel((x,y))
            avg=(r+g+b)/3
            if(avg<128):
                r=1.6*avg
                g=0
                b=1.6*avg
            else:
                r=0.4*avg+153
                g=2*avg-255
                b=0.4*avg+153
            im.putpixel((x,y),(int(r),int(g),int(b)))
            
    im.show()
    imageSave(im)

def imageSave(imagee):
    ans=input("Do you want to save the image(y/n)?")
    if ans=='y':
        imagee.save("newImage.png","PNG")
    else:
        exit()
