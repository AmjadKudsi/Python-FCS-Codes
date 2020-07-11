try:
    file = open("FCS.txt", 'r')
    file.write("This course is so exciting!")

except Exception as e:
    print("An error occured: ", e)
    file = open("FCS.txt")
    print("The file reads: ")
    print(file.read())

finally:
    file.close()