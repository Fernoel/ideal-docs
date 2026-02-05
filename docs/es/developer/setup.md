# Configuración e Instalación

## Prerrequisitos
- **PHP**: Versión 8.0 o superior.
- **Node.js**: Versión LTS.
- **Composer**: Gestor de dependencias de PHP.
- **Docker**: Para desarrollo en contenedores (recomendado).

## Pasos de Instalación

### Backend
1. Clone el repositorio `ideal-sale-api-v2`.
2. Ejecute `composer install` para instalar dependencias.
3. Copie `.env.example` a `.env` y configure sus credenciales de base de datos.
4. Ejecute `php artisan key:generate`.
5. Ejecute `php artisan migrate` para configurar el esquema de la base de datos.

### Frontend
1. Clone el repositorio `ideal-sale-circular`.
2. Ejecute `npm install` para instalar dependencias.
3. Ejecute `npm start` para lanzar el servidor de desarrollo (usualmente en `localhost:4200`).
