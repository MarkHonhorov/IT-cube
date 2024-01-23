def qwerty():
password1 = input("Введите пароль: ")
password2 = input("Повторите пароль: ")

if password1 == password2:
print("Доступ разрешен")
else:
print("Пароли не совпадают. Доступ запрещен")

if __name__ == "__qwerty__":
qwerty()