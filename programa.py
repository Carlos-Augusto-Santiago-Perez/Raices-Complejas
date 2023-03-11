# librerias
import cmath
import math
import matplotlib.pyplot as plt
from os import environ
from matplotlib.patches import Circle, Wedge

# VARIABLES
colores = [
    "#ff0000", # Rojo
    "#ffa500", # Naranja
    "#ffff00", # Amarillo
    "#008000", # Verde
    "#0000ff", # Azul
    "#4b0082", # Rosa
    "#ee82ee"  # Morado
]
var_global = {
    "movimiento": 1,
    "zonas": []
}

#Warnings
def suppress_qt_warnings():
    environ["QT_DEVICE_PIXEL_RATIO"] = "0"
    environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
    environ["QT_SCREEN_SCALE_FACTORS"] = "1"
    environ["QT_SCALE_FACTOR"] = "1"
    
# FUNCIONES
# Mover rehilete
def rehilete_Newton(axis):
    # Mover cada zona
    for zona in var_global["zonas"]:
        zona.set_theta1(zona.theta1 + var_global["movimiento"])
        zona.set_theta2(zona.theta2 + var_global["movimiento"])
    
    # Aceleracion
    var_global["movimiento"] += 1
    
    # Actualizar lo gráfico
    axis.figure.canvas.draw()

# Imprimir numero complejo
def numeroComplejo(r, i):
    nc = complex(r, i)
    print("Forma binomica: ", nc, sep="")
    return nc

# Imprimir su forma polar
def formaPolar(complejo):
    print("\nForma polar: ", cmath.polar(complejo), sep="")

# Imprimir su forma trigonometrica
def formaTrigonometrica(m, a):
    print("\nForma trigonometrica: ", round(m, 2),
          "(cos(", round(a, 2), ") +isen(", round(a, 2), "))", sep="")

# Graficar las raices
def graficar(complejo):
    fix, ax = plt.subplots()
    # Dibuja el plano
    ax.set_title('Raices complejas')
    ax.spines["left"].set_position("zero")
    ax.spines["top"].set_position("zero")
    ax.spines["right"].set_color("none")
    ax.spines["bottom"].set_color("none")
    # limites de los ejes
    xymin = -complejo[0].real - 1
    xymax = complejo[0].real + 1
    ax.set_xlim(xymin, xymax)
    ax.set_ylim(xymin, xymax)
    # grid
    ax.grid()
    # graficar circunferencia
    radius = math.sqrt(
        complejo[0].real*complejo[0].real + complejo[0].imag*complejo[0].imag)
    circle = Circle(xy=(0, 0), radius=radius, fill=False)
    ax.add_artist(circle)

    # graficar los ejes de los complejos
    i = 0
    while i < len(complejo):
        ax.quiver(0, 0, complejo[i].real, complejo[i].imag,
                  angles='xy', scale_units='xy', scale=1)
        i += 1

    # Crear zonas
    delta = 360/len(complejo)
    angulo = math.degrees(math.atan2(complejo[0].imag, complejo[0].real))
    color_index = 0
    for i in range(len(complejo)):
        wedge = Wedge((0, 0), radius, angulo, angulo + delta, alpha=0.5, color = colores[color_index % 7])
        angulo += delta
        color_index += 1
        ax.add_artist(wedge)
        var_global["zonas"].append(wedge)

    # Mover zonas
    timer = fix.canvas.new_timer(interval=1)
    timer.add_callback(rehilete_Newton, ax)
    timer.start()

    # Graficar elementos
    plt.show()

# Calcular y graficar las raices
def raices(modulo, argumento):
    complejos_lista = []
    rep = 1
    while rep == 1:
        # Se pregunta la raiz
        raiz = int(input("\nIngrese raiz: "))
        # Si la raiz no existe
        if raiz < 2:
            print("Raiz no valida, ingrese de nuevo")
            rep = 1
        # Si la raiz existe
        else:
            i = 0
            # Repetimos hasta que i = n-1
            while i < raiz:
                # calculo de las raices mediante la formula, iterando con n y k
                print("\nz", str(i), " = ", round(modulo**(1/raiz),2), "(cos(", round(argumento+2*i*cmath.pi,
                      2), "/", raiz, ")+isen(", round(argumento+2*i*cmath.pi, 2), "/", raiz, "))", sep="")
                # valor en varible
                raices_complejo = modulo**(1/raiz)*(math.cos(
                    (argumento+2*i*cmath.pi)/raiz)+1j*math.sin((argumento+2*i*cmath.pi)/raiz))
                # se imprime el valor de z(i)
                print("z", str(i), " = ", raices_complejo, sep="")
                complejos_lista.append(raices_complejo)
                i += 1
            rep = 2
    graficar(complejos_lista)


# Main c:
suppress_qt_warnings()
print("\tNumeros complejos")
real = float(input("Ingrese el valor del numero real: "))
imaginario = float(input("Ingrese el valor imaginario: "))
# Mostrar y guardar numero complejo
numero_complejo = numeroComplejo(real, imaginario)
# Mostrar forma polar
formaPolar(numero_complejo)
# Mostrar forma trigonometrica
modulo = float(math.sqrt(pow(real, 2)+pow(imaginario, 2)))
argumento = float(math.atan2(imaginario, real))
formaTrigonometrica(modulo, argumento)
# Graficar y mostrar raices
raices(modulo, argumento)
