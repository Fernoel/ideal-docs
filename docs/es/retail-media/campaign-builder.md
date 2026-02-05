# Constructor de Campañas

Cree y gestione campañas de Retail Media.

## Estructura de la Campaña
Una campaña consta de cuatro componentes principales, validados por el sistema:

| Componente | Requerido | Descripción |
|------------|-----------|-------------|
| **Vendedor (Vendor)** | **Sí** | La marca o anunciante que financia la campaña. |
| **Campaña**| **Sí** | Configuraciones generales (Fechas, Presupuesto, Nombre). |
| **Audiencia**| **Sí** | Parámetros de segmentación (Demografía, Ubicación). |
| **Creativo**| **Condicional**| Los activos visuales (Banner, Video). Requerido para campañas no MDI. |

## Tipos de Campaña
- **Estándar**: Anuncios de visualización.
- **MDI**: Integración Digital Gestionada (Creativo manejado externamente).
