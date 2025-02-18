import pandas as pd
import plotly.express as px
import streamlit as st

car_data = pd.read_csv('vehicles_us.csv')  # leer los datos

st.header("Aplicacion sobre vehiculos usados")

hist_button = st.button('Construir histograma')  # crear un botón

if hist_button:  # al hacer clic en el botón
    # escribir un mensaje
    st.write(
        'Creación de un histograma para el conjunto de datos de anuncios de venta de coches')

    # crear un histograma
    fig_1 = px.histogram(car_data, x="odometer")

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig_1, use_container_width=True)

build_histogram = st.checkbox('Construir un grafico de dispersion')

if build_histogram:  # si la casilla de verificación está seleccionada
    st.write('Construir un grafico de dispersion para la columna odómetro')

    # crear un gráfico de dispersión
    fig_2 = px.scatter(car_data, x="odometer", y="price")

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig_2, use_container_width=True)
