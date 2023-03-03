import qrcode


class QRCode:
    def __init__(self, link_main, link_secondary):
        self.linkMain = link_main
        self.linkSecondary = link_secondary
        # Qrcode proprieties
        self.qrcodeMain = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=11,
            border=2)
        self.qrcodeSecondary = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=4,
            border=2)

    def create_qrcode_main(self):
        qrcode_main = self.qrcodeMain
        qrcode_main.add_data(self.linkMain)
        qrcode_main.make(fit=True)

        image_qrcode_main = qrcode_main.make_image()
        image_qrcode_main.save('src/qrcode/qrcodeMain.png')

    def create_qrcode_secondary(self):
        qrcode_secondary = self.qrcodeSecondary
        qrcode_secondary.add_data(self.linkSecondary)
        qrcode_secondary.make(fit=True)

        image_qrcode_secondary = qrcode_secondary.make_image()
        image_qrcode_secondary.save('src/qrcode/qrcodeSecondary.png')
