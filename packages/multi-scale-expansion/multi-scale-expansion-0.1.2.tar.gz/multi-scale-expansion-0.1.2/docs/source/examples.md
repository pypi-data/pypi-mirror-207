## Quick-Start Example
```python 
import torch
from torchvision import models
import numpy as np
import matplotlib
from PIL import Image
import importlib

ms_model = importlib.import_module("multi-scale-expansion.model")
ms_datasets = importlib.import_module("multi-scale-expansion.dataset")
ms = importlib.import_module("multi-scale-expansion.classification")

device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
mock_model = models.resnet18(weights='DEFAULT')
mock_model = ms_model.get_plant_model(mock_model, list(range(6)))

mock_lr = 0.001
mock_momentum = 0.9
mock_step_size = 7
mock_gamma = 0.1
mock_criterion, mock_optimizer, mock_lr_scheduler = get_train_loss_needs(
    mock_model, mock_lr, mock_momentum, mock_step_size, mock_gamma
)

mock_datasets = {
    "train": FakeData(num_classes=6, transform=mock_transforms["train"]),
    "test": FakeData(num_classes=6, transform=mock_transforms["test"]),
}

mock_dataset_sizes = {x: len(mock_datasets[x]) for x in ['train', 'test']}
mock_dataloaders = ms_datasets.get_dataloaders(mock_datasets)

model, train_losses, train_accuracies, val_losses, val_accuracies = ms.train_model(
    device,
    mock_dataset_sizes,
    mock_dataloaders,
    mock_model,
    mock_criterion,
    mock_optimizer,
    mock_lr_scheduler,
    num_epochs=1,
    testing=True,
)
```

And now your model is ready-to-use! 
