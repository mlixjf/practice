from functools import partial


class LoggedMappingMixin:
    __slots__ = ()

    def __getitem__(self, key):
        print("Getting " + str(key))
        return super().__getitem__(key)

    def __setitem__(self, key, value):
        print("Setting {} = {!r}".format(key, value))
        return super().__setitem__(key, value)

    def __delitem__(self, key):
        print("Deleting " + str(key))
        return super().__delitem__(key)


class SetOnceMappingMixin:
    __slots__ = ()

    def __setitem__(self, key, value):
        if key in self:
            raise KeyError(str(key) + " already set")
        super().__setitem__(key, value)


class StringKeysMappingMixin:
    __slots__ = ()

    def __setitem__(self, key, value):
        if isinstance(key, str):
            raise TypeError("key must be string")
        super().__setitem__(key, value)


class LoggedDict(LoggedMappingMixin, dict):
    pass


if __name__ == '__main__':
    d = LoggedDict()
    d["x"] = 23
    print(d["x"])
    del d["x"]

    partial