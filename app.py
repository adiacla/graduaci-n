import streamlit as st
import joblib
import numpy as np

# Cargar modelo
modelo = joblib.load("primermillon.joblib")

# Título y autor
st.title("🎓 Predictor de Éxito Académico")
st.write("Autor: **Alfredo Díaz**")

# Imagen
st.image("https://buscacarrera.com.co/public/content/articulos/la-clave-del-exito-academico-como-crear-un-plan-de-estudio-efectivo.jpg", use_container_width=True)

# Introducción
st.markdown("""
Esta aplicación predice si un(a) estudiante logrará graduarse exitosamente, utilizando como base dos indicadores:
- **Nota IA** (rendimiento en Inteligencia Artificial)
- **GPA** (promedio general acumulado)

Utiliza los controles deslizantes a continuación para establecer los valores y obtener la predicción. Los valores deben estar entre **0.0 y 1.0**.
""")

# Entradas del usuario
nota_ia = st.slider("Nota IA", 0.0, 1.0, step=0.1)
gpa = st.slider("GPA", 0.0, 1.0, step=0.1)

# Hacer predicción
if st.button("🔍 Predecir"):
    entrada = np.array([[nota_ia, gpa]])
    prediccion = modelo.predict(entrada)[0]

    if prediccion == 1:
        st.success("✅ Felicitaciones, ¡te vas a graduar con honores! 🎓")
    else:
        st.error("❌ No se graduará 😢")

# Pie de página
st.markdown("---")
st.markdown("© 2025 UNAB")
