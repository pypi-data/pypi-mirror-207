from setuptools import setup, find_packages
from setuptools.command.install import install
import os
import urllib.request

class PostInstallCommand(install):
    def run(self):
        install.run(self)
        print("Downloading data files....")
        url = "https://pypi-store.s3.amazonaws.com/data.zip"
        target_dir = os.path.join(self.install_lib, "ViTest", "data")
        os.makedirs(target_dir, exist_ok = True)
        filename, headers = urllib.request.urlretrieve(url, os.path.join(target_dir, "10mb.zip"))
        
        if filename.endswith(".zip"):
            import zipfile
            with zipfile.ZipFile(filename, 'r') as zf:
                zf.extractall(target_dir)

setup(
    name = "ViTest",
    version = "1.0",
    author = "VigneshVallavan",
    author_email = "vigneshvallavan1999@gmail.com",
    description = "Custom package",
    packages = find_packages(),
    include_package_data = False,
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],    
    cmdclass = {
        'install': PostInstallCommand,
    },
    download_url = 'https://pypi-store.s3.amazonaws.com/data.zip',
)