import re
f = open("Indonesia.txt","r",encoding="latin1")
teks = f.read()
f.close()
cocok = r'di\w+'
output = re.findall(cocok,teks)
print(output)
