class PyQuerySelectorError(Exception):
    pass


class PyQuerySelector():

    def __init__(self):
        self.elements = []

    def addElement(self, tkElement, idElement: str):
        for e in self.elements:
            print(e[0] == "#" + idElement)
            if (e[0] == "#" + idElement):
                raise PyQuerySelectorError(
                    "'" + idElement + "' is already used")

        return self.elements.append(["#" + idElement, tkElement])

    def getElement(self, idElement: str):
        for e in self.elements:
            if (e[0] == "#" + idElement):
                return e[1]

        raise PyQuerySelectorError("'" + idElement + "' is not defined")

    def dropElement(self, idElement: str):
        for index, e in enumerate(self.elements):
            if (e[0] == "#" + idElement):
                del self.elements[index]
                return 0

        raise PyQuerySelectorError("'" + idElement + "' is not defined")
