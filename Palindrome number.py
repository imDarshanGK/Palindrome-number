#Program to check palindrome number or not
n=int(input("Enter a number:"))
m=n
rev=0
while n!=0:
    ud=n%10
    rev=rev*10+ud
    n=n//10
print("reverse=",rev)
if m==rev:
    print("it is a Palindrome number")
else:
    print("it is not a Palindrome number")
