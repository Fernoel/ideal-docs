# Circular Builder Module

## General Description
The Circular Builder module is the core for creating content for digital circulars. Here you can generate promotions, offers, and visual elements that are integrated into circulars. The main interface includes:

- A left sidebar menu with options such as Dashboard, Digital Circular, Circular Builder, Categories, etc.
- A store or brand selector (e.g., "Biswa First Store").
- A calendar to select publication dates.
- A table (data-grid) listing existing content items, with columns such as DAYS (validity days), DEAL TYPE (offer type), OWNER (owner), SIZE (size), and view/edit options.
- A right-side preview panel displaying promotion cards with images, prices, and discounts.

![Main Circular Builder interface](../../assets/screenshots/content%20(1).png)
> *Main Circular Builder interface with content table and preview.*

## Prerequisites for Creating Content
Before creating new content, ensure the following prerequisites are met:

1. **Node Creation**: You must have already created at least one node, which can be a Brand, Sub-Brand, or Store. This defines the context in which the content will be applied.
2. **Category Creation**: It is mandatory to have at least one category created in the Categories module. Without an assigned category, you will not be able to complete content creation, as it is a required field.

!!! warning "Requirement"
    If these prerequisites are not met, the system will not allow you to save the new content. Go to the corresponding modules (e.g., Retail Brands or Categories) to set them up first.

## Basic Workflow to Create Content
Follow these steps to create a new content item in Circular Builder:

### 1. Access the Module
- Log in to the platform as an administrator.
- In the left sidebar menu, select **Digital Circular > Circular Builder**.
- Choose the desired store or brand in the top selector (e.g., "Biswa First Store").

### 2. Start Creation
- In the main interface, click the **New Card** button (or "New Content", depending on the version).
- This will open a new tab or creation form titled "Create Single Promotion" or similar.

### 3. Complete the Creation Form
The form is divided into sections such as Content, Deal/Offer, Date Range, Media, Header, Background, etc.
Fill in all required fields (marked with *). Key fields include:

- **Content**: Title, Description, Date Text (Display), Category (select an existing one), Width, Height, and Size (e.g., Small).
- **Deal/Offer**: Card Style (e.g., Coupon), Deal Type (e.g., Static (No Price), Fixed Price, Buy X Get Y For Z), Quantity Required, Limit, UPC (product code).
- **Coupon**: If applicable, manually include a coupon with Coupon ID, Required, Limit, and Amount Off.
- **Date Range**: Starts on and Expires dates.
- **Media**: Upload or select media (images, icons), header (Headline), background (Background Color or Image), position (Position - e.g., Center).
- **Preview**: Use the right-side preview panel to see how the promotion will look in real time.

> Ensure all mandatory fields are completed; otherwise, you will not be able to save.

![Create Single Promotion form](../../assets/screenshots/content.png)
> *"Create Single Promotion" creation form with sections and preview.*

### 4. Save the Content
- Once all fields are completed, click **Save** or **Create** (the button may vary depending on the interface).
- The new content will automatically appear in the main table (data-grid) of the Circular Builder module.
- You can edit, delete, or preview the content from the table using the corresponding icons (e.g., eye icon to view, scissors to edit).

## How to Create Content Using Content Bulk Upload

The Content Bulk Upload feature allows you to create multiple content items at once by uploading a properly formatted bulk file (typically a spreadsheet or structured file containing promotion data) along with associated media files. This is especially useful when you need to create dozens or hundreds of promotions in a single operation.

!!! important "Important Prerequisite"
    Before using Bulk Upload, you must prepare and have ready a valid Content Bulk Upload file. This file must follow the exact format and structure expected by the platform (columns, required fields, naming conventions, etc.). Contact your administrator or refer to the Bulk Upload Template Documentation (if available) to obtain the correct template and instructions.

### Step-by-Step Workflow for Bulk Upload

#### Access Bulk Upload
1. Go to the Circular Builder module.
2. Select the desired store/brand using the top selector (e.g., "Biswa First Store").
3. In the main interface, click the **Bulk Upload** button (usually located near the "New Card" button).
4. This action opens the multi-step Manage Content wizard titled something like "Manage Content for [Store Name]".

#### Step 1 – Upload Your Media
- You will see a drag-and-drop area labeled "Drop your media files here" and a **+ Choose** button.
- **Important**: The system only accepts image and video file formats. Other file types will be rejected.
- Drag and drop your media files or click **+ Choose** to select them from your computer.
- Wait until all files finish uploading completely.
    - A progress indicator or status column will show when each file has been successfully processed.
    - Only when all uploads are complete will the **Next** button become active.
- Click **Next** to proceed.

#### Step 2 – Select Your Date Range
- In this step, you can define a common date range that will apply to all (or most) of the content items being uploaded.
- Use the calendar controls to set **Starts on** and **Expires** dates.
- If you do not need a specific date range for this bulk operation (or if dates are already defined in the bulk file), simply click **Next** to skip this step.

#### Step 3 – Content Upload & Category Management
The system processes the uploaded bulk file and attempts to match or create categories.

**Behavior depending on categories:**
- **If the categories already exist in the current node (brand/store)**: A success message will appear indicating that the categories were found or successfully matched.
- **If the categories are new for this node**: You will see two main options for each new category:
    - **Create**: Click the Create button to automatically generate the new category in the system.
    - **Map**: Select an existing category from the dropdown list and map the new category name to an already existing one.
- **Ignore option**: Check the Ignore checkbox for individual categories or use a "Select All / Ignore All" option if available. Ignored categories will not be created or mapped.

After handling all categories (creating, mapping, or ignoring), click **Next**.

!!! warning "Important Note about Ignoring Categories"
    - If you ignore one or more categories, the system will allow you to proceed.
    - However, in the preview step (Step 5), any content item without an assigned category will be marked with an error.
    - **To fix these errors**:
        1. Click the edit icon on the affected content item, or
        2. Click the error message/notification to open the category assignment tool.
        3. Assign a valid category and save.

#### Step 4 – Review / Preview
This step shows a complete preview of all content items that will be created from the bulk file.
Review the table carefully:
- Check titles, deal types, sizes, media assignments, dates, categories, etc.
- Look for any error indicators (especially missing categories).

> Fix any issues directly in this view if the interface allows inline editing, or go back to previous steps.

#### Step 5 – Finalize and Save
You will see a final table listing all the content items that will be created.
In this table you can:
- **Delete** individual items (if you do not want to create them)
- **Edit** individual items (modify title, deal type, category, media, etc.)

When everything looks correct and there are no remaining errors, click the **Done** button.
The system will start processing and saving all the content items.
Once completed, you will be redirected back to the main Circular Builder table, where the newly created content items will appear.

### Tips for Successful Bulk Uploads
- **Always use the official template** provided by the platform to avoid format errors.
- **Upload all related media files** before or together with the bulk file processing.
- **Be patient during media upload** — do not close the window or navigate away until all files show 100% complete.
- **Resolve category issues** before the final save to avoid having to edit many items individually later.
- **After a successful bulk upload**, use the Export button in the main table to download and verify the newly created content.

## Understanding the Content Bulk Upload Template

The Content Bulk Upload feature relies on a structured file (usually a `.xlsx`, `.xls` or `.csv`) that contains all the information needed to create multiple promotion cards at once. This template defines exactly which columns are expected, which are required, and what kind of data should go in each one.

### Where to Get the Template

- **The most reliable way** is to ask your platform administrator or the support team for the official Bulk Upload Template.
- In some versions of the platform, there may be a **Download Template** button or link inside the Bulk Upload wizard (usually visible after clicking "Bulk Upload").
- If no template is available, contact support through the Support Portal module to request the current version.

!!! important
    Using a file that does not match the expected structure will cause errors during upload. Always use the official or most recent template.

### Main Columns in the Bulk Upload Template

Below is the typical structure of the template (the exact column names and order may vary slightly depending on the platform version — always verify with your current template).

