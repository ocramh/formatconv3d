# scaffolding taken from
# https://github.com/PyMesh/PyMesh/blob/master/docker/py3.6/Dockerfile
FROM python:3.6
WORKDIR /root/
ARG BRANCH="master"
ARG NUM_CORES=2

RUN echo "deb http://ftp.us.debian.org/debian unstable main contrib non-free" >> /etc/apt/sources.list.d/unstable.list &&\
  apt-get update && apt-get install -y \
  gcc \
  g++ \
  git \
  cmake \
  libgmp-dev \
  libmpfr-dev \
  libgmpxx4ldbl \
  libboost-dev \
  libboost-thread-dev && \
  apt-get clean && \
  git clone --single-branch -b $BRANCH https://github.com/PyMesh/PyMesh.git

ENV PYMESH_PATH /root/PyMesh
ENV NUM_CORES $NUM_CORES
WORKDIR $PYMESH_PATH

RUN git submodule update --init && \
  pip install -r $PYMESH_PATH/python/requirements.txt && \
  ./setup.py bdist_wheel && \
  rm -rf build third_party/build && \
  pip install dist/pymesh2*.whl && \
  python -c "import pymesh; pymesh.test()" && \
  python $PYMESH_PATH/docker/patches/patch_wheel.py

WORKDIR /app
COPY . /app

RUN ls -la

ENTRYPOINT ["python"]
CMD ["app.py", "input_dir"]