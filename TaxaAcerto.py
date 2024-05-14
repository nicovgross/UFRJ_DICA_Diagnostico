import pandas as pd
from UFRJ_DICA_LeitorXML.LeitorXML import LeitorXML

'''
Recebe um arquivo xml como entrada e usa a classe LeitorXML para fazer a leitura do arquivo, separando-o em Dataframes legíveis
Retorna um Dataframe do questionário, com a taxa de acerto por questão
'''
def TaxaAcerto(xml_file):
    lesson = LeitorXML(xml_file)
    df_questions = lesson.analisar_questoes()
    if df_questions.empty: #caso o questionario não tenha questoes
        return df_questions
    df_questions.set_index('page_id', inplace=True)
    df_attempts = lesson.analisar_tentativas()
    if df_attempts.empty: #caso o questionário não tenha tentativas, retorne nulo
        return df_attempts

    grp_questions = df_attempts.groupby('page_id') #agrupa as tentativas por questão
    taxa_de_acerto = grp_questions['correct'].apply(lambda x: (x=='1').mean()) #faz a média das tentativas corretas
    df_questions = pd.concat([df_questions, taxa_de_acerto], axis='columns')
    df_questions.rename(columns={'correct': 'hit_rate'}, inplace=True)

    return df_questions