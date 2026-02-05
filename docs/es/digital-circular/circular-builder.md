# Módulo Circular Builder

## Descripción General
El módulo Circular Builder es el núcleo para crear contenido para volantes digitales. Aquí puedes generar promociones, ofertas y elementos visuales que se integran en los volantes. La interfaz principal incluye:

- Un menú lateral izquierdo con opciones como Dashboard, Digital Circular, Circular Builder, Categorías, etc.
- Un selector de tienda o marca (por ejemplo, "Fernando First Store").
- Un calendario para seleccionar fechas de publicación.
- Una tabla (data-grid) que lista los elementos de contenido existentes, con columnas como DÍAS (días de validez), TIPO DE OFERTA (deal type), PROPIETARIO (owner), TAMAÑO (size) y opciones de ver/editar.
- Un panel de vista previa a la derecha que muestra tarjetas de promoción con imágenes, precios y descuentos.

![Interfaz principal de Circular Builder]](../assets/screenshots/content%20(1).png)
> *Interfaz principal de Circular Builder con tabla de contenido y vista previa.*

## Prerrequisitos para Crear Contenido
Antes de crear nuevo contenido, asegúrate de cumplir con los siguientes prerrequisitos:

1. **Creación de Nodo**: Debes haber creado al menos un nodo, que puede ser una Marca, Sub-Marca o Tienda. Esto define el contexto en el que se aplicará el contenido.
2. **Creación de Categoría**: Es obligatorio tener al menos una categoría creada en el módulo de Categorías. Sin una categoría asignada, no podrás completar la creación del contenido, ya que es un campo requerido.

!!! warning "Requisito"
    Si no se cumplen estos prerrequisitos, el sistema no te permitirá guardar el nuevo contenido. Ve a los módulos correspondientes (por ejemplo, Marcas Retail o Categorías) para configurarlos primero.

## Flujo de Trabajo Básico para Crear Contenido
Sigue estos pasos para crear un nuevo elemento de contenido en Circular Builder:

### 1. Acceder al Módulo
- Inicia sesión en la plataforma como administrador.
- En el menú lateral izquierdo, selecciona **Digital Circular > Circular Builder**.
- Elige la tienda o marca deseada en el selector superior (por ejemplo, "Biswa First Store").

### 2. Iniciar Creación
- En la interfaz principal, haz clic en el botón **New Card** (o "New Content", dependiendo de la versión).
- Esto abrirá una nueva pestaña o formulario de creación titulado "Create Single Promotion" o similar.

### 3. Completar el Formulario de Creación
El formulario se divide en secciones como Contenido, Oferta/Deal, Rango de Fechas, Medios, Encabezado, Fondo, etc.
Completa todos los campos requeridos (marcados con *). Los campos clave incluyen:

- **Contenido**: Título, Descripción, Texto de Fecha (Display), Categoría (selecciona una existente), Ancho, Alto y Tamaño (por ejemplo, Pequeño).
- **Oferta/Deal**: Estilo de Tarjeta (por ejemplo, Cupón), Tipo de Oferta (por ejemplo, Estática (Sin Precio), Precio Fijo, Compra X Obtén Y por Z), Cantidad Requerida, Límite, UPC (código de producto).
- **Cupón**: Si aplica, incluye manualmente un cupón con ID de Cupón, Requerido, Límite y Descuento (Amount Off).
- **Rango de Fechas**: Fechas de inicio (Starts on) y vencimiento (Expires).
- **Medios**: Carga o selecciona medios (imágenes, iconos), encabezado (Headline), fondo (Color de Fondo o Imagen), posición (Position - por ejemplo, Centro).
- **Vista Previa**: Usa el panel de vista previa a la derecha para ver cómo lucirá la promoción en tiempo real.

> Asegúrate de que todos los campos obligatorios estén completos; de lo contrario, no podrás guardar.

![Formulario de creación](../assets/screenshots/content.png)
> *Formulario de creación "Create Single Promotion" con secciones y vista previa.*

