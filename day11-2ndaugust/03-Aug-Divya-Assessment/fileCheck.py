import glob
# for i in glob.glob('*.py'):        # to check all the files in the directorary
#     print(i)
for i in glob.glob('lo*.py'):
    print(i)                          # to check the file that starts with lo
for l in glob.glob('T_zone*.py'):
    print(l)
# for l in glob.glob('sample/log*.py'):         # to check other folder project
#     print(l) 