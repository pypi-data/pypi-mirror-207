import torch
from torchvision import transforms, models
from classification import setup_classification_model


data_transforms = {
    'train': transforms.Compose(
        [
            transforms.RandomResizedCrop(224),
            transforms.RandomHorizontalFlip(),
            transforms.ToTensor(),
            transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225]),
        ]
    ),
    'test': transforms.Compose(
        [
            transforms.Resize(256),
            transforms.CenterCrop(224),
            transforms.ToTensor(),
            transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225]),
        ]
    ),
}

if __name__ == "__main__":
    data_dir = '/Users/angelmancera/Columbia/Classes/Spring_2023/Open_Src_Dev/Taiwan_Tomato_Leaves'

    # # Configure to train with GPU
    device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")

    # # Load pre-trained model and set add classification layer
    model = models.resnet18(pretrained=True)

    setup_classification_model(device, data_dir, model, data_transforms, epochs=1)
