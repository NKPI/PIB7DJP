f = open('Test.txt', 'r')

print(f.read(10))
print(f.readline())
print(f.readline())
print(f.readlines())

print(f.name)
print(f.mode)
print(f.readable())
print(f.writable())
print(f.closed)

f.close()
print(f.closed)


fw = open("time.txt", 'w')

fw.write("We all behave like we have all the time in the world \n")
fw.write("Untill one day when we realize we have very little left\n")

l = ["Today is 2oth Nov\n", "There is nothing special about today\n", "If you want you can make it special for you\n"]

fw.writelines(l)

fw.close()

fa = open("students.csv", 'a' )

std=["Balaji", "Karthik", "small Spoorthi", "Big Spoorthi", "Satisha", "Sumantha", "Pavan"]

for i in std:
    str = i+ " just looking like a Wow!\n"
    fa.write(str)

fa = open("students.csv", 'r+' )
print(fa.tell())
fa.seek(24)
print(fa.tell())
fa.write("double wow!")


fw = open("time.txt", 'w')
fw.seek(24)
print(fa.tell())
fw.write("double")


fb = open("goldleaf.jpg", 'rb')
print(fb.readline())

import os
print(os.getcwd())

#os.mkdir("lookingwow/newdir")

#os.chdir("lookingwow")
# print(os.getcwd())
# os.chdir(r"C:\Users\nirio\PI_B7_Proj1")
#os.removedirs(r"lookingwow\newdir")

from zipfile import *
fz = ZipFile('wow.zip','w',ZIP_DEFLATED)
print(type(fz))

fz.write('Test.txt')
fz.write('time.txt')

print(fz.namelist())
f1 = open('Test.txt','r')
print(f1.read())




import pickle

class Sidi:
    def __init__(self, name,age,interest,school ):
        self.name= name
        self.age = age
        self.interest = interest
        self.school = school

    def display(self):
        print("self.name", '\n', self.age, '\n', self.interest, '\n', self.school)


Sid = Sidi('Sidharth Niranjan', 13, 'Lego', 'Pramiti')

print(Sid)
f = open("SidiText.dat", 'wb')
pickle.dump(Sid, f)

f.close()
fo = open("SidiText.dat", 'rb')

obj1=pickle.load(fo)

print(type(obj1))

obj1.display()