import os
import pymesh


class ExportToObj:
    def init():
        pass

    def file_info_from_path(self, filepath):
        """returns the file name and extension"""

        full_filename = os.path.basename(filepath)
        name, extension = os.path.splitext(full_filename)

        return name, extension

    def from_stl(self, filepath):
        valid_ext = ".stl"

        name, ext = self.file_info_from_path(filepath)
        if ext != valid_ext:
            raise ValueError("file extension must be .stl")

        mesh = pymesh.load_mesh(filepath)
        pymesh.save_mesh("{0}.obj".format(name), mesh)

    def from_ply(filepath):
        mesh = pymesh.load_mesh(file_path)
        pymesh.save_mesh("test.obj", mesh)
