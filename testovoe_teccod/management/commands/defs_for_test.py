
import math
from django.core.management import BaseCommand
#1. Написать функцию, которая принимает на вход список целых чисел и возвращает новый список, содержащий только уникальные элементы из исходного списка.
def def_dupl(data):##Ubiraem duplikati 
            index = 0
            a=[]
            while len(data) >index and data[index] not in a:
                   a.append(data[index])
                   index += 1
            index += 1
            print(a)
            return a
#2. Написать функцию, которая принимает на вход два целых числа (минимум и максимум) и возвращает список всех простых чисел в заданном диапазоне.
def if_prime_number(num):# Определим простое ли число
        index = 1
        while index-1 <= num:
            index += 1
            if num % index == 0 and num==index:
                # print(False)
                return False  
            if num % index == 0:  
                index+=1
                # print(True)
                return True
               
def def_prime_numbers(num_1, num_2):## На входе два числа (мал, боль) на выходе список простых чисел на интервале
    lst_prime_num = [i for i in range(num_1, num_2) if if_prime_number(i)==False]
    print(lst_prime_num)

#3. Создать класс Point, который представляет собой точку в двумерном пространстве. Класс должен иметь методы для инициализации координат точки, вычисления расстояния до другой точки, а также для получения и изменения координат.


class Point:
    def __init__(self,x_init,y_init):
        self.x = x_init
        self.y = y_init

    def shift(self, x, y):
        self.x += x
        self.y += y

    def __repr__(self):
        return "".join(["Point(", str(self.x), ",", str(self.y), ")"])

def distance(a, b):
    return math.sqrt((a.x-b.x)**2+(a.y-b.y)**2)

#4. Написать программу, которая сортирует список строк по длине, сначала по возрастанию, а затем по убыванию.
def len_for_sort(ss):
     return len(ss)
def sort_by_len_str(s):
    print(sorted(s, key=len_for_sort))
    print(sorted(s, key=len_for_sort, reverse=True))
     

class Command(BaseCommand):
   
    def handle(self, *args, **options):

        def_dupl([1,2,4,6,4])
        def_prime_numbers(1,10)
        if_prime_number(10)
        
        p1 = Point(10, 3)
        p2 = Point(1, 0)
        print(p1.x, p1.y, p2.x, p2.y)
        print(distance(p1,p2))

        p2.shift(2,3)

        print(p2)
        sort_by_len_str(['eqwf', 'eqrgfqekrvf', 'ekr', 'wkhbjvgeqvqev'])
