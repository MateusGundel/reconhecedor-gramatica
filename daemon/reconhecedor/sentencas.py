import re
import random

index_usage = {}


def generate(object_from_view):
    result_list = {}

    result_list.update({1: get_uma_sentenca(object_from_view, result_list)})
    result_list.update({2: get_uma_sentenca(object_from_view, result_list)})
    result_list.update({3: get_uma_sentenca(object_from_view, result_list)})

    return result_list


def get_uma_sentenca(object_from_view, result_list):
    regex = re.compile("[A-Z]")
    initial_result = get_result_production(object_from_view['producao'],
                                           object_from_view['gramatica-inicial'],
                                           0,
                                           regex)
    regex = re.compile("[A-Z]")
    continuar = 0
    while continuar < 20:
        final_result = ""
        foi_uma_vez = False
        for item in initial_result:
            if len(re.findall(regex, item)) > 0 and not foi_uma_vez:
                item = get_result_production(object_from_view['producao'], item, continuar, regex)
                foi_uma_vez = True

            final_result = final_result + item
        initial_result = final_result
        continuar += 1
        if len(re.findall(regex, final_result)) <= 0:
            if initial_result in result_list.values():
                continuar = 0
                initial_result = get_result_production(object_from_view['producao'],
                                                       object_from_view['gramatica-inicial'],
                                                       0,
                                                       regex)
            else:
                return initial_result
    return final_result


def get_result_production(object, finder, iteractions, regex):
    if len(object) > 1:
        if random.randrange(0, 2) == 1:
            object = list(reversed(object))

    for production in object:
        production_direita = str(production['direita']).replace(" ", "").split("|")
        for item in str(production['esquerda']).replace(" ", "").split("|"):
            if finder is item:
                if len(production_direita) > 1:
                    if iteractions < 10:
                        return str(production_direita[random.randrange(0, len(production_direita))])
                    else:
                        for retorno in production_direita:
                            if len(re.findall(regex, retorno)) <= 0:
                                return retorno
                        return str(production_direita[random.randrange(0, len(production_direita))])
                else:
                    return str(production_direita[0])