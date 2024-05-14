from LeitorXML import LeitorXML
import pandas as pd

questionario = LeitorXML("lesson.xml")

df_questionario = questionario.analisar_questionario()
df_questoes = questionario.analisar_questoes()
df_tentativas = questionario.analisar_tentativas()


#print("Questionnaire Data:")
#print(df_questionario)
#print("\nQuestions Data:")
#print(df_questoes)
#print(df_questoes)
#print("\nAttempts Data:")
#print(df_tentativas)


Lesson = pd.read_xml('lesson.xml')

print(Lesson)