from datetime import date

from PIL import Image, ImageDraw, ImageFont


def to_img(d):
    ms = [None, 'January', 'February', 'March', 'April', 'May', 'June',
          'July', 'August', 'Spetember', 'October', 'November', 'December']

    if not d:
        d = date.today()

    img = Image.new('RGB', (700, 1000), (255, 255, 255))
    month = Image.new('RGB', (700, 200), (255, 255, 255))
    dayfont = ImageFont.truetype('arial.ttf', 650)
    yearfont = ImageFont.truetype('arial.ttf', 200)
    monthfont = ImageFont.truetype('arial.ttf', 200)

    drawday = ImageDraw.Draw(img)
    drawyear = ImageDraw.Draw(img)
    drawmonth = ImageDraw.Draw(month)

    drawday.text((200, 50), str(d.day), font=dayfont, fill=(0, 0, 0))
    drawyear.text((200, 700), str(d.year), font=yearfont, fill=(0, 0, 0))
    drawmonth.text((0, 0), ms[d.month], font=monthfont, fill=(0, 0, 0))

    w = month.rotate(90.0)
    img.paste(w, (0, 0))

    img.save('date.png')

if __name__ == '__main__':
    to_img(None)
