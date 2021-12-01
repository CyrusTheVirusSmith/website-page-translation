# list to store file lines
lines = []
# read file

with open(r"C:\Users\CyrusSmith\Desktop\111\about-tw.html", 'r') as fp:
# read an store all lines into list
    lines = fp.readlines()
    print(lines)
# Write file
with open(r"C:\Users\CyrusSmith\Desktop\111\about-tw2.html", 'w') as fp:
    fp.writelines(lines[9:-4])