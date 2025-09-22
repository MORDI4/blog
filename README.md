# Blog – Aplikacja webowa w Flasku

Prosty blog oparty na frameworku Flask, umożliwiający tworzenie, edytowanie, usuwanie oraz publikowanie wpisów. Aplikacja wspiera również szkice, które można zapisać przed opublikowaniem.

---

## 📌 Spis treści

1. [Opis projektu](#-opis-projektu)
2. [Funkcje](#-funkcje)
3. [Technologie](#-technologie)
4. [Instalacja](#-instalacja)
5. [Użycie](#-użycie)
6. [Licencja](#-licencja)

---

## 📝 Opis projektu

Blog stworzony w ramach nauki programowania w Pythonie z wykorzystaniem frameworku Flask. Aplikacja pozwala na:

- Tworzenie nowych wpisów
- Edycję istniejących wpisów
- Usuwanie wpisów
- Przechowywanie szkiców przed opublikowaniem
- Publikację wpisów na stronie głównej

Aplikacja wykorzystuje bazę danych SQLite oraz obsługuje migracje za pomocą Flask-Migrate.

---

## 🔧 Funkcje

- Tworzenie, edytowanie i usuwanie wpisów
- Zarządzanie szkicami i opublikowanymi wpisami
- Autentykacja użytkowników (logowanie/wylogowanie)
- Obsługa sesji użytkownika
- Interfejs oparty na Bootstrapie
- Wykorzystanie Flask-WTF do obsługi formularzy

---

## ⚙️ Technologie

- Python 3.10+
- Flask 2.3.0+
- Flask-SQLAlchemy 3.0.0+
- Flask-Migrate 4.0.0+
- Flask-WTF
- Bootstrap 5
- SQLite

---

## 🚀 Instalacja

1. **Sklonuj repozytorium:**

   ```bash
   git clone https://github.com/MORDI4/blog.git
   cd blog

1. **Utwórz i aktywuj wirtualne środowisko:**

    ```bash
    python -m venv venv
    source venv/bin/activate  # Na systemach Unix/MacOS
    venv\Scripts\activate     # Na systemie Windows

1. **Zainstaluj zależności:**

    ```bash
    pip install -r requirements.txt

1. **Skonfiguruj plik .flaskenv:**

Utwórz plik .flaskenv w katalogu głównym projektu z następującą zawartością:

    ```bash
    FLASK_APP=app.py
    FLASK_ENV=development


1. **Utwórz bazę danych i wykonaj migracje:**

    ```bash
    flask db init
    flask db migrate
    flask db upgrade


1. **Uruchom aplikację:**

    ```bash
    flask run

Aplikacja będzie dostępna pod adresem http://127.0.0.1:5000/

## 🧪 Użycie
- /newpost – formularz do tworzenia nowego wpisu
- /edit-post/<id> – formularz do edycji istniejącego wpisu
- /drafts – lista zapisanych szkiców
- /delete/<id> – usunięcie wpisu (dostępne po zalogowaniu)

Aby uzyskać dostęp do funkcji wymagających logowania, użyj domyślnych danych logowania:

- Login: admin
- Hasło: admin

## 🔗 Link do aplikacji

Aplikacja jest dostępna online pod adresem:
https://blog-production-f954.up.railway.app/