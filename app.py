import pymesh


def convert_test():
    mesh = pymesh.load_mesh("data/test.stl")
    pymesh.save_mesh("test.obj", mesh)


if __name__ == '__main__':
    convert_test()
