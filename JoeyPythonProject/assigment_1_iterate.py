# Assignment 1

#   Write a python code that will iterate through any file directory
#   The script should be able to list all the files that are in a specified direcotry


import os


dir = "/Users/georgebuahin/Documents/projects/py_Joey_Edu/JoeyPythonProject"
dir2 = "/Users/georgebuahin/Documents/projects/realestatedata/frontend/driven-prop"


# for filename in os.listdir(dir):
#     file = os.path.join(dir, filename)
#     if os.path.exists(file):
#         print(file)


class jl:
    def list_files(directory):
        for filename in os.listdir(directory):
            text = f"The file name is {filename}"
            print(text)

    def list_files_with_directory(directory):
        for filename in os.listdir(directory):
            file = os.path.join(dir, filename)
            if os.path.isfile(file):
                print(file)

            # text = f"The file name is {filename}"
            # print(text)

            # file = os.path.join(dir, filename)
            # if os.path.exists(file):
            #     print(file)


jl.list_files(dir)
print("-------------------")
jl.list_files_with_directory(dir)
