# API Reference

The Ideal API is a RESTful service provided by the `Ideal-Sale-API-V2` project.

## Key Directories
- **Controllers**: `App\Http\Controllers` - Handle incoming HTTP requests.
- **Services**: `App\Services` - Contains the core business logic (e.g., `MediaService`, `NodesService`).
- **Models**: `App\Models` - Eloquent ORM definitions.
- **DTOs**: `App\Http\Requests\Domain` - Data Transfer Objects for validation.

## Authentication
All protected endpoints require a valid **Bearer Token** in the `Authorization` header.
