# JAM Shop — E-commerce Fullstack App

A full-stack web application for selling jams online, built with a focus on clean architecture, code quality, testing, and security.

## Tech Stack

| Layer | Technology |
|---|---|
| Frontend | Vue.js 3 + TypeScript |
| Backend | Django REST Framework |
| Database | MySQL |
| Payments | Stripe |
| Testing | Vitest (frontend) + Django test runner (backend) |
| Infrastructure | Docker & Docker Compose |

## Key Features

- JWT-based secure authentication
- Advanced faceted search and filters
- Online payments with Stripe
- Versioned REST API
- Full application containerization
- Unit, integration, and end-to-end tests (frontend & backend)
- Admin dashboard for product management

## Getting Started

### Prerequisites

- [Docker and Docker Compose](https://docs.docker.com/get-docker/)
- A [Stripe](https://stripe.com) account (test keys)

### Setup

1. Clone the repository
```bash
git clone https://github.com/Cristina-MariaG/JAM_APP_-Ecommerce-.git
cd JAM_APP_-Ecommerce-
```

2. Create your environment file from the example
```bash
cp .env.example .env.local
```

3. Fill in your own values in `.env.local` (Stripe keys, DB passwords, etc.)

4. Create external networks and volumes
```bash
./setup.sh
```

5. Launch the stack
```bash
docker-compose up
```

The following URLs will be available:
- Frontend: http://localhost:8000/
- Backend API: http://localhost:8213/

## Running Tests

### Frontend

```bash
# Run all tests
docker exec jam-front npm run test

# Watch mode
docker exec jam-front npm run watch

# Coverage report
docker exec jam-front npm run coverage
```

### Backend

```bash
# Enter the container
docker exec -it jam-back bash

# Run all tests
python3.10 manage.py test back_app/tests -v 2

# Run a specific test file
python3.10 manage.py test back_app/tests -k test_refresh_token

# Or in one line
docker exec jam-back python3.10 manage.py test back_app/tests -v 2
```

## Project Structure

```
JAM_APP/
├── backend/        # Django REST API
├── front/          # Vue.js 3 frontend
├── docker-compose.yml
├── setup.sh        # Network and volume setup
└── .env.example    # Environment variables template
```
