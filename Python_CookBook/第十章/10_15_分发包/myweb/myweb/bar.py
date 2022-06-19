from setuptools import find_packages

print("bar")

if __name__ == '__main__':
    print(find_packages(exclude=["tests", "ci", "tests.*"]))