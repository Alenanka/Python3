duration_in_sec = input("Введите количество секунд:")
if duration_in_sec.isdigit():
    duration_in_sec = int(duration_in_sec)
    if duration_in_sec < 60:
        print(duration_in_sec, "секунд")
    if 60 <= duration_in_sec < 3600:
        print(duration_in_sec // 60, "минут",
              duration_in_sec % 60, "секунд")
    if 3600 <= duration_in_sec < 86400:
        print(duration_in_sec // 3600, "часов,",
              duration_in_sec % 3600 // 60, "минут,",
              duration_in_sec % 60, "секунд")
    if duration_in_sec >= 86400:
        print(duration_in_sec // 86400, "дней,",
              duration_in_sec % 86400 // 3600, "часов,",
              duration_in_sec % 3600 // 60, "минут,",
              duration_in_sec % 60, "секунд")
else:
    print("Введено не число")