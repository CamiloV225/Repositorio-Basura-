def calc_area (r):
    area=3.1415*r**2
    return area
def calc_longitud(r):
    longitud=2*3.1415*r
    return longitud
def principal ():
    r=float(input("Ingrese el radio del circulo: "))
    area=calc_area(r)
    longitud=calc_longitud(r)
    print(f"El area de la cicunferencia es de: {area} cm, y su longitud es de: {longitud} cm")
if __name__=='__main__':
    principal()