import streamlit as st
from figuritas import *
from visualizador import Visualizador3DPlotly, cargar_datos, guardar_datos

def main():
    st.title("Visualización de Superficies 3D")
    opciones = ["Plano", "Paraboloide", "Sinusoide", "Hiperboloide", "Cono", "Cilindro", 
                "Hiperboloide Una Hoja", "Hiperboloide Dos Hojas", "Esfera", "Cargar Datos"]

    seleccion = st.sidebar.selectbox("Seleccione el tipo de superficie:", opciones)

    if seleccion == "Plano":
        pendiente = st.sidebar.number_input("Pendiente del plano:", value=1.0)
        superficie = Plano((-5, 5), (-5, 5), pendiente)
    elif seleccion == "Paraboloide":
        coef = st.sidebar.number_input("Coeficiente del paraboloide:", value=1.0)
        superficie = Paraboloide((-5, 5), (-5, 5), coef)
    elif seleccion == "Sinusoide":
        frecuencia = st.sidebar.number_input("Frecuencia de la sinusoide:", value=1.0)
        superficie = Sinusoide((-5, 5), (-5, 5), frecuencia)
    elif seleccion == "Hiperboloide":
        coef = st.sidebar.number_input("Coeficiente del hiperboloide:", value=1.0)
        superficie = Hiperboloide((-5, 5), (-5, 5), coef)
    elif seleccion == "Cono":
        coef = st.sidebar.number_input("Coeficiente del cono:", value=1.0)
        superficie = Cono((-5, 5), (-5, 5), coef)
    elif seleccion == "Cilindro":
        radio = st.sidebar.number_input("Radio del cilindro:", value=1.0)
        superficie = Cilindro((-5, 5), (-5, 5), radio)
    elif seleccion == "Hiperboloide Una Hoja":
        coef = st.sidebar.number_input("Coeficiente del hiperboloide de una hoja:", value=1.0)
        superficie = HiperboloideUnaHoja((-5, 5), (-5, 5), coef)
    elif seleccion == "Hiperboloide Dos Hojas":
        coef = st.sidebar.number_input("Coeficiente del hiperboloide de dos hojas:", value=1.0)
        superficie = HiperboloideDosHojas((-5, 5), (-5, 5), coef)
    elif seleccion == "Esfera":
        radio = st.sidebar.number_input("Radio de la esfera:", value=1.0)
        superficie = Esfera((-5, 5), (-5, 5), radio)
    elif seleccion == "Cargar Datos":
        cargar_datos()
        return

    visualizador = Visualizador3DPlotly(superficie)
    visualizador.mostrar_con_plotly()

    x, y, z = superficie.generar_datos()
    guardar_datos(x, y, z)

if __name__ == "__main__":
    main()
