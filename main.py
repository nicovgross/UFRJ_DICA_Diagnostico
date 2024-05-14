import os
import pandas as pd
import numpy as np
from Diagnostico import Diagnostico

Activities = "UFRJ_DICA_Diagnostico/backup_DICA/activities"
diagnostico = Diagnostico(Activities)
print(diagnostico.head(50))