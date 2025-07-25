import pandas as pd
import plotly.express as px
import streamlit as st

# Cargar datos
car_data = pd.read_csv('vehicles_us.csv')

# Título del dashboard
st.header('Análisis de anuncios de venta de vehículos')

# Botón para histograma
hist_button = st.button('Construir histograma') 
if hist_button:
    st.write('Histograma del kilometraje (odómetro) de los vehículos')
    fig_hist = px.histogram(car_data, x="odometer", 
                          title="Distribución del kilometraje",
                          labels={'odometer': 'Kilometraje'})
    st.plotly_chart(fig_hist, use_container_width=True)

# Botón para gráfico de dispersión (nuevo)
scatter_button = st.button('Construir gráfico de dispersión')
if scatter_button:
    st.write('Relación entre precio y kilometraje de los vehículos')
    fig_scatter = px.scatter(car_data, x="odometer", y="price",
                           title="Precio vs Kilometraje",
                           labels={'odometer': 'Kilometraje', 'price': 'Precio ($)'},
                           trendline="lowess")
    st.plotly_chart(fig_scatter, use_container_width=True)
