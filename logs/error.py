import re
import os
import gzip
import datetime
import matplotlib.pyplot as plt
import pandas as pd

logs = []

def getLogs(logs):


    files = os.listdir('/home/emustafaj/Downloads/apache2/')
    datereg = r'[A-Z][a-z]{2} [A-Z][a-z]{2} [0-9]{2} [0-9]{2}:[0-9]{2}:[0-9]{2}.[0-9]{6} [0-9]{4}'
    ipreg = r'[0-9]*\.[0-9]*\.[0-9]*\.[0-9]*:[0-9]*'

   
    for file in files:
       
        if 'error' in file:
            if file.endswith('.gz'):

                pass
            else:

                with open('/home/emustafaj/Downloads/apache2/' + file) as f:
                    while True:
                        
                        x = dict()
                        line = f.readline()
                        mess = line[line.rfind(']') + 1:].strip()
                        
                        if not line:
                            break
                        if 'emustafaj' in line:    
                            time = re.findall(datereg,line)
                            if time == []:
                                continue
                            # dateTime = datetime.datetime.strptime(time[0], '%a %b %d %H:%M:%S.%f %Y').date()
                            # print(time)
                            clnt = re.findall(ipreg,line)
                            x['user'] = clnt[0]
                            if time != []:
                                dateTime = datetime.datetime.strptime(time[0], '%a %b %d %H:%M:%S.%f %Y').date()
                                x['time'] = dateTime
                            x['error'] = mess[:50]
                            
                            logs.append(x)
    




def getGraph(mess):
    getLogs(logs)
        
    logss = sorted(logs, key=lambda k: k['time'])

    temp = {}

    for i in logss:
        if temp.get(i['time']) == None:
            temp[i['time']] = 1
        else:
            temp[i['time']] += 1

    arr = list(temp.keys())
    arr.sort()

    freq = []
    for i in arr:
        freq.append(temp[i])

    arr2 = []

    for i in arr:
        arr2.append(str(i))
    plt.figure(figsize=(20,8))
    plt.ylim((0,50))
    plt.bar(arr2, freq)
    plt.xticks(rotation=90)
    plt.show()

data = []
getLogs(logs)
print(logs)
for i in logs[0:25]:
    data.append([i['user'], str( i['time']), i['error']])

fig, ax = plt.subplots()
fig.patch.set_visible(False)
ax.axis('off')
ax.axis('tight')
colLabels = ['user', 'time','error']
df = pd.DataFrame(data, columns=colLabels)

table = ax.table(
    cellText=df.values,
    colLabels=df.columns,
    cellLoc='center',
    loc='center'
)
table.set_fontsize(25)
#fig.tight_layout()
plt.savefig('errorstable.png',dpi = 600)