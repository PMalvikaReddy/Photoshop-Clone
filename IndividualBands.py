from PIL import ImageFilter,Image
# im = Image.open(r"hands.jpg")
# out = im.filter(ImageFilter.DETAIL)
# source = im.split()

# R, G, B = 0, 1, 2

# # select regions where red is less than 100
# mask = source[R].point(lambda i: i < 100 and 255)

# # process the green band
# out = source[G].point(lambda i: i * 0.7)

# # paste the processed band back, but only where red was < 100
# source[G].paste(out, None, mask)

# # build a new multiband image
# # im = Image.merge(im.mode, source)
# # imout = im.point(lambda i: expression and 255)
# # im.show()
print(Image.getcolors(maxcolors=256))