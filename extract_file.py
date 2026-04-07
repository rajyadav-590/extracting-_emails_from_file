#importing re module.
import re
#opening sample.txt file in rt mode for redinng the content ofthe file.
with open("sample.txt","rt") as fh:
    #reading the content of file.
    file_read = fh.read()
#making pattern to recognize in the sample.txt file.
pattern = r"\b[a-zA-Z][a-zA-Z0-9._-]*@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}\b"
a = re.findall(pattern,file_read)
print(a)
print(len(a))