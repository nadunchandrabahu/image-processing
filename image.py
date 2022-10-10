from PIL import Image, ImageFilter

# converts to black and white, blurs and saves as png
'''
with Image.open("pikachu.jpg") as img:
    img = img.convert("L")
    filtered_img = img.filter(ImageFilter.BLUR)
    filtered_img.save("b&w pikachu.png", "png")
    filtered_img.show()
'''

# to reduce size of image and make thumbnail, saved as png

'''
with Image.open("astro.jpg", mode="r") as img:
    img.thumbnail((640, 640))
    img.save("astro-converted.png", "png")
'''
