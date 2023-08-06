import os
from setuptools import Extension, setup

C_SOURCE_DIR = "c_tasep_lib/"
C_INCLUDE_DIR = "c_tasep_include/"
C_SOURCE_FILES = []
with open("README.md", "r") as fh:
    long_description = fh.read()


for file in os.listdir(C_SOURCE_DIR):
    if file.endswith(".c"):
        C_SOURCE_FILES.append(os.path.join(C_SOURCE_DIR, file))

for file in os.listdir("src/tasep/"):
    if file.endswith(".c"):
        C_SOURCE_FILES.append(os.path.join("src/tasep/", file))


setup_args = dict(
    ext_modules = [
        Extension(
            'tasep',
            define_macros = [('MAJOR_VERSION', '0'),
                             ('MINOR_VERSION', '1')],
            include_dirs = ['/usr/local/include', C_INCLUDE_DIR],
            libraries = ['m'],
            library_dirs = ['/usr/local/lib', C_SOURCE_DIR],
            sources = C_SOURCE_FILES,
            language="c"
            )
        ],
    long_description=long_description,
    long_description_content_type="text/markdown"

)

setup(**setup_args)
