import cv2
import torch
import numpy as np
import torchvision
from PIL import Image
import warnings
warnings.filterwarnings("ignore", category=UserWarning)

class Detector:
    """
    Detector class for thermal face detection.

    Attributes
    ----------
    model : torch.jit.ScriptModule
        The TorchScript model for thermal face detection.
    original_shape : tuple
        The original shape of the input image.

    Methods
    -------
    preprocess(img)
        Preprocess the input image and store its original shape.
    resize_bbox(bbox)
        Resize the bounding box to match the original image dimensions.
    detect(img)
        Detect a face in the input image and return the bounding box.
    """
    def __init__(self, model_path):
        self.model = torch.jit.load(model_path)
    
    def preprocess(self, img):
        if isinstance(img, Image.Image):
            img = np.array(img)

        self.original_shape = img.shape[:2]
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        img = cv2.resize(img, (160, 160))
        img = torch.from_numpy(img).unsqueeze(0).float()
        img = img / 255.0
        return [img]

    def resize_bbox(self, bbox):
        scale_y, scale_x = np.array(self.original_shape) / np.array([160, 160])
        bbox = np.array(bbox)
        bbox[[0, 2]] = bbox[[0, 2]] * scale_x
        bbox[[1, 3]] = bbox[[1, 3]] * scale_y
        return bbox

    def detect(self, img):
        """
        Detect a face in the input image and return the bounding box.

        Parameters
        ----------
        img : PIL.Image.Image or numpy.ndarray
            The input image as a PIL Image or numpy array.

        Returns
        -------
        numpy.ndarray
            The bounding box for the detected face in the format [x1, y1, x2, y2].
        """
        img = self.preprocess(img)
        output = self.model(img)
        bbox = output[1][0]['boxes'][0].cpu().detach().numpy()
        bbox = self.resize_bbox(bbox)
        return bbox
