import numpy as np
from ClaseNodo import Nodo
class Cola:
    __lista=None

    def __init__(self):
        self.__lista=None

    def insertar(self, dato):
        if self.__lista is None:
            nodo = 