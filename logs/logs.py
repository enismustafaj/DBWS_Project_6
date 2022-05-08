import re
import datetime
import matplotlib.pyplot as plt
import os
import lzma
import pandas as pd

logs = []

def getLogs(logs):

    parts = [
        r'(?P<host>\S+)',                   
        r'\S+',                             
        r'(?P<user>\S+)',                   
        r'\[(?P<time>.+)\]',                
        r'"(?P<request>.+)"',               
        r'(?P<status>[0-9]+)',              
        r'(?P<size>\S+)',                   
        r'"(?P<referer>.*)"',               
        r'"(?P<agent>.*)"',                 
    ]
    pattern = re.compile(r'\s+'.join(parts)+r'\s*\Z')
    files = os.listdir('/home/emustafaj/Downloads/apache2')

   
    for file in files:
       
        if 'access' in file:
            if file.endswith('.xz'):

                pass
            else:

                with open('/home/emustafaj/Downloads/apache2/' + file) as f:
                    while True:
                        line = f.readline()

                        if not line:
                            break
                        if 'emustafaj' in  line:
                            m = pattern.match(line)
                            res = m.groupdict()
                            logs.append(res)



def showgraph(arr,freq, lab):
    plt.figure(figsize=(20,8))
    plt.ylim((0,50))
    plt.bar(arr, freq, label = lab)
    plt.xticks(rotation=90)
    plt.legend()
    plt.show()



def getFrequency(page, datefreq, lab):
    ip = []
    date = []
    broswer = []
    logs = []
    getLogs(logs)
    #print(logs)

    for i in logs:
        dateTime = datetime.datetime.strptime(i['time'].split(' ')[0], '%d/%b/%Y:%H:%M:%S').date()
        i['time'] = dateTime

    logss = sorted(logs, key=lambda k: k['time']) 


    for i in logss:
        if page in  i['request'].split(' ')[1]:
            ip.append(i['host'])
            date.append(i['time'])
            temp =''
            if 'Firefox' in i['agent']:
                temp = 'Firefox'
            elif 'Chrome' in i['agent']:
                temp = 'Chrome'
            else:
                temp = 'Safari'
            broswer.append(temp)
    
    
    for i in date:
        if datefreq.get(i) == None:
            datefreq[i] = 1
        else:
            datefreq[i] += 1
    
    arr = list(datefreq.keys())
    arr.sort()
    freq = []
    arr2 = []
    for i in arr:
        freq.append(datefreq[i])
    for j in arr:
        arr2.append(str(j))

    showgraph(arr2,freq,lab)

# indexFreq = {}
# getFrequency('/~emustafaj/screens/admin/admin_login.html',indexFreq, 'Admin Page')

# searchFreq = {}
# getFrequency('/~emustafaj/screens/search/main_search.html',searchFreq, 'Search Page')

# homePage = {}
# getFrequency('/~emustafaj/index.html',homePage, 'Home Page')
# getLogs(logs)

# print(logs)
getLogs(logs)

data = []
for i in logs[0:25]:
    browser = ''
    if 'Firefox' in i['agent']:
        browser = 'Firefox'
    elif 'Chrome' in i['agent']:
        browser = 'Chrome'
    else:
        browser = 'Safari'
    data.append([i['host'], str(datetime.datetime.strptime(i['time'].split(' ')[0], '%d/%b/%Y:%H:%M:%S').date()), browser])

fig, ax = plt.subplots()
fig.patch.set_visible(False)
ax.axis('off')
ax.axis('tight')
colLabels = ['host', 'time','agent']
df = pd.DataFrame(data, columns=colLabels)

table = ax.table(
    cellText=df.values,
    colLabels=df.columns,
    cellLoc='center',
    loc='center'
)
table.set_fontsize(25)
#fig.tight_layout()
plt.savefig('SampledDataTable.png',dpi = 600)




