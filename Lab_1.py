print("Вводить время ЧИСЛАМИ в формате [ЧАСЫ] [МИНУТЫ]")

TimeInList = input().split()
if len(TimeInList) != 2:
    print("Не корректное количество аргументов.")
    exit()

Hours = int(TimeInList[0])
Minute = int(TimeInList[1])


def IsCorrect(InHours, InMinute):
    if InHours > 23 or InHours < 0 or TimeInList[0] == "-0":
        print("Введены недопустимые данные: часы должны быть от 0 до 23.")
        return False
    if InMinute > 59 or InMinute < 0:
        print("Введены недопустимые данные: минуты должны быть от 0 до 59.")
        return False
    return True


def IsExept(InHours, InMinute):
    if InHours == 00 and InMinute == 00:
        return "полночь"
    if InHours == 12 and InMinute == 00:
        return "полдень"
    return False


def TextHours(InHours):
    FinalTextHours = 0
    if InHours == 0:
        FinalTextHours = "часов"
    if InHours == 1:
        FinalTextHours = "час"
    if 1 < InHours < 5:
        FinalTextHours = "часа"
    if 4 < InHours < 21:
        FinalTextHours = "часов"
    if InHours == 21:
        FinalTextHours = "час"
    if 22 < InHours < 24:
        FinalTextHours = "часа"

    return str(InHours) + ' ' + FinalTextHours


def TextMinute(InMinute):
    FinalTextMinute = 0
    if InMinute == 0:
        return ""

    match InMinute:

        case 1:
            FinalTextMinute = "минута"
        case 21:
            FinalTextMinute = "минута"
        case 31:
            FinalTextMinute = "минута"
        case 41:
            FinalTextMinute = "минута"
        case 51:
            FinalTextMinute = "минута"

        case 2:
            FinalTextMinute = "минуты"
        case 22:
            FinalTextMinute = "минуты"
        case 32:
            FinalTextMinute = "минуты"
        case 42:
            FinalTextMinute = "минуты"
        case 52:
            FinalTextMinute = "минуты"

        case 3:
            FinalTextMinute = "минуты"
        case 23:
            FinalTextMinute = "минуты"
        case 33:
            FinalTextMinute = "минуты"
        case 43:
            FinalTextMinute = "минуты"
        case 53:
            FinalTextMinute = "минуты"

        case 4:
            FinalTextMinute = "минуты"
        case 24:
            FinalTextMinute = "минуты"
        case 34:
            FinalTextMinute = "минуты"
        case 44:
            FinalTextMinute = "минуты"
        case 54:
            FinalTextMinute = "минуты"

        case _:
            FinalTextMinute = "минут"
    return ' ' + str(InMinute) + ' ' + FinalTextMinute


def TextDay(InHours):
    if 0 <= InHours < 6:
        return "ночи"
    if 6 <= InHours < 12:
        return "утра"
    if 12 <= InHours < 18:
        return "дня"
    if 18 <= InHours < 24:
        return "вечера"


def TextMinute00(InMinute):
    if InMinute == 0:
        return "ровно"
    else:
        return ""


def main():
    if IsCorrect(Hours, Minute):
        if IsExept(Hours, Minute):
            print(IsExept(Hours, Minute))
        else:
            print(TextHours(Hours) + TextMinute(Minute) + " " + TextDay(Hours) + " " + TextMinute00(Minute))


if __name__ == "__main__":
    main()
