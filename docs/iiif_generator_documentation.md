# Enhanced Academic IIIF Manifest Generator - Documentation

## Overview

The Enhanced Academic IIIF Manifest Generator is a comprehensive tool designed for scholarly image comparison and analysis. It creates IIIF 3.0 compliant manifests with viewer-specific optimization for academic publications.

## Key Features

### 🎯 **Viewer Compatibility**
- **Universal Mode**: Generates cookbook-format manifests for Mirador 3 + TheseusViewer
- **OSD Optimized**: Creates multi-canvas manifests for OpenSeadragon compatibility
- **Dual Output**: Generates both versions simultaneously

### 📐 **Smart Layout Engine**
- **Automated positioning** based on layout presets
- **Intelligent scaling** ensures all elements fit in preview
- **Aspect ratio preservation** for all layout types
- **Visual preview** with interactive placeholders

### 🔧 **Advanced Features**
- **Auto-fetch IIIF dimensions** from image service endpoints
- **Library management** for reusable image manifests
- **Validation & testing** with compatibility checks
- **Fine-tuning controls** for precise coordinate adjustment

---

## Getting Started

### 1. Individual Image Manifests

Create standalone manifests for individual images:

#### **Required Fields**
- **IIIF Image URL**: Full URL to the image file
- **IIIF Service ID**: Base URL for the IIIF Image API service
- **Title (Italian)**: Primary title for the image
- **Manifest ID**: Unique identifier for the manifest

#### **Optional Fields**
- **Title (English)**: Secondary title
- **Descriptions**: Italian and English descriptions
- **Metadata**: Artist, date, institution information

#### **Workflow**
1. Enter IIIF Service ID
2. Click "🔍 Auto-fetch Info" to retrieve dimensions
3. Fill in title and metadata fields
4. Click "🚀 Generate Manifest"
5. Save to library for reuse in comparisons

### 2. Comparison Layouts

Create multi-image comparison manifests:

#### **Layout Types**

##### **Horizontal Row**
- Arranges images in a horizontal sequence
- Maintains aspect ratios
- Automatically scales to fit canvas width
- Centers vertically within available space

##### **Horizontal Row (Balanced Heights)**
- Scales all images to the same height (400px default)
- Maintains aspect ratios by adjusting widths
- Optimal for direct size comparisons

##### **Storyboard Layout**
- Optimized for sequential viewing
- Consistent height (350px) with variable widths
- Small vertical offset for visual flow

##### **Main + Derivatives (1+N)**
- Primary image positioned at top
- Smaller derivative images arranged below
- Ideal for showing source + variations

##### **2x2 Grid**
- Arranges up to 4 images in a grid pattern
- Equal cell sizes for each image
- Systematic comparison layout

##### **Vertical Stack**
- Images arranged vertically
- Maintains aspect ratios
- Automatically scales to fit canvas height
- Centers horizontally within available space

#### **Comparison Workflow**
1. **Select Target Viewer** (Universal, OSD, or Dual)
2. **Import Images** from library (selection order = display order)
3. **Choose Layout Type** → positions calculated automatically
4. **Preview Layout** with visual placeholders
5. **Optional Fine-tuning** → click placeholders to adjust coordinates
6. **Generate Manifest(s)** with precise coordinates

---

## Advanced Features

### 🔍 **Auto-Fetch Functionality**
The tool can automatically retrieve image dimensions from IIIF services:

```
Service URL: https://example.com/iiif/image123
Auto-fetched: width=2641, height=2001
Generated URL: https://example.com/iiif/image123/full/max/0/default.jpg
```

**Benefits:**
- Eliminates manual dimension entry
- Ensures accuracy
- Populates image URL automatically

### 📚 **Library Management**
Store and reuse individual image manifests:

- **Save to Library**: Store generated manifests for reuse
- **Import/Export**: Backup and share manifest collections
- **Organized Display**: View saved manifests with metadata
- **Selective Import**: Choose specific images for comparisons

