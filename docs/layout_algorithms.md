# Layout Algorithms

Detailed explanation of positioning systems and layout calculations used in the IIIF Editorial Toolkit.

## 🎯 Overview

The toolkit uses intelligent algorithms to position images within IIIF manifests, optimizing for different viewing contexts and academic use cases. Each algorithm considers factors like aspect ratios, image sizes, padding, and viewer compatibility.

## 📐 Coordinate System

### Canvas Coordinates
- **Origin**: Top-left corner (0, 0)
- **X-axis**: Increases rightward
- **Y-axis**: Increases downward
- **Units**: Pixels
- **Format**: `xywh=x,y,width,height`

### Target Syntax
```json
{
  "target": "canvas#xywh=100,150,400,300",
  "type": "SpecificResource",
  "source": "canvas"
}
```

## 🔄 Layout Algorithms

### 1. Horizontal Row Layout

**Purpose**: Basic side-by-side comparison

**Algorithm**:
```javascript
function horizontalLayout(images, padding) {
  const positions = [];
  let x = padding;
  const maxHeight = Math.max(...images.map(img => img.height));
  
  images.forEach(img => {
    positions.push({
      x: x,
      y: padding + (maxHeight - img.height) / 2, // Center vertically
      width: img.width,
      height: img.height
    });
    x += img.width + padding;
  });
  
  return {
    canvasWidth: x,
    canvasHeight: maxHeight + (padding * 2),
    positions
  };
}
```

**Characteristics**:
- Maintains original aspect ratios
- Vertically centers images
- Calculates total canvas width
- Good for: Basic comparisons

**Use Cases**:
- Comparing paintings of different sizes
- Manuscript page sequences
- Before/after comparisons

### 2. Horizontal Balanced Layout

**Purpose**: Equal-height comparison for detailed analysis

**Algorithm**:
```javascript
function horizontalBalancedLayout(images, padding, targetHeight) {
  const positions = [];
  let x = padding;
  
  images.forEach(img => {
    const scale = targetHeight / img.height;
    const scaledWidth = Math.round(img.width * scale);
    
    positions.push({
      x: x,
      y: padding,
      width: scaledWidth,
      height: targetHeight
    });
    x += scaledWidth + padding;
  });
  
  return {
    canvasWidth: x,
    canvasHeight: targetHeight + (padding * 2),
    positions
  };
}
```

**Characteristics**:
- All images scaled to same height
- Maintains aspect ratios
- Optimizes for detail comparison
- Good for: Art analysis, manuscripts

**Use Cases**:
- Comparing artwork details
- Paleographic analysis
- Iconographic studies

### 3. Storyboard Layout

**Purpose**: Optimized viewing experience with aspect ratio consideration

**Algorithm**:
```javascript
function storyboardLayout(images, padding, targetHeight) {
  const positions = [];
  let x = padding;
  
  // Scale images to target height
  const scaledImages = images.map(img => ({
    ...img,
    scaledWidth: Math.round(img.width * (targetHeight / img.height)),
    scaledHeight: targetHeight
  }));
  
  // Calculate total width
  const totalWidth = scaledImages.reduce((sum, img) => sum + img.scaledWidth, 0);
  let canvasWidth = totalWidth + (padding * (images.length + 1));
  
  // Prevent overly wide canvases (max 3:1 ratio)
  const maxWidth = targetHeight * 3;
  if (canvasWidth > maxWidth) {
    const scaleDown = maxWidth / canvasWidth;
    canvasWidth = maxWidth;
    scaledImages.forEach(img => {
      img.scaledWidth = Math.round(img.scaledWidth * scaleDown);
    });
  }
  
  // Position images
  scaledImages.forEach(img => {
    positions.push({
      x: x,
      y: padding,
      width: img.scaledWidth,
      height: img.scaledHeight
    });
    x += img.scaledWidth + padding;
  });
  
  return {
    canvasWidth,
    canvasHeight: targetHeight + (padding * 2),
    positions
  };
}
```

**Characteristics**:
- Prevents overly wide canvases
- Maintains readability
- Optimizes for viewing experience
- Good for: Presentations, teaching

### 4. Main + Derivatives Layout

**Purpose**: Hierarchical display with primary image and supporting details

