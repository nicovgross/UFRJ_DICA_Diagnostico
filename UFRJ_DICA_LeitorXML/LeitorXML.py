"""
    Este código visa transformar o conteúdo do documento lessons em dataframes legíveis.

    Foi feito este esforço pois o XML dos arquivos são estruturados de maneira complexa, de modo que
    conversores de XML comum não conseguem ler o arquivo.

"""


import xml.etree.ElementTree as ET  
import pandas as pd


"""
    A classe LeitorXML recebe como parâmetro o arquivo XML.
    Para usa-la, é muito simples. Basta instanciar a classe

    LeitorXML("nome_do_arquivo.xml")

    e utilizar os métodos analisar_questionario(), analisar_questoes(), analisar_tentativas()
    retorna dataframes de questionario, questões e tentativas dos alunos.

"""

"""

    Sobre os DataFrames, eles são construidos utilizando as informações que julguei ser relevantes
    a respeito dos tópicos. É passivo de alteração caso seja necessário.

"""
class LeitorXML:
    def __init__(self, xml_file):
        self.tree = ET.parse(xml_file)
        self.root = self.tree.getroot()

    def analisar_questionario(self):
        dados_questionario = []
        for lesson in self.root.iter('lesson'):
            dados_licao = {
                'lesson_id': lesson.attrib.get('id'),
                'name': lesson.findtext('name'),
                'grade': lesson.findtext('grade'),
                'max_answer': lesson.findtext('maxanswers'),
                'max_attempt': lesson.findtext('maxattempts')
            }
            dados_questionario.append(dados_licao)
        return pd.DataFrame(dados_questionario)

    def analisar_questoes(self):
        dados_questao = []
        for lesson in self.root.iter('lesson'):
            for pages in lesson.iter('pages'):
                for page in pages:
                    #page_id = page.attrib.get('id')
                    dados_questao.append({
                        'page_id': page.attrib.get('id'),
                        'lesson_id': lesson.attrib.get('id'),
                        'qtype': page.findtext('qtype'),
                        'qoption': page.findtext('qoption'),
                        'title': page.findtext('title')
                        })
        return pd.DataFrame(dados_questao)

    def analisar_tentativas(self):
        dados_tentativas = []
        for lesson in self.root.iter('lesson'):
            for pages in lesson.iter('pages'):
                for page in pages:
                    for answers in page.iter('answers'):
                        for answer in answers:
                            for attempts in answer:
                                for attempt in attempts:
                                    dados_tentativas.append({
                                        'id': attempt.attrib.get('id'),
                                        'user_id': attempt.findtext('userid'),
                                        'page_id': page.attrib.get('id'),
                                        'answer_id': answer.attrib.get('id'),
                                        'retry': attempt.findtext('retry'),
                                        'correct': attempt.findtext('correct'),
                                        'score': answer.findtext('score'),
                                        'grade': answer.findtext('grade'),
                                        'useranswer': attempt.findtext('useranswer'),
                                        'timeseen': attempt.findtext('timeseen')
                                    })
        return pd.DataFrame(dados_tentativas)