import lxml.etree

tree = lxml.etree.parse('capec.xml')
root = tree.getroot()

#Import list of field names into dictionary
frequencies = {}
with open("fields.txt") as fields:
    for line in fields:
        strippedline = line.strip()
        frequencies[strippedline] = 0

ns = "{http://capec.mitre.org/capec-2}"

#Count fields in XML
for keys, values in frequencies.items():
    
    key = ns + keys
    for _ in root[2].iter(key):
        frequencies[keys] += 1

import pandas as pd
from bokeh.plotting import figure, show

data = {}
data['Entries'] = frequencies

df_data = pd.DataFrame(data).sort_values(by='Entries', ascending=True)
series = df_data.loc[:,'Entries']

p = figure(width=800, y_range=series.index.tolist(), title="Attack Pattern Histogram")

p.xaxis.axis_label = 'Frequency'
p.xaxis.axis_label_text_font_size = '10pt'
p.xaxis.major_label_text_font_size = '8pt'

p.yaxis.axis_label = 'Field'
p.yaxis.axis_label_text_font_size = '10pt'
p.yaxis.major_label_text_font_size = '8pt'

j = 1
for k,v in series.iteritems():
  
  #Print fields, values, orders
  #print (k,v,j) 
  p.rect(x=v/2, y=j, width=abs(v), height=0.4,
    width_units="data", height_units="data")
  j += 1

show(p)