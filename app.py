import pandas as pd
import streamlit as str
import plotly_express as px

car_data = pd.read_csv("./datasets/df_vehicles_mod.csv")

str.title('Dashboard de vehículos usados de Estados Unidos')

str.header('Tipos de vehículo por fabricante')
pivot_manufacturer = car_data.pivot_table(
    index='manufacturer', columns='type', values='fuel', aggfunc='count')
fig = px.bar(pivot_manufacturer,
             labels={'model_year': 'Año de fabricación',
                     'count': 'Cantidad', 'condition': 'Condición', 'type': 'Tipo'},
             barmode='stack')
fig.update_layout(
    xaxis=dict(
        tickangle=70
    )
)
str.plotly_chart(fig, use_container_width=True)

str.header('Año de fabricación y condicion del vehiculo')
not_na_car_data = car_data[~car_data['model_year'].isna()]
fig = px.histogram(not_na_car_data,
                   x='model_year',
                   color='condition',
                   labels={'model_year': 'Año de fabricación',
                           'count': 'Cantidad', 'condition': 'Condición'},
                   )
fig.update_layout(
    height=600,
)
str.plotly_chart(fig, use_container_width=True)


str.header('Comparación de precios entre fabricantes')
opt_fr_1 = str.selectbox(label='Seleccionar fabricante 1',
                         options=car_data['manufacturer'].unique(),
                         )
opt_fr_2 = str.selectbox(label='Seleccionar fabricante 2',
                         options=car_data['manufacturer'].unique(),
                         index=1
                         )
check_norm = str.checkbox(label='Histograma normalizado',
                          value=True)
fig = px.histogram(car_data[(car_data['manufacturer'] == opt_fr_1) | (car_data['manufacturer'] == opt_fr_2) & (car_data['price'] > 100)],
                   x='price',
                   color='manufacturer',
                   histnorm='percent' if check_norm else '',
                   nbins=80,
                   labels={'price': 'Precio', 'manufacturer': 'Fabricante'},
                   )
str.plotly_chart(fig, use_container_width=True)

str.header('Comparación de precios y año de modelo')
fig = px.scatter(car_data,
                 x='model_year',
                 y='price',
                 color='type',
                 labels={'price': 'Precio',
                         'model_year': 'Año del modelo',
                         'type': 'Tipo'}
                 )
str.plotly_chart(fig, use_container_width=True)
