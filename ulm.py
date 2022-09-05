laptop = open("hp.txt", "w+")
laptop.write("tv\n")
laptop.write("phone\n")
laptop.write("mobile\n")
laptop.close()

laptop = open("hp.txt", "a+")
laptop.write("sofa\n")
laptop.close()

laptop = open("hp.txt")
print(laptop.read())
laptop.close()
