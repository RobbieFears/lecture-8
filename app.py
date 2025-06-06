import streamlit as st
import pandas as pd
import plotly.express as px

# Leer el archivo CSV
df = pd.read_csv('vehicles_us.csv')

# Encabezado
st.header("Análisis de Vehículos Usados")

# Vista previa de los datos
st.write("Vista previa del conjunto de datos:")
st.write(df.head())

# Botón para mostrar histograma
if st.button("Mostrar Histograma"):
    columna = df.columns[0]  # Cambia esta columna si deseas otra
    fig = px.histogram(df, x=columna, title=f"Histograma de {columna}")
    st.plotly_chart(fig)

# Botón para mostrar gráfico de dispersión
if st.button("Mostrar Gráfico de Dispersión"):
    if len(df.columns) >= 2:
        x_col = df.columns[0]
        y_col = df.columns[1]
        fig = px.scatter(df, x=x_col, y=y_col, title=f"Dispersión: {x_col} vs {y_col}")
        st.plotly_chart(fig)
    else:
        st.write("No hay suficientes columnas para crear un gráfico de dispersión.")