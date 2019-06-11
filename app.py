import pymesh

mesh = pymesh.load_mesh("data/test.stl")
pymesh.save_mesh("test.obj", mesh)