import os
from skimage import io, transform
import torch
import torchvision
from torch.autograd import Variable
import torch.nn as nn
import torch.nn.functional as F
from torch.utils.data import Dataset, DataLoader
from torchvision import transforms#, utils
# import torch.optim as optim

import numpy as np
from PIL import Image
import glob

from data_loader import RescaleT
from data_loader import ToTensor
from data_loader import ToTensorLab
from data_loader import SalObjDataset

from model import U2NET # full size version 173.6 MB

class U2Net():
    def __init__(self):
        model_dir = os.path.join(os.getcwd(), 'saved_models', 'u2net', 'u2net.pth')
        print("...load U2NET---173.6 MB")
        self.net = U2NET(3,1)
        if torch.cuda.is_available():
            self.net.load_state_dict(torch.load(model_dir))
            self.net.cuda()
        else:
            self.net.load_state_dict(torch.load(model_dir, map_location='cpu'))
        self.net.eval()
    
    def matt_model(self, image_dir):
        img_name_list = glob.glob(image_dir + os.sep + '*')
        print(img_name_list)
        test_salobj_dataset = SalObjDataset(img_name_list = img_name_list,
                                        lbl_name_list = [],
                                        transform=transforms.Compose([RescaleT(320),
                                                                      ToTensorLab(flag=0)])
                                        )
        test_salobj_dataloader = DataLoader(test_salobj_dataset,
                                        batch_size=1,
                                        shuffle=False)
        resultpath = os.path.join(image_dir, "result", "")
        if not os.path.exists(resultpath):
            os.makedirs(resultpath)
        result_urls = []
        for i_test, data_test in enumerate(test_salobj_dataloader):
            print("inferencing:",img_name_list[i_test].split(os.sep)[-1])
            inputs_test = data_test['image']
            inputs_test = inputs_test.type(torch.FloatTensor)
            if torch.cuda.is_available():
                inputs_test = Variable(inputs_test.cuda())
            else:
                inputs_test = Variable(inputs_test)
            torch.set_printoptions(profile='full')
            d1,d2,d3,d4,d5,d6,d7= self.net(inputs_test)
            # normalization
            pred = d1[:,0,:,:]
            pred = normPRED(pred)
            # save results to test_results folder
            result_urls.append(save_output(img_name_list[i_test],pred,resultpath))

            del d1,d2,d3,d4,d5,d6,d7


# normalize the predicted SOD probability map
def normPRED(d):
    ma = torch.max(d)
    mi = torch.min(d)

    dn = (d-mi)/(ma-mi)

    return dn

def save_output(image_name,pred,result_path):

    predict = pred
    predict = predict.squeeze()
    predict_np = predict.cpu().data.numpy()

    im = Image.fromarray(predict_np*255).convert('RGB')
    img_name = image_name.split(os.sep)[-1]
    image = io.imread(image_name)
    imo = im.resize((image.shape[1],image.shape[0]),resample=Image.BILINEAR)
    oimg = Image.open(image_name)
    oimg = oimg.convert("RGBA")
    x, y = oimg.size
    for i in range(x):
        for k in range(y):
            color = imo.getpixel((i, k))
            ocolor = oimg.getpixel((i, k))
            if color[0] > 245:
                newcolor = (ocolor[0], ocolor[1], ocolor[2], 255)
            elif color[0] < 10:
                newcolor = (ocolor[0], ocolor[1], ocolor[2], 0)
            else:
                newcolor = (ocolor[0], ocolor[1], ocolor[2], color[0])
            oimg.putpixel((i, k), newcolor)
    aaa = img_name.split(".")
    bbb = aaa[0:-1]
    imidx = bbb[0]
    for i in range(1,len(bbb)):
        imidx = imidx + "." + bbb[i]
    oname = result_path+imidx+".png"
    oimg.save(oname)
    return oname
