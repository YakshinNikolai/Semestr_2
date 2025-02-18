a = input()
b = input()
def first_last(letter, st):
     fc=0
     mayfc=1
     lc=0
     for i in range(len(st)):
         if letter in st[i]:
             if mayfc==1:
                 fc=i 
                 mayfc=0
             lc=i
     return (fc, lc)
print(first_last(a,b))
