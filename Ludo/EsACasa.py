'''
Write a script that accepts three integer numbers:

check that the numbers are different;
determine whether the numbers are perfect numbers (the sum of the divisors is equal to the number itself);
add the perfect numbers together.
'''
def num_check(num1,num2,num3):
    if num1 != num2 and num1 != num3 and num3!=num2:
        return True
    else:
        return False 

def somma_perfetta(num1,num2,num3):
    a=0
    if perfetto(num1):
        a+=num1
    if perfetto(num2):
        a+=num2
    if perfetto(num3):
        a+=num3
    return a    

def perfetto(num):
    somma=0
    for i in range(1,num):
        if num%i==0:
            somma+=i
    if somma==num:
        return True
    else:
        return False 










check = False
num1=0
num2=0
num3=0
while check == False: 
    num1 = int(input("Inserisci il primo numero: "))
    num2 = int(input("Inserisci il secondo numero: "))
    num3 = int(input("Inserisci il terzo numero: "))
    check = num_check(num1,num2,num3)
print(somma_perfetta(num1,num2,num3))


