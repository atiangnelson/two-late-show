#  Late Show API

A full-featured Flask REST API for managing user accounts and personal notes with authentication and PostgreSQL integration.

---

##  Setup Instructions

### 1. Clone the Repository

```
git clone 
cd late-show-api
```



### 3. Install Dependencies



### 4. Set Up PostgreSQL

1. Access PostgreSQL:

```bash
sudo -u postgres psql
```

2. Create the database and user:

```
CREATE DATABASE late_show_db;
CREATE USER student WITH PASSWORD '12345';
GRANT ALL PRIVILEGES ON DATABASE late_show_db TO student;
ALTER DATABASE late_show_db OWNER TO student;
\q
```

3.  Change schema ownership:

```
psql -U postgres -d late_show_db
ALTER SCHEMA public OWNER TO student;
```

---

##  How to Run

### 1. Set Environment Variables



```
FLASK_APP=app
FLASK_ENV=development
SECRET_KEY=dev-secret
```

### 2. Run Migrations

```
flask db init         
flask db migrate -m "Initial migration"
flask db upgrade
```

### 3. Seed the Database


python seed.py


### 4. Start the Flask Server


flask run






### Register

```http
POST /register
Content-Type: application/json

{
  "username": "user1",
  "email": "user1@example.com",
  "password": "password"
}
```

### Login

```http
POST /login
Content-Type: application/json

{
  "email": "user1@example.com",
  "password": "password"
}
```

**Response:**
```json
{
  "access_token": "JWT_TOKEN"
}
```

Use this token in all protected routes by setting:

```
Authorization: Bearer JWT_TOKEN
```

---

