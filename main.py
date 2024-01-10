from PIL import Image, ImageDraw
import os
for file in os.listdir('.'):
    if file.endswith('.jpg'):
        im = Image.open(file)

        im = im.convert('RGBA')

        for x in range(im.size[0]):
            for y in range(im.size[1]):
                data = im.getpixel((x, y))
                if data[0] > 230 and data[1] > 230 and data[2] > 230:
                    im.putpixel((x, y), (0, 0, 0, 0))

        rad = 20
        im2 = im.copy()
        draw = ImageDraw.Draw(im2)
        for x in range(im.size[0]):
            for y in range(im.size[1]):
                data = im.getpixel((x, y))
                r = data[0]
                g = data[1]
                b = data[2]
                if r+g+b >= 1:
                    draw.ellipse((x-rad, y-rad, x+rad, y+rad), fill=(255, 255, 255))
                

        im3 = im2.copy()

        for x in range(im.size[0]):
            for y in range(im.size[1]):
                data = im.getpixel((x, y))
                if data[3] > 1:
                    im3.putpixel((x, y), data)

        im3.save("n"+file[:-3]+"png", 'PNG')




    print("done")
print("done")