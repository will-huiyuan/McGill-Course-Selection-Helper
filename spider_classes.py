from insirt_to_excel import *
from bs4 import BeautifulSoup as BS
import requests
import re
from rewrite_mcgill_class import Course
from sys import stdout as s_s


def get_course_info(info_page_url):
    """
    :param info_page_url: str
    :during set up course class for each course
    :return an object of <course>
    """
    file = requests.get(info_page_url)
    soup = BS(file.text, "lxml")
    # deal with title
    title_block = soup.find_all(id="page-title")
    title = title_block[0].string.strip()
    title = title.strip(")").split("(")
    if len(title) > 1:
        credit = title[-1].strip().split(" ")[0]
        try:
            credit = float(credit)
        except:
            print("Error! Could not convert to float! credit is:", credit)
            credit = None
    else:
        credit = None
    course = title[0].strip().split()
    name = " ".join(course[0:2])
    description = " ".join(course[2:])
    # deal with main block
    main_block = soup.find(id="block-system-main")
    a_lists = main_block.select('p')
    info_len = len(a_lists)
    # deal with offered by
    # initialize info
    info = []
    offer_by, faculty, specific_description, terms, instructors, time = ["None", "None", "None", "None", "None", "None"]
    pointer = 0
    if info_len > pointer:
        offer = a_lists[pointer].text.strip().strip(")").split("(")
        offer_by = offer[0].split(":")[1].strip()
        pointer += 1

        faculty = offer[1]
        specific_description = a_lists[pointer].text.strip()
        if re.match("^Administered by", specific_description):
            faculty = faculty + " " + specific_description
            pointer += 1
            specific_description = a_lists[pointer].text.strip()
        pointer += 1
    if info_len > pointer:
        terms = a_lists[pointer].text.split(":")[1].strip().split(",")
        pointer += 1
    if info_len > pointer:
        instructors = a_lists[pointer].text.split(":")[1].strip().split(";")
        pointer += 1

    if info_len > pointer:
        info_raw = a_lists[pointer:]
        for i in info_raw:
            if re.match("\d hour", i.text):
                time = i.text.strip()
            else:
                info.append(i.text.strip())
    course_dict = {"name": name, "description": description, "credit": credit,
                   "offer_by": offer_by, "faculty": faculty,
                   "specific_description": specific_description,
                   "terms": terms, "instructors": instructors,
                   "time": time, "info": info, "course_url": info_page_url}

    return Course(course_dict)


def get_courses(list_page_url, page=0):
    """
    :param page: int, temp use for test
    :param list_page_url: str
    :return: list of <course>
    :during use get_course_info to set up course class for each course
    """
    course_list = []

    if list_page_url is not None:
        url = list_page_url
    else:
        url = f"https://www.mcgill.ca/study/2022-2023/courses/search?page={page}"
    response = requests.get(url)
    print(url)
    # initialize BS
    soup = BS(response.text, "lxml")
    courses_block = soup.find_all(class_=f"views-row")
    for i, courses in enumerate(courses_block):
        web_link = (courses.find("a")["href"])
        web_link = "https://www.mcgill.ca" + web_link
        # todo 可以添加一个内容识别，看看外部内容是否和内部的内容一样
        course_list.append((get_course_info(web_link)))
        print("\r", "●" * (i + 1), "o" * (len(courses_block) - i - 1), sep="", end="")
        s_s.flush()
        print("")
    return course_list


def get_all_courses(start_page=0, end_page=9999):
    """

    :return: a list of <courses>
    """
    full_course_list = []
    recent_page = start_page
    while True:
        url = f"https://www.mcgill.ca/study/2022-2023/courses/search?page={recent_page}"
        response = requests.get(url)
        # initialize BS
        soup = BS(response.text, "lxml")
        recent_page += 1
        class_block = soup.find_all(class_=f"views-row")
        print("page:", recent_page)
        if recent_page == end_page or class_block == []:
            break
        for course_ in get_courses(url):
            full_course_list.append(course_)
            append(course_)
    print(f"The traversal is complete. {recent_page - 1} pages have been traversed")
    return full_course_list


if __name__ == "__main__":
    os.popen('mshta vbscript:msgbox("open main.py, not this one!",,"wrong file")(window.close)')
