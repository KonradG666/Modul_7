from faker import Faker
f = Faker(['pl_PL', 'en_US', 'it_IT'])


class BaseContact:
    def __init__(self, name, surname, phone, email):
        self.name = name
        self.surname = surname
        self.phone = phone
        self.email = email

    def __repr__(self):
        return f"Names(name={self.name} surname={self.surname}, phone={self.phone}, email={self.email})"

    def __str__(self):
        return f'{self.name} {self.surname} , {self.email}'

    def contact(self):
        print(f'Wybieram numer: {self.phone} i dzwonię do: {self.name} {self.surname}')
        print(f"Full name lenght {self.label_length} is characters.")

    @property
    def label_length(self):
        name_lenght = len(self.name)
        surname_lenght = len(self.surname)
        return name_lenght + surname_lenght


class BusinessContact(BaseContact):
    def __init__(self, company, position, business_phone, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.company = company
        self.position = position
        self.business_phone = business_phone

    def __repr__(self):
        return f"Names(name={self.name} surname={self.surname}, phone={self.phone}, email={self.email}, company={self.company}, position={self.position}, business_phone={self.business_phone})"

    def __str__(self):
        return f'{self.name} {self.surname}, {self.email}'

    def contact_bus(self):
        print(f'Wybieram numer: {self.business_phone} i dzwonię do {self.position} {self.surname}')
        print(f"Full name lenght {self.label_length} is characters.")


person1 = BaseContact(name="Dmitri", surname="Kovaltchuk", phone=504564298, email="dmitri.kovaltchuk@redarmy.ru")
person2 = BaseContact(name="John", surname="Rambo", phone=782432125, email="john.rambo@usarmy.us")
person3 = BaseContact(name="Kung", surname="Pao", phone=5557778888, email="kung.pao@chnarmy.ch")
person4 = BaseContact(name="Grzegorz", surname="Braun", phone=222556789, email="grzegorz.braun@conf.eu")
person5 = BaseContact(name="Leszek", surname="Miller", phone=607823456, email="leszek.miller@sld.pl")
person_new = BaseContact(name=f.first_name(), surname=f.last_name(), phone=f.phone_number(), email=f.email())

person1 = BusinessContact(name="Dmitri", surname="Kovaltchuk", phone=504564298, email="dmitri.kovaltchuk@redarmy.ru",
                          company="Red Army", position="captain", business_phone=222558790)
person2 = BusinessContact(name="John", surname="Rambo", phone=782432125, email="john.rambo@usarmy.us",
                          company="US Army", position="major", business_phone=222558780)
person3 = BusinessContact(name="Kung", surname="Pao", phone=5557778888, email="kung.pao@chnarmy.ch",
                          company="Chinese Army", position="general", business_phone=222558770)
person4 = BusinessContact(name="Grzegorz", surname="Braun", phone=222556789, email="grzegorz.braun@conf.eu",
                          company="Confederation", position="oppositionist", business_phone=222558760)
person5 = BusinessContact(name="Leszek", surname="Miller", phone=607823456, email="leszek.miller@sld.pl", company="SLD",
                          position="expert", business_phone=222558750)
person_new = BusinessContact(name=f.first_name(), surname=f.last_name(), phone=f.phone_number(), company=f.company(),
                             position=f.job(), business_phone=f.phone_number(), email=f.email())

names = [person1, person2, person3, person4, person5, person_new]
for person in names:
    print(person)

person1.contact()


def create_contact(contact_type, n):
    contacts = []
    if contact_type == "Business":
        for i in range(n):
            new_contact = BusinessContact(name=f.first_name(), surname=f.last_name(), phone=f.phone_number(),
                                          company=f.company(), position=f.job(), business_phone=f.phone_number(),
                                          email=f.email())
            contacts.append(new_contact)
            print(f" {new_contact}")
    elif contact_type == "Base":
        for i in range(n):
            new_contact = BaseContact(name=f.first_name(), surname=f.last_name(), phone=f.phone_number(),
                                      email=f.email())
            contacts.append(new_contact)
            print(f" {new_contact}")
    return contacts


create_contact("Business", 10)

print('------------------------------------------------------------------------------')