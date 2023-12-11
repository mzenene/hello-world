class Umbhuliso():
    def __init__(self,igama,iminyaka,ilizwe):
        self.igama=igama
        self.iminyaka=iminyaka
        self.ilizwe=ilizwe

    def veza(igama,iminyaka,ilizwe):
        if(igama!=""):
            print(f"Molo {igama} uneminyaka eyi{iminyaka} uvela kwilizwe lase {ilizwe}")
        else:
            print(f"Yazi uwuva ! ndithe kuwe ubhale igama,iminyaka nendawo uvela kuyo")
