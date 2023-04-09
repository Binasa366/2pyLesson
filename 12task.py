s=int(input("Введите сумму: "))
p=int(input("Введите произведение: "))
for x in range(s):
 for y in range(p):
  if s == x + y and p == x * y:
   print(f"Задуманные числа - {x} и {y}")