# Задание 6
# Создайте словарь, в котором ключом будет являться число от 1 до 27,
# а значением - буквы английского алфавита.
# Решите эту задачу с помощью генератора словаря
Holidays = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
June = {Summer : Winter for Summer,Winter in zip(range(1,27), Holidays)}
print(June)