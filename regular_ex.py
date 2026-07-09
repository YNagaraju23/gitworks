import re
word="aaaaaabbbbbb cccccd12345678 #$%^#bbbbabbb"
word1="this is a string"
repeat=""
for i in word:
    if i not in repeat:
        repeat=repeat+i
print(repeat)
word2=re.search(r'ccd',word)
print(word2)
print(word2.start())
print(word2.end())

print(re.findall("c",word))
regex='\d+'
match=re.findall(regex,word)
print(match)

p=re.compile('\d+')
print(re.findall(p,word))
p=re.compile('ab*')
print(re.findall(p,word))

##############################
print("4***************************")
print(re.split(' ',word1))
print("5********************************")
print(re.subn('this','thus',word1))

word="this .is a. string"
word2=re.search(r"\.",word)
print(word2.start())
print(word2.end())
print("1****************")
word2=re.search(r"[h]",word)
print(word2.start())
print(word2.end())
print("2*********************")
result=re.findall(r"[a-z]",word)
print(result)
print("3*********************")
result=re.findall(r"^[a-z]",word)
print(result)
print("4 ends with doller$")
result=re.search(r'string$',word)
print(result.start())
print(result.end())
print("5 . means any character")
result=re.search(r'th.s',word)
print(result.start())
print(result.end())
print("6 | or means or operation a or b")
result=re.search(r'a|b',word)
print(result.start())
print(result.end())