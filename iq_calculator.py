import streamlit as st
import scipy.stats as stats
import pandas as pd

def calculate_qi_stats(pisa_mean, pisa_sd, pisa_mean_global, pisa_sd_global, qi_mean_global, qi_sd_global):
    qi_sd_national = (pisa_sd / pisa_sd_global) * qi_sd_global
    qi_mean_national = ((pisa_mean - pisa_mean_global) / pisa_sd_global) * qi_sd_global + qi_mean_global
    return qi_mean_national, qi_sd_national

def generate_probability_table(qi_mean, qi_sd, scores):
    data = {
        "QI Score": [],
        "Probabilidade (%)": []
    }
    
    for score in scores:
        z_score = (score - qi_mean) / qi_sd
        probability = 1 - stats.norm.cdf(z_score)
        data["QI Score"].append(score)
        data["Probabilidade (%)"].append(probability * 100)  # Convertendo para percentual
    
    df = pd.DataFrame(data)
    return df

def calculate_probability(qi_mean, qi_sd, user_score):
    z_score = (user_score - qi_mean) / qi_sd
    probability = 1 - stats.norm.cdf(z_score)
    return probability * 100  # Convertendo para percentual

def main():
    st.title("Calculadora de QI Nacional")

    #National IQ score and std
    pisa_mean = st.number_input("Digite o score médio de matemática do PISA:", value=379.0)
    pisa_sd_diff = st.number_input("Digite a diferença da performance de matemática PISA entre o percentil 90 e percentil 10:", value=194.0)
    pisa_mean_global = 500
    pisa_sd_global = 100
    qi_mean_global = 100
    qi_sd_global = 15

    qi_mean_national, qi_sd_national = calculate_qi_stats(
        pisa_mean, pisa_sd_diff / 2.56, pisa_mean_global, pisa_sd_global, qi_mean_global, qi_sd_global
    )
    st.write(f"Média do QI nacional: {qi_mean_national:.2f}")
    st.write(f"Desvio padrão do QI nacional: {qi_sd_national:.2f}")

    
    # Probability table
    scores = [50, 60, 70, 80, 90, 100, 110, 120, 130]
    probability_table = generate_probability_table(qi_mean_national, qi_sd_national, scores)
    st.write("Tabela de Probabilidade:")
    st.table(probability_table)

    # User IQ score
    user_score = st.number_input("Digite um valor de QI para calcular a probabilidade de encontrar alguém com QI maior ou igual:", value=100)
    probability = calculate_probability(qi_mean_national, qi_sd_national, user_score)
    st.write(f"Probabilidade de encontrar alguém com QI maior ou igual a {user_score}: {probability:.2f}%")

if __name__ == "__main__":
    main()
