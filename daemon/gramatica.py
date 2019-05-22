"""
    objeto de retorno
    {
    "gramatica-nao-terminal": "A, B",
    "gramatica-terminal": "a, b",
    "gramatica-inicial": "S",
    "producao": [
        {
            "id": 1,
            "esquerda": "A",
            "direita": "AB"
        },
        {
            "id": 2,
            "esquerda": "BB",
            "direita": "C"
        }]
    }
"""
#           N - conjunto finito de não-terminais (ou variáveis)  {}
#           T - conjunto finito de terminais {}
#           P - conjunto finito de regras de produção
#           S - símbolo inicial da gramática

sentenca_vazia = "&"


def verifica(object_from_view):
    objeto_flags = {
        "is_gram_irrestrita": 1,
        "is_gram_sensivel": 1,
        "is_gram_livre": 1,
        "is_gram_regular": 1
    }
    for product in object_from_view["producao"]:
        if (objeto_flags["is_gram_irrestrita"] > 0):
            if (not (is_gram_irrestrita(product["esquerda"], product["direita"], object_from_view))):
                objeto_flags["is_gram_irrestrita"] = 0

        if (objeto_flags["is_gram_sensivel"] > 0):
            if (not (is_gram_sensivel(product["esquerda"], product["direita"]))):
                objeto_flags["is_gram_sensivel"] = 0

        if (objeto_flags["is_gram_livre"] > 0):
            if (not (is_gram_livre(product["esquerda"], product["direita"], object_from_view))):
                objeto_flags["is_gram_livre"] = 0

        if (objeto_flags["is_gram_regular"] > 0):
            if (not (is_gram_regular(product["esquerda"], product["direita"], object_from_view))):
                objeto_flags["is_gram_regular"] = 0

    if (objeto_flags["is_gram_irrestrita"] > 0):
        objeto_flags["is_gram_irrestrita"] = 2

    if (objeto_flags["is_gram_sensivel"] > 0):
        objeto_flags["is_gram_sensivel"] = 2

    if (objeto_flags["is_gram_livre"] > 0):
        objeto_flags["is_gram_livre"] = 2

    if (objeto_flags["is_gram_regular"] > 0):
        objeto_flags["is_gram_regular"] = 2

    # print(objeto_flags)
    if objeto_flags["is_gram_regular"] == 2:
        return type_and_enums_gramatica(3)
    elif objeto_flags["is_gram_livre"] == 2:
        return type_and_enums_gramatica(2)
    elif objeto_flags["is_gram_sensivel"] == 2:
        return type_and_enums_gramatica(1)
    elif objeto_flags["is_gram_irrestrita"] == 2:
        return type_and_enums_gramatica(0)

    return "Não foi identificado nenhum tipo de gramática"
    # return objeto_flags


def is_gram_irrestrita(lado_esquerdo, lado_direito, object_from_view):  # 0
    for char in lado_esquerdo:
        if (char in object_from_view["gramatica-nao-terminal"]):
            return True
    return False


def is_gram_sensivel(lado_esquerdo, lado_direito):  # 1
    return True if ((len(lado_esquerdo) <= len(lado_direito)) and (
            len(lado_direito) >= len(lado_esquerdo) and not (sentenca_vazia in lado_direito))) else False


def is_gram_livre(lado_esquerdo, lado_direito, object_from_view):  # 2
    possui_N = False
    for char in lado_esquerdo:
        if (char in object_from_view["gramatica-nao-terminal"]):
            if (possui_N != True):
                possui_N = True
            else:
                return False
    return True if ((possui_N == True) and (not (sentenca_vazia in lado_direito))) else False


def is_gram_regular(lado_esquerdo, lado_direito, object_from_view):  # 3
    # lado esquerdo
    possui_N = False
    for char in lado_esquerdo:
        if (char in object_from_view["gramatica-nao-terminal"]):
            if (possui_N == True):
                return False
            possui_N = True
    # lado direito
    for index, char in enumerate(lado_direito):
        if (len(lado_direito) > 2):
            return False
        if (not (char in object_from_view["gramatica-terminal"])):
            return False
        elif (not (lado_direito[index + 1] in object_from_view["gramatica-terminal"])):
            return False
    return True if (possui_N) else False


def type_and_enums_gramatica(num_tipo):
    type_num_name = {
        0: "Gramática Irrestrita - GI",
        1: "Gramática Sensível ao contexto - GSC",
        2: "Gramática Livre de Contexto - GLC",
        3: "Gramática Regular - GR"
    }
    return type_num_name[num_tipo]
