import codecs
key = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20)
lines_per_file = 50
smallfile = None
with codecs.open('C:\\Users\\CyrusSmith\\Desktop\\test\\Split files\\home-page(listreet)-en.html', 'r', 'utf-8') as bigfile:
    for lineno, line in enumerate(bigfile):
        if lineno % lines_per_file == 0:
            if smallfile:
                smallfile.close()
            small_filename = 'C:\\Users\\CyrusSmith\\Desktop\\test\\Split files\\home-page(listreet)-en_{}.html'.format(lineno)
            smallfile = codecs.open(small_filename, "w", 'utf-8')
        smallfile.write(line)
    if smallfile:
        smallfile.close()
