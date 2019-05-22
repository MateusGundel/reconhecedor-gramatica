import re


def verifica(object_from_view):
    lista = []
    lista.append(verifica_entrada_gramatica(object_from_view))
    lista.append(verifica_entrada_producao(object_from_view))
    print(lista)


def verifica_entrada(regex, objects):
    if not len(re.findall(regex, objects) == len(objects)):
        return False


def verifica_entrada_gramatica(object_from_view):
    if str(object_from_view['gramatica-terminal']).endswith(","):
        return False, "Termina com vírgula"
    regex_terminal = re.compile("[a-z, &]")
    regex_non_terminal = re.compile("[A-Z, ]")
    regex_inicial = re.compile("[A-Z]")
    if not len(re.findall(regex_terminal, object_from_view['gramatica-terminal'])) == len(
            object_from_view['gramatica-terminal']):
        return False, "Terminal deve possuir somente letras Maiúscula e \",\""
    if not len(re.findall(regex_non_terminal, object_from_view['gramatica-nao-terminal'])) == len(
            object_from_view['gramatica-nao-terminal']):
        return False, "Não terminal deve possuir somente letras minúsculas e \",\""
    if not len(re.findall(regex_inicial, object_from_view['gramatica-inicial'])) == len(
            object_from_view['gramatica-inicial']):
        return False, "Letra inicial deve possuir somente letra uma minúsculas"
    return True


def verifica_entrada_producao(object_from_view):
    non_terminal = str(object_from_view['gramatica-nao-terminal']).replace(" ", "").replace(",", "").replace("|", "")
    terminal = str(object_from_view['gramatica-terminal']).replace(" ", "").replace(",", "").replace("|", "")
    list_esquerda = []
    for production in object_from_view['producao']:
        print(list_esquerda)
        for item in str(production['esquerda']).replace(",", "").replace(" ", ""):
            if not item in non_terminal:
                return False, "A Gramática não possui o não terminal " + item + " da produção"
        for item in str(production['direita']).replace(",", "").replace(" ", ""):
            if not item in terminal and not item in non_terminal:
                return False, "A Gramática não possui o terminal " + item + " da produção"
    return True
