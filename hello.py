import classes
# method will prompt the user to enter name,age and country and will initialize 
# and return them as object of class Umbhuliso
def buza():
     igama = input("Ungubani?: ")
     iminyaka =input("Uneminyaka emingaphi?: ")
     ilizwe =input("uvela phi?: ")

     umbhuliso =classes.Umbhuliso(igama,iminyaka,ilizwe)
     return umbhuliso
    
umbhuliso=buza()
classes.Umbhuliso.veza(umbhuliso.igama,umbhuliso.iminyaka,umbhuliso.ilizwe)
