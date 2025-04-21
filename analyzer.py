import spacy
import re
from collections import Counter
from textblob import TextBlob

class ReleaseAnalyzer:
    def __init__(self):
        # Carregar modelo de linguagem em português
        self.nlp = spacy.load('pt_core_news_sm')
        
        # Palavras comuns que podem indicar redundância quando repetidas
        self.common_words = set(['empresa', 'produto', 'serviço', 'cliente', 'mercado', 
                                'tecnologia', 'inovação', 'qualidade', 'solução', 'projeto'])
        
        # Palavras que podem indicar jargões corporativos
        self.jargoes = set(['sinergia', 'proativo', 'disruptivo', 'escalável', 'otimizar', 
                           'paradigma', 'alavancagem', 'verticalizar', 'ecossistema', 'holístico'])
        
        # Informações essenciais que um release deve conter
        self.info_essenciais = ['quem', 'o que', 'quando', 'onde', 'por que', 'como']
        
        # Dicionário de editorias e palavras-chave relacionadas
        self.editorias = {
            'esporte': ['atleta', 'jogo', 'campeonato', 'competição', 'time', 'equipe', 'vitória', 'derrota', 'treinador', 'técnico'],
            'entretenimento': ['filme', 'série', 'música', 'show', 'artista', 'ator', 'atriz', 'diretor', 'lançamento', 'estreia'],
            'tecnologia': ['inovação', 'aplicativo', 'software', 'hardware', 'digital', 'internet', 'dispositivo', 'plataforma', 'startup', 'inteligência artificial'],
            'economia': ['mercado', 'investimento', 'economia', 'financeiro', 'bolsa', 'ações', 'empresa', 'negócio', 'lucro', 'prejuízo'],
            'política': ['governo', 'presidente', 'ministro', 'congresso', 'senado', 'câmara', 'eleição', 'partido', 'lei', 'projeto']
        }
        
    def analisar_release(self, texto, editoria=None):
        """Analisa um release e retorna um relatório com pontuação e sugestões."""
        doc = self.nlp(texto)
        
        # Inicializar pontuação (0-100)
        pontuacao = 100
        
        # Inicializar lista de problemas e sugestões
        problemas = []
        sugestoes = []
        
        # Análise de redundâncias
        redundancias = self._verificar_redundancias(doc)
        if redundancias:
            pontuacao -= min(len(redundancias) * 5, 20)  # Máximo de 20 pontos de penalidade
            problemas.append(f"Encontramos {len(redundancias)} palavras repetidas em excesso.")
            sugestoes.append("Considere usar sinônimos para: " + ", ".join(redundancias))
        
        # Análise de voz passiva
        voz_passiva = self._verificar_voz_passiva(texto)
        if voz_passiva:
            pontuacao -= min(len(voz_passiva) * 3, 15)  # Máximo de 15 pontos de penalidade
            problemas.append(f"Encontramos {len(voz_passiva)} ocorrências de voz passiva.")
            sugestoes.append("Considere reescrever em voz ativa: " + "; ".join(voz_passiva[:3]))
        
        # Análise de comprimento de parágrafos e frases
        problemas_comprimento, sugestoes_comprimento, penalidade_comprimento = self._verificar_comprimento(texto)
        if problemas_comprimento:
            pontuacao -= penalidade_comprimento
            problemas.extend(problemas_comprimento)
            sugestoes.extend(sugestoes_comprimento)
        
        # Análise de jargões
        jargoes_encontrados = self._verificar_jargoes(doc)
        if jargoes_encontrados:
            pontuacao -= min(len(jargoes_encontrados) * 2, 10)  # Máximo de 10 pontos de penalidade
            problemas.append(f"Encontramos {len(jargoes_encontrados)} jargões corporativos.")
            sugestoes.append("Considere substituir: " + ", ".join(jargoes_encontrados))
        
        # Análise de informações essenciais
        info_faltantes = self._verificar_info_essenciais(texto)
        if info_faltantes:
            pontuacao -= min(len(info_faltantes) * 5, 25)  # Máximo de 25 pontos de penalidade
            problemas.append(f"Seu release pode estar faltando informações essenciais.")
            sugestoes.append("Considere incluir: " + ", ".join(info_faltantes))
        
        # Análise de clareza e objetividade
        clareza_score, clareza_problemas, clareza_sugestoes = self._verificar_clareza(texto)
        pontuacao -= (100 - clareza_score) * 0.15  # Máximo de 15 pontos de penalidade
        if clareza_problemas:
            problemas.extend(clareza_problemas)
            sugestoes.extend(clareza_sugestoes)
        
        # Análise de editoria (se fornecida)
        editoria_feedback = ""
        if editoria and editoria.lower() in self.editorias:
            relevancia = self._verificar_relevancia_editoria(texto, editoria.lower())
            if relevancia < 0.3:
                pontuacao -= 10
                problemas.append(f"Seu release tem baixa relevância para a editoria de {editoria}.")
                sugestoes.append(f"Considere incluir mais termos relacionados à {editoria}.")
                editoria_feedback = f"Seu release parece não estar bem alinhado com a editoria de {editoria}. Considere revisar o conteúdo para torná-lo mais relevante."
            elif relevancia < 0.6:
                editoria_feedback = f"Seu release está parcialmente alinhado com a editoria de {editoria}. Pode melhorar a relevância."
            else:
                editoria_feedback = f"Muito bem, marujo! Seu release condiz com a editoria de {editoria} que você quer trabalhar. Avante!"
        
        # Garantir que a pontuação esteja entre 0 e 100
        pontuacao = max(0, min(100, pontuacao))
        
        # Preparar feedback náutico baseado na pontuação
        feedback_nautico = self._gerar_feedback_nautico(pontuacao)
        
        # Preparar relatório final
        relatorio = {
            'pontuacao': round(pontuacao),
            'feedback_nautico': feedback_nautico,
            'problemas': problemas,
            'sugestoes': sugestoes,
            'editoria_feedback': editoria_feedback
        }
        
        return relatorio
    
    def _verificar_redundancias(self, doc):
        """Verifica palavras repetidas em excesso no texto."""
        # Contar palavras significativas (substantivos, verbos, adjetivos)
        palavras = [token.text.lower() for token in doc 
                   if token.pos_ in ['NOUN', 'VERB', 'ADJ'] 
                   and not token.is_stop and len(token.text) > 3]
        
        # Contar ocorrências
        contador = Counter(palavras)
        
        # Identificar palavras repetidas em excesso (mais de 3 vezes)
        # Damos mais atenção a palavras comuns que são frequentemente redundantes
        redundancias = []
        for palavra, contagem in contador.items():
            if palavra in self.common_words and contagem > 2:
                redundancias.append(palavra)
            elif contagem > 3:
                redundancias.append(palavra)
                
        return redundancias
    
    def _verificar_voz_passiva(self, texto):
        """Identifica ocorrências de voz passiva no texto."""
        # Padrões comuns de voz passiva em português
        padroes_voz_passiva = [
            r'\bfoi\s+\w+ado\b', r'\bfoi\s+\w+ido\b', 
            r'\bforam\s+\w+ados\b', r'\bforam\s+\w+idos\b',
            r'\bé\s+\w+ado\b', r'\bé\s+\w+ido\b',
            r'\bsão\s+\w+ados\b', r'\bsão\s+\w+idos\b',
            r'\bsera\s+\w+ado\b', r'\bsera\s+\w+ido\b',
            r'\bserão\s+\w+ados\b', r'\bserão\s+\w+idos\b'
        ]
        
        voz_passiva = []
        for padrao in padroes_voz_passiva:
            matches = re.finditer(padrao, texto, re.IGNORECASE)
            for match in matches:
                voz_passiva.append(match.group(0))
                
        return voz_passiva
    
    def _verificar_comprimento(self, texto):
        """Verifica o comprimento de parágrafos e frases."""
        problemas = []
        sugestoes = []
        penalidade = 0
        
        # Dividir em parágrafos
        paragrafos = [p for p in texto.split('\n') if p.strip()]
        
        # Verificar parágrafos muito longos (mais de 6 linhas ou 600 caracteres)
        paragrafos_longos = [p for p in paragrafos if len(p) > 600]
        if paragrafos_longos:
            problemas.append(f"Encontramos {len(paragrafos_longos)} parágrafos muito longos.")
            sugestoes.append("Considere dividir parágrafos longos em unidades menores para melhorar a legibilidade.")
            penalidade += min(len(paragrafos_longos) * 3, 15)
        
        # Verificar frases muito longas (mais de 30 palavras)
        frases = re.split(r'[.!?]+', texto)
        frases_longas = [f for f in frases if len(f.split()) > 30]
        if frases_longas:
            problemas.append(f"Encontramos {len(frases_longas)} frases muito longas.")
            sugestoes.append("Considere dividir frases longas em unidades menores para melhorar a clareza.")
            penalidade += min(len(frases_longas) * 2, 10)
            
        return problemas, sugestoes, penalidade
    
    def _verificar_jargoes(self, doc):
        """Identifica jargões corporativos no texto."""
        palavras = [token.text.lower() for token in doc]
        jargoes_encontrados = [palavra for palavra in palavras if palavra in self.jargoes]
        return list(set(jargoes_encontrados))  # Remover duplicatas
    
    def _verificar_info_essenciais(self, texto):
        """Verifica se o release contém as informações essenciais."""
        texto_lower = texto.lower()
        info_faltantes = []
        
        # Verificar cada informação essencial
        for info in self.info_essenciais:
            # Verificação simplificada - poderia ser mais sofisticada
            if info not in texto_lower and not any(termo in texto_lower for termo in self._termos_relacionados(info)):
                info_faltantes.append(info)
                
        return info_faltantes
    
    def _termos_relacionados(self, info):
        """Retorna termos relacionados a cada informação essencial."""
        mapeamento = {
            'quem': ['empresa', 'organização', 'pessoa', 'profissional', 'equipe'],
            'o que': ['produto', 'serviço', 'evento', 'lançamento', 'iniciativa'],
            'quando': ['data', 'dia', 'mês', 'ano', 'período', 'prazo'],
            'onde': ['local', 'cidade', 'país', 'endereço', 'região'],
            'por que': ['motivo', 'razão', 'objetivo', 'propósito', 'meta'],
            'como': ['método', 'processo', 'forma', 'maneira', 'procedimento']
        }
        return mapeamento.get(info, [])
    
    def _verificar_clareza(self, texto):
        """Avalia a clareza e objetividade do texto."""
        # Análise simplificada de clareza
        problemas = []
        sugestoes = []
        
        # Verificar frases muito curtas em sequência (estilo telegráfico)
        frases = re.split(r'[.!?]+', texto)
        frases_curtas_consecutivas = 0
        for frase in frases:
            if len(frase.split()) < 5 and len(frase.strip()) > 0:
                frases_curtas_consecutivas += 1
            else:
                frases_curtas_consecutivas = 0
                
            if frases_curtas_consecutivas >= 3:
                problemas.append("Detectamos várias frases muito curtas em sequência.")
                sugestoes.append("Considere combinar algumas frases curtas para melhorar o fluxo do texto.")
                break
        
        # Verificar uso excessivo de adjetivos
        doc = self.nlp(texto)
        adjetivos = [token.text for token in doc if token.pos_ == 'ADJ']
        total_palavras = len([token for token in doc if not token.is_punct])
        
        proporcao_adjetivos = len(adjetivos) / total_palavras if total_palavras > 0 else 0
        if proporcao_adjetivos > 0.15:  # Mais de 15% de adjetivos
            problemas.append("Seu texto contém muitos adjetivos, o que pode reduzir a objetividade.")
            sugestoes.append("Considere reduzir o uso de adjetivos e focar em fatos concretos.")
        
        # Calcular pontuação de clareza (0-100)
        clareza_score = 100
        if frases_curtas_consecutivas >= 3:
            clareza_score -= 20
        clareza_score -= min(int(proporcao_adjetivos * 100), 30)
        
        # Penalizar por frases muito longas
        frases_longas = [f for f in frases if len(f.split()) > 25]
        clareza_score -= min(len(frases_longas) * 5, 30)
        
        return clareza_score, problemas, sugestoes
    
    def _verificar_relevancia_editoria(self, texto, editoria):
        """Verifica a relevância do texto para a editoria especificada."""
        if editoria not in self.editorias:
            return 0.5  # Valor neutro se a editoria não for reconhecida
        
        # Palavras-chave para a editoria
        palavras_chave = self.editorias[editoria]
        
        # Contar ocorrências de palavras-chave
        texto_lower = texto.lower()
        ocorrencias = sum(1 for palavra in palavras_chave if palavra in texto_lower)
        
        # Calcular relevância (0-1)
        relevancia = min(ocorrencias / len(palavras_chave), 1.0)
        
        return relevancia
    
    def _gerar_feedback_nautico(self, pontuacao):
        """Gera feedback com temática náutica baseado na pontuação."""
        if pontuacao >= 90:
            return "Vento em popa, marujo! Seu release está navegando em águas cristalinas. Avante toda!"
        elif pontuacao >= 80:
            return "Bons ventos, marujo! Seu release está em bom curso, com apenas alguns pequenos ajustes de vela necessários."
        elif pontuacao >= 70:
            return "Mar agitado à frente, marujo! Seu release precisa de alguns ajustes para navegar com mais segurança."
        elif pontuacao >= 60:
            return "Atenção no leme, marujo! Seu release está enfrentando algumas ondas e precisa de correções de rota."
        elif pontuacao >= 50:
            return "Tempestade à vista, marujo! Seu release precisa de reparos significativos antes de zarpar."
        else:
            return "SOS, marujo! Seu release está fazendo água. É hora de voltar ao estaleiro para uma reforma completa."
