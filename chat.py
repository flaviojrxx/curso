import streamlit as st
import google.generativeai as genai
import pandas as pd

# --- CONFIGURAÇÃO DA IA ---
# Substitua pelo seu código de API
API_KEY = "SUA_CHAVE_AQUI"
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')

# --- CONFIGURAÇÃO DA PÁGINA (UX) ---
st.set_page_config(page_title="Finanças Pro", page_icon="📈", layout="wide")

st.title("💰 Experiência Financeira Digital")
st.markdown("""
Esta plataforma integra **IA Generativa** e **Análise de Dados** para ajudar você a entender 
melhor o seu dinheiro. Use o chat para dúvidas ou o simulador ao lado para projeções.
""")

# --- BARRA LATERAL (SIMULADOR DE DADOS) ---
with st.sidebar:
    st.header("📊 Simulador de Investimentos")
    st.info("Cálculos demonstrativos baseados em juros compostos.")
    
    aporte = st.number_input("Quanto quer investir hoje? (R$)", min_value=0.0, value=1000.0)
    taxa_anual = st.slider("Taxa de Juros Anual (%)", 0.0, 20.0, 12.0)
    anos = st.number_input("Por quantos anos?", min_value=1, max_value=50, value=5)

    if st.button("Simular Crescimento"):
        # Lógica de Dados com Python
        dados_lista = []
        valor_acumulado = aporte
        taxa_mensal = (1 + taxa_anual/100)**(1/12) - 1
        meses = anos * 12

        for mes in range(meses + 1):
            if mes > 0:
                valor_acumulado *= (1 + taxa_mensal)
            # Guardamos apenas o fechamento de cada ano no gráfico para ficar limpo
            if mes % 12 == 0:
                dados_lista.append({"Ano": mes // 12, "Valor": round(valor_acumulado, 2)})

        df = pd.DataFrame(dados_lista)
        
        st.success(f"Em {anos} anos, você teria: R$ {valor_acumulado:,.2f}")
        st.line_chart(df.set_index("Ano"))
        st.table(df) # Demonstração de persistência de dados em tabela

# --- CHATBOT COM IA (RELACIONAMENTO) ---
st.subheader("🤖 Assistente Virtual Financeiro")

# Inicializa o histórico de chat (Persistência de Contexto)
if "messages" not in st.session_state:
    st.session_state.messages = []

# Exibe mensagens anteriores
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Input do usuário
if prompt := st.chat_input("Ex: O que é inflação? ou Como economizar 10% do salário?"):
    # Adiciona pergunta do usuário ao histórico
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Gera resposta com a IA
    with st.chat_message("assistant"):
        with st.spinner("Pensando..."):
            contexto_ia = (
                "Você é um assistente de relacionamento financeiro amigável e didático. "
                "Explique conceitos complexos de forma simples. Se o usuário perguntar sobre "
                "investimentos, mencione a importância da segurança e diversificação."
            )
            
            try:
                response = model.generate_content(f"{contexto_ia}\n\nPergunta: {prompt}")
                texto_resposta = response.text
                st.markdown(texto_resposta)
                st.session_state.messages.append({"role": "assistant", "content": texto_resposta})
            except Exception as e:
                st.error("Erro ao conectar com a IA. Verifique sua chave de API.")

# Rodapé (UX/Segurança)
st.markdown("---")
st.caption("Aviso: Esta é uma simulação educacional. Não constitui recomendação de investimento.")
