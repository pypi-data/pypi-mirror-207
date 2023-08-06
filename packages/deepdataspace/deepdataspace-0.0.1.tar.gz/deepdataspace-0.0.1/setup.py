import os
from setuptools import setup

version = "0.0.1"
description = "A tool for CV dataset labeling, visualizing and analysing"
with open("README.md", "r") as fp:
    long_description = fp.read()
url = "https://idea.edu.cn/cvr.html"
author = "cvr@idea"
classifiers = [
    "Development Status :: 4 - Beta",
    "Intended Audience :: Information Technology",
    "Intended Audience :: Science/Research",
    "Topic :: Scientific/Engineering :: Artificial Intelligence",
    "Topic :: Scientific/Engineering :: Image Processing",
    "Topic :: Scientific/Engineering :: Image Recognition",
    "Topic :: Scientific/Engineering :: Information Analysis",
    "Topic :: Scientific/Engineering :: Visualization",
    "Operating System :: MacOS :: MacOS X",
    "Operating System :: POSIX :: Linux",
    "Operating System :: Microsoft :: Windows",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.8",
    "Programming Language :: Python :: 3.9",
    "Programming Language :: Python :: 3.10",
]


def get_version():
    ver = os.environ.get("DDS_PACKAGE_VERSION", None)
    if ver is not None:
        return ver
    return str(version)


def find_packages(pkg_dir: str):
    """
    把 pkg_dir 目录下所有 python package 都找出来并返回
    所谓 python package，是至少包含 __init__.py 的文件目录
    """
    found = []

    for top, dirs, files in os.walk(pkg_dir):
        has_init = False
        has_python = False
        for file in files:
            if file == "__init__.py":
                has_init = True
            if file.endswith(".py"):
                has_python = True

        if has_init and has_python:
            found.append(top)

    return found


setup(name="deepdataspace",
      version=get_version(),  # the package version, it may be different from the release version
      description=description,
      long_description=long_description,
      url=url,
      author=author,
      author_email="huweiqiang@idea.edu.cn",
      packages=find_packages("deepdataspace"),
      include_package_data=True,
      py_modules=["dds"],
      entry_points={
          "console_scripts": [
              "dds=dds:main",
          ],
      },
      install_requires=[
          "celery==5.2.7",
          "click==8.1.3",
          "cryptography==39.0.1",
          "Django==4.1.1",
          "djangorestframework==3.14.0",
          "django-cors-headers==3.13.0",
          "numpy==1.21.5",
          "opencv-contrib-python-headless==4.6.0.66",
          "opencv-python-headless==4.6.0.66",
          "psutil==5.9.2",
          "pydantic==1.10.2",
          "pymongo==4.2.0",
          "PyYAML==6.0",
          "Pillow==8.4.0",
          "redis==4.3.4",
          "requests==2.28.1",
          "scikit-learn==1.0.2",
          "sentry-sdk==1.19.1",
          "tqdm==4.64.1",
          "whitenoise==6.2.0"
      ],
      classifiers=classifiers,
      )
