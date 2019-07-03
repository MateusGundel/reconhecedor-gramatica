class transformation:
    count_nao_terminal = 0

    def __init__(self, object_from_view):
        producoes = {}
        for prod in object_from_view["producao"]:
            producoes.update({prod["esquerda"]: prod["direita"].split("|")})
        self.elimina_producoes_vazias(producoes)
        self.recursao_a_esquerda(producoes)

    def elimina_producoes_vazias(self, producoes):
        for producao in producoes:
            print(str(producao) + " : " + str(producoes[producao]))

    def elimina_producoes_unitarias(self, producoes):

        pass

    def elimina_simbolos_inuteis(self, producoes):
        pass

    def fatoracao(self, producoes):
        pass

    def recursao_a_esquerda(self, producoes):
        for producao in producoes:
            for word in producoes[producao]:
                print(    self.get_non_terminal_value())
        pass

    def resolve_ambiguidade(self):  # opcional, nem fudendo q a gente vai fazer
        pass

    def get_non_terminal_value(self):
        self.count_nao_terminal += 1
        return self.count_nao_terminal
