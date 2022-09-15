# 5. Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.


from fileinput import close

poly_f = open("HW2\poly_1.txt")
f = (poly_f.readline())
f = f.replace(" = 0", "")
# print(f)
poly_f.close()

poly_s = open("HW2\poly_2.txt")
s = poly_s.readline()
s = s.replace(" = 0", "")
# s = s[:len(s) - 4]
# print(s)
poly_s.close()

u = s + " + " + f + " = 0"
print(u)

with open('poly_sum.txt', 'w') as file:
    file.writelines(u)
    file.close()