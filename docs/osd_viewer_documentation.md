# OpenSeadragon IIIF Viewer - User Instructions

## Overview

The OpenSeadragon IIIF Viewer is a specialized tool for displaying IIIF manifests in academic contexts. It intelligently handles different manifest types and provides optimized viewing experiences for scholarly image comparison.

---

## Getting Started

### 🚀 **Loading a Manifest**

#### **Method 1: Select from Dropdown**
1. Use the **"Seleziona Layout"** dropdown
2. Choose from pre-configured manifests:
   - **Composizione Completa** - Full comparison layout
   - **Layout Semplificato** - Simplified arrangement  
   - **Sequenza Singola** - Single sequence viewing
3. Click **"Carica Manifest"**

#### **Method 2: Custom Manifest URL**
1. Enter your manifest URL in the text field
2. Click **"Carica Manifest"**
3. Wait for the "Manifest caricato con successo" status message

### 📊 **Viewer Status**
Monitor the status panel for:
- **Stato**: Current loading/error status
- **Immagini**: Number of images in manifest
- **Dimensioni**: Canvas dimensions

---

## Navigation Controls

### 🎮 **Basic Controls**

#### **Zoom**
- **Mouse Wheel**: Zoom in/out
- **Double Click**: Zoom to point
- **+ Button**: Zoom in
- **- Button**: Zoom out

#### **Pan**
- **Click & Drag**: Move around the image
- **Arrow Keys**: Navigate (if enabled)

#### **Reset**
- **Home Button (⌂)**: Return to full view
- **Right Click**: Quick reset (context menu)
- **"Reset Vista" Button**: Reset to original view

### 🔄 **Advanced Controls**

#### **Rotation**
- **Rotation Control**: Rotate image clockwise/counterclockwise
- **Keyboard Shortcuts**: R key (if enabled)

#### **Full Screen**
- **Full Screen Button**: Toggle full screen mode
- **ESC Key**: Exit full screen

---

## Manifest Types & Behavior

### 📄 **Single Image Manifests**
**What it shows**: One image with full zoom/pan capabilities
**Navigation**: Standard OpenSeadragon controls
**Best for**: Detailed examination of individual images

### 🔄 **Multi-Canvas Manifests**
**What it shows**: Sequential images with navigation
**Navigation**: Automatic navigation controls appear
**Features**:
- **Previous/Next buttons** (◀ Precedente / Successivo ▶)
- **Image counter** (1/3, 2/3, etc.)
- **Image titles** displayed in navigation bar

**Controls**:
- **Precedente**: Go to previous image
- **Successivo**: Go to next image
- **Counter**: Shows current position in sequence

### 🎨 **Positioned Compositions**
**What it shows**: Multiple images arranged in a single canvas
**Navigation**: Pan and zoom to explore different areas
**Features**:
- **Spatial relationships** preserved
- **Comparison viewing** enabled
- **Unified zoom/pan** across all images

**Limitations**:
- May show only one image if coordinates are problematic
- Requires proper IIIF 3.0 positioning format

---

## Viewer Modes

### 🎭 **Composition Mode**
**Activated when**: Manifest has positioned annotations
**Display**: All images shown in spatial relationship
**Navigation**: Pan to explore different areas
**Zoom**: Unified zoom across all images

### 📚 **Sequential Mode**
**Activated when**: Manifest has multiple canvases
**Display**: One image at a time with navigation
**Navigation**: Previous/Next buttons
**Zoom**: Independent zoom for each image

### 🖼️ **Single Image Mode**
**Activated when**: Manifest has one image
**Display**: Full image with standard controls
**Navigation**: Standard OpenSeadragon controls
**Zoom**: Full zoom capabilities

---

## Troubleshooting

### ❌ **Common Issues**

#### **"Errore nel caricamento" Message**
**Causes**:
- Invalid manifest URL
- CORS issues with image server
- Malformed IIIF manifest

**Solutions**:
1. Check manifest URL is accessible
2. Verify IIIF service is online
3. Try a different manifest
4. Check browser console for detailed errors

#### **Only One Image Shows in Composition**
**Causes**:
- Coordinate positioning issues
- OpenSeadragon interpretation problems
- Manifest format incompatibility

**Solutions**:
1. Try the "Adatta Confronto" button
2. Use "Reset Vista" to recalculate view
3. Check if manifest works in other viewers
4. Verify coordinate format in manifest

#### **Navigation Controls Don't Appear**
**Causes**:
- Single image manifest (navigation not needed)
- JavaScript loading issues
- Manifest structure problems

**Solutions**:
1. Refresh the page
2. Check browser console for errors
3. Verify manifest has multiple items
4. Try loading a different manifest

#### **Images Don't Load**
**Causes**:
- IIIF service unavailable
- Network connectivity issues
- Invalid image service URLs