### 4. Guardar el Contenido
- Una vez completados todos los campos, haz clic en **Save** o **Create** (el botón puede variar según la interfaz).
- El nuevo contenido aparecerá automáticamente en la tabla principal (data-grid) del módulo Circular Builder.
- Puedes editar, eliminar o previsualizar el contenido desde la tabla usando los iconos correspondientes (por ejemplo, icono de ojo para ver, tijeras para editar).

## Cómo Crear Contenido Usando Carga Masiva (Bulk Upload)

La función de Carga Masiva de Contenido te permite crear múltiples elementos de contenido a la vez subiendo un archivo masivo formateado correctamente (típicamente una hoja de cálculo o archivo estructurado que contiene datos de promociones) junto con los archivos multimedia asociados. Esto es especialmente útil cuando necesitas crear docenas o cientos de promociones en una sola operación.

!!! important "Prerrequisito Importante"
    Antes de usar la Carga Masiva, debes preparar y tener listo un archivo de Carga Masiva de Contenido válido. Este archivo debe seguir el formato y estructura exactos esperados por la plataforma (columnas, campos requeridos, convenciones de nomenclatura, etc.). Contacta a tu administrador o consulta la Documentación de Plantilla de Carga Masiva (si está disponible) para obtener la plantilla e instrucciones correctas.

### Flujo de Trabajo Paso a Paso para Carga Masiva

#### Acceder a Carga Masiva
1. Ve al módulo Circular Builder.
2. Selecciona la tienda/marca deseada usando el selector superior (por ejemplo, "Fernando First Store").
3. En la interfaz principal, haz clic en el botón **Bulk Upload** (generalmente ubicado cerca del botón "New Card").
4. Esta acción abre el asistente de Gestión de Contenido titulado algo como "Manage Content for [Store Name]".

#### Paso 1 – Subir tus Medios
- Verás un área de arrastrar y soltar etiquetada como "Drop your media files here" y un botón **+ Choose**.
- **Importante**: El sistema solo acepta formatos de archivo de imagen y video. Otros tipos de archivo serán rechazados.
- Arrastra y suelta tus archivos multimedia o haz clic en **+ Choose** para seleccionarlos desde tu computadora.
- Espera hasta que todos los archivos terminen de subirse completamente.
    - Un indicador de progreso o columna de estado mostrará cuando cada archivo haya sido procesado exitosamente.
    - Solo cuando todas las cargas estén completas se activará el botón **Next**.
- Haz clic en **Next** para continuar.

#### Paso 2 – Seleccionar tu Rango de Fechas
- En este paso, puedes definir un rango de fechas común que se aplicará a todos (o la mayoría) de los elementos de contenido que se están subiendo.
- Usa los controles de calendario para establecer las fechas de **Starts on** (Inicio) y **Expires** (Vencimiento).
- Si no necesitas un rango de fechas específico para esta operación masiva (o si las fechas ya están definidas en el archivo masivo), simplemente haz clic en **Next** para omitir este paso.

#### Paso 3 – Carga de Contenido y Gestión de Categorías
El sistema procesa el archivo masivo subido e intenta coincidir o crear categorías.

**Comportamiento dependiendo de las categorías:**
- **Si las categorías ya existen en el nodo actual (marca/tienda)**: Aparecerá un mensaje de éxito indicando que las categorías fueron encontradas o coincidieron exitosamente.
- **Si las categorías son nuevas para este nodo**: Verás dos opciones principales para cada nueva categoría:
    - **Create**: Haz clic en el botón Create para generar automáticamente la nueva categoría en el sistema.
    - **Map**: Selecciona una categoría existente de la lista desplegable y mapea el nombre de la nueva categoría a una ya existente.
- **Opción Ignorar**: Marca la casilla Ignore para categorías individuales o usa una opción "Select All / Ignore All" si está disponible. Las categorías ignoradas no serán creadas ni mapeadas.

