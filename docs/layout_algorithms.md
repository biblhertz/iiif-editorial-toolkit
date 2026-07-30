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

**Characteristics**:
- Fixed target height, consistent readability across images
- Optimizes for viewing experience
- Good for: Presentations, teaching

### 4. Main + Derivatives Layout

**Purpose**: Hierarchical display with primary image and supporting details

**Characteristics**:
- Hierarchical arrangement
- Primary image emphasized
- Supporting details below
- Good for: Featured works with details

### 5. Grid Layout (2x2)

**Purpose**: Systematic comparison in grid format

**Characteristics**:
- Fixed 2×2 grid, equal-sized cells sized from the canvas dimensions
- Systematic arrangement
- Good for: Systematic comparisons

### 6. Vertical Stack Layout

**Purpose**: Chronological or sequential vertical arrangement

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

**See also:** [IIIF Compliance](./iiif_compliance.md) | [Generator Guide](./generator_guide.md)
