from math import log2, ceil


class Scales:
    def __init__(self):
        self.right = 0
        self.left = 0
        self.counter = 0

    def check(self):
        self.counter += 1
        if self.left < self.right:
            print("Взвешивание №",self.counter, " ", self.left, " < ", self.right)
        elif self.left > self.right:
            print("Взвешивание №",self.counter, " ", self.left, " > ", self.right)
        else:
            print("Взвешивание №",self.counter, " ", self.left, " = ", self.right)
        return self.right == self.left

    def info(self):
        return str(self.left) + " ? " + str(self.right)


class Bell1g(Scales):
    bell = False

    def add_1g(self):
        if not self.bell:
            self.right += 1
            self.bell = True
            print("Добавляем гирю на правую чашу", self.info())

    def rem_1g(self):
        if self.bell:
            self.right -= 1
            self.bell = False
            print("Убираем гирю с правой чаши", self.info())


class Rice(Bell1g):
    def __init__(self, weight):
        super().__init__()
        self.weight = int(weight)
        self.b0 = bin(self.weight)[2:]
        self.length = len(self.b0)

    def add_sahar(self):
        self.left = self.right
        print("Досыпаем рис на левую чашу", self.info())
        self.check()

    def relocate_sahar(self):
        self.right += self.left
        self.left = 0
        print("Пересыпаем рис с левой на правую чашу", self.info())

    def get_rice(self):
        for i in self.b0:
            if i == '1':
                self.add_1g()
            else:
                self.rem_1g()
            self.add_sahar()
            self.relocate_sahar()
        self.rem_1g()


def main():
    text = "Приветствую!\n\nТекст задачи:\nПредставьте, что у вас есть мешок риса,из которого вам нужно отмерить " \
           "ровно 1 кг.\nВ вашем распоряжении простейшие весы с двумя чашами,куда можно пересыпать рис, и гирька " \
           "весом 1 г.\nКакое минимальное взвешиваний понадобится, чтобы отмерить 1 кг риса?\n\nРешение:\n" \
           "В простоейшем варианте задача решается как длина двоичной записи искомого кол-ва риса в г.\n" \
           "1000г. = 1111101000. Соответсвенно 10 взвешиваний. Проверим так ли это.\n"
    print(text)
    r = Rice('1000')
    r.get_rice()
    text = "Ответ: 10 взвешиваний.\n Спасибо! Всего доброго!"


if __name__ == '__main__':
    main()
