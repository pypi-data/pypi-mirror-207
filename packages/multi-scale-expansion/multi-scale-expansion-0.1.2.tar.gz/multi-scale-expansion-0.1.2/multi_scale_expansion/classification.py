import torch
import time
import copy
from . import dataset as ms_ds
from . import model as ms_model


def train_model(
    device, dataset_sizes, dataloaders, model, criterion, optimizer, scheduler, num_epochs=25, testing=False
):
    """
    Train and fine-tune previously auto-generated model.

    :param device: To work allow PyTorch to work with GPU.
    :type kind: torch.device
    :param dataset_sizes: Stores the dataset sizes for the training and test data.
    :type kind: dict()
    :param dataloaders: 2 dataloaders containing the training and testing data.
    :type kind: torch.utils.data.DataLoader
    :param model: The model to train.
    :type kind: torch.nn.Module
    :param criterion: Loss function.
    :type kind: function, torch.nn.CrossEntropyLoss().
    :param optimizer: Optimization algorithm choice.
    :type kind: torch.optim.Optimizer()
    :param scheduler: Modifies learning rate gradually with training.
    :type kind: torch.optim.lr_scheduler.*
    :param num_epochs: Epochs to train on.
    :type kind: int
    :param testing: Whether we are testing the function or running it normally.
    :type kind: boolean

    :return model: Trained model.
    :rtype: torch.nn.Module
    :return train/val_losses: Per epoch train and val losses
    :rtype: list()
    :return train/val_accuracies: Per epoch train and val accuracies
    :rtype: list()
    """
    since = time.time()

    best_model_wts = copy.deepcopy(model.state_dict())
    best_acc = 0.0

    train_losses = []
    val_losses = []
    train_accuracies = []
    val_accuracies = []

    for epoch in range(num_epochs):
        print(f'Epoch {epoch}/{num_epochs - 1}')
        print('-' * 10)

        for phase in ['train', 'test']:
            if phase == 'train':
                model.train()
            else:
                model.eval()

            running_loss = 0.0
            running_corrects = 0

            # Iterate over data.
            for inputs, labels in dataloaders[phase]:
                inputs = inputs.to(device)
                labels = labels.to(device)

                # zero the parameter gradients
                optimizer.zero_grad()

                # forward
                # track history if only in train
                with torch.set_grad_enabled(phase == 'train'):
                    outputs = model(inputs)
                    _, preds = torch.max(outputs, 1)
                    loss = criterion(outputs, labels)

                    # backward + optimize only if in training phase
                    if phase == 'train':
                        loss.backward()
                        optimizer.step()

                # statistics
                running_loss += loss.item() * inputs.size(0)
                running_corrects += torch.sum(preds == labels.data)
            if phase == 'train':
                scheduler.step()

            epoch_loss = running_loss / dataset_sizes[phase]
            epoch_acc = running_corrects.double() / dataset_sizes[phase]
            if phase == "train":
                train_losses.append(epoch_loss)
                train_accuracies.append(epoch_acc)
            else:
                val_losses.append(epoch_loss)
                val_accuracies.append(epoch_acc)

            print(f'{phase} Loss: {epoch_loss:.4f} Acc: {epoch_acc:.4f}')

            if phase == 'test' and epoch_acc > best_acc:
                best_acc = epoch_acc
                best_model_wts = copy.deepcopy(model.state_dict())

            if testing:
                break

        print()

    time_elapsed = time.time() - since
    print(f'Training complete in {time_elapsed // 60:.0f}m {time_elapsed % 60:.0f}s')
    print(f'Best val Acc: {best_acc:4f}')

    # load best model weights
    model.load_state_dict(best_model_wts)
    return model, train_losses, train_accuracies, val_losses, val_accuracies


def setup_classification_model(
    device,
    ds_path,
    model,
    transforms,
    mock_datasets=None,
    lr=0.001,
    momentum=0.9,
    step_size=7,
    gamma=0.1,
    epochs=15,
    testing=False,
):
    """
    Set up dataset and return trained model and info.

    :param ds_path: Path containing ds with train and test dirs.
    :type kind: str()
    :param model: Model that we'd like to adapt for our classification purposes.
    :type kind: torch.nn.Module
    :param transforms: Transformations to apply on train and test data, depend on model.
    :type kind: dict() containing torchvision.transforms.Compose() as values
    :param lr: Learning rate.
    :type kind: float()
    :param momentum: Momentum hyperparameter.
    :type kind: float()
    :param step_size: Step size hyperparameter for scheduler.
    :type kind: int()
    :param gamma: Gamma hyperparameter.
    :type kind: float()
    :param num_epochs: Epochs to train on.
    :type kind: int
    :param testing: Whether we are testing the function or running it normally.
    :type kind: boolean

    :return model: Trained model.
    :rtype: torch.nn.Module
    :return train/val_losses: Per epoch train and val losses
    :rtype: list()
    :return train/val_accuracies: Per epoch train and val accuracies
    :rtype: list()
    """

    datasets = ms_ds.get_datasets(ds_path, transforms)
    class_names = datasets["train"].class_labels.values()
    if testing:
        datasets = mock_datasets
        class_names = list(range(6))
    dataset_sizes = {x: len(datasets[x]) for x in ['train', 'test']}
    dataloaders = ms_ds.get_dataloaders(datasets)

    new_model = ms_model.get_plant_model(model, class_names)  # list(range(6))

    criterion, optimizer, lr_scheduler = ms_model.get_train_loss_needs(new_model, lr, momentum, step_size, gamma)

    return train_model(
        device,
        dataset_sizes,
        dataloaders,
        new_model,
        criterion,
        optimizer,
        lr_scheduler,
        num_epochs=epochs,
        testing=testing,
    )
