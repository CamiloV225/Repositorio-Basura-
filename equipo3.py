from datetime import datetime
from datetime import timedelta

def calcularFecha(proximaCita):
    fechaCita=datetime.now()    
    fechaSigCita= fechaCita+timedelta(proximaCita)

    return fechaSigCita 

def calcularDiasDosis(edadPaciente):
    di = 0
    if edadPaciente >= 60:
        di = 7
    else:
        di = 3
    return di

def calcularDosis(pesoPaciente):
    d = 0
    if pesoPaciente >=80:
        d = 40
    else:
        d = 20
    return d

def valorMedicamento (dosis, dias,fabMedicamento):
    f = fabMedicamento
    v = 0
    g = dosis*dias
    if g%120 == 0:
        v = f(g//120)
    else:
        v = f*((g//120)+1)
    return v

def costoPaciente(medicamento):
    c = 0
    c = medicamento+2*medicamento+0.2*medicamento
    return c


def principal ():
    
    nomPaciente = input("Nombre del paciente: ")
    fechaNacimiento = input ("Ingrese Fecha de Nacimiento (DD/MM/AAAA): ")
    motivoConsulta = input("Motivo de Consulta: ")
    nMedicamento = input("Medicamento: ")
    cita = datetime.now ()
    presentacionMedicamento = input("Presentacion del Medicamento: ")
    tipoMedicamento = input("Tipo de Medicamento (Pediatrico o No Pediatrico): ")
    sustanciaMedicamento = input("Sustancia del Medicamento: ")
    pesoPaciente = int(input("Peso del Paciente (kg): "))
    edadPaciente = int(input("Edad del Paciente: "))
    fabMedicamento = int(input("Ingrese el valor del medicamento: "))
    dias = calcularDiasDosis(edadPaciente)
    dosis = calcularDosis(pesoPaciente)
    medicamento = valorMedicamento (dosis,dias,fabMedicamento)
    costo = costoPaciente(medicamento)
    proximaCita = int(input("Digite los días para la siguiente cita: "))
    sigCita = calcularFecha(proximaCita)
    print (f"Datos del paciente: Nombre: {nomPaciente} , Edad: {edadPaciente}, Peso: {pesoPaciente}Kg, Diagnostico: {motivoConsulta}")
    print (f"Formula: {nMedicamento} {dosis} gotas por {dias} días. Tomar con un poco de agua o jugo.")
    print (f"Fecha: {cita}")
    print (f"Costo: ${costo}")
   
    print (f"Proxima cita en {sigCita}")



if __name__=='__main__':
    # Nombre del Medicamento = Humulus Lupulus
    # Presentación del Medicamento = Gotas
    # Tipo de Medicamento = No Pediatrico 
    # Sustancia del Medicamento = Lúpulo
    principal ()
