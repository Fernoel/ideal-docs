# Architecture

The Ideal platform is built on a modern, decoupled architecture consisting of two main repositories.

## Components

### 1. Backend (`Ideal-Sale-API-V2`)
- **Framework**: Laravel (PHP).
- **Database**: PostgreSQL (Primary), DynamoDB (High performance/Caching).
- **Cloud Infrastructure**: AWS (S3 for storage, Lambda for serverless functions).
- **Media**: ImageKit integration for real-time image optimization.

### 2. Frontend (`ideal-sale-circular`)
- **Framework**: Angular.
- **Type**: Single Page Application (SPA).
- **State Management**: RxJS / NGRX (if applicable).

## Data Flow
The Frontend communicates with the Backend via a **RESTful API**. Authentication is handled via **JWT (JSON Web Tokens)**.
