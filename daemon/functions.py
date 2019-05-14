import json

class Functions:
    sentenca_vazia = "&"
    def __init__(self):
        pass
    def process(self, array_from_view):
        print(array_from_view)
        return "meu ovo esquerdo"
    def verifica_entrada(self, N, T, P, S, producoes):
    #N - conjunto finito de não-terminais (ou variáveis)  {}
    #T - conjunto finito de terminais {}
    #P - conjunto finito de regras de produção
    #S - símbolo inicial da gramática
        pass
    def is_gram_irrestrita(self, lado_esquerdo, lado_direito, N): #0
        return True if (lado_esquerdo in N) else False
    def is_gram_sensivel(self, lado_esquerdo, lado_direito): #1
        return True if ((len(lado_esquerdo) <= len(lado_direito)) and (len(lado_direito) >= len(lado_esquerdo) and not(self.sentenca_vazia in lado_direito))) else False
    def is_gram_livre(self): #2
        pass
    def is_gram_regular(self): #3
        pass

    def type_and_enums_gramatica(self, num_tipo):
        type_num_name= {
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