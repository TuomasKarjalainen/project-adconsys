from sklearn import preprocessing
import torch.nn as nn
import torch.nn.functional as F
from torch import nn, optim
import numpy as np
import torch

def predict(path, model):
    """
    Function for prediction.
    You can define all 8 values and output is the predict to MenovesiLaskAs.
    
    
    EXAMPLE :
    ----------------------------------
    predict('/home/jovyan/work/TeamAdconsys/Tuomas/Sprint 6/','multimargin.pth')
    
    
    Parameters
    ----------
    
    path :
        - Your path to pre-trained neural network (pth.file)
        
    model :
        - Pre-trained Network
        - pth-file
        

    Returns
    
    -------
    
    Nothing.    
    
    """


#     v1 = float(input("value_1LaskAs:"))
#     v2 = float(input("value_MenoM:"))
#     v3 = float(input("value_UlkoLampotila:"))
#     v4 = float(input("value_LammitysS:"))
#     v5 = float(input("value_TuloM:"))
#     v6 = float(input("value_TuloilmaLaskettuAs:"))
#     v7 = float(input("value_PoistoM:"))
#     v8 = float(input("value_PatterinPaluuvesiM:"))

    # TESTI 1
    # row: 32646, (41.67)
#     a1 = 0
#     a2 = 0.3954457095251318
#     a3 = 0.388262599469496
#     a4 = 0.24719999999999998
#     a5 = 0.5264326965792981
#     a6 = 0.2836842105263158
#     a7 = 0.5202702702702703
#     a8 = 0.3266117580232888
    
    # TESTI 2
    # row: 55517, (52.53)
    a1 = 1
    a2 = 0.5317967231324631
    a3 = 0.2102122015915119
    a4 = 0.1856
    a5 = 0.48778320746334963
    a6 = 0.2026315789473685
    a7 = 0.5386977886977885
    a8 = 0.2717977847202499

    # NÄMÄ KÄYTTÖÖN KUN EI KÄYTETÄ TESTIARVOJA
#     tonparray = np.array([v1, v2, v3, v4, v5, v6, v7, v8])
#     normalized = preprocessing.normalize([tonparray])
#     tulo = torch.from_numpy(normalized)
    
    tonparray = np.array([a1, a2, a3, a4, a5, a6, a7, a8]) # TESTIARVOJA VARTEN
    tulo = torch.from_numpy(tonparray) # TESTIARVOJA VARTEN
    
    print("Tensor:")
    print(tulo)
    print('\npath:', path+model)
    model = torch.load(path+model)
    criterion = nn.MultiMarginLoss()
    optimizer = optim.Adam(model.parameters(), lr=0.001)
    print("\nModel:")
    print(model)
    
    with torch.no_grad():
        tulo = tulo.view(1,8)
        logps = model(tulo.float())
        ps = torch.exp(logps)
        top_p, top_class = ps.topk(1, dim=1)
        value = top_class.item()
        print(f"\nPrediction to MenovesiLaskAs: {value}°C")
        
    