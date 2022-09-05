import io


def closeObj(fileObject: io.TextIOWrapper):
    fileObject.close()
    print(fileObject, "closed")


month = open("dates.txt", "w+")
month.write("jan\nfeb\nmar\napr\n")
closeObj(month)

monthfile = open("dates.txt", "r+")
print(monthfile.read())
closeObj(monthfile)
