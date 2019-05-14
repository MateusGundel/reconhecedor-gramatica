class Functions:
    def __init__(self):
        pass
    def process(self, array_from_view):
        return "meu ovo esquerdo"
    def verifica_entrada(self, N, T, P, S, producoes):
    #N - conjunto finito de não-terminais (ou variáveis)  {}
    #T - conjunto finito de terminais {}
    #P - conjunto finito de regras de produção
    #S - símbolo inicial da gramática
        pass
    def is_gram_irrestrita(self): #0
        pass
    def is_gram_sensivel(self, N, T, P): #1
        #if(len(N) <= )
        pass
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