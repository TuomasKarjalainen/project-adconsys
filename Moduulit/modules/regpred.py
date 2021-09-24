from sklearn import preprocessing
import torch.nn as nn
import torch.nn.functional as F
from torch import nn, optim
import numpy as np
import torch
from pickle import dump, load
from sklearn.preprocessing import MinMaxScaler
import sys


def predictreg(path, model, vector=[], specs=False):
    """
    Function for regression model's prediction.
    
    MAKE SURE YOU HAVE SCALER.PKL AND PRE-TRAINED MODEL ON THE PATH YOU DEFINED !
    
    
    EXAMPLE :
    ----------------------------------
    predictreg('/home/jovyan/work/TeamAdconsys/Tuomas/Sprint 8/','10epoch.pth', [1,2,3,4,5,6,7,8])    
    
    
    Parameters
    ----------
    
    path :
        - Your path to pre-trained regression neural network (pth.file)
        
    model :
        - Pre-trained Network
        - pth-file
        
    vector :
        - Unique vector to predict one output.
        - Eight values
        - [1,8] shaped vector
        
    specs :
        - True if you want to print the model, input tensor and path.

    Returns
    
    -------
    
    Nothing.    
    
    """
    if len(vector) != 8:
        msg = "Check input vector size! Should be [1,8]"
        sys.exit(msg)
    else:
        scaler = load(open(path+'scaler.pkl', 'rb'))
        vector = scaler.transform([vector])
        tulo = torch.from_numpy(vector)
        if specs:
            print("\nTensor:", tulo)
            print('\npath:', path+model)
        model = torch.load(path+model)
        if specs:
            print("\nModel used in prediction:")
            print(model)
        with torch.no_grad():
            output = model(tulo.float())
            output = output.item()
#             print(f"\nPrediction to MenovesiLaskAs: {output}°C")
        return  output
        
    