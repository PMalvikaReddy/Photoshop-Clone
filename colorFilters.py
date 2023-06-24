from PIL import Image

with Image.open("sky.jpg") as im:
    size=width,height=im.size
    for x in range(width):
        for y in range(height):
            r,g,b=im.getpixel((x,y))
            #im.putpixel((x,y),(int(r/4),int(g/4),int(b/4)))#converts the recieved rgb values..and prints the image
            #im.putpixel((x,y),(255-r,255-g,255-b)) works
            avg=(r+g+b)/3
            '''im.putpixel((x,y),(int(avg),int(avg),int(avg)))'''#greyscale
            '''if(r<128):
                r=2*avg
            else:
                r=255    
            im.putpixel((x,y),(int(r),int(g),int(b))) #redscale image'''
            if(r<128):
                r=2*avg
            else:
                r=255 
            if(g<128):
                g=2*avg
            else:
                g=255       
            im.putpixel((x,y),(int(r),int(g),int(b)))#yellow scale

im.show()