import check_package
check_package.check_package()
from spider_classes import *
from insirt_to_excel import *

print("This file can download all the course information from McGill's official website and automatically "
      "organize it into an excel table (under the directory of the file). Mode 1 can download all the courses, "
      "but I don't recommend you to do this, it will take a long time. Mode 2 can download the course with the "
      "specified number of pages and attach it to the form. " +
      "\n" +
      "When you want to end the program, please use keyboard interrupt as much as possible, otherwise the file "
      "may not be opened. At this time, please delete the excel file and run the program again " +
      "\n" +
      "Enjoy!")
while True:

    mode = input("select mode: 1 for cover mode, 2 for append mode,'exit()' to exit.:")
    if mode == "1":
        cover_all()
        get_all_courses()
        exit(0)
    elif mode == "2":
        start = input("which page do you want to start with?(input a number)")
        end = input("at which page do you want to stop?(input a number)")
        try:
            start = int(start)
            end = int(end)
        except:
            print("invalid input, cannot convert to int!")
            continue
        if start > end:
            print("your start is bigger than end!")
            continue
        elif start > 520:
            sure = input("now, mcgill only have 520 pages of courses, are you sure with your input?(y/n)")
            if sure == "y":
                pass
            elif sure == "n":
                continue
            else:
                print("invalid input!")
                continue

        get_all_courses(start - 1, end)
        exit(0)
    elif mode == 'exit()':
        print("bye")
        exit(0)
    else:
        print("invalid input!")