**Algorithm**:
```javascript
function mainDerivativesLayout(images, padding) {
  const positions = [];
  const mainImg = images[0];
  const derivatives = images.slice(1);
  
  // Position main image
  positions.push({
    x: padding,
    y: padding,
    width: mainImg.width,
    height: mainImg.height
  });
  
  // Calculate derivative dimensions
  const derivativeWidth = derivatives.length > 0 ? 
    Math.floor((mainImg.width - (padding * (derivatives.length - 1))) / derivatives.length) : 0;
  const derivativeHeight = Math.round(derivativeWidth * 0.75); // 4:3 aspect ratio
  
  // Position derivatives
  let derivX = padding;
  const derivY = mainImg.height + (padding * 2);
  
  derivatives.forEach(img => {
    positions.push({
      x: derivX,
      y: derivY,
      width: derivativeWidth,
      height: derivativeHeight
    });
    derivX += derivativeWidth + padding;
  });
  
  return {
    canvasWidth: mainImg.width + (padding * 2),
    canvasHeight: mainImg.height + derivativeHeight + (padding * 3),
    positions
  };
}
```

**Characteristics**:
- Hierarchical arrangement
- Primary image emphasized
- Supporting details below
- Good for: Featured works with details

### 5. Grid Layout (2x2)

**Purpose**: Systematic comparison in grid format

**Algorithm**:
```javascript
function gridLayout(images, padding, cellWidth, cellHeight) {
  const positions = [];
  const gridSize = Math.ceil(Math.sqrt(images.length));
  
  images.forEach((img, index) => {
    const row = Math.floor(index / gridSize);
    const col = index % gridSize;
    
    positions.push({
      x: padding + (col * (cellWidth + padding)),
      y: padding + (row * (cellHeight + padding)),
      width: cellWidth,
      height: cellHeight
    });
  });
  
  const canvasWidth = (cellWidth * gridSize) + (padding * (gridSize + 1));
  const canvasHeight = (cellHeight * gridSize) + (padding * (gridSize + 1));
  
  return {
    canvasWidth,
    canvasHeight,
    positions
  };
}
```

**Characteristics**:
- Equal-sized cells
- Systematic arrangement
- Scalable to any number of images
- Good for: Systematic comparisons

### 6. Vertical Stack Layout

**Purpose**: Chronological or sequential vertical arrangement

**Algorithm**:
```javascript
function verticalStackLayout(images, padding) {
  const positions = [];
  let y = padding;
  const maxWidth = Math.max(...images.map(img => img.width));
  
  images.forEach(img => {
    positions.push({
      x: padding + Math.round((maxWidth - img.width) / 2), // Center horizontally
      y: y,
      width: img.width,
      height: img.height
    });
    y += img.height + padding;
  });
  
  return {
    canvasWidth: maxWidth + (padding * 2),
    canvasHeight: y,
    positions
  };
}
```

**Characteristics**:
- Vertical arrangement
- Horizontally centered
- Maintains aspect ratios
- Good for: Chronological sequences

## 🎨 Scaling Algorithms

### Proportional Scaling
```javascript
function proportionalScale(originalWidth, originalHeight, targetWidth, targetHeight) {
  const scaleX = targetWidth / originalWidth;
  const scaleY = targetHeight / originalHeight;
  const scale = Math.min(scaleX, scaleY); // Maintain aspect ratio
  
  return {
    width: Math.round(originalWidth * scale),
    height: Math.round(originalHeight * scale),
    scale: scale
  };
}
```

### Adaptive Scaling
```javascript
function adaptiveScale(images, canvasWidth, canvasHeight, padding) {
  const totalNaturalWidth = images.reduce((sum, img) => sum + img.width, 0);
  const totalPadding = padding * (images.length + 1);
  const availableWidth = canvasWidth - totalPadding;
  
  if (totalNaturalWidth > availableWidth) {
    const scale = availableWidth / totalNaturalWidth;
    return images.map(img => ({
      ...img,
      scaledWidth: Math.round(img.width * scale),
      scaledHeight: Math.round(img.height * scale)
    }));
  }
  
  return images; // No scaling needed
}
```

## 🔧 Optimization Strategies

### Performance Considerations

#### Canvas Size Optimization
- **Maximum dimensions**: 8192x8192 (browser limit)
- **Recommended ratio**: 3:1 maximum aspect ratio
- **Memory usage**: Consider total pixel count
- **Viewer limits**: Test with target viewers

