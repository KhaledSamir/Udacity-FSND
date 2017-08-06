import urllib

__mypath__ = '/Users/khaled/Desktop/Udacity/Lesson4/Myfile.txt'


def detect():
    txtfile = open(__mypath__, 'r')
    lines = txtfile.readlines()
    for line in lines:
        print check_BadWords(line)
    txtfile.close()


def check_BadWords(textToCheck):
    url = "http://www.purgomalum.com/service/containsprofanity?text=" + textToCheck
    connection = urllib.urlopen(url)
    result = connection.read()
    return result


detect()
