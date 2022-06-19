
class Spam:

    def bar(self, x: int, y: int):
        print("bar1:", x, y)

    def bar(self, s: str, n: int = 0):
        print("bar2:", s, n)


if __name__ == '__main__':
    spam = Spam()
    spam.bar(1, 2)
    spam.bar("hello")
    print(Spam.__dict__)