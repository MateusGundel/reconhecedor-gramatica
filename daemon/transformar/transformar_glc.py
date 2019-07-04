class transformation:
    count_nao_terminal = 0
    sentenca_vazia = "&"
    producoes = {}
    terminais = []
    nao_terminais = []
    gramatica_inicial = ""

    def __init__(self, object_from_view):
        print(object_from_view)
        self.producoes = {}
        self.terminais = object_from_view["gramatica-terminal"].replace(" ", "").split(",")
        self.nao_terminais = object_from_view["gramatica-nao-terminal"].replace(" ", "").split(",")
        self.gramatica_inicial = object_from_view["gramatica-inicial"]
        for prod in object_from_view["producao"]:
            self.producoes.update({prod["esquerda"]: prod["direita"].replace(" ", "").split("|")})
        #print(self.producoes)
        self.elimina_producoes_vazias()
        #print(self.producoes)
        self.elimina_producoes_unitarias()
        #print(self.producoes)
        self.elimina_simbolos_inuteis()
        #print(self.producoes)
        #self.fatoracao()
        #print(self.producoes)
        #self.recursao_a_esquerda()
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
        for elemento in self.nao_terminais:
            is_in_a_prod = False
            for producao in self.producoes:
                if (elemento == producao):
                    continue
                else:
                    for node in self.producoes[producao]:
                        if (elemento in node):
                            is_in_a_prod = True
            if(not(is_in_a_prod)):
                del self.producoes[elemento]

    def fatoracao(self):
        for producao in self.producoes:
            list_prod_recursividade = []
            for elemento in enumerate(self.producoes[producao]):
                for elemento_comp in self.producoes[producao]:
                    if(elemento == elemento_comp):
                        continue
                    elif(elemento[0] == elemento_comp[0]):
                        list_prod_recursividade.append(elemento)
                        new_variable = str(self.get_non_terminal_value())
                        #self.producoes.update({new_variable: [elemento, elemento_comp])
                        
        #count = 0
        # letters = []
        # for producao in self.producoes:
        #     for word in self.producoes[producao]:
        #         for letter in word:
        #             if letter in self.nao_terminais:
        #                 letters.append({"letter":letter, "word":word, "producao":producao})
        # for item in letters:
        #     for item2 in letters:
        #         if item["letter"] == item2["letter"] and item["producao"] != item2["producao"]:
                    
                    # print("B-------------- "+str(item["letter"])+ "  "+str(item["word"])+"  "+ str(item["producao"]))
                    # print("2--------- "+str(item2["letter"])+ "  "+str(item2["word"])+"  "+ str(item2["producao"]))


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
                        new_variable = str(self.get_non_terminal_value())
                        producoes.update({new_variable:[(p+producao.replace(recursao[1], "")).replace(recursao[0], "")+new_variable, "&"]})
        if new_variable is not None:
            for index, producao in enumerate(producoes[recursao[0]]):
                producoes[recursao[0]][index] = producoes[recursao[0]][index]+new_variable
        self.producoes = producoes

    def resolve_ambiguidade(self): #opcional
        pass

    def get_non_terminal_value(self):
        self.count_nao_terminal += 1
        return self.count_nao_terminal

    def get_producoes(self):
        return self.producoes
