import pymesh
import os
import sys

WHITELISTED_FORMATS = ['.obj', '.off', '.ply', '.stl', '.mesh']


def convert_test():
    mesh = pymesh.load_mesh("data/test.stl")
    pymesh.save_mesh("test.obj", mesh)


def convert_files_in_dir(input_dir):
    pwd = os.getcwd()
    save_to_dir = os.path.join(pwd, 'converted_files')

    # try:
    #     os.mkdir(save_to_dir)
    # except OSError:
    #     print("creation of the directory %s failed" % save_to_dir)
    #     sys.exit()

    print("files will be saved in %s" % save_to_dir)
    file_converted = 0

    for f in os.listdir(input_dir):
        name, ext = os.path.splitext(f)

        if ext not in WHITELISTED_FORMATS:
            print('skipping file %s' % name)
            continue

        mesh = pymesh.load_mesh(os.path.join(input_dir, f))
        pymesh.save_mesh(os.path.join(
            'converted_files', '{}.obj'.format(name)), mesh)
        file_converted = file_converted + 1

    print('job completed. total files converted: {}'.format(file_converted))


if __name__ == '__main__':
    if len(sys.argv) == 1:
        print('you must pass an input directory')
        sys.exit()

    convert_files_in_dir(sys.argv[1])