#### Tile Generation
- **Optimal tile size**: 256x256 or 512x512
- **Overlap**: 1-2 pixels for seamless viewing
- **Levels**: Calculate appropriate pyramid levels
- **Compression**: Balance quality and file size

### Quality Considerations

#### Resolution Matching
```javascript
function calculateOptimalResolution(images, targetViewingSize) {
  const avgDPI = images.reduce((sum, img) => sum + img.dpi, 0) / images.length;
  const targetDPI = Math.min(avgDPI, 300); // Max 300 DPI for web
  
  return {
    width: Math.round(targetViewingSize.width * (targetDPI / 72)),
    height: Math.round(targetViewingSize.height * (targetDPI / 72))
  };
}
```

#### Detail Preservation
- **Minimum size**: Ensure smallest image is readable
- **Maximum size**: Prevent unnecessary scaling
- **Aspect ratio**: Maintain original proportions
- **Sharpness**: Avoid over-scaling

## 📊 Algorithm Selection Guide

### Use Case Matrix

| Layout Type | Best For | Image Count | Complexity |
|-------------|----------|-------------|------------|
| Horizontal | Basic comparison | 2-4 | Low |
| Horizontal Balanced | Detail analysis | 2-6 | Medium |
| Storyboard | Presentations | 3-8 | Medium |
| Main + Derivatives | Featured works | 2-5 | High |
| Grid 2x2 | Systematic study | 4 | Low |
| Vertical Stack | Sequences | 2-10 | Low |

### Performance Matrix

| Layout Type | Canvas Size | Memory Usage | Loading Time |
|-------------|-------------|--------------|--------------|
| Horizontal | Variable | Medium | Fast |
| Horizontal Balanced | Predictable | High | Medium |
| Storyboard | Optimized | Medium | Fast |
| Main + Derivatives | Compact | Low | Fast |
| Grid 2x2 | Square | Medium | Fast |
| Vertical Stack | Tall | Medium | Medium |

## 🔍 Advanced Techniques

### Dynamic Positioning
```javascript
function dynamicLayout(images, viewerCapabilities) {
  const layout = detectOptimalLayout(images, viewerCapabilities);
  
  switch (layout.type) {
    case 'detail-focused':
      return horizontalBalancedLayout(images, layout.padding, layout.targetHeight);
    case 'overview-focused':
      return storyboardLayout(images, layout.padding, layout.targetHeight);
    case 'hierarchical':
      return mainDerivativesLayout(images, layout.padding);
    default:
      return horizontalLayout(images, layout.padding);
  }
}
```

### Responsive Positioning
```javascript
function responsiveLayout(images, screenSize) {
  const isMobile = screenSize.width < 768;
  const isTablet = screenSize.width < 1024;
  
  if (isMobile) {
    return verticalStackLayout(images, 50); // Smaller padding
  } else if (isTablet) {
    return storyboardLayout(images, 75, 400); // Smaller target height
  } else {
    return horizontalBalancedLayout(images, 100, 600);
  }
}
```

### Viewer-Specific Optimization
```javascript
function optimizeForViewer(layout, viewerType) {
  switch (viewerType) {
    case 'mirador':
      return {
        ...layout,
        targetFormat: 'string', // Use string targets
        coordinateSystem: 'percentage'
      };
    case 'openseadragon':
      return {
        ...layout,
        targetFormat: 'object', // Use object targets
        coordinateSystem: 'pixel'
      };
    default:
      return layout;
  }
}
```

## 💡 Best Practices

### Algorithm Selection
1. **Consider use case**: Choose based on viewing purpose
2. **Test performance**: Verify with actual data
3. **Validate output**: Check with target viewers
4. **Document decisions**: Record rationale

### Parameter Tuning
1. **Start with defaults**: Use recommended values
2. **Test iteratively**: Adjust based on results
3. **Consider context**: Adapt to specific needs
4. **Monitor performance**: Track metrics

### Quality Assurance
1. **Visual inspection**: Review all layouts
2. **Cross-viewer testing**: Verify compatibility
3. **Performance testing**: Check loading times
4. **User testing**: Gather feedback

---

**Next:** [IIIF Compliance](./iiif-compliance.md) | [API Reference](./api-reference.md)
