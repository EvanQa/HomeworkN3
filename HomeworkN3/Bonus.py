#1
month_num: int = int(input("Enter number between 1-12 :"))

# if month_num == 1:
#     print("January")
# elif month_num == 2:
#     print("February")
# elif month_num == 3:
#     print("March")
# elif month_num == 4:
#     print("April")
# elif month_num == 5:
#     print("May")
# elif month_num == 6:
#     print("June")
# elif month_num == 7:
#     print("July")
# elif month_num == 8:
#     print("August")
# elif month_num == 9:
#     print("September")
# elif month_num == 10:
#     print("October")
# elif month_num == 11:
#     print("November")
# elif month_num == 12:
#     print("December")
# else:
#     print("not in range")

#2

match month_num:
    case 1:
        print("January")
    case 2:
        print("February")
    case 3:
        print("March")
    case 4:
        print("April")
    case 5:
        print("May")
    case 6:
        print("June")
    case 7:
        print("July")
    case 8:
        print("August")
    case 9:
        print("September")
    case 10:
        print("October")
    case 11:
        print("November")
    case 12:
        print("December")
    case _:
        print("not in range ")