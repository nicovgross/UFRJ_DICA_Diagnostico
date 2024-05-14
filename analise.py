import os
import pandas as pd
from TaxaAcerto import TaxaAcerto

'''Activities = "UFRJ_DICA_Diagnostico/backup_DICA/activities"
for folder in os.listdir(Activities): 
    if 'lesson' in folder:
        lesson_folder = os.path.join(Activities, folder)
        if os.path.isdir(lesson_folder):
            for file in os.listdir(lesson_folder):
                if file == 'lesson.xml':
                    Lesson = os.path.join(lesson_folder, file)
                    q = TaxaAcerto(Lesson)
                    if q.empty:
                        break
                    print(q)'''


#q = TaxaAcerto("UFRJ_DICA_Diagnostico/backup_DICA/activities/lesson_656148/lesson.xml")
q = TaxaAcerto("UFRJ_DICA_Diagnostico/backup_DICA/activities/lesson_585303/lesson.xml")
print(q)