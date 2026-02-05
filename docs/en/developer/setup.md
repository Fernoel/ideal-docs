# Setup & Installation

## Prerequisites
- **PHP**: Version 8.0 or higher.
- **Node.js**: LTS Version.
- **Composer**: PHP Dependency Manager.
- **Docker**: For containerized development (recommended).

## Installation Steps

### Backend
1. Clone the `ideal-sale-api-v2` repository.
2. Run `composer install` to install dependencies.
3. Copy `.env.example` to `.env` and configure your database credentials.
4. Run `php artisan key:generate`.
5. Run `php artisan migrate` to set up the database schema.

### Frontend
1. Clone the `ideal-sale-circular` repository.
2. Run `npm install` to install dependencies.
3. Run `npm start` to launch the development server (usually on `localhost:4200`).
