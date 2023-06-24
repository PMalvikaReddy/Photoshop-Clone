from PIL import Image

def function1(im):
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
    im.show()