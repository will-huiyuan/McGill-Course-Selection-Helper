import os
class Course:
    """

    """
    longest_info_length = 0
    # todo add more variables like prerequest or corequest

    def __init__(self, course_dict):
        """
        :param course_dict: 要求至少有课程名称，terms，offered by,url
        """
        check_tup = ("name", "terms", "offer_by", "course_url")
        for i in check_tup:
            if i not in course_dict:
                print("wrong dict!", i)
                self.status = "invalid"
                break

        self.name = course_dict["name"]
        self.description = course_dict["description"]
        self.credit = course_dict["credit"]
        self.offer_by = course_dict["offer_by"]
        self.faculty = course_dict["faculty"]
        self.specific_description = course_dict["specific_description"]
        self.terms = course_dict["terms"]
        self.instructors = course_dict["instructors"]
        self.time = course_dict["time"]
        self.info = course_dict["info"]
        self.course_url = course_dict["course_url"]

        self.check_longest_info_length(len(course_dict["info"]))

    @classmethod
    def check_longest_info_length(cls, num):
        if num > cls.longest_info_length:
            cls.longest_info_length = num

if __name__ == "__main__":
    os.popen('mshta vbscript:msgbox("open main.py, not this one!",,"wrong file")(window.close)')
