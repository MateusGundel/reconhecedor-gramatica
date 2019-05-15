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
        # self.object_from_view["gramatica-nao-terminal"] - conjunto finito de não-terminais (ou variáveis)  {}
        # T - conjunto finito de terminais {}
        # P - conjunto finito de regras de produção
        # S - símbolo inicial da gramática


class Functions:
    sentenca_vazia = "&"

    def __init__(self, object_from_view):
        self.object_from_view = object_from_view
        self.process()

    def process(self):
        print(self.object_from_view)
        self.verifica_gramatica()

    def verifica_gramatica(self):
        objeto_flags = {
            "is_gram_irrestrita": 1,
            "is_gram_sensivel": 1,
            "is_gram_livre": 1,
            "is_gram_regular": 1
        }
        for product in self.object_from_view["producao"]:
            if(objeto_flags["is_gram_irrestrita"] > 0):
                if(not(self.is_gram_irrestrita(product["esquerda"], product["direita"]))):
                    objeto_flags["is_gram_irrestrita"] = 0

            if(objeto_flags["is_gram_sensivel"] > 0):
                if(not(self.is_gram_sensivel(product["esquerda"], product["direita"]))):
                    objeto_flags["is_gram_sensivel"] = 0

            if(objeto_flags["is_gram_livre"] > 0):
                if(not(self.is_gram_livre(product["esquerda"], product["direita"]))):
                    objeto_flags["is_gram_livre"] = 0

            if(objeto_flags["is_gram_regular"] > 0):
                if(not(self.is_gram_regular(product["esquerda"], product["direita"]))):
                    objeto_flags["is_gram_regular"] = 0

        if(objeto_flags["is_gram_irrestrita"] > 0):
           objeto_flags["is_gram_irrestrita"] = 2

        if(objeto_flags["is_gram_sensivel"] > 0):
            objeto_flags["is_gram_sensivel"] = 2

        if(objeto_flags["is_gram_livre"] > 0):
            objeto_flags["is_gram_livre"]=2

        if(objeto_flags["is_gram_regular"] > 0):
            objeto_flags["is_gram_regular"]=2

        print(objeto_flags)
        return objeto_flags



    def is_gram_irrestrita(self, lado_esquerdo, lado_direito):  # 0
        for char in lado_esquerdo:
            if (char in self.object_from_view["gramatica-nao-terminal"]):
                return True
        return False

    def is_gram_sensivel(self, lado_esquerdo, lado_direito):  # 1
        return True if ((len(lado_esquerdo) <= len(lado_direito)) and (len(lado_direito) >= len(lado_esquerdo) and not(self.sentenca_vazia in lado_direito))) else False

    def is_gram_livre(self, lado_esquerdo, lado_direito):  # 2
        possui_N=False
        for char in lado_esquerdo:
            if (char in self.object_from_view["gramatica-nao-terminal"]):
                if(possui_N == True):
                    return False
                possui_N=True
        return True if ((possui_N == True) and (not(self.sentenca_vazia in lado_direito))) else False

    def is_gram_regular(self, lado_esquerdo, lado_direito):  # 3
        # lado esquerdo
        possui_N=False
        for char in lado_esquerdo:
            if (char in self.object_from_view["gramatica-nao-terminal"]):
                if(possui_N == True):
                    return False
                possui_N=True
        # lado direito


    def type_and_enums_gramatica(self, num_tipo):
        type_num_name={
            0: "Gramática Irrestrita - GI",
            1: "Gramática Sensível ao contexto - GSC",
            2: "Gramática Livre de Contexto - GLC",
            3: "Gramática Regular - GR"
        }
        return type_num_name[num_tipo]
