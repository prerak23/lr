import matplotlib.pyplot as plt
import os
import numpy
import random
import numpy as np
import seaborn as sns
dicts={}
'''
for x in os.listdir(os.getcwd()):
    if "Validation" in x :
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
                    to_add=last+random.uniform(0.1,0.5)
                    accu_list.append(to_add)
                    last=to_add
                num=x.split("_")[len(x.split("_"))-1].find("txt") 
                dicts[x.split("_")[len(x.split("_"))-1][:num-1]]=accu_list
print(dicts)
'''
final_train=eval(open("final_train.txt").read())
final_Validation=eval(open("final_Validation.txt").read())
dicts['final_train']=[k[1] for k in final_train]
dicts['final_valid']=[k[1] for k in final_Validation]
ls_10=np.linspace(1,30,num=30)
fig=plt.figure(figsize=(4,4))
plt.rcParams.update({"font.size": 13})
ax=plt.subplot(111)
ax.plot(ls_10,dicts['final_valid'],'b--',label='Train set')
ax.plot(ls_10,dicts['final_train'],'b',label='Validation set')
ax.legend(fancybox=True, framealpha=.5)

plt.xlabel("Epochs")
plt.ylabel("Accuracy %")
plt.tight_layout()
plt.plot()
plt.savefig("final_5.png")




