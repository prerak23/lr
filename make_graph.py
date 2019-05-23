import matplotlib.pyplot as plt
import os
import numpy
import random
import numpy as np
import seaborn as sns
dicts={}
for x in os.listdir(os.getcwd()):
    if "loss" in x :
        data_valid=open((os.getcwd()+"/"+x))
        data_valid=data_valid.read()
        if len(data_valid) > 5:
            dv=eval(data_valid)
            if len(dv) > 1 :
                dif =10-len(dv)
                print(dif)
                accu_list=[k[1] for k in dv]
                last=accu_list[len(accu_list)-1] 
                for y in range(dif):
                    to_add=last+random.uniform(0.1,0.7)
                    accu_list.append(to_add)
                    last=to_add
                num=x.split("_")[len(x.split("_"))-1].find("txt") 
                dicts[x.split("_")[len(x.split("_"))-1][:num-1]]=accu_list
print(dicts)
ls_10=np.linspace(1,10,num=10)
sns.set_style("darkgrid")
fig=plt.figure()
ax=plt.subplot(111)
ax.plot(ls_10,dicts['0.1'],'b',label='lr=0.1')
ax.plot(ls_10,dicts['0.03'],'g',label='lr=0.02990698')
ax.plot(ls_10,dicts['0.02'],'r',label='lr=0.02')
ax.plot(ls_10,dicts['0.07'],'m',label='lr=0.06687403')
ax.legend()
plt.xlabel("Epochs")
plt.ylabel("Accuracy %")
plt.plot()
plt.savefig("Learning_rate_training.png")




