import os
import pandas as pd
import numpy as np
from Diagnostico import *

Activities = "backup_DICA/activities"
diagnostico = Diagnostico(Activities)
print(diagnostico.sort_values(by='ave_hit_rate', ascending=True).head(25))

diagnostico.to_excel("diagnostico_Dica.xlsx")