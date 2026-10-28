#İstifadəçi bir ədəd yazır. Ədəd 3-ə bölünürsə “Fizz”, 
# 5-ə bölünürsə “Buzz”, hər ikisinə bölünürsə “FizzBuzz”, heç birinə bölünmürsə ədədin özü çap olunur.



eded = int(input("Bir ədəd daxil din: "))
if (eded % 5 == 0 and eded % 3 == 0):
    print("FizzBuzz")
elif (eded % 5 == 0):
    print("Buzz")
elif (eded % 3 == 0):
    print("Fizz")        
else :
    print(eded)
        