#1                                          elif way

grade: int = int(input("enter your grade"))

# if grade >= 0 and grade <= 40:
#     print("try harder next time...")
# elif grade >=41 and grade <=60:
#     print("you're getting there, need some more work")
# elif grade >=61 and grade <=80:
#     print("pretty good")
# elif grade >=81 and grade <=95:
#     print("awesome!")
# elif grade >=96 and grade <=100:
#     print("excellent!!!You're a Star!")
# else:
#     print("illegal grade")
#2                                            match_case way

match grade:
    case 0:
        print("try harder next time... ")
    case 0:
        print("try harder next time...")
    case 1 | 2 | 3:
        print("try harder next time...")
    case _ if  4 <= grade <=  40:
        print("try harder next time...")
    case _ if 41 <= grade <= 60:
        print("you're getting there, need some more work")
    case _ if 61 <= grade <= 80:
        print("pretty good")
    case _ if 81 <= grade <= 95:
        print("awesome!")
    case _ if 96 <= grade <= 100:
        print("excellent!!!You're a Star!")
    case _:
        print("illegal grade")


