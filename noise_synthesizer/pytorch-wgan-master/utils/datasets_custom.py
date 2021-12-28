import glob
import random
import os
import numpy as np

import mrcfile

from torch.utils.data import Dataset
from PIL import Image
import torchvision.transforms as transforms

import utils.mrc as mrc

def load_mrc(path, standardize=False):
    #with open(path, 'rb') as f:
    #    content = f.read()
    #image, header, extended_header = mrc.parse(content)
    #print("!!!!!!!!!!!")
    #print(path)
    image=mrcfile.open(path,permissive=True)
    #print("!!!!!!!!!!!")
    #print(path)
    image=image.data
    if standardize:
        image = image - header.amean
        image /= header.rms
    return Image.fromarray(image)
def load_image(path):
    x = np.array(load_mrc(path), copy=False)
    x = x.astype(np.float32) # make sure dtype is single precision
    mu = x.mean()
    std = x.std()
    x = (x - mu)/std
    return x
class CustomDataset(Dataset):
    def __init__(self, root, train=True , transform=None):
        #self.transform = transforms.Compose(transforms_)
        self.transform=transform
        #self.files = sorted(glob.glob(os.path.join(root, "train") + "/*.*"))
        self.files = sorted(glob.glob(root + "/*.*"))
        if train == False:
            #self.files.extend(sorted(glob.glob(os.path.join(root, "test") + "/*.*")))
            #just for test
            #self.files.extend(sorted(glob.glob(root + "/*.*")))
            self.files=(sorted(glob.glob(root + "/*.*")))

    def __getitem__(self, index):
        img = load_image(self.files[index % len(self.files)])
        img = self.transform(img)
        return img,index
        #return {"img": img,"i":index}

    def __len__(self):
        return len(self.files)
