import streamlit as st
import google.generativeai as genai
import pandas as pd

API_KEY = "AIzaSyDsC-YuBt1xI9Wi4KBGJx4yL7BB6N68qfA"
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')

st.set_page_config(page_title="Finanças Pro", page_icon="📈", layout="wide")

st.title("💰 Experiência Financeira Digital")
st.markdown("""
Esta plataforma integra **IA Generativa** e **Análise de Dados** para ajudar você a entender 
melhor o seu dinheiro. Use o chat para dúvidas ou o simulador ao lado para projeções.
""")

with st.sidebar:
    st.header("📊 Simulador de Investimentos")
    st.info("Cálculos demonstrativos baseados em juros compostos.")
    
    aporte = st.number_input("Quanto quer investir hoje? (R$)", min_value=0.0, value=1000.0)
    taxa_anual = st.slider("Taxa de Juros Anual (%)", 0.0, 20.0, 12.0)
    anos = st.number_input("Por quantos anos?", min_value=1, max_value=50, value=5)

    if st.button("Simular Crescimento"):
        dados_lista = []
        valor_acumulado = aporte
        taxa_mensal = (1 + taxa_anual/100)**(1/12) - 1
        meses = anos * 12

        for mes in range(meses + 1):
            if mes > 0:
                valor_acumulado *= (1 + taxa_mensal)
            if mes % 12 == 0:
                dados_lista.append({"Ano": mes // 12, "Valor": round(valor_acumulado, 2)})

        df = pd.DataFrame(dados_lista)
        
        st.success(f"Em {anos} anos, você teria: R$ {valor_acumulado:,.2f}")
        st.line_chart(df.set_index("Ano"))
        st.table(df)

st.subheader("🤖 Assistente Virtual Financeiro")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Ex: O que é CDB? ou Como economizar dinheiro?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("Consultando inteligência financeira..."):
            contexto_ia = (
                "Você é um assistente de relacionamento financeiro amigável e didático. "
                "Explique conceitos complexos de forma simples."
            )
            
            try:
                response = model.generate_content(f"{contexto_ia}\n\nPergunta: {prompt}")
                texto_resposta = response.text
                st.markdown(texto_resposta)
                st.session_state.messages.append({"role": "assistant", "content": texto_resposta})
            except Exception as e:
                st.error("Erro na API.")

st.markdown("---")
st.caption("Aviso: Esta é uma simulação educacional. Não constitui recomendação de investimento.")
st.caption("Aviso: Esta é uma simulação educacional. Não constitui recomendação de investimento.")
