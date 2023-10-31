# Open Prices

Exploring ways to enrich OpenFoodFacts with product prices.

## Setup

Prerequisites
- this project is developed in Python Django
- you need `pipenv` installed
- optional : PostgreSQL

1. Install dependencies
```
pipenv install
```

2. Environment variables
- duplicate `.env.example`
- rename to `.env`
- fill it with your credentials

3. Run migrations
```
pipenv run python manage.py migrate
```

## Usage

Run the server

```
pipenv run python manage.py runserver
```

## Other

Setup a PostgreSQL database

```
// create the database
psql -c "CREATE USER open_prices_team WITH PASSWORD 'password'"
psql -c "CREATE DATABASE open_prices OWNER open_prices_team"
psql -c "GRANT ALL PRIVILEGES ON DATABASE open_prices to open_prices_team"
psql -c "ALTER USER open_prices_team CREATEROLE CREATEDB"

// update your .env
DATABASE_URL = "postgres://open_prices_team:password@localhost:/open_prices"
```

Run tests

```
pipenv run test
```
