# Marcas Minoristas (Tiendas)

Este módulo permite gestionar las ubicaciones de las tiendas (nodos). Es el lugar central para configurar ajustes específicos de la tienda, datos de ubicación y parámetros de integración.

## Campos de Configuración de la Tienda

Al crear o editar una tienda, los siguientes campos están disponibles. Los campos **Obligatorios** deben completarse para guardar la tienda.

| Campo | Tipo | Obligatorio | Descripción |
|-------|------|-------------|-------------|
| `name` | Texto | **Sí** | El nombre visible de la tienda. |
| `address.address1` | Texto | **Sí** | Dirección principal. |
| `address.city` | Texto | **Sí** | Ciudad. |
| `address.state` | Texto | **Sí** | Estado o Provincia. |
| `address.zip` | Texto | **Sí** | Código Postal. |
| `phone` | Texto | **Sí** | Número de teléfono de contacto. |
| `googleMapsHref` | Texto | **Sí** | Enlace directo a la ubicación en Google Maps. |
| `circularPath` | Texto | **Sí** | URL única para el circular (ej. `ofertas-semanales`). Debe ser única. |
| `active` | Booleano | **Sí** | Controla si la tienda es visible y está activa en el sistema. |
| `showContactInformation`| Booleano | **Sí** | Muestra u oculta la dirección/teléfono en el circular público. |
| `googlePlaceId` | Texto | **Sí** | ID de la API de Google Places (usado para mapas/SEO). |
| `latitude` | Decimal | **Sí** | Coordenada de Latitud GPS. |
| `longitude` | Decimal | **Sí** | Coordenada de Longitud GPS. |

### Configuración Opcional
- **Hours (Horario)**: Campo de texto para el horario de atención.
- **Notes (Notas)**: Notas internas para administradores.
- **Theme (Tema)**: Identificador de tema personalizado para sobrescribir el predeterminado de la marca.
- **Go Live Date (Fecha de Lanzamiento)**: Fecha programada para que la tienda esté activa.
- **Coupon Integration (Integración de Cupones)**: Ajustes para conectar con proveedores de cupones externos.

### Reglas de Validación Técnica
- **Circular Path**: Validado por `CircularPathRule`. Debe ser único dentro de la jerarquía de la marca.
- **National ID**: Validado por `NationalIdRule`.
- **Coordenadas**: Latitud y Longitud son requeridas para la funcionalidad de localizador de tiendas.
