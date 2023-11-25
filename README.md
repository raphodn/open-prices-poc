# Open Prices

Exploring ways to enrich OpenFoodFacts with product prices.

## Setup

Prerequisites
- this project is developed in Python Django
- you need `pipenv` installed
- optional : PostgreSQL

1. Install dependencies
```
pipenv install --dev
```

2. Setup a PostgreSQL database
```
// create the database
psql -c "CREATE USER open_prices_team WITH PASSWORD 'password'"
psql -c "CREATE DATABASE open_prices_poc OWNER open_prices_team"
psql -c "GRANT ALL PRIVILEGES ON DATABASE open_prices_poc to open_prices_team"
psql -c "ALTER USER open_prices_team CREATEROLE CREATEDB"

// update your .env
DATABASE_URL = "postgres://open_prices_team:password@localhost:/open_prices_poc"
```

3. Environment variables
- duplicate `.env.example`
- rename to `.env`
- fill it with your credentials

4. Run migrations
```
pipenv run python manage.py migrate
```

## Usage

Run the server

```
pipenv run python manage.py runserver
```

## Contribute

Setup pre-commit
```
pipenv run pre-commit install
```

Run tests
```
pipenv run test
```
