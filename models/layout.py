from PIL import Image, ImageFont, ImageDraw


class Layout:
    def __init__(self, indicator, page, cord_qrcode_main, cord_description, cord_qrcode_secondary):
        self.indicator = indicator
        self.page = page
        self.cordQrcodeMain = cord_qrcode_main
        self.cordDescription = cord_description
        self.cordQrcodeSecondary = cord_qrcode_secondary
        if self.indicator == 1:
            self.image = Image.open('src/layout/layout.png')
        else:
            self.image = Image.open(f'src/png/{self.page}.png')

    def insert_qrcode_main(self):
        image = self.image
        qrcode_main = Image.open('src/qrcode/qrcodeMain.png')
        image.paste(qrcode_main, self.cordQrcodeMain)

    def insert_description(self, text):
        image = self.image
        font = ImageFont.truetype('src/font/openSans.ttf', 30)
        color = (0, 0, 0)
        draw = ImageDraw.Draw(image)
        draw.multiline_text(self.cordDescription, text, font=font, fill=color, align='left')

    def insert_qrcode_secondary(self):
        image = self.image
        qrcode_secondary = Image.open('src/qrcode/qrcodeSecondary.png')
        image.paste(qrcode_secondary, self.cordQrcodeSecondary)

    def save(self, page):
        image = self.image
        image.save(f'src/png/{page}.png')
