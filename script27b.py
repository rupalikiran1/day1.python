#reclen = 20
#with open('cities.bin','wb') as f:
   # n = int(input('Enter the number of cities'))
    #for x in range(n):
     #   city = input('enter the city')
     #   city = city + (reclen - len(city))*""
      #  city = city.encode()
       # f.write(city)

     # program 2
reclen = 20
with open('cities.bin','wb') as f:
        n = int(input('record number'))
        f.seek(reclen * (n-1))
        str = f.read(reclen)
        str = str.decode()
        print(str)
       