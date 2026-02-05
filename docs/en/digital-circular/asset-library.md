# Asset Library

The Asset Library is the central repository for all media files (images, videos) used across Digital Circulars and Retail Media campaigns.

## Image Upload Process
The system utilizes a secure **Presigned URL** workflow to handle high-performance uploads directly to cloud storage.

1.  **Request Upload**: The frontend requests a secure upload URL from the backend.
2.  **Direct Upload**: The file is uploaded directly to the S3 bucket using the provided URL.
3.  **Processing**: The system processes the image (extracting metadata like width, height, mime type) and registers it in the database.
4.  **Caching**: The system automatically triggers a `ClearImagekitCacheJob` to ensure the new asset is immediately available via the ImageKit CDN.

## Folder Structure
Assets are organized logically to ensure separation between brands and stores:

`uploads/{brand_namespace}/{node_namespace}/{date_namespace}/`

- **brand_namespace**: Unique identifier for the retail chain.
- **node_namespace**: Unique identifier for the specific store/location.
- **date_namespace**: Timestamp-based folder to prevent collisions.

## Supported Formats
- **Images**: JPG, PNG, WEBP.
- **Videos**: MP4 (used in Video Deals and Retail Media).

## Technical Details (`MediaService`)
- **Presigned Uploads**: Handled by `createPresignedUploads` in `MediaService.php`.
- **System Images**: Icons and logos are stored in specific `sys/` paths.
- **Resolution**: The system automatically detects image dimensions (`width`, `height`) upon upload.
