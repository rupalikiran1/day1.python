# three modes
#read,write,append

#creation a object
#f = open('myfile.txt','w')
#taking user input
#str = input('enter the name')
#writing to the file
#f.write(str)
#closing the filec
#f.close()

# program 2
#f = None
#try:
 #   fileName = input('enter the fileName')
  #  f = open(fileName,'r')
   # str = f.read()
    #print(str)
#except FileNotFoundError:
#    print("file not found")
#finally:
 #   if f is not None:
  #      f.close()
#print("bye")

# program 1
# read,write and append

# opening the file
#f = open("myfile2.txt",'w')
# taking input from the user
#name = input('Enter the name')
#writing to file
#f.write(name)
#closing
#f.close()

# program 2
#fileName = input('please enter the fileName')
#f = open(fileName,'r')
#str = f.read()
#print(str)
#f.close()

# program 3
#f = None
#try:
 #   fileName = input('enter the fileName')
  #  f = open(fileName,'r')
   # str = f.read()
    #print(str)
#except FileNotFoundError:
#    print("file not found")
#finally:
 #   if f is not None:
  #      f.close()

# program 4

f = open('myfile3.txt',"w")
while str != "@":
    str = input('Enter the name'+'\n')
    if str != '@':
        f.write(str + '\n')
        f.close()
        