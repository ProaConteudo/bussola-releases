import os
import tempfile
from analyzer import ReleaseAnalyzer

# Criar um analisador de releases
analyzer = ReleaseAnalyzer()

# Exemplo de release para teste
release_teste = """
A Empresa XYZ anuncia hoje o lançamento de seu novo produto inovador, que promete revolucionar o mercado. 
O produto foi desenvolvido pela equipe de pesquisa da empresa, que trabalhou incansavelmente para criar uma solução única.
A solução oferecida pela empresa é considerada por especialistas como uma das mais inovadoras do mercado.
O produto será lançado no próximo mês e estará disponível em todas as lojas da empresa.
A empresa espera que o produto seja bem recebido pelos clientes, que sempre valorizaram a qualidade dos produtos da empresa.
O CEO da empresa afirmou que o produto representa um marco importante para a empresa.
Foi decidido pela diretoria que o preço será competitivo.
"""

# Teste com diferentes editorias
editorias = ["Esporte", "Tecnologia", "Economia", ""]

print("=== TESTE DA BÚSSOLA DE RELEASES ===\n")

# Testar análise básica
print("TESTE 1: Análise básica sem editoria")
resultado = analyzer.analisar_release(release_teste)
print(f"Pontuação: {resultado['pontuacao']}/100")
print(f"Feedback náutico: {resultado['feedback_nautico']}")
print("\nProblemas encontrados:")
for problema in resultado['problemas']:
    print(f"- {problema}")
print("\nSugestões:")
for sugestao in resultado['sugestoes']:
    print(f"- {sugestao}")
print("\n" + "="*50 + "\n")

# Testar com editoria de tecnologia
print("TESTE 2: Análise com editoria de Tecnologia")
resultado = analyzer.analisar_release(release_teste, "Tecnologia")
print(f"Pontuação: {resultado['pontuacao']}/100")
print(f"Feedback náutico: {resultado['feedback_nautico']}")
print(f"Feedback de editoria: {resultado['editoria_feedback']}")
print("\n" + "="*50 + "\n")

# Testar com release melhorado
release_melhorado = """
A XYZ Tech anuncia hoje o lançamento do TechNavigator 3000, uma ferramenta de inteligência artificial que otimiza processos de desenvolvimento de software.

Desenvolvido ao longo de dois anos, o TechNavigator utiliza algoritmos avançados para identificar gargalos em processos de programação e sugerir melhorias. A ferramenta reduz em até 40% o tempo de desenvolvimento, segundo testes realizados com 50 empresas parceiras.

O lançamento oficial acontecerá em 15 de maio de 2025, durante a Conferência de Tecnologia de São Paulo. Os interessados poderão adquirir o produto através do site oficial ou revendedores autorizados.

"Estamos revolucionando a forma como as equipes de desenvolvimento trabalham", afirma Maria Silva, CEO da XYZ Tech. "Nossa tecnologia não apenas aumenta a produtividade, mas também melhora a qualidade do código final."

A empresa investiu R$ 5 milhões no desenvolvimento desta solução e espera recuperar o investimento em 18 meses, conforme projeções do departamento financeiro.
"""

print("TESTE 3: Análise de release melhorado com editoria de Tecnologia")
resultado = analyzer.analisar_release(release_melhorado, "Tecnologia")
print(f"Pontuação: {resultado['pontuacao']}/100")
print(f"Feedback náutico: {resultado['feedback_nautico']}")
print(f"Feedback de editoria: {resultado['editoria_feedback']}")
print("\nProblemas encontrados:")
for problema in resultado['problemas']:
    print(f"- {problema}")
print("\nSugestões:")
for sugestao in resultado['sugestoes']:
    print(f"- {sugestao}")
print("\n" + "="*50 + "\n")

# Testar com release com muita voz passiva
release_voz_passiva = """
Foi anunciado hoje pela empresa ABC que um novo sistema será implementado. O projeto foi desenvolvido por uma equipe especializada e será gerenciado pelo departamento de TI. 

Espera-se que os resultados sejam alcançados em seis meses. Os usuários serão treinados pela equipe de suporte. O sistema foi testado exaustivamente e foi aprovado por todos os gerentes.

É esperado que a produtividade seja aumentada em 30%. Os custos serão reduzidos significativamente.
"""

print("TESTE 4: Análise de release com excesso de voz passiva")
resultado = analyzer.analisar_release(release_voz_passiva)
print(f"Pontuação: {resultado['pontuacao']}/100")
print(f"Feedback náutico: {resultado['feedback_nautico']}")
print("\nProblemas encontrados:")
for problema in resultado['problemas']:
    print(f"- {problema}")
print("\nSugestões:")
for sugestao in resultado['sugestoes']:
    print(f"- {sugestao}")
print("\n" + "="*50 + "\n")

print("Testes concluídos com sucesso!")
