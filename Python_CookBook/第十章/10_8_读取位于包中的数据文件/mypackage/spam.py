import pkgutil
print(__package__)
data = pkgutil.get_data(__file__, "somedata.dat")
