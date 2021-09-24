import torch
from torch import nn
from torch import optim
from matplotlib import pyplot as plt

def neuroverkko(model, epochit, optimizer, criterion,train_loader,test_loader):
    
    """[Opettaa määrittämäsi mallin valitsemallasi epoch määrällä, optimizerilla ja criterionilla]

    Parameters:
        model ([type]): [torc.nn.sequentialissa luotu model] pitää määrittää ennen funktion ajamista
        epochit ([type]): [int] epochejen määrä
        optimizer ([type]): [torch.optim] torchvisionin optimizer, pitää määrittää ennen funktion ajamista
        criterion ([type]): [from torch import nn kirjaston funktio] määritä itsellesi sopiva criterion ennen kuin ajat funktion
        train_loader ([type]): [data loader] täällä funktio lataa datan kouluttamiseen. määrittele tämä etukäteen
        test_loader ([type]): [data loader] täällä funktio lataa datan testaamiseen. määrittele tämä etukäteen
    Returns:
        palauttaa tallennetun .pth tiedoston missä on opetettu malli.
    """

    
    malli = model
    optimizeri = optimizer
    criterioni  = criterion
    traininglosses = []
    testinglosses = []
    testaccuracy = []
    totalsteps = []
    epochs = epochit
    steps = 0
    running_loss = 0
    print_every = 800

    for epoch in range(epochs):
        for inputs, targets in train_loader:
            steps += 1
            
            #sitten perus looppi
            optimizer.zero_grad()

            logps = malli.forward(inputs.float())
            loss = criterioni(logps, targets)
            loss.backward()
            optimizeri.step()

            running_loss += loss.item()
            #test settiä
            if steps % print_every == 0:
                test_loss = 0
                accuracy = 0
                model.eval()
                with torch.no_grad():
                    for inputs, targets in test_loader:
                        
                        logps = malli.forward(inputs.float())
                        batch_loss = criterioni(logps, targets)

                        test_loss += batch_loss.item()

                        # Lasketaan tarkkuus
                        ps = torch.exp(logps)
                        top_p, top_class = ps.topk(1, dim=1)
                        equals = top_class == targets.view(*top_class.shape)
                        accuracy += torch.mean(equals.type(torch.FloatTensor)).item()

                traininglosses.append(running_loss/print_every)
                testinglosses.append(test_loss/len(test_loader))
                testaccuracy.append(accuracy/len(test_loader))
                totalsteps.append(steps)
                print(  #millä tehään duunia
                      f"Epoch {epoch+1}/{epochs}.. " #epookit
                      f"Step {steps}.. " #joka viides steppi printataan
                      f"Train loss: {running_loss/print_every:.3f}.. " 
                      f"Test loss: {test_loss/len(test_loader):.3f}.. "
                      f"Test accuracy: {accuracy/len(test_loader):.3f}")
                running_loss = 0
                malli.train() #trainataan modelli
                
    
    
    # Plotataan mallin tarkkuus, harjoitusvirhe sekä testi/validointi -virhe
    #plt.figure(figsize=(15,10))
    plt.plot(totalsteps, traininglosses, label='Train Loss')
    plt.plot(totalsteps, testinglosses, label='Test Loss')
    plt.plot(totalsteps, testaccuracy, label='Test Accuracy')
    plt.xlabel("Step")
    plt.ylabel("Accuracy")
    plt.legend()
    plt.grid()
    plt.show()
    vastaus = (input('Haluatko tallentaa mallin? (y/n)'))
    
    if vastaus == 'y':
        
        PATH = str(input('enter the filename.pth'))
        torch.save(malli, PATH)
    else:
        print('model not saved')
    return print('Done')

def neuroverkkoregressio(model, epochit, optimizer, criterion,train_loader,test_loader):
    
    """[Opettaa määrittämäsi mallin valitsemallasi epoch määrällä, optimizerilla ja criterionilla]

    Parameters:
        model ([type]): [torc.nn.sequentialissa luotu model] pitää määrittää ennen funktion ajamista
        epochit ([type]): [int] epochejen määrä
        optimizer ([type]): [torch.optim] torchvisionin optimizer, pitää määrittää ennen funktion ajamista
        criterion ([type]): [from torch import nn kirjaston funktio] määritä itsellesi sopiva criterion ennen kuin ajat funktion
        train_loader ([type]): [data loader] täällä funktio lataa datan kouluttamiseen. määrittele tämä etukäteen
        test_loader ([type]): [data loader] täällä funktio lataa datan testaamiseen. määrittele tämä etukäteen
    Returns:
        palauttaa tallennetun .pth tiedoston missä on opetettu malli.
    """

    
    malli = model
    optimizeri = optimizer
    criterioni  = criterion
    traininglosses = []
    testinglosses = []
    testaccuracy = []
    totalsteps = []
    epochs = epochit
    steps = 0
    running_loss = 0
    print_every = 800

    for epoch in range(epochs):
        for inputs, targets in train_loader:
            steps += 1
       
            #sitten perus looppi
            optimizer.zero_grad()

            logps = malli.forward(inputs.float())
            loss = criterioni(logps, targets.float())
            loss.backward()
            optimizeri.step()

            running_loss += loss.item()
            #test settiä
            if steps % print_every == 0:
                test_loss = 0
                accuracy = 0
                model.eval()
                with torch.no_grad():
                    for inputs, targets in test_loader:
                  
                        logps = malli.forward(inputs.float())
                        batch_loss = criterioni(logps, targets.float())

                        test_loss += batch_loss.item()

                        # Lasketaan tarkkuus
                        ps = torch.exp(logps)
                        top_p, top_class = ps.topk(1, dim=1)
                        equals = top_class == targets.view(*top_class.shape)
                        accuracy += torch.mean(equals.type(torch.FloatTensor)).item()

                traininglosses.append(running_loss/print_every)
                testinglosses.append(test_loss/len(test_loader))
                testaccuracy.append(accuracy/len(test_loader))
                totalsteps.append(steps)
                print(  #millä tehään duunia
                      f"Epoch {epoch+1}/{epochs}.. " #epookit
                      f"Step {steps}.. " #joka viides steppi printataan
                      f"Train loss: {running_loss/print_every:.3f}.. " 
                      f"Test loss: {test_loss/len(test_loader):.3f}.. "
                      f"Test accuracy: {accuracy/len(test_loader):.3f}")
                running_loss = 0
                malli.train() #trainataan modelli
                
    
    
    # Plotataan mallin tarkkuus, harjoitusvirhe sekä testi/validointi -virhe
    #plt.figure(figsize=(15,10))
    plt.plot(totalsteps, traininglosses, label='Train Loss')
    plt.plot(totalsteps, testinglosses, label='Test Loss')
    plt.plot(totalsteps, testaccuracy, label='Test Accuracy')
    plt.xlabel("Step")
    plt.ylabel("Accuracy")
    plt.legend()
    plt.grid()
    plt.show()
    vastaus = (input('Haluatko tallentaa mallin? (y/n)'))
    
    if vastaus == 'y':
        
        PATH = str(input('enter the filename.pth'))
        torch.save(malli, PATH)
    else:
        print('model not saved')
    return print('Done')