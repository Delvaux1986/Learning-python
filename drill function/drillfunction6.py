def final_grade(exam, projects):
    if(exam >= 90 or projects >= 10):
        print('GG tu as eu 100%')
    elif(exam >= 75 and projects >= 5):
        print('GG tu as eu 90%')
    elif(exam >= 50 and projects >=2):
        print('Bofff tu as eu 75% pas ouf')
    else:
        print('000000000')

final_grade(100, 12)
final_grade(85, 5)