### 🎨 **Visual Positioning**
Interactive preview system:

- **Real-time Preview**: See layout changes immediately
- **Placeholder Boxes**: Visual representation of image positions
- **Click-to-Select**: Choose images for fine-tuning
- **Coordinate Display**: View and edit precise XYWH values

### ✅ **Validation & Testing**
Built-in quality assurance:

- **IIIF Compliance**: Validates against IIIF 3.0 specification
- **Viewer Compatibility**: Tests manifest structure for different viewers
- **Direct Testing**: Open manifests in Mirador 3, TheseusViewer, etc.

---

## Viewer Compatibility

### 🎭 **Mirador 3 + TheseusViewer**
**Format**: Single canvas with positioned annotations
```json
{
  "target": "canvas#xywh=530,50,482,392",
  "body": { "id": "image.jpg", "type": "Image" }
}
```

**Advantages:**
- Excellent composition support
- Precise positioning
- Annotation capabilities
- IIIF 3.0 compliant

### 🌊 **OpenSeadragon**
**Format**: Multi-canvas sequential manifest
```json
{
  "items": [
    { "id": "canvas1", "items": [{"body": {"id": "image1.jpg"}}] },
    { "id": "canvas2", "items": [{"body": {"id": "image2.jpg"}}] }
  ]
}
```

**Advantages:**
- High-performance viewing
- Smooth zoom/pan
- Reliable single-image display
- Sequential navigation

### 📊 **Compatibility Matrix**

| Feature | Mirador 3 | TheseusViewer | OpenSeadragon |
|---------|-----------|---------------|---------------|
| Single Images | ✅ Excellent | ✅ Excellent | ✅ Excellent |
| Positioned Compositions | ✅ Excellent | ✅ Good | ⚠️ Limited |
| Multi-Canvas | ✅ Excellent | ✅ Good | ✅ Excellent |
| Annotations | ✅ Advanced | ✅ Basic | ❌ None |

---

## Technical Specifications

### 🔧 **Manifest Structure**
Generated manifests follow IIIF Presentation API 3.0:

```json
{
  "@context": ["http://iiif.io/api/presentation/3/context.json"],
  "id": "https://example.com/manifest.json",
  "type": "Manifest",
  "label": {"it": ["Title"], "en": ["Title"]},
  "behavior": ["multi-part"],
  "items": [...]
}
```

### 📐 **Coordinate System**
- **Canvas Size**: 1600×700 pixels (default)
- **Padding**: 100 pixels (adjustable)
- **Coordinates**: Absolute positioning (x,y,width,height)
- **Scaling**: Automatic for horizontal/vertical layouts

### 🎯 **Layout Calculations**

#### **Horizontal Row Scaling**
```javascript
// Calculate natural sizes
const naturalSizes = images.map(img => ({
  width: img.width * (targetHeight / img.height),
  height: targetHeight
}));

// Scale if total width exceeds canvas
const scale = totalWidth > canvasWidth ? 
  (canvasWidth - padding) / totalWidth : 1;
```

#### **Vertical Stack Scaling**
```javascript
// Calculate natural sizes
const naturalSizes = images.map(img => ({
  width: targetWidth,
  height: img.height * (targetWidth / img.width)
}));

// Scale if total height exceeds canvas
const scale = totalHeight > canvasHeight ? 
  (canvasHeight - padding) / totalHeight : 1;
```

---

## Best Practices

### 🎨 **For Scholarly Publications**
1. **Use descriptive titles** in both Italian and English
2. **Include institutional metadata** (artist, date, institution)
3. **Choose appropriate layouts** for your comparison goals
4. **Test in multiple viewers** before publication

### 📐 **For Precise Positioning**
1. **Start with layout presets** for base positioning
2. **Use Adobe Illustrator workflow** for complex layouts
3. **Fine-tune coordinates** using the built-in tools
4. **Generate dual outputs** for maximum compatibility

