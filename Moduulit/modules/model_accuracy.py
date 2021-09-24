from timeit import default_timer as timer 
import matplotlib.pyplot as plt
import numpy as np
import torch
import torch.nn as nn

def accuracy(model, data_loader):
    """
    Function performs model accuracy.
    
    EXAMPLE:
    ----------------------------------
    accuracy('multimargin.pth', test_loader)    
    
    Parameters
    ----------
    
    model :
        - pth.file
          
    data_loader :
        - Define dataloader. For example it can be test_loader or large_test_loader.
        - Define it with dataloaders-function before calling this function.

    Returns
    
    -------
    
    Nothing
    
    """
    print("-------------------------------------------------------------")
    print("----------------------- Model Accuracy ----------------------")
    print("-------------------------------------------------------------\n")
    start = timer()
    print(f"Model: {model}\n")
    model = torch.load(model)
    predictions = []
    right_values = []
    values = []
    with torch.no_grad():
        for inputs, targets in data_loader:

            targets = targets.squeeze_()
            targets = targets.type(torch.LongTensor)
            logps = model(inputs.float())

            ps = torch.exp(logps)
            top_p, top_class = ps.topk(1, dim=1)
            equals = top_class == targets.view(*top_class.shape)

            for index, value in enumerate(equals):
                right_values.append(targets[index].item())
                values.append(inputs[index])
                predictions.append(top_class[index].item())

    plt.figure(figsize=(15,10))
    plt.plot(predictions, label='predictions')
    plt.plot(right_values, label='right_values')
    plt.legend()
    plt.grid()
    plt.show()
    
    predictions = np.array(predictions)
    right_values = np.array(right_values) 
    
    print("\nAccuracy:", sum(right_values==predictions)/len(predictions))
    end = timer()
    print("\n\nDone in", round(end-start,2),"seconds.")