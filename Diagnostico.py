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
Concatena todas as lições em um único DataFrame, com a descrição de cada lição e calcula quantos usuários fizeram aquela lição
'''
def ConcatLessons(Activities):
    df_lessons = pd.DataFrame()
    user_count = []

    for Lesson in iterateFolder(Activities):
        df_lesson = LeitorXML(Lesson).analisar_questionario()
        df_lessons = pd.concat([df_lessons, df_lesson], axis='index')

        df_attempts = LeitorXML(Lesson).analisar_tentativas()
        if df_attempts.empty:
            user_count.append(0)
            continue
        user_count.append(len(df_attempts['user_id'].unique()))

    df_lessons.set_index("lesson_id", inplace=True)
    df_lessons.insert(2, "user_count", user_count)
    df_lessons.drop(['grade', 'max_answer', 'max_attempt'], axis='columns', inplace=True)
    return df_lessons


'''
Concatena todas as questões de todas todas as lições em um único DataFrame e calcula taxa de acerto de cada questão
usando a função 'TaxaAcerto'
'''
def ConcatQuestions(Activities):
    df_questions = pd.DataFrame()

    for Lesson in iterateFolder(Activities):
        df_lesson = TaxaAcerto(Lesson)
        if df_lesson.empty:
            continue
        df_questions = pd.concat([df_questions, df_lesson], axis='index')
                        
    df_questions.drop(['qtype', 'qoption', 'title'], axis='columns', inplace=True)
    return df_questions


'''
Concatena todas as tentativas de todas as lições em um único dataframe
'''
def ConcatAttempts(Activities):
    df_attempts = pd.DataFrame()

    for Lesson in iterateFolder(Activities):
        df_lesson = LeitorXML(Lesson).analisar_tentativas()
        if df_lesson.empty:
            continue
        df_attempts = pd.concat([df_attempts, df_lesson], axis='index')

    return df_attempts

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
    df_diagnostico = df_diagnostico.round({'ave_hit_rate':2})

    df_diagnostico.dropna(inplace=True) 

    return df_diagnostico