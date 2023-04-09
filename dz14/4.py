# Задание 4
# Напишите функцию итератор, которая будет перебирать список чисел Фибоначчи из предыдущего задания.
# Опустошите итератор двумя способами.
# Если вы не сделали предыдущее задание, воспользуйтесь списком: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
def fibonacci ():
  f = 0
  f1 = f2 = 1
  print(f,f1, f2, end=" ")
  for inna  in range(8):
    f1, f2 = f2, f1 + f2
    yield f2

LOL=fibonacci()
spisok =list(LOL)
lala= iter (spisok)
# for Kazan in lala:#С ПОМОЩЬЮ ЦИКЛА
#     print (Kazan,end=" ")

# popo= 0#С ПОМОЩЬЮ WHILE
# while popo <8:
#    print (next (lala), end = " " )
#    popo+=1
