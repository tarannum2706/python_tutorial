
# program to check the word is anagram or not
# An anagram is a word or phrase formed by rearranging the letters in another word or phrase.

def anagram(str1,str2):
  string1=''.join(sorted(str1,key=str.lower)).strip().lower()
#   print(string1)
  string2=''.join(sorted(str2,key=str.lower)).strip().lower()
#   print(string2)
  if string1 == string2:
        return True
  else:
        return False
    
print(anagram("Hello","elloo"))
print(anagram("nag a ram","anagram"))
print(anagram("George Bush","He bugs Gore"))
print(anagram("signature ","a true Sign"))

              