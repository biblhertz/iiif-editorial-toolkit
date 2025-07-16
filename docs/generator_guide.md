# Generator Guide

Complete guide to creating IIIF manifests with the Academic Toolkit generators.

## 🎯 Choosing the Right Generator

### Enhanced Academic Generator (`iiif_generator.html`)
**Use when you need:**
- Complex multi-image comparisons
- Advanced layout algorithms
- Multiple viewer compatibility
- Extensive customization options
- Academic publishing features

### OpenSeadragon Generator (`osd_generator.html`)
**Use when you need:**
- Simple, focused interface
- OpenSeadragon-specific optimizations
- Quick manifest creation
- Teaching or presentation materials

## 🔧 Getting Started

### 1. Individual Image Manifests

Both generators follow the same basic workflow for individual images:

#### Required Fields
- **IIIF Image URL**: Full URL to the image
- **IIIF Service ID**: Base service URL (without `/info.json`)
- **Title (Italian)**: Primary title
- **Manifest ID**: Unique identifier for the manifest

#### Optional Fields
- **Title (English)**: Secondary language title
- **Description**: Detailed description in both languages
- **Artist**: Creator information
- **Date**: Creation date
- **Institution**: Holding institution

#### Auto-Fetch Feature
1. Enter the IIIF Service ID
2. Click "🔍 Auto-fetch Info"
3. Dimensions are automatically retrieved
4. Image URL is populated if empty

**Example Service ID:**
```
https://fotothek.biblhertz.it/iiif/3/dpub%2Fhsah0410%2Fhsah_0410_09.jp2
```

### 2. Building Your Library

#### Save Individual Manifests
1. Generate individual manifest
2. Click "💾 Save to Library"
3. Manifests are stored locally
4. Export library for backup

#### Library Management
- **Export**: Download entire library as JSON
- **Import**: Load previously exported library
- **Delete**: Remove individual manifests
- **Clear**: Remove entire library

### 3. Creating Comparisons

#### Import from Library
1. Switch to "🔄 Comparison Layouts" tab
2. Select images from library using checkboxes
3. Click "📥 Import Selected"
4. Images appear in comparison list

#### Layout Types

##### Enhanced Academic Generator (6 layouts):

**1. Horizontal Row**
- Images placed side by side
- Maintains original aspect ratios
- Good for: Basic comparisons

**2. Horizontal Row (Balanced Heights)**
- All images scaled to same height
- Optimized for detail comparison
- Good for: Art analysis, manuscripts

**3. Storyboard Layout**
- Optimized for viewing experience
- Considers canvas aspect ratio
- Good for: Presentations, teaching

**4. Main + Derivatives (1+N)**
- One large main image
- Smaller derivative images below
- Good for: Primary source with details

**5. 2x2 Grid**
- Four images in grid format
- Equal sized cells
- Good for: Systematic comparisons

**6. Vertical Stack**
- Images stacked vertically
- Horizontally centered
- Good for: Chronological sequences

##### OpenSeadragon Generator (4 layouts):

**1. Horizontal**
- Basic side-by-side arrangement
- Original proportions maintained

**2. Horizontal Balanced**
- Equal heights for comparison
- Target height customizable

**3. Horizontal Upscale**
- Favors smaller images
- Ensures detail visibility

**4. Main + Derivatives**
- Primary image with thumbnails
- Hierarchical presentation

### 4. Viewer Compatibility (Enhanced Generator Only)

#### Universal (Single Canvas)
- Single canvas with positioned images
- Works with: Mirador 3, TheseusViewer
- Best for: Complex academic viewing

#### Simple Manifest (Multi-Canvas)
- Multiple canvases, one per image
- Works with: Basic IIIF viewers
- Best for: Simple navigation

#### Dual Output
- Generates both Universal and Simple
- Maximum compatibility
- Best for: Unknown target viewers

## 🎨 Advanced Features

### Fine-Tuning Positions (Enhanced Generator)

1. Generate comparison manifest
2. Click individual images in preview
3. Adjust coordinates manually
4. Update positions in real-time

