import re
s = "atlantic, express, avalanche, station "
print(s)
replaced = re.sub('e[^e]{3}ess', 'REMOVED', s)
print (replaced)
