import math
from BigNumber import BigNumber

def gen_multiple_lst(value1 = 3, value2 = 5, limit = 1000): 
    """
       Создание списка чисел кратных первому значению или второму в пределах заданного лимита.
       Creating a list of numbers that are multiples of the first value or the second within the specified limit.
    """
    return [i for i in range(1, limit) if i % value1 == 0 or i % value2 == 0]

def sum_of_list_items(lst):
    """
       Сумма все элементов списка
       Sum of list items
    """
    sum = 0
    for i in lst:
        sum += i
    return sum

def gen_fibonacci_sequence(fibonacci_sequence = [1, 1], limit = 4000000):
    """
       Создание последовательности чисел Фибоначчи с максимальным числом в последовательности не превышающим limit.
       Creating a sequence of Fibonacci numbers with the maximum number in the sequence not exceeding limit.
    """
    sum = fibonacci_sequence[-1] + fibonacci_sequence[-2]
    if sum <= limit:
        fibonacci_sequence.append(sum)
        return gen_fibonacci_sequence(fibonacci_sequence, limit)
    return fibonacci_sequence

def sum_even_fibonacci_numbers(fibonacci_sequence):
    """
       Сумма четных чисел из последовательности Фибоначчи.
       The sum of the even numbers from the Fibonacci sequence.
    """
    start_ind = 3
    if fibonacci_sequence[0]:
        start_ind = 2
    sum = 0
    for i in range(start_ind, len(fibonacci_sequence), 3):
        sum += fibonacci_sequence[i]
    return sum

def is_simple_divider(divisor):
    """
       Функция проверяет является ли делитель простым числом.
       The function checks if the divisor is a prime number.
    """
    for i in range(2, int(math.sqrt(divisor)) + 1):
        if divisor % i == 0:
            return False
    return True

def create_all_simple_dividers_of_number(number):
    """
        Функция возвращает список всех простых делителей числа.
        The function returns a list of all prime divisors of a number.
    """
    simple_dividers = []
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0 and is_simple_divider(i):
            simple_dividers.append(i)
    return simple_dividers

