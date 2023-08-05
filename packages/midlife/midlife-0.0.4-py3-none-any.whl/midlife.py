import pandas as pd
import matplotlib.pyplot as plt
import subprocess as sp
import numpy as np
from sklearn.metrics import r2_score as r2
import warnings
warnings.filterwarnings('ignore')
import sys
if len(sys.argv)<3:
 print('enter regression-degree(int) and sex: M or F')
 print('for example, midlife 3 M')
 exit(0)
sp.call('wget -nc https://data.cdc.gov/api/views/chcz-j2du/rows.csv', shell=True)
d=pd.read_csv('rows.csv')
years=d.Year.unique()
degree=int(sys.argv[1])
print('degree=',degree)
a1=[]
a2=[]
a3=[]
a4=[]
a5=[]
sex=sys.argv[2]
for i in years:
 a=d.loc[(d.Year==i) &
  (d['Sex']==sex) & (d['Age Group']=='40-44 years'),'Total Deaths']
 a1.append(int(a))
 a=d.loc[(d.Year==i) &
  (d['Sex']==sex) & (d['Age Group']=='45-49 years'),'Total Deaths']
 a2.append(int(a))
 a=d.loc[(d.Year==i) &
  (d['Sex']==sex) & (d['Age Group']=='50-54 years'),'Total Deaths']
 a3.append(int(a))
 a=d.loc[(d.Year==i) &
  (d['Sex']==sex) & (d['Age Group']=='55-59 years'),'Total Deaths']
 a4.append(int(a))
 a=d.loc[(d.Year==i) &
  (d['Sex']==sex) & (d['Age Group']=='60-64 years'),'Total Deaths']
 a5.append(int(a))

model=np.poly1d(np.polyfit(years[0:-2],a1[0:-2],degree))
print('40-44 years:',round((a1[-1]-int(model(2020)))/int(model(2020)),3))
error=r2(model(years[0:-2]),a1[0:-2])
print('r2=',round(error,3),'\n')
#print(a1)
#print(int(model(2020)),'\n')

model=np.poly1d(np.polyfit(years[0:-2],a2[0:-2],degree))
print('45:49 years:',round((a2[-1]-int(model(2020)))/int(model(2020)),3))
error=r2(model(years[0:-2]),a2[0:-2])
print('r2=',round(error,3),'\n')

model=np.poly1d(np.polyfit(years[0:-2],a3[0:-2],degree))
print('50-54 years:',round((a3[-1]-int(model(2020)))/int(model(2020)),3))
error=r2(model(years[0:-2]),a3[0:-2])
print('r2=',round(error,3),'\n')

model=np.poly1d(np.polyfit(years[0:-2],a4[0:-2],degree))
print('55-59 years:',round((a4[-1]-int(model(2020)))/int(model(2020)),3))
error=r2(model(years[0:-2]),a4[0:-2])
print('r2=',round(error,3),'\n')

model=np.poly1d(np.polyfit(years[0:-2],a5[0:-2],degree))
print('60-65 years:',round((a5[-1]-int(model(2020)))/int(model(2020)),3))
error=r2(model(years[0:-2]),a5[0:-2])
print('r2=',round(error,3),'\n')

def main():
 plt.ylim([0,170000])
 plt.plot(years,a1,':k')
 plt.plot(years,a2,'-k')
 plt.plot(years,a3,'--k')
 plt.plot(years,a4,'-.k')
 plt.plot(years,a5,':k',linewidth=2)
 plt.legend(('40-44 years','45-49 years','50-54 years','55-59 years','60-64 years'),loc='upper left')
 plt.title('Impact of COVID-19 on montality of '+sex+'-midlife')
 plt.savefig(str(sex)+'midlife.png')
main()
plt.show()