Después de manejar todas las categorías (crear, mapear o ignorar), haz clic en **Next**.

!!! warning "Nota Importante sobre Ignorar Categorías"
    - Si ignoras una o más categorías, el sistema te permitirá continuar.
    - Sin embargo, en el paso de vista previa (Paso 5), cualquier elemento de contenido sin una categoría asignada será marcado con un error.
    - **Para corregir estos errores**:
        1. Haz clic en el icono de edición en el elemento de contenido afectado, o
        2. Haz clic en el mensaje/notificación de error para abrir la herramienta de asignación de categorías.
        3. Asigna una categoría válida y guarda.

#### Paso 4 – Revisión / Vista Previa
Este paso muestra una vista previa completa de todos los elementos de contenido que serán creados desde el archivo masivo.
Revisa la tabla cuidadosamente:
- Verifica títulos, tipos de oferta, tamaños, asignaciones de medios, fechas, categorías, etc.
- Busca cualquier indicador de error (especialmente categorías faltantes).

> Corrige cualquier problema directamente en esta vista si la interfaz permite la edición en línea, o regresa a los pasos anteriores.

#### Paso 5 – Finalizar y Guardar
Verás una tabla final listando todos los elementos de contenido que serán creados.
En esta tabla puedes:
- **Eliminar** elementos individuales (si no deseas crearlos)
- **Editar** elementos individuales (modificar título, tipo de oferta, categoría, medios, etc.)

Cuando todo se vea correcto y no haya errores restantes, haz clic en el botón **Done**.
El sistema comenzará a procesar y guardar todos los elementos de contenido.
Una vez completado, serás redirigido de vuelta a la tabla principal de Circular Builder, donde aparecerán los elementos de contenido recién creados.

### Consejos para Cargas Masivas Exitosas
- **Usa siempre la plantilla oficial** proporcionada por la plataforma para evitar errores de formato.
- **Sube todos los archivos multimedia relacionados** antes o junto con el procesamiento del archivo masivo.
- **Sé paciente durante la carga de medios** — no cierres la ventana ni navegues fuera hasta que todos los archivos muestren 100% completo.
- **Resuelve problemas de categorías** antes del guardado final para evitar tener que editar muchos elementos individualmente más tarde.
- **Después de una carga masiva exitosa**, usa el botón Export en la tabla principal para descargar y verificar el contenido recién creado.

## Entendiendo la Plantilla de Carga Masiva de Contenido

La función de Carga Masiva de Contenido se basa en un archivo estructurado (usualmente un `.xlsx`, `.xls` o `.csv`) que contiene toda la información necesaria para crear múltiples tarjetas de promoción a la vez. Esta plantilla define exactamente qué columnas se esperan, cuáles son obligatorias y qué tipo de datos deben ir en cada una.

### Dónde Obtener la Plantilla

- **La forma más confiable** es solicitar la Plantilla de Carga Masiva oficial a tu administrador de plataforma o al equipo de soporte.
- En algunas versiones de la plataforma, puede haber un botón o enlace de **Descargar Plantilla** dentro del asistente de Carga Masiva (generalmente visible después de hacer clic en "Bulk Upload").
- Si no hay una plantilla disponible, contacta a soporte a través del módulo Support Portal para solicitar la versión actual.

!!! important "Importante"
    Usar un archivo que no coincida con la estructura esperada causará errores durante la carga. Usa siempre la plantilla oficial o más reciente.

### Columnas Principales en la Plantilla de Carga Masiva

A continuación se muestra la estructura típica de la plantilla (los nombres exactos de las columnas y el orden pueden variar ligeramente según la versión de la plataforma — verifica siempre con tu plantilla actual).

| Nombre de Columna | ¿Requerido? | Descripción / Formato Esperado | Valores de Ejemplo | Notas |
| :--- | :---: | :--- | :--- | :--- |
| **Title** | Sí | El título principal de la tarjeta de promoción (en inglés o el idioma seleccionado) | `"2x1 en Pastas"` | Mantenlo corto y atractivo |
| **Description** | No | Descripción más larga o detalles de la oferta | `"Lleva 2 paquetes y paga solo 1"` | Puede incluir saltos de línea si el sistema lo soporta |
| **Deal Type** | Sí | El tipo de oferta / promoción | `Fixed Price`, `Buy X Get Y For Z`, `Amount Off`, `Static (No Price)`, `Coupon`, `# for Price` | Debe coincidir exactamente con uno de los valores permitidos |
| **Card Style** | Sí | Estilo visual de la tarjeta | `Coupon`, `Banner`, `Standard`, `Menu Item` | Afecta el diseño y los campos disponibles |
| **Size** | Sí | Tamaño de cuadrícula de la tarjeta en el volante | `1x1`, `1x2`, `2x1`, `2x2`, `3x1`, etc. | Valores comunes: 1×1, 1×2, 2×2 |
| **Width** | Sí | Valor del ancho (numérico) | `1`, `2`, `3` | Usualmente coincide con el primer número en Size |
| **Height** | Sí | Valor de la altura (numérico) | `1`, `2` | Usualmente coincide con el segundo número en Size |
| **Category** | Sí | Nombre de la categoría donde pertenece esta promoción | `"Bebidas"`, `"Lácteos"`, `"Frutas y Verduras"` | Debe existir o será creada/mapeada en el paso 3 |
| **Starts On** | No | Fecha de inicio de la promoción | `2026-02-08 00:00` | Formato: YYYY-MM-DD HH:MM o solo YYYY-MM-DD |
| **Expires** | No | Fecha de fin de la promoción | `2026-02-14 23:59` | Si está vacío, puede usar un rango de fechas predeterminado o global |
| **Coupon ID** | Condicional | Identificador único para el cupón (solo si Deal Type = Coupon) | `CUPON2026-XYZ123` | Requerido solo para promociones estilo cupón |
| **Amount Off** | Condicional | Cantidad de descuento (moneda o porcentaje) | `5.99`, `30%`, `$4.00 OFF` | Depende del Deal Type |
| **Quantity Required** | Condicional | Número de artículos necesarios para activar la oferta | `2` | Usado en ofertas tipo "Buy X Get Y" |
| **Limit** | No | Usos máximos por cliente o límite total | `1`, `4`, `Unlimited` | "Unlimited" o dejar en blanco si no hay límite |
| **UPC / SKU** | No | Código(s) de producto – puede ser uno o múltiples (separados por comas) | `7501234567890`, `7509876543210` | Usado para promociones específicas de producto |
| **Media Filename 1** | Condicional | Nombre del archivo de imagen principal (debe subirse en el Paso 1) | `promo_bebidas_2x1.jpg` | Nombre exacto incluyendo extensión |
| **Media Filename 2** | No | Imagen secundaria o icono | `icon_descuento.png` | Opcional – depende del estilo de tarjeta |
| **Headline** | No | Texto corto resaltado (a menudo aparece en negrita) | `"¡Oferta Exclusiva!"` | Opcional pero recomendado |
| **Background Color** | No | Código de color Hex para fondo | `#FF0000`, `#FFFFFF` | Solo si no se usa imagen de fondo |
| **Language** | No | Código de idioma de esta fila | `EN`, `ES` | Usualmente EN o ES – por defecto el idioma de la plataforma si está vacío |

### Reglas Clave y Mejores Prácticas