def is_palindrom(number):
    """
       Функция определяет является ли число палиндромом.
       The function determines whether the number is a palindrome.
    """
    number = str(number)
    for i in range(len(number) // 2):
        if number[i] != number[-1 - i]:
            return False
    return True


def search_max_palindrom(number_order):
    """
       Поиск максимального палиндрома, полученного умножением двух целых чисел одинакового порядка. number_order - порядок числа (1 - 10 : 99, 2 - 100 : 999 и так далее).
       Search for the maximum palindrome obtained by multiplying two integers of the same order. number_order - the order of the number (1 - 10: 99, 2 - 100: 999, and so on).
    """
    lim = 9
    for i in range(number_order):
        lim *= 10
    lim += 10 ** number_order - 1
    max_palindrom = 0
    for i in range(lim, lim - 10 ** number_order * 9, -1):
        for j in range(i, lim - 10 ** number_order * 9, -1):
            mul = i * j
            if is_palindrom(mul) and mul > max_palindrom:
                max_palindrom = mul
    return max_palindrom

def is_divided_by_all_dividers(number, range_div_A, range_div_B):
    """
       Проверяем число на делимость числам от range_div_A до range_div_B.
       Check the number for divisibility to numbers from range_div_A to range_div_B.
    """
    gen_dividers = list(range(range_div_A, range_div_B))
    for i in gen_dividers:
        if number % i:
            return False
    return True


def least_multiple():
    """
       Поиск наименьшего кратного множества целых чисел от 1 до 20. 
       Мы знаем, что наименьшее число, которое делится на числа от 1 до 10 - это число 2520. Значит, мы будем проверять на делимость только числа кратные числу 2520,
       так как другие варианты не будут делиться на все числа от 1 до 10.
       Search for the smallest multiple of integers from 1 to 20.
       We know that the smallest number that is divided by numbers from 1 to 10 is the number 2520. Therefore, we will check for divisibility only numbers that are multiples of 2520,
       as other options will not be divided into all numbers from 1 to 10.
    """
    number = 2520
    while not(is_divided_by_all_dividers(number, 11, 20)):
        number += 2520
    return number

def delta_sum_of_squares_and_square_of_sum(limit):
    """
       Разность между суммой квадратов и квадратом суммы.
       The difference between the sum of the squares and the square of the sum.
    """
    sum_of_squares = 0
    square_of_sum = 0
    for i in range(1, limit + 1):
        sum_of_squares += i ** 2
        square_of_sum += i
    square_of_sum = square_of_sum ** 2
    return abs(sum_of_squares - square_of_sum)

def get_simple_number(limit):
    """
       Нахождение n-го простого числа. limit - это какое по счету простое число.
       Finding the nth prime. limit - is a prime number.
    """
    count = 0
    simple_number = 2
    while count < limit:
        if is_simple_divider(simple_number):
            count += 1
        simple_number += 1 + simple_number % 2
    if limit > 1:
        return simple_number - 2
    elif limit == 1:
        return simple_number - 1
    else:
        return 

def file_processing_big_number():
    """
       Обработка файла с большим числом.
       Processing a file with a large number.
    """
    big_number_str = ''
    with open('big_number.txt') as big_number:
        for line in big_number:
            big_number_str += ''.join(line.split('\n'))
    return big_number_str

def find_first_nonzero_product(big_number, start_ind_end_ind_product = [0, 4, 1]):
    """
       Функция ищет первое ненулевое произведение в большом числе и возвращает результат в виде списка [start_ind, end_ind, product].
       start_ind - это индекс начала чисел ненулевого произведения;
       end_ind - это индекс конца, до которого рассчитывалось произведение (необходим для корректной работы рекурсии);
       product - это произведение чисел от start_ind до end_ind.
       The function searches for the first nonzero product in a large number and returns the result in the form of a list [start_ind, end_ind, product].
       start_ind is the index of the beginning of numbers of a nonzero product;
       end_ind is the end index to which the product was calculated (necessary for the recursion to work correctly);
       product is the product of numbers from start_ind to end_ind.
    """
    if start_ind_end_ind_product[1] >= len(big_number):
        return [start_ind_end_ind_product[1], start_ind_end_ind_product[1], 0]
    current_product = 1
    for i in range(start_ind_end_ind_product[0], start_ind_end_ind_product[1]):
        current_product *= int(big_number[i])
    if current_product == 0:
        start_ind_end_ind_product[0] += 1
        start_ind_end_ind_product[1] += 1
        return find_first_nonzero_product(big_number, start_ind_end_ind_product)
    start_ind_end_ind_product[2] = current_product
    return start_ind_end_ind_product

def largest_product_of_consecutive_digits(number_of_consecutive_digits):
    """
       Поиск максимального произведения n-последовательных чисел в большом числе.
       Search for the maximum product of n-consecutive numbers in a large number.
    """
    big_number = file_processing_big_number()
    list_of_results = find_first_nonzero_product(big_number, [0, number_of_consecutive_digits, 1])
    current_product = list_of_results[2]
    max_product = current_product
    i = list_of_results[0]
    while i < len(big_number) - number_of_consecutive_digits:
        if (current_product == 0):
            i += number_of_consecutive_digits
            list_of_results = find_first_nonzero_product(big_number, [i, i + number_of_consecutive_digits, 1])
            current_product = list_of_results[2]
            i = list_of_results[0]
        else:
            current_product = (current_product // int(big_number[i])) * int(big_number[i + number_of_consecutive_digits])
            i += 1
        if current_product > max_product:
            max_product = current_product
    return max_product

def get_special_three_of_pythagoras(sum):
    """
       Расчет особой тройки Пифагора. Сумма чисел тройки Пифагора должна быть: a + b + c = sum.
       Calculation of a special triple of Pythagoras. The sum of the numbers of the Pythagorean triple should be: a + b + c = sum.
    """
    for a in range(sum // 2):
        for b in range(a + 1, sum // 2):
            c = math.sqrt(a ** 2 + b ** 2)
            if str(c)[-1] == '0':
                if a + b + c == sum:
                    return [a, b, int(c)]

def sum_of_simple_numbers(limit):
    """
       Сумма всех простых чисел меньше limit.
       The sum of all primes is less than limit.
    """
    sum = 0
    potential_prime = 2
    while potential_prime < limit:
        if is_simple_divider(potential_prime):
            sum += potential_prime
        potential_prime += 1 + potential_prime % 2
    return sum

def print_matrix_2d(matrix_2d):
    """
       Вывод двумерного массива данных в консоль в виде таблицы.
       Output of a two-dimensional data array to the console in the form of a table.
    """
    for i in range(len(matrix_2d)):
        for j in range(len(matrix_2d[0])):
            print('{:>4}'.format(matrix_2d[i][j]), end = ' ')
        print()

def file_processing_set_of_number():
    """
       Обработка файла set_of_numbers.txt и создание на его основе двумерного массива чисел.
       Processing the set_of_numbers.txt file and creating, based on its two-dimensional array of numbers.
    """
    matrix_2d = []
    with open('set_of_numbers.txt') as data:
        for line in data:
            matrix_2d.append([int(i) for i in line.strip().split(' ')])
    return matrix_2d

def search_max_product_vertical_in_matrix_2d(max_product, n, matrix2d):
    """
       Поиск максимального произведения n - чисел по вертикале в двумерном массиве чисел.
       Search for the maximum product of n - numbers vertically in a two-dimensional array of numbers.
    """
    for j in range(len(matrix2d[0])):
        i = 0
        while i <= len(matrix2d) - n:
            current_product = 1
            for k in range(i, i + n):
                current_product *= matrix2d[k][j]
            if current_product > max_product:
                max_product = current_product
            i += 1
    return max_product

def search_max_product_horizontal_in_matrix_2d(max_product, n, matrix2d):
    """
       Поиск максимального произведения n - чисел по горизонтале в двумерном массиве чисел.
       Search for the maximum product of n - numbers horizontally in a two-dimensional array of numbers.
    """
    for i in range(len(matrix2d)):
        j = 0
        while j <= len(matrix2d[0]) - n:
            current_product = 1
            for k in range(j, j + n):
                current_product *= matrix2d[i][k]
            if current_product > max_product:
                max_product = current_product
            j += 1
    return max_product

def extract_diagonal_numbers_from_matrix_2d(ind_i, ind_j, matrix2d, diagonal_left_right_up_down = True):
    """
       Извлечение из двумерного массива диагонали в соответствии со стартовыми индексами ind_i, ind_j и направлением диагонали diagonal_left_right_up_down.
       diagonal_left_right_up_down - направление извлечения чисел из диагонали. Стандартное значение True: диагональ слева направо сверху вниз. False: диагональ слева направо снизу вверх.
       Функция возвращает список значений заданной диагонали.
       Extraction of a diagonal from a two-dimensional array in accordance with the start indices ind_i, ind_j and the diagonal direction diagonal_left_right_up_down.
       diagonal_left_right_up_down - the direction of extraction of numbers from the diagonal. The default value is True: diagonal from left to right from top to bottom. False: diagonal from left to right from bottom to top.
       The function returns a list of values for the given diagonal.
    """
    diagonal_numbers = []
    if diagonal_left_right_up_down:
        limit_i = len(matrix2d)
        if ind_i == 0:
            limit_i = len(matrix2d) - ind_j
        while ind_i < limit_i:
            diagonal_numbers.append(matrix2d[ind_i][ind_j])
            ind_i += 1
            ind_j += 1
    else:
        limit_i = 0
        if ind_i == len(matrix2d) - 1:
            limit_i += ind_j
        while ind_i >= limit_i:
            diagonal_numbers.append(matrix2d[ind_i][ind_j])
            ind_i -= 1
            ind_j += 1
    return diagonal_numbers

def search_max_product_in_list_numbers(max_product, n, diagonal_numbers):
    """
       Поиск максимального произведения n - чисел в списке чисел.
       Search for the maximum product of n - numbers in the list of numbers.
    """
    i = 0
    while i <= len(diagonal_numbers) - n:
        current_product = 1
        for j in range(i, i + n):
            current_product *= diagonal_numbers[j]
        if current_product > max_product:
            max_product = current_product
        i += 1
    return max_product
    
def search_max_product_diagonals_in_matrix_2d(max_product, n, matrix2d):
    """
       Поиск максимального произведения n-чисел во всех диагоналях двумерного массива.
       Search for the maximum product of n-numbers in all diagonals of a two-dimensional array.
    """
    i = len(matrix2d) - n
    j = 0
    while j <= len(matrix2d[0]) - n:
        diagonal_numbers = extract_diagonal_numbers_from_matrix_2d(i, j, matrix2d)
        max_product = search_max_product_in_list_numbers(max_product, n, diagonal_numbers)
        if i:
            i -= 1
        else:
            j += 1
    i = n - 1
    j = 0
    while j <= len(matrix2d[0]) - n:
        diagonal_numbers = extract_diagonal_numbers_from_matrix_2d(i, j, matrix2d, False)
        max_product = search_max_product_in_list_numbers(max_product, n, diagonal_numbers)
        if i != len(matrix2d) - 1:
            i += 1
        else:
            j += 1
    return max_product

def max_all_product_in_matrix_2d(n):
    """
       Поиск максимального произведения n-чисел в двумерном массиве, расположенных в любом направлении (вверх, вниз, вправо, влево или по диагонали).
       Search for the maximum product of n-numbers in a two-dimensional array located in any direction (up, down, right, left or diagonally).
    """
    matrix2d = file_processing_set_of_number()
    max_product = search_max_product_vertical_in_matrix_2d(0, n, matrix2d)
    max_product = search_max_product_horizontal_in_matrix_2d(max_product, n, matrix2d)
    max_product = search_max_product_diagonals_in_matrix_2d(max_product, n, matrix2d)
    return max_product


def count_all_natural_divisors_of_number(number):
    """
       Функция подсчитывает общее количество натуральных делителей числа.
       The function counts the total number of natural divisors of a number.
    """
    count = 2
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            count += 2
    if number > 1:
        return count
    elif number == 1:
        return 1
    return 0

def generator_of_triangle_numbers():
    """
       Генератор треугольных чисел.
       Triangular number generator.
    """
    number = 1
    i = 1
    while True:
        yield number
        i += 1
        number += i


def triangular_number_with_a_large_number_of_divisors(limit):
    """
       Функция возвращает треугольное число, у которого количество делителей больше limit.
       The function returns a triangular number whose number of divisors is greater than limit.
    """
    gen_iter = generator_of_triangle_numbers()
    triangl_number = next(gen_iter)
    count = count_all_natural_divisors_of_number(triangl_number)
    while count <= limit:
        triangl_number = next(gen_iter)
        count = count_all_natural_divisors_of_number(triangl_number)
    return triangl_number

def file_processing_set_of_big_numbers():
    """
       Обработка файла set_of_big_numbers.txt с очень большими числами.
       Processing set_of_big_numbers.txt file with very large numbers.
    """
    list_of_big_numbers = []
    with open('set_of_big_numbers.txt') as all_big_numbers:
        for line in all_big_numbers:
            list_of_big_numbers.append(line.strip())
    return list_of_big_numbers

def sum_all_big_numbers():
    """
       Сумма всех больших чисел. Функция возвращает объект класса BigNumber, в котором значение суммы сохраненно в атрибуте big_number.
       The sum of all the big numbers. The function returns an object of class BigNumber in which the value of the sum is stored in the big_number attribute.
    """
    list_of_big_numbers = file_processing_set_of_big_numbers()
    object_with_sum = BigNumber('0')
    for i in list_of_big_numbers:
        object_with_sum = object_with_sum + BigNumber(i)
    return object_with_sum

def count_collatz_sequence(number, memory):
    """
       Функция вычисляет количество элементов последовательности Коллатца. number - это значение первого элемента последовательности.
       memory - это словарь первых элементов последовательностей и их количества.
       The function calculates the number of elements in the Collatz sequence. number is the value of the first element of the sequence.
       memory is a dictionary of the first elements of sequences and their quantity.
    """
    if number < 1:
        raise ValueError('The number must be a natural number')
    count = 0
    while number != 1:
        if number in memory:
            count += memory[number] - 1
            break
        if number % 2:
            number = 3 * number + 1
        else:
            number = number // 2
        count += 1
    return count + 1

def first_number_of_longest_Collatz_sequence(limit):
    """
       Функция вычисляет начало самой длинной последовательности Коллатца, начальный элемент которой меньше limit.
       The function calculates the beginning of the longest Collatz sequence, whose initial element is less than limit.
    """
    max_length = 0
    first_number = 1
    i = first_number
    memory = {}
    while i < limit:
        count = count_collatz_sequence(i, memory)
        memory[i] = count
        if count > max_length:
            max_length = count
            first_number = i
        i += 1
    return first_number



