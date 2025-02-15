#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import unicodedata   #provides different Unicode databases; Unicode determines how strings are saved on computer
import tkinter as tk


# In[2]:


data = pd.read_csv("vocabulary.csv")


# In[25]:


def GetInfoShort(dataF):
    print("Length of each column: ", len(data), "\n")
    
    for i in data.columns:
        print("Column: ", i)
        print("   ", "dtype: ", data.dtypes[i], " NaN: ", pd.isnull(data[i]).values.any(), "\n")
        
    print("\n","number of columns: ", len(data.columns))
    print(data.isnull().values.any())
    
def normalize(s):
  return unicodedata.normalize("NFKC", s).strip()   #converts string s to 1 Unicode
    
def Shuffle(dataF):
    lst = []
    for i in range(len(data)):
        n = dataF['vocab'][np.random.randint(len(dataF))]
        while n in lst:
            n = dataF['vocab'][np.random.randint(len(dataF))]
        
        lst.append(n)
    return lst

def Check(n1, n2):
    if normalize(n1) == normalize(n2):
        n =  'True!'
    else:
        n = 'False!' + ' True Translation: ' + n2
    return n

def Check2(dataF, vocab, UI):
    print('Check', vocab)   #DEBUG
    ind = dataF.index[dataF['vocab'] == vocab].tolist()   #get index of defintion
    print(ind)   #DEBUG
    check = str(dataF['definition'][ind[0]])   #get definition using index
    print(UI, check)    #DEBUG
    label2.configure(text= Check(UI, check))

def Normal(dataF):
    my_list = list(dataF['vocab'])
    return my_list

def Update(lst, n):
    lst.clear()
    lst.append(n)    #make vocab a list to make it manipulateable in functions
    print(lst)    #DEBUG
    return lst

def Show(string):
    try:
        label.configure(text = string)

    except StopIteration:
        print("end")
        return


# In[27]:


#Shuffle(data)
root = tk.Tk()

label = tk.Label(root, width = 40, height=4)
label.pack()

label2 = tk.Label(root, width = 40, height=4)
label2.pack()

ent = tk.Entry(root, width= 30)
ent.pack()

lst = Shuffle(data)     #get list with vocab
print(lst)   #DEBUG
my_iteration = iter(lst)   #get list in Iterator - form

#runs first:
vocab = list()
vocab = Update(vocab, next(my_iteration))
print(vocab)        #DEBUG
Show(vocab[0])
print('->', vocab)  #DEBUG

my_button = tk.Button(root, 
                      text= "Next", 
                      padx = 10, 
                      pady = 10, 
                      command= lambda:[Update(vocab, next(my_iteration, 'End!')), Show(vocab[0])])
my_button.pack()
#bug: vocab value doesn't change after pressing Next button

my_button2 = tk.Button(root, 
                      text= "Check", 
                      padx = 10, 
                      pady = 10, 
                      command= lambda: Check2(data, vocab[0], ent.get()))
my_button2.pack()
#Iteration(iter(lst))

root.mainloop()


# In[ ]:


GetInfoShort(data)
print(data)

