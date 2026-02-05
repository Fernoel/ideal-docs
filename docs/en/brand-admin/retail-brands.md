# Retail Brands (Stores)

This module allows you to manage store locations (nodes). It is the central place for configuring store-specific settings, location data, and integration parameters.

## Store Configuration Fields

When creating or editing a store, the following fields are available. **Required** fields must be filled out for the store to be saved.

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `name` | String | **Yes** | The display name of the store. |
| `address.address1` | String | **Yes** | Primary street address. |
| `address.city` | String | **Yes** | City name. |
| `address.state` | String | **Yes** | State or Province code. |
| `address.zip` | String | **Yes** | Zip or Postal Code. |
| `phone` | String | **Yes** | Contact phone number. |
| `googleMapsHref` | String | **Yes** | Direct link to the Google Maps location. |
| `circularPath` | String | **Yes** | Unique URL slug for the circular (e.g., `weekly-ad`). Must be unique. |
| `active` | Boolean | **Yes** | Controls whether the store is visible and active in the system. |
| `showContactInformation`| Boolean | **Yes** | Toggles the display of address/phone on the public circular. |
| `googlePlaceId` | String | **Yes** | The Google Places API ID for the location (used for maps/SEO). |
| `latitude` | Float | **Yes** | GPS Latitude coordinate. |
| `longitude` | Float | **Yes** | GPS Longitude coordinate. |

### Optional Configuration
- **Hours**: Text field for store operating hours.
- **Notes**: Internal notes for administrators.
- **Theme**: Custom theme identifier to override the brand default.
- **Go Live Date**: Scheduled date for the store to go live.
- **Coupon Integration**: Settings for connecting to third-party coupon providers.
- **Sneak Peek**: Enable "sneak peek" functionality for upcoming ads.

### Technical Validation Rules
- **Circular Path**: Validated by `CircularPathRule`. Must be unique within the brand hierarchy.
- **National ID**: Validated by `NationalIdRule`.
- **Coordinates**: Latitude and Longitude are required for the store locator functionality.
