import streamlit as st

# Título

st.title("Teste Exato de Fisher")

# Seção Inicial (Conceito)
## O que é? Quando surgiu?
st.write(
    "O Teste Exato de Fisher, também conhecido como Teste de Fisher, é um teste de hipótese "
    "utilizado para avaliar a associação entre duas (ou mais) variáveis categóricas. "
    "Ele nos ajuda a verificar se dois tratamentos diferentes produzem efeitos distintos em uma variável de interesse."
)
with st.expander("Para entender melhor, considere o seguinte cenário:"):
    st.write(
        "Uma empresa de bolos deseja investigar se adicionar a palavra 'caseiro' à embalagem "
        "tem algum impacto nas vendas do produto. Para isso, foi elaborado um experimento com 100 consumidores, "
        "que serão divididos entre dois tipos de embalagem."
    )

    st.write(
        "- Embalagem A: versão atual, já disponível no mercado.")
    st.write(
        "- Embalagem B: idêntica à A, mas com a palavra 'caseiro' destacada."
    )

    st.write(
        "Cada consumidor será exposto a uma dessas versões, e o resultado observado será se o bolo foi ou não comprado. "
        "Dessa forma, teremos dois tratamentos (embalagem A e B) e dois desfechos possíveis (comprou ou não comprou)."
    )

    st.write(
        "A empresa quer entender se vale a pena investir em uma nova embalagem. "
        "Se a palavra 'caseiro' não influenciar nas vendas, esse investimento pode ser em vão. "
        "Pior ainda, se houver uma reação negativa à nova embalagem, pode haver uma queda nas vendas."
    )

### É possível um hyperlink para um outro streamlit de Teste de Hipótese? 'Saiba mais'
## Utilidade?

## Quais áreas isso é/pode ser aplicado?



# Seção Principal (Como funciona: Suposições e Algoritmo)
## Suposições

## Estrutura de Teste de Hipótese

## Passo a passo teórico (Algoritmo)



# Seção Final (Exemplos aplicados)
## Exemplo 1

## Exemplo 2
# Bibliografia
