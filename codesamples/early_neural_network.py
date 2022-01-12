#!/usr/bin/env python
# coding: utf-8

# In[3]:


import torch
from torch import nn
from torch.utils.data import DataLoader
from torchvision import datasets, transforms
from torchvision.transforms import ToTensor, Lambda, Compose
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score
from pipetorch.train import *


# In[4]:


# set data directory
data_dir = './images/splitfolders/'

#preparing the transform method to transform data into a Tensor object
transform = transforms.Compose([
    #transforms.RandomRotation(20),
    #transforms.RandomHorizontalFlip(),
    transforms.ToTensor()]) 
    
train_set = datasets.ImageFolder(data_dir + 'train', transform=transform) #contents from the 'train' folder is put in train_set
test_set = datasets.ImageFolder(data_dir + 'test', transform=transform)

train_dataloader = DataLoader(train_set, batch_size=32, shuffle=True)#train_set is made into a dataloader, shuffled
test_dataloader = DataLoader(test_set, batch_size=32, shuffle=True)


# In[5]:


print(train_dataloader)


# In[3]:


# Get cpu or gpu device for training.
device = "cuda" if torch.cuda.is_available() else "cpu"
print("Using {} device".format(device))

# Define model
class NeuralNetwork(nn.Module):
    def __init__(self):
        super(NeuralNetwork, self).__init__()
        self.flatten = nn.Flatten() #the images are flattened (pixels are placed end to end)
        self.linear_relu_stack = nn.Sequential(
            nn.Linear(373248, 512), # in the first layer, 373248 is the amount of input features, 512 is the output amount
            nn.ReLU(),
            nn.Linear(512, 512), #second layer, input and output features is 512 (maybe this could be larger?)
            nn.ReLU(),
            nn.Linear(512, 10) #output layer, input features is 512, output features is 10 (these 10 is what the NN uses to 'learn')
        )

    def forward(self, x): #this function runs the above code with our data 'x' passed to it
        x = self.flatten(x)
        logits = self.linear_relu_stack(x)
        return logits

    def post_forward(self, y): 
        return torch.argmax(y, axis=1) #returns the highest value from a tensor object (jeroen wrote this function)
    
model = NeuralNetwork().to(device) #model is passed to gpu
print(model)


# In[4]:


loss_fn = nn.CrossEntropyLoss() #loss function is defined (we should try different ones, jeroen mentioned MSELoss and BCELoss)
optimizer = torch.optim.SGD(model.parameters(), lr=1e-3) #the optimizer is defined


# In[5]:


def train(dataloader, model, loss_fn, optimizer): #function for training the NN
    size = len(train_dataloader)
    model.train()
    for batch, (X, y) in enumerate(train_dataloader):
        X, y = X.to(device), y.to(device)

        # Compute prediction error
        pred = model(X)
        loss = loss_fn(pred, y)

        # Backpropagation
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

        if batch % 100 == 0:
            loss, current = loss.item(), batch * len(X)
            print(f"loss: {loss:>7f}  [{current:>5d}/{size:>5d}]")


# In[6]:


def test(dataloader, model, loss_fn): #function for testing
    size = len(test_dataloader)
    num_batches = len(test_dataloader)
    model.eval()
    test_loss, correct = 0, 0
    with torch.no_grad():
        for X, y in dataloader:
            X, y = X.to(device), y.to(device)
            pred = model(X)
            test_loss += loss_fn(pred, y).item()
            correct += (pred.argmax(1) == y).type(torch.float).sum().item()
    test_loss /= num_batches
    correct /= size
    print(f"Test Error: \n Accuracy: {(100*correct):>0.1f}%, Avg loss: {test_loss:>8f} \n")


# In[ ]:





# In[7]:


#epochs = 5
#for t in range(epochs):
#    print(f"Epoch {t+1}\n-------------------------------")
#    train(train_dataloader, model, loss_fn, optimizer)
#    test(test_dataloader, model, loss_fn)
#print("Done!")


# In[8]:


model = NeuralNetwork()


# In[9]:


t = trainer(model, loss_fn, train_dataloader, test_dataloader, gpu=0, metrics=accuracy_score) #NN is passed to t with parameters


# In[10]:


t.train(5, (1e-5, 1e-4))


# In[ ]:




