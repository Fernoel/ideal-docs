# Recetas

El módulo de Recetas permite crear y gestionar contenido culinario que puede asociarse con productos en el circular.

## Estructura de Datos de la Receta

Cada receta consta de los siguientes puntos de datos:

| Campo | Tipo | Descripción |
|-------|------|-------------|
| `name` | Texto | El título de la receta. |
| `serves` | Entero | Número de personas para las que rinde la receta. |
| `cookTime` | Texto | Tiempo requerido para cocinar (ej. "30 mins"). |
| `prepTime` | Texto | Tiempo requerido para preparar ingredientes. |
| `ingredients` | Lista | Una lista estructurada de ingredientes (`RecipeIngredient`). |
| `instructions` | JSON | Instrucciones paso a paso de preparación. |
| `notes` | JSON | Notas adicionales o consejos del chef. |
| `validFrom` | Fecha | La fecha desde la cual la receta es visible. |
| `validTo` | Fecha | La fecha de expiración (opcional). |

## Multimedia
Las recetas pueden tener un activo visual asociado:
- **Imagen**: Foto de alta calidad del plato terminado (`RecipeImageMedia`).
- **Video**: Video instructivo (`VideoMedia`).

## Integración
Las recetas pueden vincularse a **Ofertas** a través del tipo `RecipeDeal`. Esto permite a los clientes ver los ingredientes en oferta directamente desde la página de la receta.
