from distutils.core import setup


# setup(name="myweb",
#       version="1.0",
#       author="Kang",
#       author_email="123@Kang.com",
#       url="http://www.123.com",
#       packages=["myweb"]
#       )
#
#
# from setuptools import find_packages
from setuptools import find_packages

if __name__ == '__main__':
    print(find_packages(exclude=["tests", "ci", "tests.*"]))