### Validation and Testing

1. Switch to "✅ Validation & Testing" tab
2. Enter manifest URL or paste JSON
3. Click "🔍 Validate IIIF"
4. Review compliance report

### Auto-Fetch Best Practices

#### Supported Services
- IIIF Image API 2.1
- IIIF Image API 3.0
- Most major cultural institutions

#### Troubleshooting
- **CORS errors**: Some institutions block cross-origin requests
- **Authentication**: Some services require authentication
- **Invalid URLs**: Check URL encoding for special characters

## 📋 Manifest Structure

### Individual Manifest
```json
{
  "@context": ["http://iiif.io/api/presentation/3/context.json"],
  "id": "https://example.com/manifest.json",
  "type": "Manifest",
  "label": { "it": ["Title"], "en": ["Title"] },
  "summary": { "it": ["Description"], "en": ["Description"] },
  "behavior": ["individuals"],
  "metadata": [...],
  "items": [...]
}
```

### Comparison Manifest (Universal)
```json
{
  "@context": ["http://iiif.io/api/presentation/3/context.json"],
  "id": "https://example.com/comparison.json",
  "type": "Manifest",
  "label": { "it": ["Comparison"], "en": ["Comparison"] },
  "behavior": ["multi-part"],
  "viewingDirection": "left-to-right",
  "items": [{
    "type": "Canvas",
    "width": 1600,
    "height": 900,
    "items": [{
      "type": "AnnotationPage",
      "items": [
        {
          "type": "Annotation",
          "motivation": "painting",
          "target": "canvas#xywh=100,100,400,300",
          "body": { "type": "Image", ... }
        }
      ]
    }]
  }]
}
```

## 🔄 Workflow Examples

### Art History Comparison
1. Create individual manifests for each artwork
2. Save to library with detailed metadata
3. Import 2-4 artworks for comparison
4. Use "Horizontal Balanced" layout
5. Generate Universal manifest for Mirador
6. Test in multi-viewer tool

### Manuscript Analysis
1. Create manifests for each manuscript page
2. Include paleographic metadata
3. Import sequential pages
4. Use "Storyboard" layout
5. Generate dual output for flexibility
6. Validate IIIF compliance

### Digital Exhibition
1. Create individual manifests with rich metadata
2. Organize by theme or period
3. Create multiple comparison layouts
4. Use "Main + Derivatives" for featured works
5. Generate Simple manifests for broad compatibility
6. Test across multiple viewers

## 🚨 Common Issues

### Auto-Fetch Failures
- **Solution**: Manually enter dimensions
- **Prevention**: Check CORS policy of image server

### Large Canvas Sizes
- **Issue**: Performance problems in viewers
- **Solution**: Reduce padding or use balanced layouts

### Viewer Compatibility
- **Issue**: Manifest works in one viewer but not another
- **Solution**: Use dual output or test with validation tool

### Missing Metadata
- **Issue**: Manifests lack required fields
- **Solution**: Use validation tool to check compliance

## 💡 Best Practices

### Naming Conventions
- Use descriptive manifest IDs
- Include dates in filenames
- Follow institutional standards

### Image Selection
- Ensure consistent quality
- Consider aspect ratios
- Test zoom levels

### Layout Design
- Consider viewing context
- Test on different screen sizes
- Optimize for intended use

### Documentation
- Include rich metadata
- Provide multi-language support
- Document custom behaviors

## 🔍 Troubleshooting

### Service Detection
If auto-fetch fails:
1. Check if `/info.json` endpoint exists
2. Verify CORS headers allow requests
3. Test with manual dimension entry

### Layout Issues
If positioning seems wrong:
1. Check original image dimensions
2. Verify padding values
3. Test with different layout types

### Validation Errors
If manifest validation fails:
1. Check required fields
2. Verify URL formats
3. Test with simple manifest first

---

**Next:** [Viewer Guide](./viewer-guide.md) | [Layout Algorithms](./layout-algorithms.md)