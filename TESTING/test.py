import os

path = './TESTING/help/'
files = os.listdir(path)
for file in files:
    with open(path+file) as f:
        tags = ['s', 'w', 'h', 'd']
        readline = f.readline()[:-1].split(' ')
        if all(item in readline for item in tags):
            print(True, path+file)
            
#         print(f.readline())



