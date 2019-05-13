import re
f = open("KEI.htm","r",encoding="latin1")
teks = f.read()
f.close()
cocok = r'([\w+]+)</a></td>\
<td>\d\.\d\d</td>\
<td>\d\.\d\d</td>\
<td>\d\.\d\d</td>\
<td>([\d.\d\d]+)'
output = re.findall(cocok,teks)
print(output)

