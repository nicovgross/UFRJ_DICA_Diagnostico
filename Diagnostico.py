import os
import pandas as pd
from UFRJ_DICA_LeitorXML.LeitorXML import LeitorXML
from TaxaAcerto import TaxaAcerto


'''
Itera sobre os arquivos da pasta 'activities' até encontrar um arquivo 'lesson.xml', e o retorna 
'''
def iterateFolder(Activities):
    for folder in os.listdir(Activities): 
        if 'lesson' in folder:
            lesson_folder = os.path.join(Activities, folder)
            if os.path.isdir(lesson_folder):
                for file in os.listdir(lesson_folder):
                    if file == 'lesson.xml':
                        yield os.path.join(lesson_folder, file)


'''
Concatena as lições em um único DataFrame, com a descrição de cada lição
'''
def ConcatLessons(Activities):
    df_lessons = pd.DataFrame()

    for Lesson in iterateFolder(Activities):
        df_lesson = LeitorXML(Lesson).analisar_questionario()
        df_lessons = pd.concat([df_lessons, df_lesson], axis='index')

    df_lessons.set_index('lesson_id', inplace=True)
    df_lessons.drop(['grade', 'max_answer', 'max_attempt'], axis='columns', inplace=True)
    return df_lessons


'''
Concatena todas as questões de todas todas as lições em um único DataFrame e calcula taxa de acerto de cada questão
usando a função 'TaxaAcerto'
'''
def ConcatQuestions(Activities):
    df_questions = pd.DataFrame()

    for Lesson in iterateFolder(Activities):
        q = TaxaAcerto(Lesson)
        if q.empty:
            continue
        df_questions = pd.concat([df_questions, q], axis='index')
                        
    df_questions.drop(['qtype', 'qoption', 'title'], axis='columns', inplace=True)
    return df_questions


'''
Retorna um diagnósticos das lições, com a taxa média de acerto de cada lição
'''
def Diagnostico(Activities):
    df_lessons = ConcatLessons(Activities)
    df_questions = ConcatQuestions(Activities)

    grp_questions = df_questions.groupby('lesson_id')
    ave_hit_rate = grp_questions['hit_rate'].mean()
    df_diagnostico = pd.concat([df_lessons, ave_hit_rate], axis='columns')
    df_diagnostico.rename(columns={'hit_rate':'ave_hit_rate'}, inplace=True)

    return df_diagnostico