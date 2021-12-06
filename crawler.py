from PIL import Image


class Crawler:
    def __init__(self):
        self.max_images = 5

    def crawl(self, search):
        images = []
        # TODO: dummy since i don't have scraping twitter, instagram set up
        for x in range(self.max_images):
            images.append(Image.open(f'./bee{x}.jpg'))

        return images
        