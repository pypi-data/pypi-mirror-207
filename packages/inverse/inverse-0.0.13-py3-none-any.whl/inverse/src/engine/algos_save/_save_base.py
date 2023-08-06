from inverse.src.classes.abstract_data import id_ekle, DataAbstract
from inverse.src.utils.inverse_typings import npar


# from inverse.src.classes.db_ops import DB_class_Opt


def base_save_on_begin_rand(self: DataAbstract, matrix: npar) -> None:
    say = -1
    big_list = []
    part_say = -1
    for i in range(len(matrix)):
        numbers = list(matrix[i])  # list(random.randint(0, 100) for _ in range(n))
        numbers += id_ekle(i, len(matrix))
        if len(big_list) == self.threshold:
            say = 0
            part_say += 1
            self.save_part(part_say, big_list)
            big_list = [numbers]
        else:
            say += 1
            big_list.append(numbers)
    if big_list:
        part_say += 1
        self.save_part(part_say, big_list)


def base_save_on_begin_rand_yedek(self: DataAbstract, matrix: npar) -> None:
    say = -1
    big_list = []

    for i in range(len(matrix)):
        numbers = list(matrix[i])  # list(random.randint(0, 100) for _ in range(n))
        numbers += id_ekle(i, len(matrix))
        if len(big_list) == self.threshold:
            say += 1
            self.save_part(say, big_list)
            big_list = [numbers]
        else:
            big_list.append(numbers)
    if big_list:
        say += 1
        self.save_part(say, big_list)
