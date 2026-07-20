class NoArvoreNaria:
    def __init__(self, info):
        self.info = info
        self.prim = None
        self.prox = None

    # getters e setters
    def get_info(self):
        return self.info

    def set_info(self, info):
        self.info = info

    def get_prim(self):
        return self.prim

    def set_prim(self, prim):
        self.prim = prim

    def get_prox(self):
        return self.prox

    def set_prox(self, prox):
        self.prox = prox