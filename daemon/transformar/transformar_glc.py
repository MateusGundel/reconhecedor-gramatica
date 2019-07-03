class transformation:
    count_nao_terminal = 0
    sentenca_vazia = "&"
    producoes = {}

    def __init__(self, object_from_view):
        self.producoes = {}
        for prod in object_from_view["producao"]:
            self.producoes.update({prod["esquerda"]: prod["direita"].replace(" ", "").split("|")})
        print(self.producoes)
        self.elimina_producoes_vazias()
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
        pass

    def elimina_simbolos_inuteis(self):
        pass

    def fatoracao(self):
        pass

    def recursao_a_esquerda(self):
        producoes = self.producoes
        list_recursoes = []
        new_variable = None
        for producao in producoes:
            for word in producoes[producao]:
                for letter in word:
                    for prod2 in producoes:
                        if letter == prod2 and producao != prod2:
                            for word2 in producoes[prod2]:
                                for letter2 in word2:
                                    if letter2 == letter and letter2 != word2:
                                        list_recursoes.append((prod2,producao))

        for recursao in list_recursoes:
            for index, producao in enumerate(producoes[recursao[0]]):
                if recursao[1] in producao:
                    for p in producoes[recursao[1]]:
                        producoes[recursao[0]].pop(index)
                        new_variable = "V"+str(self.get_non_terminal_value())
                        producoes.update({new_variable:[(p+producao.replace(recursao[1], ""))
                                         .replace(recursao[0], "")+new_variable, "&"]})
        if new_variable is not None:
            for index, producao in enumerate(producoes[recursao[0]]):
                producoes[recursao[0]][index] = producoes[recursao[0]][index]+new_variable

        self.producoes = producoes

    def resolve_ambiguidade(self):  # opcional, nem fudendo q a gente vai fazer
        pass

    def get_non_terminal_value(self):
        self.count_nao_terminal += 1
        return self.count_nao_terminal