**Solutions**:
1. Check internet connection
2. Try loading manifest again
3. Verify IIIF service is accessible
4. Check browser network tab for failed requests

### 🔧 **Advanced Troubleshooting**

#### **Performance Issues**
**Symptoms**: Slow loading, choppy navigation
**Solutions**:
1. Check image resolution settings
2. Verify IIIF service performance
3. Try with smaller images
4. Check browser memory usage

#### **Coordinate Misalignment**
**Symptoms**: Images positioned incorrectly
**Solutions**:
1. This is a known OpenSeadragon limitation
2. Use "Adatta Confronto" for better fit
3. Consider using Mirador 3 for complex compositions
4. Check manifest coordinates in other viewers

---

## Best Practices

### 📋 **For Optimal Viewing**

#### **Manifest Selection**
- **Use simple manifests** for complex compositions
- **Test manifests** in multiple viewers
- **Verify IIIF service reliability**

#### **Navigation Strategy**
- **Start with full view** using Home button
- **Use zoom gradually** for detail examination
- **Pan systematically** to explore compositions
- **Reset frequently** to maintain orientation

#### **Performance Optimization**
- **Close other browser tabs** for better performance
- **Use modern browsers** (Chrome, Firefox, Safari)
- **Ensure stable internet connection**
- **Allow JavaScript execution**

### 🎯 **For Scholarly Work**

#### **Image Analysis**
- **Use systematic navigation** to examine all areas
- **Compare zoom levels** across images
- **Take screenshots** at specific zoom levels
- **Document viewing parameters** for reproducibility

#### **Presentation Preparation**
- **Test manifests beforehand** in target environment
- **Have backup viewing options** ready
- **Practice navigation** for smooth presentations
- **Prepare alternative access methods**

---

## Technical Specifications

### 🔧 **Supported Formats**
- **IIIF Presentation API 3.0**
- **IIIF Image API 2.0/3.0**
- **JSON-LD context**
- **Standard image formats** (JPEG, PNG, TIFF)

### 📐 **Display Parameters**
- **Canvas scaling**: Automatic to fit viewport
- **Zoom levels**: Up to 2x pixel ratio
- **Minimum zoom**: 0.8x (configurable)
- **Animation time**: 1.2 seconds
- **Blend time**: 0.1 seconds

### 🎮 **Control Settings**
- **Scroll to zoom**: Enabled
- **Click to zoom**: Enabled
- **Double-click zoom**: Enabled
- **Pan constraints**: Enabled during pan
- **Rotation**: Optional (configurable)

---

## Keyboard Shortcuts

### ⌨️ **Navigation**
- **Arrow Keys**: Pan image (if enabled)
- **+ / -**: Zoom in/out
- **Home**: Return to full view
- **Space**: Toggle full screen
- **ESC**: Exit full screen

### 🔄 **Advanced**
- **R**: Rotate (if rotation enabled)
- **F**: Full screen toggle
- **Ctrl+0**: Reset zoom to 100%

*Note: Some shortcuts may depend on browser and configuration*

---

## Integration Notes

### 🔗 **For Developers**
- **Embed code**: Available for integration
- **API access**: OpenSeadragon API available
- **Customization**: Controls and appearance configurable
- **Event handling**: Mouse/touch events supported

### 📊 **For Content Creators**
- **Manifest testing**: Use validation tools
- **Coordinate precision**: Test positioning carefully
- **Performance**: Optimize image services
- **Accessibility**: Consider screen readers

---

## FAQ

### ❓ **Frequently Asked Questions**

**Q: Why do some compositions show only one image?**
A: This is due to OpenSeadragon's interpretation of positioned annotations. Use "Adatta Confronto" or try Mirador 3 for better composition support.

**Q: Can I save or bookmark specific views?**
A: The viewer doesn't support bookmarking specific zoom/pan positions. Use screenshots for reference.

**Q: How do I report issues with manifests?**
A: Check the browser console for errors and verify the manifest works in other IIIF viewers first.

**Q: Can I use this viewer offline?**
A: The viewer requires internet access to load IIIF manifests and images from remote servers.

**Q: What's the maximum image size supported?**
A: Limited by browser memory and IIIF service capabilities. Very large images may perform slowly.

---

## Support Resources

### 📖 **Documentation**
- [OpenSeadragon Documentation](https://openseadragon.github.io/)
- [IIIF Presentation API](https://iiif.io/api/presentation/3.0/)
- [IIIF Image API](https://iiif.io/api/image/3.0/)

### 🧪 **Testing Tools**
- [IIIF Validator](https://iiif.io/api/validator/)
- [Mirador 3](https://projectmirador.org/)
- [Universal Viewer](https://universalviewer.io/)

### 💡 **Best Practices**
- Always validate manifests before deployment
- Test in multiple viewers for compatibility
- Consider viewer limitations when creating manifests
- Provide alternative access methods for users

---

*Instructions last updated: December 2024*