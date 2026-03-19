# break,  continue keywords
for i in range(1,6): # 0,1,2,3,4
    if i%2==0:
        continue
    print(i)


for i in range(20,51):
    if i%2!=0:
        continue
    print(i)    
    
name="krishna kumar singh"

for c in name:
    if c not in "aeiou":
        continue
    print(c)

name="rajesh"
count=0
for c in name:
    if c in "aeiou":
        count+=1

print("Total Number of Vowels:",count)



a=[15,56,67,40,68,35]

for i in a:
    if i%5==0:
        print(i)

# Prime Number 
n=12
isPrime=True
for i in range(2,n//2):
    if n%i==0:
        isPrime=False
        break

if isPrime:
    print(n," is  Prime Number")
else:    
    print(n," is not Prime Number")


# Count Number of Digit
n=7687687689798
temp=n
count=0

while temp>0:
    temp//=10
    count+=1

print("Number of Digit is:",count)

# Sum of Digit
n=5465
temp=n
sum=0

while temp>0:
    rem=temp%10
    temp//=10
    sum+=rem

print("Sum if Digit is:",sum)

# reverse digits
n=12345
temp=n
rev=0

while temp>0:
    rem=temp%10
    temp//=10
    rev=rev*10+rem

print("Reversed Value:",rev)    









