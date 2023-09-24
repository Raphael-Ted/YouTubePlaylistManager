from googleapiclient.discovery import build
import re

def print_dict(dic):
    for i in dic.keys():
        print(i + ': ' + str(dic[i]))

