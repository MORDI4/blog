from blog import db
from blog.models import Entry
from faker import Faker
import random

# Inicjalizacja Faker
fake = Faker()

# Ile wpisów chcesz wygenerować
NUM_ENTRIES = 10

for _ in range(NUM_ENTRIES):
    entry = Entry(
        title=fake.sentence(nb_words=6),  # losowy tytuł
        body=fake.paragraph(nb_sentences=5),  # losowy tekst
        pub_date=fake.date_time_this_year(),  # losowa data w tym roku
        is_published=random.choice([True, False])  # losowo opublikowany lub nie
    )
    db.session.add(entry)

# Zapis do bazy
db.session.commit()

print(f"{NUM_ENTRIES} nowych wpisów zostało dodanych do bazy danych!")
