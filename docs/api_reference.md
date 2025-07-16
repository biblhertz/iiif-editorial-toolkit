# API Reference

Technical specifications and API documentation for the IIIF Academic Toolkit.

## 🔧 Core Functions

### Manifest Generation

#### `generateIndividualManifest(options)`

Creates a IIIF 3.0 compliant manifest for a single image.

**Parameters:**
- `options` (Object): Configuration options
  - `imageUrl` (string): Full URL to the image
  - `imageService` (string): IIIF service base URL
  - `titleIt` (string): Italian title
  - `titleEn` (string): English title (optional)
  - `summaryIt` (string): Italian description (optional)
  - `summaryEn` (string): English description (optional)
  - `manifestId` (string): Unique manifest identifier
  - `baseUrl` (string): Base URL for manifest hosting
  - `width` (number): Image width in pixels
  - `height` (number): Image height in pixels
  - `artist` (string): Artist name (optional)
  - `date` (string): Creation date (optional)
  - `institution` (string): Holding institution (optional)

**Returns:**
- `Object`: IIIF 3.0 compliant manifest

**Example:**
```javascript
const manifest = generateIndividualManifest({
  imageUrl: "https://example.com/image.jpg",
  imageService: "https://example.com/iiif/image1",
  titleIt: "Garofalo, Trionfo di Bacco, 1540",
  titleEn: "Garofalo, Triumph of Bacchus, 1540",
  manifestId: "garofalo-trionfo-bacco",
  baseUrl: "https://manifests.example.com/",
  width: 1000,
  height: 693,
  artist: "Garofalo (Benvenuto Tisi)",
  date: "1540",
  institution: "Gemäldegalerie Alte Meister, Dresden"
});
```

#### `generateComparisonManifest(images, layoutType, options)`

Creates a comparison manifest with multiple positioned images.

**Parameters:**
- `images` (Array): Array of image objects
  - `id` (string): Unique identifier
  - `title` (string): Display title
  - `imageUrl` (string): Full image URL
  - `serviceId` (string): IIIF service URL
  - `width` (number): Image width
  - `height` (number): Image height
- `layoutType` (string): Layout algorithm to use
  - `"horizontal"` - Side-by-side arrangement
  - `"horizontal-balanced"` - Equal heights
  - `"horizontal-upscale"` - Favor smaller images
  - `"storyboard"` - Optimized for viewing
  - `"main-derivatives"` - Primary + secondary images
  - `"grid-2x2"` - 2x2 grid arrangement
  - `"vertical"` - Vertical stack
- `options` (Object): Configuration options
  - `padding` (number): Padding between images (default: 100)
  - `targetHeight` (number): Target height for balanced layouts (default: 600)
  - `canvasWidth` (number): Override canvas width
  - `canvasHeight` (number): Override canvas height
  - `titleIt` (string): Italian title
  - `titleEn` (string): English title
  - `summaryIt` (string): Italian description

**Returns:**
- `Object`: IIIF 3.0 compliant comparison manifest

**Example:**
```javascript
const comparisonManifest = generateComparisonManifest([
  {
    id: "image1",
    title: "Leonardo da Vinci",
    imageUrl: "https://example.com/leonardo.jpg",
    serviceId: "https://example.com/iiif/leonardo",
    width: 1200,
    height: 800
  },
  {
    id: "image2",
    title: "Michelangelo",
    imageUrl: "https://example.com/michelangelo.jpg",
    serviceId: "https://example.com/iiif/michelangelo",
    width: 1000,
    height: 1200
  }
], "horizontal-balanced", {
  padding: 100,
  targetHeight: 600,
  titleIt: "Confronto: Leonardo e Michelangelo",
  titleEn: "Comparison: Leonardo and Michelangelo"
});
```

### Layout Algorithms

#### `calculateLayoutPositions(layoutType, images, options)`

Calculates positioning for images based on layout algorithm.

