import json
import daemon.gramatica as gramatica


class Functions:

    def __init__(self):
        pass

    def process(self, object_from_view):
        gramatica.verifica(object_from_view)
