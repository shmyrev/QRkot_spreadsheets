## Проект QRKot

Приложение для Благотворительного фонда поддержки котиков QRKot.  
Фонд собирает пожертвования на различные целевые проекты: на медицинское  
обслуживание нуждающихся хвостатых, на обустройство кошачьей колонии в  
подвале, на корм оставшимся без попечения кошкам — на любые цели, связанные  
с поддержкой кошачьей популяции.  
Добавлена возможность формирования отчёта в гугл-таблице  

## Технологии
* Python 3.10.10  
* FastAPI 0.78.0  

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/shmyrev/QRkot_spreadsheets.git
```

```
cd QRkot_spreadsheets
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv venv
```

* Если у вас Linux/macOS

    ```
    source venv/bin/activate
    ```

* Если у вас windows

    ```
    source venv/scripts/activate
    ```

Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Создайте и заполните файл .env (пример .env.sample):
```
DATABASE_URL=sqlite+aiosqlite:///./fastapi.db
SECRET=secret
FIRST_SUPERUSER_EMAIL=admin@admin.com
FIRST_SUPERUSER_PASSWORD=admin

TYPE=service_account
PROJECT_ID=your_projectid
PRIVATE_KEY_ID=your_private_key
PRIVATE_KEY=-----BEGIN PRIVATE KEY-----your_private_key-----END PRIVATE KEY-----
CLIENT_EMAIL=client@your_projectid.iam.gserviceaccount.com
CLIENT_ID=123456789012345678901
AUTH_URI=https://accounts.google.com/o/oauth2/auth
TOKEN_URI=https://oauth2.googleapis.com/token
AUTH_PROVIDER_X509_CERT_URL=https://www.googleapis.com/oauth2/v1/certs
CLIENT_X509_CERT_URL=https://www.googleapis.com/robot/v1/metadata/x509/client%40your_projectid=.iam.gserviceaccount.com
EMAIL=your@gmail.com
```

Выполните миграции:
```
alembic upgrade head 
```

Запустите проект:
```
uvicorn app.main:app --reload
```

## Примеры запросов:
GET-запрос:
```
/charity_project/
```

Request:
```
[
  {
    "name": "string",
    "description": "string",
    "full_amount": 0,
    "id": 0,
    "invested_amount": 0,
    "fully_invested": true,
    "create_date": "2019-08-24T14:15:22Z",
    "close_date": "2019-08-24T14:15:22Z"
  }
]
```

POST-запрос:
```
/charity_project/
```

Request:
```
{
  "name": "string",
  "description": "string",
  "full_amount": 0
}
```