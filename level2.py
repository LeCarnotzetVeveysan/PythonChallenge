str = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
newstr= ""

url = "http://www.pythonchallenge.com/pc/def/map"

for x in url:
  num = ord(x)
  if (num >= 97) and (num <= 122):
    num += 2
    if(num > 122):
      num -= 26
    newstr += chr(num)
  else:
    newstr += x
print(newstr)