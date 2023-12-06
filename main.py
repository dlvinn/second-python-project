import os

file_path = 'C:/Users/96478/Downloads/assignment3-q1.pro'
print(file_path)

if os.path.isfile(file_path):
    os.remove(file_path)
    print("file has successefully been deleted")
else:
    print("this file does not exist!!")
