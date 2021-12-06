import torch
import torchvision.models as models
from PIL import Image
from torchvision import transforms


class Model:

    def __init__(self):
        self.model = models.resnet101(pretrained=True)
        print('resnet101 initialized')

        with open("imagenet_classes.txt", "r") as f:
            self.categories = [s.strip() for s in f.readlines()]

    def predict(self, image):
        preprocess = transforms.Compose([
            transforms.Resize(256),
            transforms.CenterCrop(224),
            transforms.ToTensor(),
            transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[
                                 0.229, 0.224, 0.225]),
        ])
        input_tensor = preprocess(image)
        #create a mini-batch as expected by the model
        input_batch = input_tensor.unsqueeze(0)

        with torch.no_grad():
            output = self.model(input_batch)

        #get the highest match
        index = torch.argmax(output[0])
        index = index.item()

        return self.categories[index]
