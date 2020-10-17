import requests
import json
import numpy as np
import pandas as pd

url = 'https://raw.githubusercontent.com/pomber/covid19/master/docs/timeseries.json'
reponse = requests.get(url)
dati = json.loads(reponse.content)

nation = "Italy"
da = "01/02/2020"
a = "29/02/2020"

one = []  
two = []
tre = []
for info in dati[nation]:
  one.append(info["recovered"])
  two.append(info["confirmed"])
  tre.append(info["deaths"])


atp = np.array([one, two, tre])
arr = atp.reshape(269, 3)
dates = pd.date_range('20200122', periods = len(two))

#df = pd.DataFrame(data = arr, index = dates)
df = pd.DataFrame(data = arr, index = dates, columns = list("ABC"))
print(df)



