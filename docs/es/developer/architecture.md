# Arquitectura

La plataforma Ideal está construida sobre una arquitectura moderna y desacoplada que consta de dos repositorios principales.

## Componentes

### 1. Backend (`Ideal-Sale-API-V2`)
- **Framework**: Laravel (PHP).
- **Base de Datos**: PostgreSQL (Primaria), DynamoDB (Alto rendimiento/Caché).
- **Infraestructura en la Nube**: AWS (S3 para almacenamiento, Lambda para funciones serverless).
- **Multimedia**: Integración con ImageKit para optimización de imágenes en tiempo real.

### 2. Frontend (`ideal-sale-circular`)
- **Framework**: Angular.
- **Tipo**: Aplicación de Página Única (SPA).
- **Gestión de Estado**: RxJS / NGRX (si aplica).

## Flujo de Datos
El Frontend se comunica con el Backend a través de una **API RESTful**. La autenticación se maneja mediante **JWT (JSON Web Tokens)**.
