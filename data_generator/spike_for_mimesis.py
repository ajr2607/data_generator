from mimesis import Address
from mimesis import Person
from mimesis.enums import Gender
from mimesis.locales import Locale

gb = Address(locale=Locale.EN_GB)

person = Person(Locale.EN)

print(person.full_name(gender=Gender.FEMALE), ',', person.full_name(gender=Gender.MALE))
print(gb.region())
