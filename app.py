import streamlit as st
import analyzer

def main():
    # Configuração da página
    st.set_page_config(
        page_title="Bússola de Releases - Proa Conteúdo",
        page_icon="🧭",
        layout="wide"
    )
    
    # Estilo personalizado com cores náuticas
    st.markdown("""
    <style>
    .main {
        background-color: #f0f8ff;
    }
    .stApp {
        background-image: linear-gradient(to bottom, #f0f8ff, #e6f2ff);
    }
    h1, h2, h3 {
        color: #003366;
    }
    .stTextInput, .stTextArea {
        background-color: #ffffff;
        border: 1px solid #003366;
        border-radius: 5px;
    }
    .stButton>button {
        background-color: #003366;
        color: white;
        border-radius: 5px;
    }
    .stButton>button:hover {
        background-color: #004080;
    }
    .highlight {
        padding: 10px;
        border-radius: 5px;
        margin-bottom: 10px;
    }
    .good {
        background-color: #e6f7e6;
        border-left: 5px solid #28a745;
    }
    .medium {
        background-color: #fff3cd;
        border-left: 5px solid #ffc107;
    }
    .bad {
        background-color: #f8d7da;
        border-left: 5px solid #dc3545;
    }
    .header-container {
        display: flex;
        align-items: center;
        margin-bottom: 20px;
    }
    .logo {
        max-width: 100px;
        margin-right: 20px;
    }
    .nautical-divider {
        text-align: center;
        margin: 20px 0;
        color: #003366;
    }
    </style>
    """, unsafe_allow_html=True)
    
    # Cabeçalho com tema náutico
    st.markdown("""
    <div class="header-container">
        <h1>🧭 Bússola de Releases</h1>
    </div>
    <h3>Navegue com segurança pelas águas da comunicação</h3>
    """, unsafe_allow_html=True)
    
    # Divisor náutico
    st.markdown('<div class="nautical-divider">⚓ ⚓ ⚓</div>', unsafe_allow_html=True)
    
    # Introdução
    st.markdown("""
    Bem-vindo, marujo! A **Bússola de Releases** irá guiar seu texto para águas tranquilas, 
    analisando aspectos como redundâncias, voz passiva, clareza e muito mais. 
    Insira seu release abaixo e descubra como melhorar sua navegação textual.
    """)
    
    # Área para inserção do texto
    release_text = st.text_area("Digite seu release aqui:", height=250, 
                               placeholder="Cole seu texto aqui para análise...")
    
    # Seleção de editoria
    col1, col2 = st.columns([3, 1])
    with col1:
        st.markdown("**Qual a editoria do seu release?** (opcional)")
    with col2:
        editoria = st.selectbox(
            "Editoria",
            ["", "Esporte", "Entretenimento", "Tecnologia", "Economia", "Política", "Outra"],
            label_visibility="collapsed"
        )
    
    # Botão de análise
    if st.button("Analisar Release"):
        if release_text:
            with st.spinner("Navegando pelas águas do seu texto..."):
                # Criar instância do analisador
                release_analyzer = analyzer.ReleaseAnalyzer()
                
                # Analisar o texto
                resultado = release_analyzer.analisar_release(release_text, editoria)
                
                # Exibir resultados
                st.markdown('<div class="nautical-divider">🌊 🌊 🌊</div>', unsafe_allow_html=True)
                
                # Pontuação e feedback náutico
                pontuacao = resultado['pontuacao']
                
                # Determinar classe CSS baseada na pontuação
                if pontuacao >= 80:
                    pontuacao_class = "good"
                elif pontuacao >= 60:
                    pontuacao_class = "medium"
                else:
                    pontuacao_class = "bad"
                
                # Exibir pontuação com estilo
                st.markdown(f"""
                <div class="highlight {pontuacao_class}">
                    <h2>Pontuação: {pontuacao}/100</h2>
                    <p>{resultado['feedback_nautico']}</p>
                </div>
                """, unsafe_allow_html=True)
                
                # Feedback de editoria (se fornecido)
                if resultado['editoria_feedback']:
                    st.markdown(f"""
                    <div class="highlight medium">
                        <h3>Sobre a editoria:</h3>
                        <p>{resultado['editoria_feedback']}</p>
                    </div>
                    """, unsafe_allow_html=True)
                
                # Problemas encontrados
                if resultado['problemas']:
                    st.markdown("<h3>🚨 Atenção no convés!</h3>", unsafe_allow_html=True)
                    for problema in resultado['problemas']:
                        st.markdown(f"- {problema}")
                
                # Sugestões de melhoria
                if resultado['sugestoes']:
                    st.markdown("<h3>🧭 Ajustes de rota sugeridos:</h3>", unsafe_allow_html=True)
                    for sugestao in resultado['sugestoes']:
                        st.markdown(f"- {sugestao}")
                
                # Divisor náutico final
                st.markdown('<div class="nautical-divider">⚓ ⚓ ⚓</div>', unsafe_allow_html=True)
                
                # Mensagem de incentivo
                st.markdown("""
                **Lembre-se, marujo:** Um bom release é como um navio bem construído - 
                deve ser robusto, equilibrado e capaz de transportar sua mensagem com segurança 
                até o destino final.
                """)
        else:
            st.error("Por favor, insira um texto para análise.")
    
    # Rodapé
    st.markdown("""
    <div style="text-align: center; margin-top: 50px; color: #003366;">
        <p>Desenvolvido por <a href="https://proaconteudo.com.br/" target="_blank">Proa Conteúdo</a> | 2025</p>
        <p style="font-size: 0.8em;">Navegando juntos pelas águas da comunicação</p>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
