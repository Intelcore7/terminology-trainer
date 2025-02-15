#!/usr/bin/env python
# coding: utf-8

# In[11]:


import pandas as pd
import numpy as np
import unicodedata   #provides different Unicode databases; Unicode determines how strings are saved on computer
import tkinter as tk


# In[13]:


data = pd.read_csv("alkane.csv")


# In[33]:


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
    #print('Check', vocab)   #DEBUG
    ind = dataF.index[dataF['vocab'] == vocab].tolist()   #get index of defintion
    #print(ind)   #DEBUG
    check = str(dataF['definition'][ind[0]])   #get definition using index
    #check = GetDefinition(data, vocab[0])
    #print(UI, check)    #DEBUG
    checking.configure(text= Check(UI, check))

def GetDefinition(dataF, vocab):
    ind = dataF.index[dataF['vocab'] == vocab].tolist()
    #print('Check', vocab)   #DEBUG
    ind = dataF.index[dataF['vocab'] == vocab].tolist()   #get index of defintion
    #print(ind)   #DEBUG
    check = str(dataF['definition'][ind[0]])   #get definition using index
    return check

def Normal(dataF):
    my_list = list(dataF['vocab'])
    return my_list

def Update(lst, n):
    lst.clear()
    lst.append(n)    #make vocab a list to make it manipulateable in functions
    #print(lst)    #DEBUG
    return lst

def Show(string):
    try:
        vocabular.configure(text = string)

    except StopIteration:
        print("end")
        return

def Counter(ncount, counter, my_list):
    if ncount < len(my_list):
        ncount += 1
    counter[0] = ncount
    count.configure(text = (ncount , "/" , len(my_list)))
    #print(n , "/" , len(my_list))   #DEBUG
    return counter

def History(vocab, Text, lst):
    history_vocab = lst[lst.index(vocab) -1]    #-1 to get last vocab in lst to display in history; not current
    t= f"{lst.index(vocab)}) {history_vocab} - {GetDefinition(data, history_vocab)} \n"
    Text.insert(tk.END, t)




# In[39]:


#Shuffle(data)
root = tk.Tk()

text = tk.Text(root, width= 30, height= 10)
text.grid(row= 1, column= 1, rowspan= 4)

vocabular = tk.Label(root, width = 40, height=2)
vocabular.grid(row= 1, column= 2)

checking = tk.Label(root, width = 40, height=2)
checking.grid(row= 2, column= 2)


count = tk.Label(root, width = 40, height=2)
count.grid(row= 3, column= 2)

chronik= tk.Label(root, width = 10, height=1, text= "History")
chronik.grid(row= 0, column= 1)

ent = tk.Entry(root, width= 30)
ent.grid(row= 4, column= 2)

lst = Shuffle(data)     #get list with vocab
history = lst.copy()
#print(lst)   #DEBUG
my_iteration = iter(lst)   #get list in Iterator - form

#Set up - Counter
counter = [0]
counter = Counter(counter[0], counter, history)

#runs first:
vocab = list()
vocab = Update(vocab, next(my_iteration))
#print(vocab)        #DEBUG
Show(vocab[0])
#print('->', vocab)  #DEBUG

my_button1 = tk.Button(root, 
                      text= "Next", 
                      padx = 10, 
                      pady = 10, 
                      command= lambda:[Update(vocab, 
                                       next(my_iteration, 'End!')), 
                                       Show(vocab[0]),
                                       Counter(counter[0], counter, history),
                                       History(vocab[0], text, lst)
                                      ])
my_button1.grid(row= 5, column= 2)

#bug: vocab value doesn't change after pressing Next button

my_button2 = tk.Button(root, 
                      text= "Check", 
                      padx = 10, 
                      pady = 10, 
                      command= lambda: Check2(data, vocab[0], ent.get()))
my_button2.grid(row= 5, column= 3)
#Iteration(iter(lst))

root.mainloop()


# In[ ]:


GetInfoShort(data)
print(data)


# In[ ]:




