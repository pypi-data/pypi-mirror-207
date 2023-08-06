import torch.nn as nn
import torch.optim as optim
from torch.optim import lr_scheduler


def get_plant_model(model, class_names):
    """
    Train and fine-tune previously auto-generated model.

    :param model: The model to build on.
    :type kind: torch.nn.Module
    :param class_names: Classes for classification task.
    :type kind: list()

    :return model: Model with additional classification layer.
    :rtype: torch.nn.Module
    """
    num_ftrs = model.fc.in_features
    model.fc = nn.Linear(num_ftrs, len(class_names))
    return model


def get_train_loss_needs(model_ft, lr, momentum, step_size, gamma):
    """
    Train and fine-tune previously auto-generated model.

    :param model_ft: The actual model.
    :type kind: torch.nn.Module
    :param lr: Learning rate.
    :type kind: float
    :param momentum: Momentum parameter to be specified.
    :type kind: float
    :param step_size: step_size
    :type kind: int
    :param gamma: Gamma value to be specified for lr_scheduler.
    :type kind: float

    :return criterion: Trained model.
    :rtype: function, nn.CrossEntropyLoss()
    :return optimizer_ft: The defined optimizer.
    :rtype: torch.optim.SGD
    :return exp_lr_scheduler: Defined learning rate scheduler
    :rtype: torch.optim.lr_scheduler.StepLR
    """

    criterion = nn.CrossEntropyLoss()
    optimizer_ft = optim.SGD(model_ft.parameters(), lr=lr, momentum=momentum)
    exp_lr_scheduler = lr_scheduler.StepLR(optimizer_ft, step_size=step_size, gamma=gamma)
    return criterion, optimizer_ft, exp_lr_scheduler
