# Задание 2
# Напишите функцию-генератор, которая выдает буквы английского алфавита от a до z.
# Опустошите генератор любым способом

def Zenit ():
   spisok = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
   for i in spisok:
      yield i
aboba=Zenit()
i = 0
while i<26 :
    print (next (aboba))
    i+=1