### 🔧 **For Technical Integration**
1. **Validate manifests** before deployment
2. **Test viewer compatibility** with your specific use case
3. **Use consistent naming conventions** for manifest IDs
4. **Backup manifest library** regularly

---

## Troubleshooting

### ❓ **Common Issues**

#### **Auto-fetch Fails**
- **Check IIIF service URL** format
- **Verify CORS headers** on image service
- **Try manual dimension entry** as fallback

#### **Preview Doesn't Show Images**
- **Import images from library** first
- **Select a layout type** to trigger positioning
- **Check that images have position data**

#### **Manifest Validation Errors**
- **Verify required fields** are filled
- **Check IIIF service URLs** are accessible
- **Ensure proper JSON structure**

#### **Viewer Compatibility Issues**
- **Use Universal mode** for Mirador 3/TheseusViewer
- **Use OSD mode** for OpenSeadragon
- **Generate dual outputs** for maximum compatibility

### 🔧 **Advanced Troubleshooting**

#### **Layout Scaling Problems**
- **Check image dimensions** are correct
- **Verify canvas size** settings
- **Adjust padding** if elements are too close

#### **Coordinate Precision**
- **Use Adobe Illustrator** for complex layouts
- **Fine-tune with coordinate inputs**
- **Test in target viewer** before finalizing

---

## API Reference

### 🔧 **Core Functions**

#### **generateIndividualManifest()**
Creates a single-image IIIF manifest
- **Input**: Form data (title, URL, dimensions, metadata)
- **Output**: IIIF 3.0 compliant manifest JSON

#### **generateComparisonManifest()**
Creates multi-image comparison manifest
- **Input**: Image array, layout type, viewer target
- **Output**: Positioned composition manifest

#### **applyLayoutPreset()**
Calculates positioning for layout types
- **Input**: Layout type, padding, image dimensions
- **Output**: Position coordinates for each image

#### **fetchImageInfo()**
Retrieves image info from IIIF service
- **Input**: IIIF service URL
- **Output**: Width, height, and full image URL

### 📊 **Data Structures**

#### **Image Object**
```javascript
{
  id: "unique-identifier",
  title: "Image Title",
  imageUrl: "https://example.com/image.jpg",
  serviceId: "https://example.com/iiif/service",
  width: 2641,
  height: 2001,
  position: {
    x: 530,
    y: 50, 
    displayWidth: 482,
    displayHeight: 392
  }
}
```

#### **Layout Position**
```javascript
{
  x: 530,        // X coordinate
  y: 50,         // Y coordinate  
  displayWidth: 482,   // Display width
  displayHeight: 392   // Display height
}
```

---

## Version History

### v2.0 (Current)
- ✅ **Simplified workflow** with dropdown-driven positioning
- ✅ **Visual preview** with interactive placeholders
- ✅ **Auto-scaling** for horizontal/vertical layouts
- ✅ **Dual output** support for viewer compatibility
- ✅ **Enhanced validation** and testing features

### v1.0 (Original)
- ✅ **Basic manifest generation**
- ✅ **Library management**
- ✅ **Auto-fetch functionality**
- ✅ **Multiple layout types**

---

## Support & Resources

### 📖 **IIIF Resources**
- [IIIF Presentation API 3.0](https://iiif.io/api/presentation/3.0/)
- [IIIF Cookbook](https://iiif.io/api/cookbook/)
- [IIIF Image API](https://iiif.io/api/image/3.0/)

### 🧪 **Testing Tools**
- [Mirador 3](https://projectmirador.org/embed/)
- [TheseusViewer](https://theseusviewer.org/)
- [OpenSeadragon](https://openseadragon.github.io/)

### 💡 **Best Practices**
- Always validate manifests before deployment
- Test in multiple viewers for compatibility
- Use consistent naming conventions
- Backup manifest libraries regularly

---

*Documentation last updated: December 2024*