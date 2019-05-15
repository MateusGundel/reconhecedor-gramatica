import json

"""
    objeto de retorno
    {
    "gramatica-terminal": "A, B",
    "gramatica-nao-terminal": "a, b",
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


class Functions:
    sentenca_vazia = "&"

    def __init__(self, object_from_view):
        self.object_from_view = object_from_view
        self.process()

    def process(self):
        print(self.object_from_view)
        return "meu ovo esquerdo"

    def verifica_entrada(self, N, T, P, S, producoes):
        # N - conjunto finito de não-terminais (ou variáveis)  {}
        # T - conjunto finito de terminais {}
        # P - conjunto finito de regras de produção
        # S - símbolo inicial da gramática
        pass

    def is_gram_irrestrita(self, lado_esquerdo, lado_direito, N):  # 0
        possui_N = False
        for char in lado_esquerdo:
            if (char in N):
                return True
        return False

    def is_gram_sensivel(self, lado_esquerdo, lado_direito):  # 1
        return True if ((len(lado_esquerdo) <= len(lado_direito)) and (len(lado_direito) >= len(lado_esquerdo) and not(self.sentenca_vazia in lado_direito))) else False

    def is_gram_livre(self, lado_esquerdo, lado_direito, N):  # 2
        possui_N = False
        for char in lado_esquerdo:
            if (char in N):
                if(possui_N == True):
                    return False
                possui_N = True
        return True if ((possui_N == True) and (not(self.sentenca_vazia in lado_direito))) else False

    def is_gram_regular(self, lado_esquerdo, lado_direito, N):  # 3
        possui_N = False
        for char in lado_esquerdo:
            if (char in N):
                if(possui_N == True):
                    return False
                possui_N = True

    def type_and_enums_gramatica(self, num_tipo):
        type_num_name = {
            0: "Gramática Irrestrita - GI",
            1: "Gramática Sensível ao contexto - GSC",
            2: "Gramática Livre de Contexto - GLC",
            3: "Gramática Regular - GR"
        }
        return type_num_name[num_tipo]


"""     [
        {
            "direita": "S",
            "esquerda": "TT"
        }
    ] """
