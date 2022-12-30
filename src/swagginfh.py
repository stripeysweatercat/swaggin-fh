from byteconvert import bn2c, c2bn
from byteconvert.hexconvertion import str2ba, ba2str

def reads(filename):
    try:
        f = open(filename, "rb")
    except:
        f = open(f"{filename}.swaggin", "rb")
    temp = ba2str(f.read())
    f.close()
    return temp

def readbs(filename):
    try:
        f = open(filename, "rb")
    except:
        f = open(f"{filename}.swaggin", "rb")
    temp = []
    for i in f.read():
        temp.append(i)
    f.close()
    return temp

def writes(filename, content):
    f = open(f"{filename}.swaggin", "wb")
    f.write(bytearray(str2ba(content)))
    f.close()

def writebs(filename, arr):
    f = open(f"{filename}.swaggin", "wb")
    f.write(bytearray(arr))
    f.close()

def appends(filename, content):
    f = open(f"{filename}.swaggin", "ab")
    f.write(bytearray(str2ba(content)))
    f.close()

def appendbs(filename, arr):
    f = open(f"{filename}.swaggin", "ab")
    f.write(bytearray(arr))
    f.close()

def heads(filename, content):
    f2 = readbs(f"{filename}")
    bytearrtemp = []
    for x in str2ba(content):
        bytearrtemp.append(x)
    for i in f2:
        bytearrtemp.append(i)
    f = open(f"{filename}.swaggin", "wb")
    f.write(bytearray(bytearrtemp))
    f.close()