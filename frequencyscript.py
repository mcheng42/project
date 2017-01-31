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

#Sort counted fields in descending order
import operator
sorted_frequencies = sorted(frequencies.items(), key=operator.itemgetter(1), reverse=True)

#Output as text file
#==============================================================================
# f = open('sortedfrequencies.txt','w')
# for t in sorted_frequencies:
#     line = ' ' . join(str(x) for x in t)
#     f.write(line + '\n')
# f.close()
#==============================================================================

#Separate data 
keys,values = zip(*sorted_frequencies)
df = {"Fields": keys, "values": values}

#Output frequency bar chart
from bokeh.charts import Bar, output_file, show
from bokeh.charts.attributes import CatAttr
p = Bar(df, values="values",label=CatAttr(columns=['Fields'],sort=False),title="Attack Pattern Field Frequency",legend=False)
show(p)