| Column Name | Required? | Description / Expected Format | Example Values | Notes |
| :--- | :---: | :--- | :--- | :--- |
| **Title** | Yes | The main title of the promotion card (in English or the selected language) | `"2x1 en Pastas"` | Keep it short and attractive |
| **Description** | No | Longer description or details of the offer | `"Lleva 2 paquetes y paga solo 1"` | Can include line breaks if the system supports it |
| **Deal Type** | Yes | The type of offer / promotion | `Fixed Price`, `Buy X Get Y For Z`, `Amount Off`, `Static (No Price)`, `Coupon`, `# for Price` | Must match one of the allowed values exactly |
| **Card Style** | Yes | Visual style of the card | `Coupon`, `Banner`, `Standard`, `Menu Item` | Affects layout and available fields |
| **Size** | Yes | Grid size of the card in the circular | `1x1`, `1x2`, `2x1`, `2x2`, `3x1`, etc. | Common values: 1×1, 1×2, 2×2 |
| **Width** | Yes | Width value (numeric) | `1`, `2`, `3` | Usually matches the first number in Size |
| **Height** | Yes | Height value (numeric) | `1`, `2` | Usually matches the second number in Size |
| **Category** | Yes | Name of the category where this promotion belongs | `"Bebidas"`, `"Lácteos"`, `"Frutas y Verduras"` | Must exist or will be created/mapped in step 3 |
| **Starts On** | No | Start date of the promotion | `2026-02-08 00:00` | Format: YYYY-MM-DD HH:MM or just YYYY-MM-DD |
| **Expires** | No | End date of the promotion | `2026-02-14 23:59` | If empty, may use a default or global date range |
| **Coupon ID** | Conditional | Unique identifier for the coupon (only if Deal Type = Coupon) | `CUPON2026-XYZ123` | Required only for coupon-style promotions |
| **Amount Off** | Conditional | Discount amount (currency or percentage) | `5.99`, `30%`, `$4.00 OFF` | Depends on Deal Type |
| **Quantity Required** | Conditional | Number of items needed to activate the offer | `2` | Used in "Buy X Get Y" type offers |
| **Limit** | No | Maximum uses per customer or total limit | `1`, `4`, `Unlimited` | "Unlimited" or leave blank if no limit |
| **UPC / SKU** | No | Product code(s) – can be one or multiple (comma-separated) | `7501234567890`, `7509876543210` | Used for product-specific promotions |
| **Media Filename 1** | Conditional | Name of the main image file (must be uploaded in Step 1) | `promo_bebidas_2x1.jpg` | Exact filename including extension |
| **Media Filename 2** | No | Secondary image or icon | `icon_descuento.png` | Optional – depends on card style |
| **Headline** | No | Short highlighted text (often appears in bold) | `"¡Oferta Exclusiva!"` | Optional but recommended |
| **Background Color** | No | Hex color code for background | `#FF0000`, `#FFFFFF` | Only if no background image is used |
| **Language** | No | Language code of this row | `EN`, `ES` | Usually EN or ES – defaults to platform language if empty |

### Key Rules and Best Practices

- **Required fields** must be filled in every row. Missing required values will cause the entire row (or the whole upload) to fail.
- **Exact match for controlled fields**: Deal Type, Card Style, Size, etc. must match the values the system recognizes (case-sensitive in most cases).
- **Dates**: Use consistent format (preferably YYYY-MM-DD). If you leave them blank, the dates defined in Step 2 (or a default range) may be applied.
- **Media files**: The filenames in the spreadsheet must exactly match the names of the files you upload in Step 1 (including extension: `.jpg`, `.png`, `.mp4`, etc.).
- **One row = one promotion card**. Each row in the spreadsheet creates one individual content/promotion card.
- **Categories**: If the category name does not exist in the current brand/store, you will be prompted to create or map it in Step 3.
- **Validation**: The system performs validation during processing. Common errors include:
    - Missing required columns
    - Invalid Deal Type or Size values
    - Media filename not found among uploaded files
    - Category not resolved (not created/mapped/ignored)

### Recommended Workflow to Prepare a Bulk File

1. **Download the official template**.
2. **Fill in your promotions row by row** (one promotion = one row).
3. **Prepare all the images/videos** referenced in the "Media Filename" columns.
4. **Save the file** (preferably `.xlsx`).
5. **Go to Circular Builder** → click **Bulk Upload**.
6. **Upload your media files first** (Step 1).
7. **Proceed through the wizard**, mapping categories as needed.
8. **Review everything carefully** in the preview step.
9. **Click Done** when ready.

> **Tip**: If you have any doubts about specific column values or allowed options (for example, the complete list of Deal Types or Card Styles), ask your administrator or check inside the platform by creating a single promotion first to see the dropdown options.

## Tips and Best Practices

- **Field Validation**: If a required field is missing (such as Category), the system will display an error. Double-check the prerequisites.
- **Preview**: Always verify the preview to ensure the design looks good in different sizes (e.g., 1×1, 2×2).
- **Group Management**: For groups of content, repeat the process and use options like Bulk Upload when available.
- **Languages**: The platform supports multiple languages (e.g., English, Español), as seen in the toggles in the screenshots.
