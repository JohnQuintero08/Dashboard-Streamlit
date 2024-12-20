import pandas as pd
import streamlit as str
import plotly_express as px

car_data = pd.read_csv("./datasets/vehicles_us.csv")
hist_button = str.button('Construir histograma')
scatter_button = str.button('Construir diagrama de dispersión')

if hist_button:
    str.write('Creación de un histograma')
    fig = px.histogram(car_data, x='odometer')
    str.plotly_chart(fig, use_container_width=True)

if scatter_button:
    str.write('Creacion de un diagrama de dispersión')
    fig = px.scatter(car_data, x='odometer', y='price')
    str.plotly_chart(fig, use_container_width=True)
