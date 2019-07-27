"""
Created on Mon Mar 25 21:42:17 2019

@author: Sakib
"""
f = open("test.txt", "r")
o = open("test_formatted.csv", "a")


while True:
    first=f.readline()
    if first == '':
        break
    second=f.readline()
    third=f.readline()
    out=second.rstrip()+","+third
    #print(out)
    o.write(out)
   

f.close()
o.close()
print("Done!")
