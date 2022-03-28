import pandas as pd
from faker import Faker

from mimesis import Address
from mimesis.locales import Locale

fake = Faker('en_GB')

print(fake.address())

exp = Faker(['en_GB'])
data = [exp.profile() for i in range(100)]
df = pd.DataFrame(data)
print(df)
