str1 = 'Ann'
str2 = 'Alex'
int1 = 3
int2 = 4
int3 = 5
int4 = 7
flo1 = 2.5
flo2 = 3.5
flo3 = 4.5
res1 = int1 > int2
print(res1)
res2 = int1 < int2
print(res2)
res3 = int1 <= int2
print(res3)
res4 = int1 >= int2
print(res4)
res5 = int1 != int2
print(res5)
res6 = int1 < int3
print(res6)
res7 = int1 > int3
print(res7)
res8 = int1 >= int3
print(res8)
res9 = int1 <= int3
print(res9)
res10 = int1 != int3
print(res10)
res11 = int1 < int4
print(res11)
res12 = int1 > int4
print(res12)
res13 = int1 >= int4
print(res13)
res14 = int1 <= int4
print(res14)
res15 = int1 != int4
print(res15)
res16 = flo1 > flo2
print(res16)
res17 = flo1 < flo2
print(res17)
res18 = flo1 <= flo2
print(res18)
res19 = flo1 >= flo2
print(res19)
res20 = flo1 != flo2
print(res20)
res21 = flo1 < flo3
print(res21)
res22 = flo1 > flo3
print(res22)
res23 = flo1 >= flo3
print(res23)
res24 = flo1 <= flo3
print(res24)
res25 = flo1 != flo3
print(res24)
res26 = flo2 != flo3
print(res26)
res27 = flo2 < flo3
print(res27)
res28 = flo2 > flo3
print(res28)
res29 = int1 > int2 and int2 < int3
print(res29)
res30 = int1 <= int2 and int2 < int3
print(res30)
res31 = int1 <= int2 and int2 != int3
print(res31)
res32 = int1 <= int2 or int2 != int3
print(res32)
res33 = int1 > int2 or int2 > int3
print(res33)
res34 = int1 >= int2 or int2 > int3
print(res34)
res35 = not int1 >= int2
print(res35)
res36 = int1 > int2 or int2 < int3
print(res36)
res37 = int3 > int2 or int2 <= int1
print(res37)
res38 = int3 > int2 and int2 <= int1
print(res38)

# Задание №7
name = int(input("Vvedite tseloye chislo"))
if name < 30:
    print('Your number =', name, '< 30')
elif name == 30:
    print('Your number=', name, '= 30')
else:
    print('Your number=', name, '> 30')

# Задание №8
name1 = int(input("Vvedite tseloye chislo"))
import random
rand = random.randint(1,100)
if name1 > rand:
    print('Your number=', name1, '>', rand)
elif name1 == rand:
    print('Your number=', name1, '=', rand)
else:
    print('Your number=', name1, '<', rand)

# Задание №9
name2 = int(input("Vvedite tseloye chislo"))
rand1 = random.randint(1,100)
rand2 = random.randint(1,100)
if name2 > rand1 and name2 > rand2:
    print('Your number=', name2, '>', rand1, ', ', rand2)
elif name2 == rand1 and rand2:
    print('Your number=', name2, '=', rand1, ', ', rand2)
elif name2 > rand1 and name2 < rand2:
    print('Your number=', name2, '>', rand1, 'and < ', rand2)
elif name2 < rand1 and name2 > rand2:
    print('Your number=', name2, '< rand1, and > ', rand2)
else:
    print('Your number=', name2, '<', rand1, ', ', rand2)


























