class BigNumber:
    """
       Класс предназначен для работы и хранения очень больших целых чисел. Число всегда инициализируется ввиде строки.
       The class is designed to work and store very large integers. The number is always initialized as a string.
    """

    def __init__(self, big_number):
        self.big_number = str(big_number)

    def __add__(self, other_obj):
        """
           Переопределяем поведение при сложении экземпляров класса BigNumber. Результатом является новый экземпляр с новым большим числом (суммой двух других).
           We redefine the behavior when adding instances of the BigNumber class. The result is a new instance with a new large number (the sum of the other two).
        """
        count_other = len(other_obj.big_number)
        count_self = len(self.big_number)
        limit_to_adding = count_other
        obj_with_larger_number = self
        if count_self < limit_to_adding:
            obj_with_larger_number = other_obj
            limit_to_adding = count_self
        new_big_number = ''
        memory = 0
        for i in range(limit_to_adding):
            sum = str(int(self.big_number[-1 - i]) + int(other_obj.big_number[-1 - i]) + memory)
            memory = 0
            if len(sum) > 1:
                memory = int(sum[0])
            new_big_number += sum[-1]
        for j in range(len(obj_with_larger_number.big_number) - i - 2, -1, -1):
            if memory and int(obj_with_larger_number.big_number[j]) < 9:
                new_big_number += str(int(obj_with_larger_number.big_number[j]) + memory)
                memory = 0
            elif memory and int(obj_with_larger_number.big_number[j]) == 9:
                temp = str(int(obj_with_larger_number.big_number[j]) + memory)
                new_big_number += temp[-1]
                memory = int(temp[0])
            else:
                new_big_number += obj_with_larger_number.big_number[j]
        if memory:
            new_big_number += str(memory)
        return BigNumber(new_big_number[::-1])