- **Los campos requeridos** deben llenarse en cada fila. Valores requeridos faltantes causarán que toda la fila (o toda la carga) falle.
- **Coincidencia exacta para campos controlados**: Deal Type, Card Style, Size, etc. deben coincidir con los valores que el sistema reconoce (distingue mayúsculas y minúsculas en la mayoría de los casos).
- **Fechas**: Usa un formato consistente (preferiblemente AAAA-MM-DD). Si las dejas en blanco, se pueden aplicar las fechas definidas en el Paso 2 (o un rango predeterminado).
- **Archivos de medios**: Los nombres de archivo en la hoja de cálculo deben coincidir exactamente con los nombres de los archivos que subes en el Paso 1 (incluyendo extensión: `.jpg`, `.png`, `.mp4`, etc.).
- **Una fila = una tarjeta de promoción**. Cada fila en la hoja de cálculo crea una tarjeta de contenido/promoción individual.
- **Categorías**: Si el nombre de la categoría no existe en la marca/tienda actual, se te pedirá que la crees o mapees en el Paso 3.
- **Validación**: El sistema realiza validación durante el procesamiento. Errores comunes incluyen:
    - Columnas requeridas faltantes
    - Valores inválidos de Deal Type o Size
    - Nombre de archivo de medio no encontrado entre los archivos subidos
    - Categoría no resuelta (no creada/mapeada/ignorada)

### Flujo de Trabajo Recomendado para Preparar un Archivo Masivo

1. **Descarga la plantilla oficial**.
2. **Llena tus promociones fila por fila** (una promoción = una fila).
3. **Prepara todas las imágenes/videos** referenciados en las columnas "Media Filename".
4. **Guarda el archivo** (preferiblemente `.xlsx`).
5. **Ve a Circular Builder** → haz clic en **Bulk Upload**.
6. **Sube tus archivos de medios primero** (Paso 1).
7. **Avanza a través del asistente**, mapeando categorías según sea necesario.
8. **Revisa todo cuidadosamente** en el paso de vista previa.
9. **Haz clic en Done** cuando estés listo.

> **Consejo**: Si tienes dudas sobre valores específicos de columnas u opciones permitidas (por ejemplo, la lista completa de Tipos de Oferta o Estilos de Tarjeta), pregunta a tu administrador o verifica dentro de la plataforma creando una sola promoción primero para ver las opciones desplegables.

## Editando Contenido en Circular Builder

Una vez que el contenido (promociones/tarjetas) ha sido creado y aparece en la tabla principal (data-grid) del módulo Circular Builder, puedes editarlo en cualquier momento — ya sea individualmente o de forma masiva.

Existen dos formas principales de editar contenido:

1. **Edición Individual** (una promoción a la vez)
2. **Edición Masiva** (múltiples promociones a la vez)

### 1. Editando una Sola Promoción

**Pasos:**

1. En la pantalla principal de Circular Builder, localiza la promoción que deseas editar en la tabla.
2. Selecciona la fila deseada haciendo clic en la casilla de verificación al principio de la fila (o simplemente haz clic en la fila si la interfaz permite la selección directa).
3. Haz clic en el icono **Edit** (usualmente un lápiz) o haz doble clic en la fila — esto abrirá la promoción en la pestaña Editor.
4. Alternativamente, selecciona la fila y luego haz clic en la pestaña **Editor** en la parte superior de la interfaz.

La pantalla **Edit Single Promotion** o **EDITOR** se abrirá, mostrando todos los valores actuales de la promoción (muy similar al formulario de creación).
Puedes modificar cualquier campo que necesites:

- **Título, Descripción, Categoría**
- **Tipo de Oferta, Precio, Cantidad Requerida, Límite**, etc.
- **Fechas** (Inicio / Vencimiento)
- **Medios** (cambiar imagen, fondo, iconos)
- **Tamaño, Ancho, Alto**
- **Encabezado, configuración de Cupón, color/imagen de Fondo**, etc.

Tan pronto como termines de hacer cambios, la plataforma guarda automáticamente las modificaciones en la mayoría de los casos.
Puedes ver una notificación como "You have made 1 change to your selected cards" (Has realizado 1 cambio en tus tarjetas seleccionadas).
En algunas vistas, es posible que necesites hacer clic en **Update** o **Save** para confirmar.

El **panel de vista previa** a la derecha se actualiza en tiempo real para que puedas verificar cómo se ven los cambios.

