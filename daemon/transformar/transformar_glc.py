class transformation:
    count_nao_terminal = 0
    sentenca_vazia = "&"
    producoes = {}
    terminais = []
    nao_terminais = []
    gramatica_inicial = ""


    def __init__(self, object_from_view):
        self.producoes = {}
        self.terminais = object_from_view["gramatica-nao-terminal"].replace(" ", "").split(",")
        self.nao_terminais = object_from_view["gramatica-terminal"].replace(" ", "").split(",")
        self.gramatica_inicial = object_from_view["gramatica-inicial"]

        for prod in object_from_view["producao"]:
            self.producoes.update({prod["esquerda"]: prod["direita"].replace(" ", "").split("|")})
        print(self.producoes)
        self.elimina_producoes_vazias()
        print(self.producoes)
        self.elimina_producoes_unitarias()
        print(self.producoes)
        self.elimina_simbolos_inuteis()
        print(self.producoes)
        self.fatoracao()
        print(self.producoes)
        self.recursao_a_esquerda()
        print(self.producoes)

    def elimina_producoes_vazias(self):
        conjunto_var_leva_vazio = []
        for producao in self.producoes:
            if (self.sentenca_vazia in self.producoes[producao]):
                conjunto_var_leva_vazio.append(producao)
                self.producoes[producao].remove(self.sentenca_vazia)
        if(len(conjunto_var_leva_vazio) > 0):
            for producao in self.producoes:
                if (conjunto_var_leva_vazio[0] in self.producoes[producao]):
                    conjunto_var_leva_vazio.append(producao)
            for producao in self.producoes:
                for elemento in self.producoes[producao]:
                    for char in elemento:
                        if (char in conjunto_var_leva_vazio):
                            self.producoes[producao].append(elemento.replace(char, ""))
        
    def elimina_producoes_unitarias(self):
        for producao in self.producoes:
            for index, elemento in enumerate(self.producoes[producao]):
                if((len(elemento) == 1) and (elemento in self.nao_terminais)):
                    del self.producoes[producao][index]
                    for producao_var_unica in self.producoes[elemento]:
                        if(not(producao_var_unica in self.producoes[producao])):
                            self.producoes[producao].append(producao_var_unica)

    def elimina_simbolos_inuteis(self):
        pass

    def fatoracao(self):
        pass

    def recursao_a_esquerda(self):
        producoes = self.producoes
        for producao in producoes:
            for word in producoes[producao]:
                for letter in word:
                    for prod2 in producoes:
                        if letter == prod2 and producao != prod2:
                            for word2 in producoes[prod2]:
                                for letter2 in word2:
                                    if letter2 == letter and letter2 != word2:
                                        print(producoes[prod2])
                                        print(prod2)

        self.producoes = producoes

    def resolve_ambiguidade(self):  # opcional, nem fudendo q a gente vai fazer
        pass

    def get_non_terminal_value(self):
        self.count_nao_terminal += 1
        return self.count_nao_terminal
