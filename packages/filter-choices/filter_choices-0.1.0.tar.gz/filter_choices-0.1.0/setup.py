# Change the content according to your package.
import setuptools
import re

# Extract the version from the init file.
VERSIONFILE="__init__.py"
getversion = re.search( r"^__version__ = ['\"]([^'\"]*)['\"]", open(VERSIONFILE, "rt").read(), re.M)
if getversion:
    new_version = getversion.group(1)
else:
    raise RuntimeError("Unable to find version string in %s." % (VERSIONFILE,))

# Configurations
with open("README.md", "r") as fh:
    long_description = fh.read()
setuptools.setup(
     install_requires=['matplotlib','numpy'],        # Dependencies
     python_requires='>=3',                                   # Minimum Python version
     name='filter_choices',                                  # Package name
     version=new_version,                                     # Version
     author="Miles, Jamar,Darnell",                                     # Author name
     author_email="jamar.bailey@bison.howard.edu ",                           # Author mail
     description="Python package for my CSIII project",    # Short package description
    url="https://github.com/JamarB3/Image_Filters/tree/main",       # Url to your Git Repo
     packages=setuptools.find_packages(),                     # Searches throughout all dirs for files to include
     include_package_data=True,                               # Must be true to include files depicted in MANIFEST.in
     license_files=["LICENSE"],                               # License file
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
 )
