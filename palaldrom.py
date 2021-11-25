#WAPP TO CHECK  IF A GIVEN STRING IS PALINDROME OR NOT 

str1=input('enter any string')

if str1== str1[-1:-(len(str1)+1):-1]:
   print('string is palindrom')
else:
   print('string is not palindrom')


num=int(input("enter any number"))
temp=num
res=0
while num>0:
   r=num%10
   res=res*10+r
   num=num//10
if temp ==res:
   print('num is palindrom')
else:
   print('num is not palindrome')
