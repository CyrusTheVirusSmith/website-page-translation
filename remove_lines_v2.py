import codecs

# read file
#file1 = open('pages.csv', 'r')
#Lines = file1.readlines()
Lines = []

for line in Lines:
    #if 'html' in line.strip():
    #    file = line.strip()
       # print(file)
       # location = "C:\\Users\\CyrusSmith\\Desktop\\postcodezip\\"+file
        with codecs.open(r"C:\Users\CyrusSmith\Desktop\New folder2\about-tw.html", 'r', 'utf8') as fp:
       # print(location)
            lines = fp.readlines()
            print(lines)
        with codecs.open(r"C:\Users\CyrusSmith\Desktop\New folder2\about-tw22.html", 'w', 'utf8') as fp:
            fp.writelines(Lines[9:-4])