**Parameters:**
- `layoutType` (string): Layout algorithm identifier
- `images` (Array): Array of image objects with dimensions
- `options` (Object): Layout-specific options

**Returns:**
- `Object`: Layout result
  - `canvasWidth` (number): Required canvas width
  - `canvasHeight` (number): Required canvas height
  - `positions` (Array): Array of position objects
    - `x` (number): X coordinate
    - `y` (number): Y coordinate
    - `width` (number): Display width
    - `height` (number): Display height

**Example:**
```javascript
const layout = calculateLayoutPositions("horizontal-balanced", [
  {width: 1200, height: 800},
  {width: 1000, height: 1200}
], {
  padding: 100,
  targetHeight: 600
});

// Result:
// {
//   canvasWidth: 1300,
//   canvasHeight: 800,
//   positions: [
//     {x: 100, y: 100, width: 900, height: 600},
//     {x: 1100, y: 100, width: 500, height: 600}
//   ]
// }
```

### Validation Functions

#### `validateIIIFManifest(manifest)`

Validates IIIF manifest compliance.

**Parameters:**
- `manifest` (Object): IIIF manifest to validate

**Returns:**
- `Array`: Array of validation results
  - `valid` (boolean): Whether check passed
  - `message` (string): Human-readable result

**Example:**
```javascript
const validation = validateIIIFManifest(manifest);
validation.forEach(result => {
  console.log(`${result.valid ? '✅' : '❌'} ${result.message}`);
});
```

#### `validateImageService(serviceId)`

Validates IIIF Image Service availability.

**Parameters:**
- `serviceId` (string): IIIF service base URL

**Returns:**
- `Promise<Object>`: Service validation result
  - `valid` (boolean): Whether service is accessible
  - `info` (Object): Service info.json content
  - `error` (string): Error message if validation failed

**Example:**
```javascript
const serviceValidation = await validateImageService("https://example.com/iiif/image1");
if (serviceValidation.valid) {
  console.log("Service dimensions:", serviceValidation.info.width, "x", serviceValidation.info.height);
}
```

### Auto-Fetch Functions

#### `fetchImageInfo(serviceId)`

Retrieves image information from IIIF service.

**Parameters:**
- `serviceId` (string): IIIF service base URL

**Returns:**
- `Promise<Object>`: Image information
  - `width` (number): Image width
  - `height` (number): Image height
  - `profile` (string): Service profile level
  - `protocol` (string): IIIF protocol version

**Example:**
```javascript
try {
  const info = await fetchImageInfo("https://example.com/iiif/image1");
  console.log(`Dimensions: ${info.width} x ${info.height}`);
} catch (error) {
  console.error("Failed to fetch image info:", error);
}
```

## 🎨 Viewer API

### OpenSeadragon Viewer

#### `initializeViewer(containerId, options)`

Initializes OpenSeadragon viewer instance.

**Parameters:**
- `containerId` (string): DOM element ID for viewer container
- `options` (Object): OpenSeadragon configuration options

**Returns:**
- `Object`: OpenSeadragon viewer instance

**Example:**
```javascript
const viewer = initializeViewer("openseadragon-container", {
  showNavigator: true,
  showNavigationControl: true,
  animationTime: 1.2,
  constrainDuringPan: true
});
```

#### `loadManifestInViewer(manifestUrl, viewer)`

Loads IIIF manifest into OpenSeadragon viewer.

**Parameters:**
- `manifestUrl` (string): URL to IIIF manifest
- `viewer` (Object): OpenSeadragon viewer instance

**Returns:**
- `Promise<boolean>`: Success status

**Example:**
```javascript
const success = await loadManifestInViewer("https://example.com/manifest.json", viewer);
if (success) {
  console.log("Manifest loaded successfully");
}
```

#### `handleManifestType(manifest, viewer)`

Intelligently handles different manifest types.

**Parameters:**
- `manifest` (Object): IIIF manifest object
- `viewer` (Object): OpenSeadragon viewer instance

**Returns:**
- `void`

