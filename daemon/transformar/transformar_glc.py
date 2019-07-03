class transformation:
    count_nao_terminal = 0
    sentenca_vazia = "&"

    def __init__(self, object_from_view):
        producoes = {}
        for prod in object_from_view["producao"]:
            producoes.update({prod["esquerda"]: prod["direita"].split("|")})
        self.elimina_producoes_vazias(producoes)
        self.recursao_a_esquerda(producoes)

    def elimina_producoes_vazias(self, producoes):
        conjunto_var_leva_vazio = []
        for producao in producoes:
            if (self.sentenca_vazia in producoes[producao]):
                conjunto_var_leva_vazio.append(producao)
                producoes[producao] = producoes[producao][producoes[producao].index(
                    self.sentenca_vazia)] = producao
        if(len(conjunto_var_leva_vazio > 0)):
            for producao in producoes[producao]:
                if conjunto_var_leva_vazio[0] in producoes[producao]:
                    conjunto_var_leva_vazio.append(producao)
            for producao in producoes:
                for index, elemento in enumerate(producoes[producao]):
                    for char in elemento:
                        if (char in conjunto_var_leva_vazio):
                            producoes[producao][index].append(elemento.replace(char, ""))

    def elimina_producoes_unitarias(self, producoes):

        pass

    def elimina_simbolos_inuteis(self, producoes):
        pass

    def fatoracao(self, producoes):
        pass

    def recursao_a_esquerda(self, producoes):
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

        return producoes

    def resolve_ambiguidade(self):  # opcional, nem fudendo q a gente vai fazer
        pass

    def get_non_terminal_value(self):
        self.count_nao_terminal += 1
        return self.count_nao_terminal
