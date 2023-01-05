def check_package():
    try:
        import bs4
    except:
        print("do not have package 'bs4',use 'pip install beautifulsoup4' to install it!")
    try:
        import os
    except:
        print("do not have package 'os',cannot find package of os, check your python!")
    try:
        import requests
    except:
        print("do not have package 'requests',cannot find package of requests, check your python!")
    try:
        import re
    except:
        print("do not have package 're',cannot find package of re, check your python!")
    try:
        from sys import stdout
    except:
        print("do not have package 'sys',cannot find, check your python!")
    try:
        import rewrite_mcgill_class
    except:
        print("cannot find file 'rewrite_mcgill_class', please download the zip again")
    try:
        import spider_classes
    except:
        print("cannot find file 'spider_classes', please download the zip again")
    try:
        import insirt_to_excel
    except:
        print("cannot find file 'insirt_to_excel', please download the zip again")

