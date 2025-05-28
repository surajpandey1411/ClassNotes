l=["This is Delhi \n", "This is Paris \n","This is londan \n"]

# writing to file
with open("myfile.txt","w") as file1:
    #writing data to a file
    file1.write("Hello \n")
    file1.writelines(l)

    #Appending to file
    with open("myfile.txt","a") as file:
        file.write("Today")

        #Reading from file
        with open("myfile.txt","r+") as file1:
            #reading from a file
            print(file1.read())