**Supported Manifest Types:**
- Single canvas with single image
- Single canvas with multiple positioned images (composition)
- Multiple canvases (sequence)

### Multi-Viewer Integration

#### `switchViewer(viewerType, manifestUrl)`

Switches between different IIIF viewers.

**Parameters:**
- `viewerType` (string): Target viewer
  - `"mirador"` - Mirador 3
  - `"theseus"` - TheseusViewer
  - `"openseadragon"` - OpenSeadragon
- `manifestUrl` (string): IIIF manifest URL

**Returns:**
- `void`

**Example:**
```javascript
switchViewer("mirador", "https://example.com/manifest.json");
```

## 💾 Storage API

### Library Management

#### `saveToLibrary(manifest, metadata)`

Saves manifest to local library.

**Parameters:**
- `manifest` (Object): IIIF manifest
- `metadata` (Object): Additional metadata
  - `id` (string): Unique identifier
  - `title` (string): Display title
  - `artist` (string): Artist name
  - `date` (string): Creation date
  - `imageUrl` (string): Image URL
  - `serviceId` (string): IIIF service URL
  - `width` (number): Image width
  - `height` (number): Image height

**Returns:**
- `boolean`: Success status

**Example:**
```javascript
const success = saveToLibrary(manifest, {
  id: "artwork-1",
  title: "The Last Supper",
  artist: "Leonardo da Vinci",
  date: "1495-1498",
  imageUrl: "https://example.com/image.jpg",
  serviceId: "https://example.com/iiif/service",
  width: 1200,
  height: 800
});
```

#### `loadLibrary()`

Loads manifest library from local storage.

**Returns:**
- `Array`: Array of library items

#### `exportLibrary()`

Exports library as downloadable JSON file.

**Returns:**
- `void`

#### `importLibrary(file)`

Imports library from JSON file.

**Parameters:**
- `file` (File): JSON file containing library data

**Returns:**
- `Promise<boolean>`: Success status

## 🔍 Utility Functions

### URL Manipulation

#### `createBlobUrl(jsonObject)`

Creates blob URL for JSON object.

**Parameters:**
- `jsonObject` (Object): JSON data

**Returns:**
- `string`: Blob URL

#### `downloadJSON(data, filename)`

Downloads JSON data as file.

**Parameters:**
- `data` (Object): JSON data
- `filename` (string): Download filename

**Returns:**
- `void`

### Coordinate Conversion

#### `convertCoordinates(x, y, width, height, canvasWidth, canvasHeight)`

Converts coordinates between different coordinate systems.

**Parameters:**
- `x` (number): X coordinate
- `y` (number): Y coordinate
- `width` (number): Region width
- `height` (number): Region height
- `canvasWidth` (number): Canvas width
- `canvasHeight` (number): Canvas height

**Returns:**
- `Object`: Converted coordinates
  - `x` (number): Converted X
  - `y` (number): Converted Y
  - `width` (number): Converted width
  - `height` (number): Converted height

### Error Handling

#### `showMessage(message, type)`

Displays user notification.

**Parameters:**
- `message` (string): Message text
- `type` (string): Message type ("success", "error", "info")

**Returns:**
- `void`

#### `handleError(error, context)`

Centralized error handling.

**Parameters:**
- `error` (Error): Error object
- `context` (string): Error context

**Returns:**
- `void`

## 📊 Data Structures

### Image Object
```typescript
interface ImageObject {
  id: string;
  title: string;
  imageUrl: string;
  serviceId: string;
  width: number;
  height: number;
  artist?: string;
  date?: string;
  institution?: string;
}
```

### Layout Configuration
```typescript
interface LayoutConfig {
  padding: number;
  targetHeight?: number;
  canvasWidth?: number;
  canvasHeight?: number;
  algorithm: 'horizontal' | 'horizontal-balanced' | 'horizontal-upscale' | 
            'storyboard' | 'main-derivatives' | 'grid-2x2' | 'vertical';
}
```

