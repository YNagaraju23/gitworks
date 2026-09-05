word="aaaaabbbbbbbccccccccdddde"
repeat = ""
for i in word:
  if i not in repeat:
      repeat =repeat+i
print(repeat)