# Viewer Guide

Complete guide to using the IIIF viewers for academic research and analysis.

## 🎯 Choosing the Right Viewer

### OpenSeadragon Viewer (`osd_viewer.html`)
**Best for:**
- High-resolution image analysis
- Detailed navigation and zoom
- Sequential image viewing
- Research presentations

**Features:**
- Deep zoom capabilities
- Smooth pan and zoom
- Multi-canvas navigation
- Composition support
- Customizable controls

### Multi-Viewer Testing Tool (`iiif_viewer.html`)
**Best for:**
- Testing manifest compatibility
- Comparing viewer behaviors
- Validation and quality assurance
- Cross-platform testing

**Features:**
- Mirador 3 integration
- TheseusViewer support
- Manifest validation
- Quick viewer switching

## 🔧 OpenSeadragon Viewer

### Loading Manifests

#### Quick Test Manifests
1. Select from dropdown menu
2. Pre-loaded examples available
3. IIIF Cookbook recipes included
4. Automatic loading

#### Custom Manifest URL
1. Enter manifest URL in "Your Manifest URL" field
2. Click "🚀 Load Manifest"
3. Viewer updates automatically

#### Direct JSON Input
1. Paste manifest JSON in text area
2. Click "🚀 Load Manifest"
3. Creates temporary blob URL

### Navigation Controls

#### Mouse Controls
- **Zoom**: Mouse wheel or double-click
- **Pan**: Click and drag
- **Reset**: Right-click or reset button
- **Select**: Click on annotations (compositions)

#### Keyboard Shortcuts
- **Home**: Fit to screen
- **+/-**: Zoom in/out
- **Arrow Keys**: Pan
- **Escape**: Reset view

#### Viewer Controls
- **🏠 Fit to Screen**: Optimize for full canvas view
- **🔄 Reset View**: Return to home position
- **📐 Fit Comparison**: Optimize for comparison viewing
- **Navigator**: Thumbnail navigation (top-right)

### Manifest Types

#### Single Canvas (Simple Image)
- Single image display
- Standard navigation
- Zoom and pan controls
- Thumbnail navigation

#### Multi-Canvas (Sequence)
- Multiple images in sequence
- Navigation arrows
- Page counter
- Canvas titles
- Previous/Next buttons

#### Composition (Positioned Images)
- Multiple images on single canvas
- Positioned annotations
- Coordinate-based layout
- Simultaneous viewing

### Advanced Features

#### Intelligent Manifest Parsing
- Automatic type detection
- IIIF 2.1 and 3.0 support
- Fallback handling
- Error recovery

#### Performance Optimization
- Efficient tile loading
- Memory management
- Progressive enhancement
- Responsive design

## 🧪 Multi-Viewer Testing Tool

### Viewer Selection

#### Mirador 3
- **Strengths**: Advanced annotation, multi-window
- **Best for**: Complex scholarly viewing
- **Features**: Workspace management, comparison views
- **Use cases**: Academic research, detailed analysis

#### TheseusViewer
- **Strengths**: Comparative layouts, positioning
- **Best for**: Side-by-side comparisons
- **Features**: Specialized comparison tools
- **Use cases**: Art history, manuscript studies

### Testing Workflow

1. **Load Manifest**
   - Enter URL or select from examples
   - Click "🚀 Load Manifest"

2. **Switch Viewers**
   - Use tabs to switch between viewers
   - Compare behavior and display
   - Test navigation features

3. **Validate Manifest**
   - Click "✅ Validate"
   - Review compliance report
   - Check compatibility notes

### Validation Features

#### IIIF Compliance Check
- **Context validation**: Verifies IIIF API version
- **Structure validation**: Checks required fields
- **Type validation**: Confirms manifest type
- **Content validation**: Analyzes canvas structure

#### Compatibility Analysis
- **Multi-canvas detection**: Identifies sequence manifests
- **Composition analysis**: Checks positioning
- **Target format**: Analyzes annotation targets
- **Media support**: Checks content types

### Validation Results

#### Valid Manifest Indicators
- ✅ Valid IIIF 3.0 context
- ✅ Valid id and type
- ✅ Valid label
- ✅ Canvas(es) found
- ✅ Composition detected
- ✅ Cookbook-style targets

#### Common Issues
- ❌ Missing @context
- ❌ Invalid id format
- ❌ Missing required fields
- ❌ No items found
- ❌ Malformed annotations

