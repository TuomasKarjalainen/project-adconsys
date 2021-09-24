from timeit import default_timer as timer 
import torch.utils.data as data_utils
import pandas as pd
import torch

def dataloaders(path, overwrite=False, regmodel=True):
    """
    Function creates dataloaders for neural networks.
    
    EXAMPLE HOW TO DEFINE DATALOADERS:
    ----------------------------------
    train_loader, test_loader, val_loader, large_test_loader = dataloaders('/home/jovyan/work/TeamAdconsys/Tuomas/NN_data/new_data', overwrite=True, regmodel=True)    
    
    Parameters
    ----------
    
    path :
        - Your path to train, test and validation csv-files.
        - Example: "/home/jovyan/work/TeamAdconsys/Tuomas/NN_data/"
        - Example2: "~/work/TeamAdconsys/proj3-team-adconsys/Datat/csv"
        
    overwrite : 
        - Default: False
        - False = LammitysS values are default.
        - True = You can define LämmitysS values for example to 70 (then set 0.7 => normalized).
        
    regmodel :
        - Default: True
        - True if you are using regression model instead of classification model.
        - If you use classification model then set False. Then function rounds target values.
        - If False MAKE SURE YOU HAVE IMPORT ROUNDING
        

    Returns
    
    -------
    
    Four different dataloaders.
    
    """
    start = timer()
    print("-------------------------------------------------------------")
    print("------------------ Creating Dataloaders ---------------------")
    print("-------------------------------------------------------------\n")
    
    # Jos halutaan itse määrittää lämmitykselle jokin säätöarvo ...
    # ... esim. 0.1, 0.3 tai 0.7 niin silloin overwrite==True
    if overwrite==True:
        setvalue = float(input("Define value_LammitysS"))
    
    
    print(f"\nReading csv-files from {path}/")
    x_train = pd.read_csv(f"{path}/X_train.csv", header=0)
    
    if overwrite==True:
        x_train['value_LammitysS'] = setvalue
    
    # Removing timestamp column if it exists
    if 'timestamp' in x_train:
        x_train = x_train.drop(columns = ['timestamp'])
        
    y_train = pd.read_csv(f"{path}/y_train.csv", header=0)
    
    # Removing timestamp column if it exists
    if 'timestamp' in y_train:
        y_train = y_train.drop(columns = ['timestamp'])
    
    x_test = pd.read_csv(f"{path}/X_test.csv", header=0)
    
    # Removing timestamp column if it exists
    if 'timestamp' in x_test:
        x_test = x_test.drop(columns = ['timestamp'])
    
    if overwrite==True:
        x_test['value_LammitysS'] = setvalue
        
    y_test = pd.read_csv(f"{path}/y_test.csv", header=0)
    
    # Removing timestamp column if it exists
    if 'timestamp' in y_test:
        y_test = y_test.drop(columns = ['timestamp'])
    
    x_val = pd.read_csv(f"{path}/X_val.csv", header=0)
    
    if overwrite==True:
        x_val['value_LammitysS'] = setvalue
        
    # Removing timestamp column if it exists
    if 'timestamp' in x_val:
        x_val = x_val.drop(columns = ['timestamp'])
        
    y_val = pd.read_csv(f"{path}/y_val.csv", header=0)
    
    # Removing timestamp column if it exists
    if 'timestamp' in y_val:
        y_val = y_val.drop(columns = ['timestamp'])

    
    # TRAINLOADER
    inputs_train = torch.tensor(x_train.values)
    targets_train = torch.tensor(y_train.values)
    if regmodel != True:
        targets_train = targets_train.squeeze()
        targets_train = targets_train.type(torch.LongTensor)
    
    train = data_utils.TensorDataset(inputs_train, targets_train)
    train_loader = data_utils.DataLoader(train, batch_size=64, shuffle=True)
    
    # TESTLOADER
    inputs_test = torch.tensor(x_test.values)
    targets_test = torch.tensor(y_test.values)
    if regmodel != True:
        targets_test = targets_test.squeeze()
        targets_test = targets_test.type(torch.LongTensor)
    
    test = data_utils.TensorDataset(inputs_test, targets_test)
    test_loader = data_utils.DataLoader(test, batch_size=64)
    
    # VALIDATIONLOADER
    inputs_val = torch.tensor(x_val.values)
    targets_val = torch.tensor(y_val.values)
    if regmodel != True:
        targets_val = targets_val.squeeze()
        targets_val= targets_val.type(torch.LongTensor)
    
    val = data_utils.TensorDataset(inputs_val, targets_val)
    val_loader = data_utils.DataLoader(val, batch_size=64, shuffle=True)
    
    # LARGE TESTLOADER (Datat yhdistetty)
    train_y = pd.read_csv(f"{path}/y_train.csv")
    train = pd.read_csv(f"{path}/X_train.csv")
    
    # Removing timestamp column if it exists
    if 'timestamp' in train_y:
        train_y = train_y.drop(columns = ['timestamp'])
        
    # Removing timestamp column if it exists
    if 'timestamp' in train:
        train = train.drop(columns = ['timestamp'])
    train["y"] = train_y
    train.drop_duplicates()
    
    test_y = pd.read_csv(f"{path}/y_test.csv")
    
    # Removing timestamp column if it exists
    if 'timestamp' in test_y:
        test_y = test_y.drop(columns = ['timestamp'])
    test = pd.read_csv(f"{path}/X_test.csv")
    
    # Removing timestamp column if it exists
    if 'timestamp' in test:
        test = test.drop(columns = ['timestamp'])
    test["y"] = test_y
    test.drop_duplicates()
    
    val_y = pd.read_csv(f"{path}/y_val.csv")
    
    # Removing timestamp column if it exists
    if 'timestamp' in val_y:
        val_y = val_y.drop(columns = ['timestamp'])
    val = pd.read_csv(f"{path}/X_val.csv")
    
    # Removing timestamp column if it exists
    if 'timestamp' in val:
        val = val.drop(columns = ['timestamp'])
    val["y"] = val_y
    val.drop_duplicates()
    
    train = train.append(test)
    train = train.append(val)
    train.drop_duplicates()
    
    train_y = train['y']
    train = train.drop(columns=['y'])
    
    if overwrite==True:
        train['value_LammitysS'] = setvalue
        
    large_inputs_test = torch.tensor(train.values)
    large_targets_test = torch.tensor(train_y.values)
    
    large_test = data_utils.TensorDataset(large_inputs_test, large_targets_test)
    large_test_loader = data_utils.DataLoader(large_test, batch_size=64)
    
    print("\nDataloaders:\ntrain_loader:", len(train_loader), "\ntest_loader:", len(test_loader),"\nval_loader:", len(val_loader), "\nlarge_test_loader:", len(large_test_loader))
    
    end = timer()
    print("\n\nDone in", round(end-start,2),"seconds.")
    
    return train_loader, test_loader, val_loader, large_test_loader