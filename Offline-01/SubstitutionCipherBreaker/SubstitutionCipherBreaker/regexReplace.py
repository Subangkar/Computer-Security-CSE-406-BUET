import re
s = "atlantic, express, avalanche, station etHeaXalancHeKHentHet eUOEeWWa"
print(s)
print((re.compile(r'e[A-Z]{3}e([A-Z])\1')))
replaced = re.sub(re.compile(r'e[A-Z]{3}e([A-Z])\1'), 'REMOVED', s)
print (replaced)
