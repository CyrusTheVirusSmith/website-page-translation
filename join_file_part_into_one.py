# Python program to
# demonstrate merging of
# two files

#import
import codecs

# Creating a list of filenames
filenames = ['C:\\Users\\CyrusSmith\\Desktop\\test\\Split files\\home-page(listreet)-af0.html', 'C:\\Users\\CyrusSmith\\Desktop\\test\\Split files\\home-page(listreet)-af1.html', 'C:\\Users\\CyrusSmith\\Desktop\\test\\Split files\\home-page(listreet)-af2.html', 'C:\\Users\\CyrusSmith\\Desktop\\test\\Split files\\home-page(listreet)-af3.html', 'C:\\Users\\CyrusSmith\\Desktop\\test\\Split files\\home-page(listreet)-af4.html', 'C:\\Users\\CyrusSmith\\Desktop\\test\\Split files\\home-page(listreet)-af5.html', 'C:\\Users\\CyrusSmith\\Desktop\\test\\Split files\\home-page(listreet)-af6.html', 'C:\\Users\\CyrusSmith\\Desktop\\test\\Split files\\home-page(listreet)-af7.html', 'C:\\Users\\CyrusSmith\\Desktop\\test\\Split files\\home-page(listreet)-af8.html', 'C:\\Users\\CyrusSmith\\Desktop\\test\\Split files\\home-page(listreet)-af9.html', 'C:\\Users\\CyrusSmith\\Desktop\\test\\Split files\\home-page(listreet)-af10.html', 'C:\\Users\\CyrusSmith\\Desktop\\test\\Split files\\home-page(listreet)-af11.html', 'C:\\Users\\CyrusSmith\\Desktop\\test\\Split files\\home-page(listreet)-af12.html', 'C:\\Users\\CyrusSmith\\Desktop\\test\\Split files\\home-page(listreet)-af13.html', 'C:\\Users\\CyrusSmith\\Desktop\\test\\Split files\\home-page(listreet)-af14.html', 'C:\\Users\\CyrusSmith\\Desktop\\test\\Split files\\home-page(listreet)-af15.html', 'C:\\Users\\CyrusSmith\\Desktop\\test\\Split files\\home-page(listreet)-af16.html', 'C:\\Users\\CyrusSmith\\Desktop\\test\\Split files\\home-page(listreet)-af17.html', 'C:\\Users\\CyrusSmith\\Desktop\\test\\Split files\\home-page(listreet)-af18.html', 'C:\\Users\\CyrusSmith\\Desktop\\test\\Split files\\home-page(listreet)-af19.html', 'C:\\Users\\CyrusSmith\\Desktop\\test\\Split files\\home-page(listreet)-af20.html', 'C:\\Users\\CyrusSmith\\Desktop\\test\\Split files\\home-page(listreet)-af21.html', 'C:\\Users\\CyrusSmith\\Desktop\\test\\Split files\\home-page(listreet)-af22.html', 'C:\\Users\\CyrusSmith\\Desktop\\test\\Split files\\home-page(listreet)-af23.html']

# Open file3 in write mode
with codecs.open('C:\\Users\\CyrusSmith\\Desktop\\test\\Split files\\home-page(listreet)-af_joined.html', 'w', 'utf-8') as outfile:
    # Iterate through list
    for names in filenames:
        # Open each file in read mode
        with codecs.open(names) as infile:
            # read the data from file1 and
            # file2 and write it in file3
            outfile.write(infile.read())

        # Add '\n' to enter data of file2
        # from next line
        outfile.write("\n")