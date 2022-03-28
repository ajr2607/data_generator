import pandas as pd
from faker import Faker

fake = Faker('en_GB')

exp = Faker(['en_GB'])
data = [exp.profile() for i in range(100)]
df = pd.DataFrame(data)

from pathlib import Path

filepath = Path('/data_generator/sample_data.csv');
filepath.parent.mkdir(parents=True, exist_ok=True);
df.to_csv(filepath);

df.to_csv(index=False)
