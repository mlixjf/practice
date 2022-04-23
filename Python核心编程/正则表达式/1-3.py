import re

bt = "bat|bet|bit"
m = re.match(bt, "bat")
if m is not None:
    print(m.group())

m = re.match(bt, "he bit me")
if m is not None:
    print(m.group())

m = re.match(bt, "blt")
if m is not None:
    print(m.group())

m = re.search(bt, "he bit me")
if m is not None:
    print(m.group())

anyend = ".end"

m = re.match(anyend, "bend")
if m is not None:
    print(m.group())

m = re.match(anyend, "end")
print(m)

print(re.match(anyend, "\nend"))
print(re.search(anyend, "The end."))

patt314 = '3.14'
print(re.match(patt314, "3014"))
print(re.match(patt314, "3.14"))

pi_patt = "3\.14"
print(re.match(pi_patt, "3014"))
print(re.match(pi_patt, "3.14"))



patt = "[cr][23][dp][o2]"
print(re.match(patt, "c3po"))
print(re.match(patt, "c2do"))
print(re.match("r2d2|c3po", "c2do"))

patt = "\w+@(\w+\.)*\w+\.com"
print(re.match(patt, "nobody@www.xxx.com"))

patt = "\w\w\w-\d\d\d"
print(re.match(patt, "avc-123"))

patt = "(\w\w\w)-(\d\d\d)"
m = re.match(patt, "abc-123")
print(m.group())
print(m.group(1))
print(m.group(2))
print(m.groups())

m = re.match("(a)(b)", "ab")
print(m.group())
print(m.groups())

m = re.search("test", "Hellotest")
print(m)
# print(m.group())
m = re.search("test", "testHello")
print(m)

s = "data"
print(re.search(s, "data"))
m = re.search(s, "data")

m = re.search("^The", "The end.")
print(m.group())
print(re.search("^The", "end. The"))

print(re.search(r"\bthe", "bite the dog"))
print(re.search(r"\Bthe", "bite the dog"))
print(re.search(r'\bthe', 'bitethe dog'))
print(re.search(r'\Bthe', 'bitethe dog'))

print(re.findall("car", "car"))
print(re.search("car", "scary"))
print(re.findall('car', 'carry the barcardi to the car'))

s = "This and that"
print(re.findall(r"(th\w+) and (th\w+)", s, re.I))

repl = "Mr. Smith"
string = "attn: X\n\nDear X,\n"
print(re.sub("X", repl, string))
print(re.subn( "X", repl, string))