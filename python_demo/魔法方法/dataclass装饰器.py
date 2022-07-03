from dataclasses import dataclass


@dataclass
class Lang:
    name: str = "python"
    strong_type: bool = True
    static_type: bool = True
    age: int = 28

    def __post_init__(self):
        print("这是父类")


@dataclass
class Test(Lang):

    def __post_init__(self):
        super().__post_init__()
        print("这是子类")

# print(Lang.__annotations__)
# lang = Lang()
# lang_1 = Lang(age=29)
# print(lang)
# print(lang == lang_1)
t = Test()

_, interval = "-1"
print(interval.split("-"))