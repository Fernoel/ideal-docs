# Referencia de API

La API de Ideal es un servicio RESTful proporcionado por el proyecto `Ideal-Sale-API-V2`.

## Directorios Clave
- **Controladores**: `App\Http\Controllers` - Manejan las solicitudes HTTP entrantes.
- **Servicios**: `App\Services` - Contiene la lógica de negocio central (ej. `MediaService`, `NodesService`).
- **Modelos**: `App\Models` - Definiciones de ORM Eloquent.
- **DTOs**: `App\Http\Requests\Domain` - Objetos de Transferencia de Datos para validación.

## Autenticación
Todos los endpoints protegidos requieren un **Token Bearer** válido en el encabezado `Authorization`.
