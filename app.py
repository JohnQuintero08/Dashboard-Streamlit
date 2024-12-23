import pandas as pd
import streamlit as str
import plotly_express as px

car_data = pd.read_csv("./datasets/df_vehicles_mod.csv")

str.title('Dashboard de vehículos usados de Estados Unidos')

# hist_button = str.button('Construir histograma')
# scatter_button = str.button('Construir diagrama de dispersión')

# if hist_button:
str.header('Tipos de vehículo por fabricante')
pivot_manufacturer = car_data.pivot_table(
    index='manufacturer', columns='type', values='fuel', aggfunc='count')
fig = px.bar(pivot_manufacturer,
             labels={'manufacturer': 'Fabricante',
                     'value': 'Cantidad de vehículos'},
             barmode='stack')
fig.update_layout(
    xaxis=dict(
        tickangle=70
    )
)
str.plotly_chart(fig, use_container_width=True)

# if scatter_button:
str.header('Año de fabricación y condicion del vehiculo')
not_na_car_data = car_data[~car_data['model_year'].isna()]
fig = px.histogram(not_na_car_data,
                   x='model_year',
                   color='condition',
                   labels={'model_year': 'Año de fabricación',
                           'count': 'Cantidad'},
                   )
fig.update_layout(
    height=600,
)
str.plotly_chart(fig, use_container_width=True)