### Position Object
```typescript
interface Position {
  x: number;
  y: number;
  width: number;
  height: number;
}
```

### Validation Result
```typescript
interface ValidationResult {
  valid: boolean;
  message: string;
  category?: 'structure' | 'content' | 'compliance';
}
```

## 🚀 Integration Examples

### React Component
```jsx
import React, { useState, useEffect } from 'react';

const IIIFViewer = ({ manifestUrl }) => {
  const [viewer, setViewer] = useState(null);
  
  useEffect(() => {
    const initViewer = async () => {
      const viewerInstance = initializeViewer('iiif-container', {
        showNavigator: true,
        showNavigationControl: true
      });
      
      if (manifestUrl) {
        await loadManifestInViewer(manifestUrl, viewerInstance);
      }
      
      setViewer(viewerInstance);
    };
    
    initViewer();
  }, [manifestUrl]);
  
  return <div id="iiif-container" style={{ width: '100%', height: '600px' }} />;
};
```

### Vue.js Component
```vue
<template>
  <div>
    <div id="iiif-viewer" ref="viewerContainer"></div>
    <button @click="switchLayout">Switch Layout</button>
  </div>
</template>

<script>
export default {
  name: 'IIIFViewer',
  props: {
    manifestUrl: String
  },
  data() {
    return {
      viewer: null,
      currentLayout: 'horizontal'
    };
  },
  mounted() {
    this.initializeViewer();
  },
  methods: {
    async initializeViewer() {
      this.viewer = initializeViewer(this.$refs.viewerContainer, {
        showNavigator: true
      });
      
      if (this.manifestUrl) {
        await loadManifestInViewer(this.manifestUrl, this.viewer);
      }
    },
    switchLayout() {
      const layouts = ['horizontal', 'horizontal-balanced', 'storyboard'];
      const currentIndex = layouts.indexOf(this.currentLayout);
      const nextIndex = (currentIndex + 1) % layouts.length;
      this.currentLayout = layouts[nextIndex];
      
      // Regenerate manifest with new layout
      // Implementation depends on your data structure
    }
  }
};
</script>
```

### Express.js Backend
```javascript
const express = require('express');
const app = express();

app.get('/api/manifest/:id', async (req, res) => {
  try {
    const manifestData = await getManifestData(req.params.id);
    const manifest = generateIndividualManifest(manifestData);
    
    res.json(manifest);
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
});

app.post('/api/comparison', async (req, res) => {
  try {
    const { images, layoutType, options } = req.body;
    const manifest = generateComparisonManifest(images, layoutType, options);
    
    res.json(manifest);
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
});

app.listen(3000, () => {
  console.log('IIIF API server running on port 3000');
});
```

## 🔧 Configuration

### Environment Variables
```bash
# Base URL for manifest hosting
MANIFEST_BASE_URL=https://manifests.example.com/

# Default image service settings
DEFAULT_IMAGE_SERVICE_LEVEL=level2
DEFAULT_IMAGE_FORMAT=image/jpeg

# Viewer configuration
ENABLE_DEEP_ZOOM=true
MAX_ZOOM_LEVEL=10
TILE_SIZE=256
```

### Configuration Object
```javascript
const config = {
  manifests: {
    baseUrl: 'https://manifests.example.com/',
    defaultLanguage: 'en',
    supportedLanguages: ['en', 'it', 'fr', 'de']
  },
  viewer: {
    defaultZoomLevel: 1,
    enableNavigation: true,
    showThumbnails: true,
    animationTime: 1.2
  },
  layout: {
    defaultPadding: 100,
    maxCanvasWidth: 8192,
    maxCanvasHeight: 8192,
    preferredAspectRatio: '16:9'
  }
};
```

---

This API reference provides comprehensive documentation for developers integrating or extending the IIIF Academic Toolkit. For usage examples and tutorials, see the [Examples](./examples.md) documentation.

**Previous:** [Examples](./examples.md) | **Up:** [Main Documentation](./README.md)