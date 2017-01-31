import lxml.etree
tree = lxml.etree.parse('capec.xml')
root = tree.getroot()

frequencies = {}
with open("fields.txt") as fields:
    for line in fields:
        strippedline = line.strip()
        frequencies[strippedline] = 0

ns = "{http://capec.mitre.org/capec-2}"

for keys, values in frequencies.items():
    
    key = ns + keys
    for _ in root[2].iter(key):
        frequencies[keys] += 1

#==============================================================================
# for keys,values in frequencies.items():
#     print(values)    
#==============================================================================

import operator
sorted_frequencies = sorted(frequencies.items(), key=operator.itemgetter(1), reverse=True)


#==============================================================================
# f = open('sortedfrequencies.txt','w')
# for t in sorted_frequencies:
#     line = ' ' . join(str(x) for x in t)
#     f.write(line + '\n')
# f.close()
#==============================================================================

keys,values = zip(*sorted_frequencies)

df = {"Fields": keys, "values": values}


from bokeh.charts import Bar, output_file, show, hplot
from bokeh.charts.attributes import ColorAttr, CatAttr
from bokeh.charts.builders.bar_builder import BarBuilder

p = Bar(df, values="values",label="Fields",title="Attack Pattern Field Frequency",sort=False,legend=False)
output_file("frequencies.html")
show(p)


