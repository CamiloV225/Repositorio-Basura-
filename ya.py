def calc_area (r, math):
    area=math.pi*r**2
    return area
def calc_longitud(r, math):
    longitud=2*math.pi*r
    return longitud
def principal ():
    import math 
    r=float(input("Ingrese el radio del circulo: "))
    area=calc_area(r, math)
    longitud=calc_longitud(r, math)
    print(f"El area de la cicunferencia es de: {area} cm, y su longitud es de: {longitud} cm")
if __name__=='__main__':
    principal()