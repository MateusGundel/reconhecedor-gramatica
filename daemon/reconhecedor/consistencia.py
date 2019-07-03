import re


def verifica(object_from_view):
    lista = []
    lista.append(verifica_entrada_gramatica(object_from_view))
    lista.append(verifica_entrada_producao(object_from_view))
    print(lista)
    for (valido, text) in lista:
        if not valido:
            return valido, text
    return True, ""

def verifica_entrada(regex, objects):
    if not len(re.findall(regex, objects)) == len(objects):
        return False


def verifica_entrada_gramatica(object_from_view):
    if str(object_from_view['gramatica-terminal']).endswith(","):
        return False, "Termina com vírgula"
    if verifica_entrada(re.compile("[a-z, &]"), object_from_view['gramatica-terminal']):
        return False, "Terminal deve possuir somente letras Maiúscula e \",\""
    if verifica_entrada(re.compile("[A-Z, ]"), object_from_view['gramatica-nao-terminal']):
        return False, "Não terminal deve possuir somente letras minúsculas e \",\""
    if verifica_entrada(re.compile("[A-Z]"), object_from_view['gramatica-inicial']):
        return False, "Letra inicial deve possuir somente letra uma minúsculas"
    return True, ""


def verifica_entrada_producao(object_from_view):
    non_terminal = str(object_from_view['gramatica-nao-terminal']).replace(" ", "").replace("|", "")
    terminal = str(object_from_view['gramatica-terminal']).replace(" ", "").replace("|", "")
    for production in object_from_view['producao']:
        if "," in production['direita'] or "," in production['esquerda']:
            return False, "Deve ser utilizado \"|\" para separar as produções ao invés de \",\""
        for item in str(production['esquerda']).replace(",", "").replace(" ", ""):
            if not item in terminal and not item in non_terminal:
                return False, "A Gramática não possui o não terminal \"" + item + "\" que está na produção"
        for item in str(production['direita']).replace(",", "").replace(" ", "").replace("|", ""):
            if not item in terminal and not item in non_terminal:
                return False, "A Gramática não possui o terminal \"" + item + "\" que está na produção"
    return True, ""
