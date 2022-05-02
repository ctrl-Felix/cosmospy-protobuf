import os

def touch(fname, times=None):
    with open(fname, 'a'):
        os.utime(fname, times)

def walk_through_subdirectory(directory):
    for root, dirs, files in os.walk(directory):
        open(os.path.join(root, "__init__.py"), 'a').close()
        for dir in dirs:
            walk_through_subdirectory(dir)


walk_through_subdirectory("cosmospy_protobuf")