> **Consejo**: Usa los botones **← Previous** y **Next →** para navegar y editar rápidamente varias promociones una tras otra sin volver a la tabla principal.

### 2. Edición Masiva (Editando Múltiples Promociones a la Vez)

La edición masiva es muy útil cuando necesitas aplicar el mismo cambio a muchas promociones simultáneamente — por ejemplo:

- Cambiar la categoría para un grupo de artículos
- Actualizar el rango de fechas para una campaña completa
- Modificar el tipo de oferta, tamaño, color de fondo o cualquier otro campo común en múltiples tarjetas

**Pasos:**

1. En la tabla principal de Circular Builder, selecciona dos o más promociones:
    - Haz clic en la casilla de verificación al principio de cada fila que desees editar.
    - O usa **Shift + clic** o **Ctrl + clic** para seleccionar múltiples filas rápidamente.

2. Una vez que al menos dos elementos están seleccionados, el sistema activa el modo de edición masiva.
    - Usualmente verás una notificación o la pestaña Editor se volverá disponible para edición masiva.

3. Haz clic en la pestaña **Editor** (ahora etiquetada algo como **Edit Multiple Promotions**).

4. La pantalla **Edit Multiple Promotions** se abre:
    - El formulario se ve similar al formulario de edición individual, pero los cambios realizados aquí se aplicarán a **todas las promociones seleccionadas**.
    - Los campos que actualmente tienen valores diferentes entre los elementos seleccionados pueden aparecer en blanco, con un símbolo "-", o resaltados en amarillo.

5. **Modifica solo los campos que deseas actualizar** para todas las promociones seleccionadas.
    - Ejemplos:
        - Cambiar **Categoría** → selecciona una nueva de la lista
        - Actualizar **Rango de Fechas** → establece nuevas fechas de Inicio / Vencimiento
        - Cambiar **Tipo de Oferta, Tamaño, Color de Fondo**, etc.

6. Deja los campos en blanco si no deseas cambiarlos (solo los campos modificados serán aplicados).

7. Después de hacer los cambios deseados, haz clic en el botón **Update [X] Cards** (por ejemplo, "Update 4 Cards").

8. El sistema aplica los cambios a todas las promociones seleccionadas.
    - Aparece un mensaje de confirmación (por ejemplo, "You have made X changes to your selected cards").
    - Las actualizaciones se guardan inmediatamente.

9. Regresa a la tabla principal para verificar que todas las promociones seleccionadas ahora reflejen los nuevos valores.

**Notas Importantes sobre Edición Masiva:**

- **Solo se aplican los campos cambiados**. Si dejas un campo vacío o sin cambios, mantendrá su valor original para cada promoción.
- **Advertencia de valores mixtos**: Cuando las promociones seleccionadas tienen valores diferentes en un campo, el campo puede mostrar "-" o estar resaltado. Ten cuidado — actualizarlo sobrescribirá todas las variaciones con el nuevo valor.
- **Sin vista previa individual por tarjeta en modo masivo** — la vista previa muestra un ejemplo representativo.
- Usa la edición masiva para **cambios de consistencia** (categoría, fechas, estilo, etc.). Para ediciones muy específicas o únicas, usa la edición individual.

**Mejor Práctica:**
Siempre revisa algunos elementos en la tabla principal después de una edición masiva para confirmar que los cambios se aplicaron correctamente.

## Consejos y Mejores Prácticas

- **Validación de Campos**: Si falta un campo requerido (como Categoría), el sistema mostrará un error. Verifica nuevamente los prerrequisitos.
- **Vista Previa**: Verifica siempre la vista previa para asegurarte de que el diseño se vea bien en diferentes tamaños (por ejemplo, 1×1, 2×2).
- **Gestión de Grupos**: Para grupos de contenido, repite el proceso y usa opciones como Carga Masiva (Bulk Upload) cuando estén disponibles.
- **Idiomas**: La plataforma soporta múltiples idiomas (por ejemplo, Inglés, Español), como se ve en los interruptores en las capturas de pantalla.
