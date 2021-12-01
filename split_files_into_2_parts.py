import codecs

with codecs.open("C:\\Users\\CyrusSmith\\Desktop\\test\\Split files\\home-page(listreet)-en.html",'r', 'utf-8') as file:
    lines = file.readlines()

with codecs.open("C:\\Users\\CyrusSmith\\Desktop\\test\\Split files\\home-page(listreet)-en_1.html",'w', 'utf-8') as file:
    for line in lines[:int(len(lines)/2)]:
        file.write(line)

with codecs.open("C:\\Users\\CyrusSmith\\Desktop\\test\\Split files\\home-page(listreet)-en_2.html",'w', 'utf-8') as file:
    for line in lines[int(len(lines)/2):]:
        file.write(line)
