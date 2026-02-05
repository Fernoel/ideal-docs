# Recipes

The Recipes module allows you to create and manage culinary content that can be associated with products in the circular.

## Recipe Data Structure

Each recipe consists of the following data points:

| Field | Type | Description |
|-------|------|-------------|
| `name` | String | The title of the recipe. |
| `serves` | Integer | Number of people the recipe serves. |
| `cookTime` | String | Time required to cook (e.g., "30 mins"). |
| `prepTime` | String | Time required to prepare ingredients. |
| `ingredients` | List | A structured list of ingredients (`RecipeIngredient`). |
| `instructions` | JSON | Step-by-step preparation instructions. |
| `notes` | JSON | Additional chef notes or tips. |
| `validFrom` | Date | The date from which the recipe is visible. |
| `validTo` | Date | The expiration date (optional). |

## Media
Recipes can have an associated visual asset:
- **Image**: High-quality photo of the finished dish (`RecipeImageMedia`).
- **Video**: Instructional video (`VideoMedia`).

## Integration
Recipes can be linked to **Deals** via the `RecipeDeal` type. This allows customers to see ingredients on sale directly from the recipe page.