## 🎨 Advanced Viewing Techniques

### Comparative Analysis

#### Side-by-Side Comparison
1. Use composition manifests
2. Position images horizontally
3. Synchronize zoom levels
4. Compare details systematically

#### Overlay Comparison
1. Use semi-transparent annotations
2. Toggle visibility
3. Align registration points
4. Analyze differences

### Sequential Viewing

#### Manuscript Navigation
1. Load multi-canvas manifest
2. Use navigation controls
3. Maintain zoom level
4. Compare consecutive pages

#### Chronological Analysis
1. Organize by date
2. Use consistent scaling
3. Navigate systematically
4. Document changes

### Detail Analysis

#### High-Resolution Viewing
1. Start with overview
2. Zoom to areas of interest
3. Compare at pixel level
4. Document findings

#### Annotation Integration
1. Load annotated manifests
2. Toggle annotation visibility
3. Review scholarly notes
4. Add personal observations

## 📊 Performance Optimization

### Loading Speed
- **Tile optimization**: Choose appropriate tile sizes
- **Caching**: Enable browser caching
- **CDN usage**: Use content delivery networks
- **Compression**: Optimize image formats

### Memory Management
- **Viewport culling**: Only load visible tiles
- **Progressive loading**: Load detail on demand
- **Cleanup**: Remove unused resources
- **Monitoring**: Watch memory usage

### Network Efficiency
- **Bandwidth adaptation**: Adjust quality based on connection
- **Prefetching**: Load likely-needed tiles
- **Compression**: Use efficient formats
- **Caching**: Store frequently accessed content

## 🔍 Troubleshooting

### Common Issues

#### Manifest Won't Load
- **Check URL**: Verify manifest URL is accessible
- **CORS issues**: Ensure server allows cross-origin requests
- **Format errors**: Validate JSON syntax
- **Network problems**: Check internet connectivity

#### Images Don't Display
- **Service availability**: Verify IIIF service is running
- **Authentication**: Check if login is required
- **Format support**: Ensure image formats are supported
- **Tile errors**: Check individual tile URLs

#### Navigation Problems
- **Canvas dimensions**: Verify width/height values
- **Coordinate errors**: Check annotation positioning
- **Zoom limits**: Adjust min/max zoom levels
- **Performance**: Reduce tile size or quality

### Debugging Tools

#### Browser Developer Tools
- **Network tab**: Check failed requests
- **Console**: Review JavaScript errors
- **Elements**: Inspect DOM structure
- **Performance**: Analyze loading times

#### Manifest Validation
- **Online validators**: Use IIIF validation services
- **Built-in validation**: Use toolkit validation features
- **Manual review**: Check manifest structure
- **Test environments**: Use different viewers

## 💡 Best Practices

### Manifest Design
- **Appropriate canvas sizes**: Balance quality and performance
- **Consistent metadata**: Use standardized fields
- **Clear navigation**: Provide intuitive sequences
- **Responsive layouts**: Consider different screen sizes

### User Experience
- **Loading indicators**: Show progress for long operations
- **Error handling**: Provide clear error messages
- **Accessibility**: Support screen readers and keyboard navigation
- **Documentation**: Include usage instructions

### Performance
- **Optimize images**: Use appropriate resolution and compression
- **Minimize requests**: Reduce number of HTTP requests
- **Cache effectively**: Set appropriate cache headers
- **Monitor usage**: Track performance metrics

### Academic Use
- **Citation support**: Include proper attribution
- **Versioning**: Maintain manifest versions
- **Archival**: Ensure long-term preservation
- **Standards compliance**: Follow IIIF best practices

## 🔗 Integration Examples

### Embedding in Websites
```html
<iframe 
  src="osd_viewer.html?manifest=https://example.com/manifest.json"
  width="800" 
  height="600">
</iframe>
```

### LMS Integration
- **Moodle**: Embed as external tool
- **Canvas**: Add as external app
- **Blackboard**: Use building blocks
- **Custom**: Create wrapper applications

### Publication Integration
- **Journal articles**: Embed interactive figures
- **Digital editions**: Provide manuscript viewing
- **Exhibition catalogs**: Include comparative views
- **Teaching materials**: Add interactive examples

---

**Next:** [Layout Algorithms](./layout-algorithms.md) | [IIIF Compliance](./iiif-compliance.md)