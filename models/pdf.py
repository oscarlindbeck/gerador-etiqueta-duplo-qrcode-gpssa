from PIL import Image


class PDF:
    def __init__(self, path, image_list, name):
        self.path = path
        self.image_list = image_list
        self.name = name

    def create(self):
        images = []

        for i in self.image_list:
            i = Image.open(f'{self.path}\\src\\png\\{i}')
            images.append(i)

        base = images[0]

        images.pop(0)

        base.save(f'{self.path}\\output\\{self.name}.pdf', save_all=True, append_images=images)
