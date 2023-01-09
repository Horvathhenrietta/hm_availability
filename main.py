from availabilityChecker.checker import AvailabilityChecker as AC
from notificationSender.send import  notify_available

def menu():
    size = input('The size you are searching for: ')
    article_num = input("The number of the article: ")

    check = AC(article_num, size)
    if check.availability:
        notify_available(article_num, size)



# 1044156002, 38

menu()
