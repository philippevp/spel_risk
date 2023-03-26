import random

AANTAL_ZIJDEN = 6


class Dobbelsteen:

    def __init__(self):
        self.value = 0

    def worp(self):
        self.value = random.randint(1, AANTAL_ZIJDEN)



# def main():
#     dobbelst = Dobbelsteen()
#     dobbelst.worp()
#     print(dobbelst.value)


# if __name__ == "__main__":
#    main()
