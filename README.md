# McGill-Course-Selection-Helper 麦吉尔选课助手
  ## package requirement
   this program uses third-party package: `beautifulsoup4` `openpyxl` `requests` `lxml` ,please use commands listed below to install them.
   
   `pip install requests`
   
   `pip install openpyxl`
   
   `pip install beautifulsoup4`
   
   `pip install lxml`
  ## brief intro
  This file can download all the course information from McGill's official website and automatically organize it into an excel table (under the directory of the file). Mode 1 can download all the courses, but I don't recommend you to do this, it will take a long time. Mode 2 can download the course with the specified number of pages and attach it to the form. 

When you want to end the program, please use keyboard interrupt as much as possible, otherwise the file may not be opened. At this time, please delete the excel file and run the program again 

  ## system notice.
  This file is written for windows system (because of the use of bat), if you want to run it on mac, please delete the statement at the bottom of each file: `if __name__ == "__main__":
  os.popen('mshta vbscript:msgbox("open main.py, not this one!",,"wrong file")(window.close)')`
  

  ## 第三方库要求
  程序使用了`beautifulsoup4` `openpyxl` `requests` `lxml` 第三方库，请用下列代码安装
   
   `pip install requests`
   
   `pip install openpyxl`
   
   `pip install beautifulsoup4`
   
   `pip install lxml`
  
  ## 简介
本文件可以从麦吉尔官网下载所有课程信息，并自动整理成excel表格（在文件目录下）。 Mode 1可以下载所有的课程，但是不建议这样做，耗时很长。 Mode 2可以下载指定页数的课程，并附加在已有表格内容之下。
   当要结束程序时，请尽量使用 keyboard interrupt，否则可能导致文件损坏。此时请删除excel文件，重新运行程序。

  ##运行系统
  该文件是为windows系统写的（因为加了bat的使用），若要在mac上运行，请删除每个文件最下面的语句：`if __name__ == "__main__":
  os.popen('mshta vbscript:msgbox("open main.py, not this one!",,"wrong file")(window.close)')`
  
