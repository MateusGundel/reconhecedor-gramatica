import json
import daemon.gramatica as gramatica
import daemon.consistencia as consistencia


class Functions:

    def __init__(self):
        pass

    def process(self, object_from_view):
        consistencia.verifica(object_from_view)
        gramatica.verifica(object_from_view)
