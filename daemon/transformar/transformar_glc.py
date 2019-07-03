def __start__(object_from_view):
    producoes = {}
    for prod in object_from_view["producao"]:
        producoes.update({prod["esquerda"]:prod["direita"].split("|")})
    elimina_producoes_vazias(producoes)

def elimina_producoes_vazias(producoes):
    for producao in producoes:
        print(str(producao) + " : "+str(producoes[producao]))
def elimina_producoes_unitarias():
    pass
def elimina_simbolos_inuteis():
    pass
def fatoracao():
    pass
def recursao_a_esquerda():
    pass
def resolve_ambiguidade(): #opcional, nem fudendo q a gente vai fazer
    pass