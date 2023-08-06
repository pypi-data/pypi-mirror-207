import os
import glob
import torch
import itertools
import numpy as np
from PIL import Image


class PlantDataset(torch.utils.data.Dataset):
    """
    Collects Generalizable Dataset from strict directory structure.
    """

    def __init__(self, images_dir, image_transform):
        """
        Initializes instance vars for dataset to corresponding provided values.

        :param images_dir: Path to directory containing images.
        :type kind: str
        :param class_names: Classes for image classification task.
        :type kind: list()
        """

        self.image_transform = image_transform

        # Get a list of all class names inside the images directory
        self.classes = self.get_class_names(images_dir)

        # Assign a unique label index to each class name
        self.class_labels = {name: idx for idx, name in enumerate(self.classes)}

        image_files, labels = self.get_image_filenames_with_labels(
            images_dir,
            self.classes,
            self.class_labels,
        )

        # This is a trick to avoid memory leaks over very large datasets.
        self.image_files = np.array(image_files)
        self.labels = np.array(labels).astype("int")

        # How many total images do we need to iterate in this entire dataset?
        self.num_images = len(self.image_files)

    def __len__(self):
        """
        Returns size of the dataset from instance var.
        """
        return self.num_images

    def get_class_names(self, images_dir):
        """
        Given a directory of images, underneath which we have directories of class
        names, collect all these class names and return as a list of strings.

        :param images_dir: Path to directory containing images.
        :type kind: str
        :return class_names: List of unique class names.
        :rtype: list()
        """
        class_name_dirs = glob.glob(images_dir + "/*")
        class_names = [name.replace(images_dir + "/", "") for name in class_name_dirs]
        return sorted(class_names)  # sort just to keep consistency

    def get_image_filenames_with_labels(self, images_dir, class_names, class_labels):
        """
        Get all image filenames for files containing proper images of our dataset.

        :param images_dir: Path to directory containing images.
        :type kind: str
        :param class_names: List of unique class names.
        :type: list()
        :param class_labels: Maps to idx of class name.
        :type kind: dict()

        :return image_files: Literally it's the image file paths.
        :rtype: list()
        :return labels: Labels for each of the images.
        :rtype: list()
        """
        image_files = []
        labels = []

        supported_file_types = ["/*.jpg", "/*.jpeg", "/*.gif"]

        for name in class_names:
            # Glob all (supported) image file names in this directory
            image_class_dir = os.path.join(images_dir, name)

            # Iterate through the supported file types.  For each, glob a list of
            # all file names with that file extension.  Then combine the entire list
            # into one list using itertools.
            image_class_files = list(
                itertools.chain.from_iterable(
                    [glob.glob(image_class_dir + file_type) for file_type in supported_file_types]
                )
            )

            # Concatenate the image file names to the overall list and create a label for each
            image_files += image_class_files
            labels += [class_labels[name]] * len(image_class_files)

        return image_files, labels

    def __getitem__(self, idx):
        """
        Get item from dataset applying transform and returning label.
        It returns a general exception if the prior fails.

        :param images_dir: Path to directory containing images.
        :type kind: str
        :return image: Image after applying transform.
        :rtype: PIL Image
        :return label: Labels for the image.
        :rtype: str
        """
        try:
            image = Image.open(self.image_files[idx]).convert('RGB')
            label = self.labels[idx]

            # Apply the image transform
            image = self.image_transform(image)

            return image, label
        except Exception as exc:
            return exc


def collate_fn(batch):
    """
    Properly collates images into mini-batches for specific task and from a particular batch.

    :param batch: batch of images and labels.
    :type kind: str
    :return images: Image after applying transform.
    :rtype: torch.Tensor
    :return labels: LongTensor of labels.
    :rtype: torch.LongTensor
    """

    # Filter failed images first
    batch = list(filter(lambda x: x is not None, batch))

    # Now collate into mini-batches
    images = torch.stack([b[0] for b in batch])
    labels = torch.LongTensor([b[1] for b in batch])

    return images, labels


def get_datasets(data_dir, data_transforms):
    """
    Create train and test dataset into a dictionary.

    :param data_dir: Directory path of data folder.
    :type kind: str
    :param data_transforms: Transformations to apply to images.
    :type kind: torchvision.transform
    :return images: Image after applying transform.
    :rtype: torch.Tensor
    """
    return {x: PlantDataset(os.path.join(data_dir, x), data_transforms[x]) for x in ['train', 'test']}


def get_dataloaders(image_datasets):
    """
    Now take the datasets and make them dataloaders with specificed params.

    :param image_datasets: Actual torch train and test datasets.
    :type kind: dict()
    :return dataloaders: Dataloaders from Datasets.
    :rtype: dict() containing DataLoaders.
    """
    return {
        x: torch.utils.data.DataLoader(
            image_datasets[x], batch_size=4, shuffle=True, num_workers=0, collate_fn=collate_fn
        )
        for x in ['train', 'test']
    }
