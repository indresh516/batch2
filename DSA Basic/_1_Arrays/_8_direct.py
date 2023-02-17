import numpy as np
import pandas as pd

a = np.random.randint(1 ,25,(5,5))
df=pd.DataFrame(a, columns=('Age','hindi','maths','english','chemistry'))
print(df)