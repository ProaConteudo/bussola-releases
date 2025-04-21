# README - Bússola de Releases

## Sobre a Ferramenta

A **Bússola de Releases** é um mini-SaaS desenvolvido para a Proa Conteúdo que avalia releases de imprensa e fornece feedback personalizado com temática náutica. A ferramenta analisa aspectos como redundâncias, uso de voz passiva, clareza, comprimento de parágrafos, jargões, informações essenciais e adequação à editoria selecionada.

## Requisitos do Sistema

- Python 3.8 ou superior
- Bibliotecas Python: nltk, spacy, textblob, streamlit
- Modelo de linguagem spaCy para português: pt_core_news_sm

## Estrutura de Arquivos

- `analyzer.py`: Contém a classe principal que realiza a análise dos releases
- `app.py`: Interface de usuário desenvolvida com Streamlit
- `setup_nltk.py`: Script para baixar recursos necessários do NLTK
- `test_analyzer.py`: Script para testar as funcionalidades do analisador
- `guia_de_uso.md`: Documentação completa para usuários finais
- `iniciar_bussola.sh`: Script para iniciar a aplicação facilmente

## Instalação

1. Certifique-se de ter Python 3.8+ instalado
2. Instale as dependências necessárias:
   ```
   pip install nltk spacy textblob streamlit
   ```
3. Baixe o modelo de linguagem em português para o spaCy:
   ```
   python -m spacy download pt_core_news_sm
   ```
4. Execute o script para baixar recursos do NLTK:
   ```
   python setup_nltk.py
   ```

## Como Executar

1. Navegue até o diretório da aplicação
2. Execute o script de inicialização:
   ```
   ./iniciar_bussola.sh
   ```
3. Acesse a aplicação no navegador através do endereço fornecido (geralmente http://localhost:8501)

## Funcionalidades

A Bússola de Releases analisa:

- **Redundâncias**: Identifica palavras repetidas em excesso
- **Voz Passiva**: Detecta construções em voz passiva que podem ser melhoradas
- **Comprimento**: Avalia se parágrafos e frases estão muito longos
- **Jargões**: Identifica jargões corporativos que podem dificultar a compreensão
- **Informações Essenciais**: Verifica se o release contém as informações básicas (quem, o quê, quando, onde, por quê, como)
- **Clareza**: Analisa a estrutura geral do texto quanto à clareza e objetividade
- **Relevância para Editoria**: Quando uma editoria é selecionada, avalia a adequação do conteúdo

## Personalização

A ferramenta foi desenvolvida com o branding náutico da Proa Conteúdo, incluindo:

- Interface com cores e elementos náuticos
- Feedback com linguagem temática ("marujo", "navegar", etc.)
- Avaliações que seguem a metáfora de navegação

## Suporte e Manutenção

Para dúvidas ou problemas, consulte o guia de uso ou entre em contato com o desenvolvedor.

---

Desenvolvido para Proa Conteúdo © 2025  
*Navegando juntos pelas águas da comunicação*
