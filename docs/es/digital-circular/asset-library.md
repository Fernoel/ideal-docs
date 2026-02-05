# Biblioteca de Activos (Asset Library)

La Biblioteca de Activos es el repositorio central para todos los archivos multimedia (imágenes, videos) utilizados en los Circulares Digitales y campañas de Retail Media.

## Proceso de Carga de Imágenes
El sistema utiliza un flujo de trabajo seguro de **URL Prefirmada (Presigned URL)** para manejar cargas de alto rendimiento directamente al almacenamiento en la nube.

1.  **Solicitud de Carga**: El frontend solicita una URL de carga segura al backend.
2.  **Carga Directa**: El archivo se sube directamente al bucket S3 usando la URL proporcionada.
3.  **Procesamiento**: El sistema procesa la imagen (extrayendo metadatos como ancho, alto, tipo MIME) y la registra en la base de datos.
4.  **Caché**: El sistema activa automáticamente un trabajo `ClearImagekitCacheJob` para asegurar que el nuevo activo esté disponible inmediatamente a través de la CDN de ImageKit.

## Estructura de Carpetas
Los activos se organizan lógicamente para asegurar la separación entre marcas y tiendas:

`uploads/{brand_namespace}/{node_namespace}/{date_namespace}/`

- **brand_namespace**: Identificador único para la cadena minorista.
- **node_namespace**: Identificador único para la tienda/ubicación específica.
- **date_namespace**: Carpeta basada en fecha para prevenir colisiones.

## Formatos Soportados
- **Imágenes**: JPG, PNG, WEBP.
- **Videos**: MP4 (usado en Ofertas de Video y Retail Media).

## Detalles Técnicos (`MediaService`)
- **Cargas Prefirmadas**: Manejadas por `createPresignedUploads` en `MediaService.php`.
- **Imágenes del Sistema**: Iconos y logotipos se almacenan en rutas específicas `sys/`.
- **Resolución**: El sistema detecta automáticamente las dimensiones de la imagen (`width`, `height`) al cargar.
