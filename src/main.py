def reverse(num):
  list=""
  while num>=10:
    b=num%10
    num=num//10
    list=list+str(b)
  if num<=9:
    list=list+str(num) 
  return int(list)

no=int(input("enter number:"))

a=reverse(no)
print(a)

