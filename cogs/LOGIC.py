import os

def checktags(path, tags):
        tags = tags.split(',')
        found = []
        files = os.listdir(path)
        for file in files:
            with open(path+file) as f:
                readline = f.readline()[:-1].split(' ')
                if all(item in readline for item in tags):
                    found.append(path+file)
        
        return found