import streamlit as st
import matplotlib.pyplot as plt

# grafico
idade = [
    0, 3, 6, 9, 12, 15, 18, 24, 36, 48, 60, 72, 84, 96, 108, 120, 132, 144,
    156, 168, 180, 192, 204, 216
]
altura = [
    46.3, 56.8, 63, 67.7, 71.3, 74.4, 77.5, 82.7, 90.6, 97.5, 102, 108.5,
    114, 119.6, 124.2, 128.7, 133.4, 137.6, 142.2, 146.4, 151.7, 156.5, 159, 159.6
]

fig, ax = plt.subplots()
ax.scatter(idade, altura)
ax.set_title('Gráfico de Dispersão de Idade vs Altura')
ax.set_xlabel('Idade (meses)')
ax.set_ylabel('Altura (cm)')

def Conta():
    variante = st.session_state.entrada 
    calculo = ((-0.0015)*(variante ** 2)) + (0.7728 * variante) + 59.6026
    
    
    st.session_state.resultado = calculo


entrada = st.number_input("Digite um número", key="entrada", value=0)

st.button("Clicar", on_click=Conta)

if "resultado" in st.session_state:
    st.write(f"Resultado: {st.session_state.resultado}")
    st.pyplot(fig)


