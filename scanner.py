import os

def scan_directory(path):
    files = []
    for root, dirs, filenames in os.walk(path):
        for name in filenames:
            files.append(os.path.join(root, name))
    return files