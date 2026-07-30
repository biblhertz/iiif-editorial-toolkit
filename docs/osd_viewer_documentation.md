# OpenSeadragon IIIF Viewer - User Instructions

## Overview

The OpenSeadragon IIIF Viewer is a specialized tool for displaying IIIF manifests in academic contexts. It intelligently handles different manifest types and provides optimized viewing experiences for scholarly image comparison.

---

## Customization Instructions

### 🔧 **Repository Setup**
This viewer includes placeholder content that must be customized for your research:

#### **Required Customizations**

##### **1. Update Manifest URLs**
Replace the placeholder URLs in the dropdown:
```html
<!-- CUSTOMIZE: Replace these with your actual manifest URLs -->
<option value="https://example.com/manifest1.json">Sample Comparison 1</option>
<option value="https://example.com/manifest2.json">Sample Comparison 2</option>
<option value="https://example.com/manifest3.json">Sample Single Image</option>
```

**Replace with:**
```html
<option value="https://your-institution.edu/manifests/comparison1.json">Your Research Comparison 1</option>
<option value="https://your-institution.edu/manifests/comparison2.json">Your Research Comparison 2</option>
<option value="https://your-institution.edu/manifests/single-image.json">Your Research Single Image</option>
```

##### **2. Update Page Content**
Modify the header and descriptions:
```html
<!-- Current placeholders -->
<title>IIIF Comparison Viewer</title>
<h1>IIIF Comparison Viewer</h1>
<p>OpenSeadragon-based viewer for IIIF manifest comparison and analysis</p>

<!-- Replace with your content -->
<title>Your Research Project - IIIF Viewer</title>
<h1>Your Research Project Name</h1>
<p>Specialized viewer for [your research topic] image analysis</p>
```

##### **3. Update Configuration**
Modify the viewerConfig object:
```javascript
const viewerConfig = {
    pageTitle: "Your Research Project - IIIF Viewer",
    pageDescription: "Your research description here",
    
    defaultManifests: {
        "study1": "https://your-domain.edu/manifests/study1.json",
        "study2": "https://your-domain.edu/manifests/study2.json",
        "study3": "https://your-domain.edu/manifests/study3.json"
    },
    
    institutionName: "Your Institution Name",
    projectName: "Your Research Project Name"
};
```

##### **4. Update Navigation Language**
The current version uses English. For Italian navigation:
```javascript
// English version
prevBtn.textContent = '◀ Previous';
nextBtn.textContent = 'Next ▶';

// Italian version
prevBtn.textContent = '◀ Precedente';
nextBtn.textContent = 'Successivo ▶';
```

#### **Optional Customizations**

##### **Styling and Branding**
- Update colors to match your institution's brand
- Add institution logo to header
- Modify fonts and spacing as needed

##### **Additional Features**
- Add custom metadata display
- Include citation information
- Add export/sharing capabilities

### 📁 **File Location**
The viewer lives at `src/openseadragon/osd_viewer.html` in this repository. There is no separate template or customization-guide file — the placeholders below are marked inline in that same file with `<!-- CUSTOMIZE: -->` comments.

### 🚀 **Quick Setup Guide**
1. **Open `src/openseadragon/osd_viewer.html`** in a text editor
2. **Replace the placeholder manifest URLs** (`Sample Comparison 1/2`, `Sample Single Image`) with your own — the IIIF Cookbook example entries below them can stay for testing
3. **Update page title and descriptions**
4. **Modify the `viewerConfig` object** with your project details
5. **Test with your manifests** by opening the file in a browser
6. **Deploy** alongside the rest of the toolkit (see the [GitHub Pages guide](./github_pages_guide.md))

### ⚠️ **Important Notes**
- **Keep IIIF community examples** for testing functionality
- **Ensure your manifests are accessible** via HTTPS
- **Test CORS settings** if hosting on different domains
- **Validate your manifests** before deployment

---

## Getting Started

### 🚀 **Loading a Manifest**

#### **Method 1: Select from Dropdown**
1. Use the **"Quick Test Manifests"** dropdown
2. Choose from pre-configured manifests (the `Sample Comparison 1/2` and `Sample Single Image` placeholders, or the IIIF Cookbook examples)
3. Click **"🚀 Load Manifest"**

#### **Method 2: Custom Manifest URL**
1. Enter your manifest URL in the **"Your Manifest URL"** field
2. Click **"🚀 Load Manifest"**

#### **Method 3: Direct JSON Input**
1. Paste manifest JSON into the **"Or paste JSON directly"** textarea
2. Click **"🚀 Load Manifest"**

### 📊 **Viewer Status**
Monitor the info panel for:
- **Status**: Current loading/error status
- **Images**: Number of images in manifest
- **Dimensions**: Canvas dimensions

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
- **🏠 Fit to Screen**: Optimize for full canvas view
- **🔄 Reset View**: Return to home position
- **📐 Fit Comparison**: Optimize for comparison viewing

### 🔄 **Advanced Controls**

#### **Rotation**
- OpenSeadragon's built-in rotation control is enabled (`showRotationControl: true`) — no custom rotation UI or keyboard shortcut is wired up beyond this.

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
- **Previous/Next buttons** (◀ Previous / Next ▶)
- **Image counter** (1/3, 2/3, etc.)
- **Image titles** displayed in navigation bar

**Controls**:
- **◀ Previous**: Go to previous image
- **Next ▶**: Go to next image
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

#### **"Failed to load manifest" Message**
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
1. Try the "📐 Fit Comparison" button
2. Use "🔄 Reset View" to recalculate view
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
2. Use "📐 Fit Comparison" for better fit
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
A: This is due to OpenSeadragon's interpretation of positioned annotations. Use "📐 Fit Comparison" or try Mirador 3 for better composition support.

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

*Instructions last updated: 15/07/2025*
