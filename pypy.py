TimeInList = input().split()
Chasi = int(TimeInList[1])
Minuti = int(TimeInList[2])
SlovoForResultHours=0

def hours():
    global SlovoForResultHours
    if Chasi == 1:
        SlovoForResultHours = "час"

    if 1 < Chasi < 5:
        SlovoForResultHours = "часа"

    if 4 < Chasi < 12:
        SlovoForResultHours = "часа"
    return SlovoForResultHours

def minut():
    global SlovoForResultHours
    if Minuti == 1:
        SlovoForResultHours = "минута"

    if 1 < Minuti < 5:
        SlovoForResultHours = "минут"

    if 4 < Minuti < 12:
        SlovoForResultHours = "минуты"
    return SlovoForResultHours


if Chasi and Minuti == 00:
    print("полночь")
elif Chasi == 12 and Minuti == 00:
    print("полдень")
elif Chasi > 23:
    print("Введены недопустимые данные: часы должны быть от 0 до 23.")
elif Chasi == 12 and Minuti == 00:
    print("Введены недопустимые данные: минуты должны быть от 0 до 59.")
