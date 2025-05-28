file1=open("myfile.txt","w")
l=["This is Nepal\n","This is Paris \n","This is londan"]
file1.writelines(l)
file1.close()

#Append-adds at last
#Append-adds at last
file1=open("myfile.txt","a")
file1.write("\n")
file1.write("Today")
file1.write("Tomorrow")
file1.close()

file1=open("myfile.txt","r")
print("output of Readlines after appending")
print(file1.read())
print()
file1.close()

#write-overwrites
file1=open("myfile.txt","w")
file1.write("Tomorrow \n")
file1.close()

file1.open("myfile.txt","r")
print("output of readlines after writing")
print(file1.read())
print()
file1.close()