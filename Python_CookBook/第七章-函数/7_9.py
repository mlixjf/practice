from urllib.request import urlopen

import kwargs as kwargs


class UrlTemplate:

    def __init__(self, template):
        self.template = template

    def open(self, **kwargs):
        return urlopen(self.template.format_map(kwargs))


yahoo = UrlTemplate('http://finance.yahoo.com/d/quotes.csv?s={names}&f={fields}')

# for line in yahoo.open(names="IBM,AAPL,FB", fields="sl1c1v"):
#     print(line.encode("utc-8"))


def url_template(template):
    def open(**kwargs):
        return urlopen(template.format_map(kwargs))

    return open


o = dir(object())
m = dir(url_template)
print(o)
print(m)
result = (set(m) - set(o))
print(result)