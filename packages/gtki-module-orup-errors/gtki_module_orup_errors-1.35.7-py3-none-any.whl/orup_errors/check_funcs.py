""" Содержит все функции проверок для алертов из модуля all_errors"""


def check_car_number(car_number, *args, **kwargs):
    if check_len(car_number) or not is_car_num_valid(car_number):
        return True


def check_len(car_number):
    if len(car_number) < 8 or len(car_number) > 10:
        return True


def is_car_num_valid(car_number):
    """ Провекра валидности гос.номер """
    import re
    usual = re.match(
        '^[АВЕКМНОРСТУХ]\d{3}(?<!000)[АВЕКМНОРСТУХ]{2}\d{2,3}$',
        car_number)
    trailer = re.match('[АВЕКМНОРСТУХ]{2}\d{4}(?<!0000)\d{2,3}$',
                       car_number)
    agro = re.match('^\d{4}(?<!0000)[АВЕКМНОРСТУХ]{2}\d{2,3}$', car_number)
    if usual or trailer or agro:
        print('Valid True')
        return True


def check_car_has_rfid(have_rfid, choose_mode, comment, chosen_trash_cat,
                       *args, **kwargs):
    if have_rfid and choose_mode == 'manual' and len(comment) < 1 \
            and chosen_trash_cat == 'ТКО':
        return True


def check_scale_fail(weight_data: int, aliquot=10, *args, **kwargs):
    """ Проверить весы на работоспособность. Обычно WeightDataSplitter возвращает коды ошибок, не кратные 10."""
    if weight_data % aliquot != 0:
        return True


def check_brutto_on_exit(course: str, have_brutto: bool, car_protocol: str,
                         chosen_trash_cat, *args, **kwargs):
    if not have_brutto and course == "OUT" and chosen_trash_cat == 'ТКО':
        return True


def check_brutto_having_brutto(course: str, have_brutto: bool,
                               car_protocol: str, tko_protocol='rfid', *args,
                               **kwargs):
    if have_brutto and course == 'IN' and car_protocol == tko_protocol:
        return True


def check_carrier_incorrectness(carrier_name: str, carriers_list: list, *args,
                                **kwargs):
    return check_type_incorrectness(carrier_name, carriers_list)


def check_object_incorrectness(object_name: str, objects_list: list, *args,
                               **kwargs):
    return check_type_incorrectness(object_name, objects_list)


def check_platform_incorrectness(object_name: str, platforms_list: list, *args,
                               **kwargs):
    return check_type_incorrectness(object_name, platforms_list)

def check_tc_incorrectness(chosen_trash_cat, cats_list, *args, **kwargs):
    return check_type_incorrectness(chosen_trash_cat, cats_list)


def check_tt_incorrectness(type_name: str, types_list: list, *args, **kwargs):
    return check_type_incorrectness(type_name, types_list)


def check_carrier_debtor(carrier_name: str, client_name: str, debtors_list: list, comment, *args,
                         **kwargs):
    for debtor_l in debtors_list:
        if len(comment) < 1 and (check_type_correctness(carrier_name,
                                                       debtor_l[0]) or
                                 check_type_correctness(client_name,
                                                       debtor_l[0])):
            return debtor_l[1]


def check_type_correctness(given: any, list_name: list, *args, **kwargs):
    """ Проверить факт нахождение элемента given в list_name """
    if given in list_name:
        return True


def check_type_incorrectness(given: any, list_name: list, *args, **kwargs):
    """ Проверить факт НЕ нахождение элемента given в list_name """
    if given not in list_name:
        return True


def check_ar_busy(ar_status: bool, busy_status=False, *args, **kwargs):
    if ar_status == busy_status:
        return True


def other_instead_tko(chosen_trash_cat: str, tko_name='ТКО-4',
                      must_be_tko=False, *args, **kwargs):
    """ Указали какую то категорию груза, а рейс c ТКО (tko_name) был запланирован """
    if chosen_trash_cat != tko_name and must_be_tko:
        return True


def tko_instead_other(chosen_trash_cat: str, tko_name='ТКО-4',
                      must_be_tko=False, *args, **kwargs):
    """ Указали ТКО (tko_name), а рейс не был запланирован """
    if chosen_trash_cat == tko_name and not must_be_tko:
        return True


def tko_not_allowed(chosen_trash_cat, client_name, carrier_name: str, clients, *args,
                    **kwargs):
    """ Указали ТКО (tko_name), а перевозчик не перевозит ТКО """
    try:
        tko_carrier = clients[carrier_name]['tko_carrier']
        tko_client = clients[client_name]['tko_carrier']
    except KeyError:
        return
    if not (tko_client or tko_carrier) and chosen_trash_cat=='ТКО':
        return True
