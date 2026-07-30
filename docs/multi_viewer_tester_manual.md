# IIIF Multi-Viewer Tester - User Manual

## Overview

The IIIF Multi-Viewer Tester is a comprehensive testing tool that allows you to evaluate IIIF manifests across multiple viewers simultaneously. It provides side-by-side comparison of how different viewers interpret and display your manifests, making it essential for ensuring cross-platform compatibility.

---

## Interface Overview

### 🎭 **Viewer Selection Tabs**
The tool features two viewer options, switched via tabs (each tab loads the current manifest into an iframe pointing at that viewer's public embed URL):

#### **🎭 Mirador 3**
- Advanced IIIF viewer with full annotation support
- Excellent for complex compositions and scholarly features
- Best compatibility with IIIF 3.0 cookbook format

#### **📚 TheseusViewer**  
- Specialized viewer for comparative layouts
- Confirmed compatibility with cookbook-format manifests
- Optimized for academic image comparison

For OpenSeadragon-based viewing, use the separate `src/openseadragon/osd_viewer.html` tool — it is not one of this tester's tabs.

---

## Getting Started

### 🚀 **Loading a Manifest**

#### **Method 1: Quick Test Manifests**
1. Use the **"Quick Test Manifests"** dropdown
2. Select from pre-configured options:
   - **Your Cookbook Manifest** - Placeholder for your own manifest URL
   - **IIIF Cookbook - Basic Image** - Standard single-image example
   - **IIIF Cookbook - Multiple Images** - Standard multi-image example
   - **IIIF Cookbook - Annotations** - Annotation testing
3. Click **"🚀 Load Manifest"** (the same button used for all three loading methods)

#### **Method 2: Custom Manifest URL**
1. Enter your manifest URL in the **"Your Manifest URL"** field
2. Click **"🚀 Load Manifest"**
3. Monitor the status panel for loading confirmation

### 📊 **Status Monitoring**
The status panel shows:
- **Loading progress** ("Loading manifest...")
- **Success confirmation** ("Manifest loaded in [VIEWER]")
- **Error messages** with specific failure reasons
- **Current viewer** information

---

## Viewer-Specific Features

### 🎭 **Mirador 3 Tab**

#### **What It Shows**
- **Positioned compositions** with full spatial relationships
- **Annotation overlays** if present in manifest
- **Metadata panels** with detailed information
- **Navigation controls** for multi-canvas manifests

#### **Best Use Cases**
- Complex positioned compositions
- Manifests with annotations
- Scholarly comparison layouts
- Multi-canvas sequential viewing

#### **Navigation**
- **Zoom**: Mouse wheel or zoom controls
- **Pan**: Click and drag
- **Navigation**: Built-in Mirador controls
- **Metadata**: Side panels with manifest information

### 📚 **TheseusViewer Tab**

#### **What It Shows**
- **Comparative layouts** optimized for academic use
- **Cookbook-format compositions** with proper positioning
- **Clean interface** focused on image comparison
- **Responsive design** for different screen sizes

#### **Best Use Cases**
- Academic image comparison
- Cookbook-format manifests
- Publication-ready displays
- Comparative analysis layouts

#### **Navigation**
- **Zoom**: Integrated zoom controls
- **Pan**: Smooth panning interface
- **Layout**: Automatic layout optimization
- **Comparison**: Side-by-side viewing modes

---

## Validation & Testing Features

### ✅ **Manifest Validation**

#### **IIIF Compliance Testing**
Click **"✅ Validate"** to check:
- **@context**: IIIF 3.0 context validation
- **Required fields**: id, type, label validation
- **Structure**: Items and canvas validation
- **Format detection**: Multi-canvas vs composition analysis

#### **Validation Results**
Results display with color-coded feedback:
- **✅ Green**: Valid elements
- **❌ Red**: Invalid or missing elements
- **Detailed messages**: Specific validation information

### 🧪 **Compatibility Testing**

#### **Cross-Viewer Analysis**
The tool analyzes manifest structure for:
- **Single images**: Universal compatibility
- **Multi-canvas**: Sequential viewing support
- **Positioned compositions**: Viewer-specific capabilities

#### **Compatibility Matrix**
| Manifest Type | Mirador 3 | TheseusViewer |
|---------------|-----------|---------------|
| Single Image | Excellent | Excellent |
| Multi-Canvas | Excellent | Good |
| Positioned Composition | Excellent | Good |

---

## Advanced Features

### 🔍 **Manifest Analysis**

#### **Automatic Structure Detection**
The tool automatically identifies:
- **Manifest type** (single image, multi-canvas, composition)
- **Target format** (string vs object targets)
- **Compatibility recommendations**
- **Viewer-specific optimizations**

#### **Detailed Reporting**
Validation provides insights on:
- **Image count** and structure
- **Canvas dimensions** and layout
- **Annotation format** and compatibility
- **Service availability** and accessibility

### 🚀 **Quick Testing Workflow**

#### **Rapid Compatibility Check**
1. **Load manifest** in current viewer
2. **Switch between tabs** to test all viewers
3. **Compare results** across platforms
4. **Identify issues** and compatibility problems
5. **Generate reports** for optimization

#### **Comparative Analysis**
- **Side-by-side comparison** by switching tabs
- **Performance evaluation** across viewers
- **Feature support** assessment
- **User experience** comparison

---

## Troubleshooting

### ❌ **Common Issues**

#### **Manifest Loading Failures**
**Symptoms**: "Failed to load manifest" errors
**Causes**:
- Invalid manifest URL
- CORS restrictions
- Malformed JSON
- Network connectivity issues

**Solutions**:
1. **Check URL accessibility** in browser
2. **Verify JSON format** with validator
3. **Test with sample manifests** first
4. **Check browser console** for detailed errors

#### **Viewer-Specific Problems**

##### **Mirador 3 Issues**
- **Blank display**: Check manifest structure
- **No annotations**: Verify annotation format
- **Loading errors**: Check IIIF service availability

##### **TheseusViewer Issues**
- **Positioning problems**: Verify cookbook format
- **Missing images**: Check image service URLs
- **Layout errors**: Validate coordinate format

### 🔧 **Advanced Troubleshooting**

#### **Cross-Viewer Compatibility**
**Problem**: Manifest works in one viewer but not others
**Approach**:
1. **Use validation** to identify structural issues
2. **Compare target formats** (string vs object)
3. **Check coordinate systems** and scaling
4. **Test with simpler manifests** first

#### **Performance Optimization**
**Problem**: Slow loading or poor performance
**Solutions**:
1. **Test with smaller images** first
2. **Verify IIIF service performance**
3. **Check network connectivity**
4. **Use browser developer tools** for analysis

---

## Best Practices

### 📋 **For Manifest Testing**

#### **Systematic Testing Approach**
1. **Start with validation** before viewer testing
2. **Test in order of complexity**: Single image → Multi-canvas → Compositions
3. **Use sample manifests** to verify tool functionality
4. **Document compatibility** issues for future reference

#### **Comparative Analysis**
- **Test both viewers** for comprehensive coverage
- **Note viewer-specific behaviors** and limitations
- **Document performance differences**
- **Identify optimal viewer** for each use case

### 🎯 **For Academic Use**

#### **Publication Preparation**
- **Test manifests** in intended publication platform
- **Verify accessibility** of IIIF services
- **Document viewer compatibility** for readers
- **Prepare alternative formats** if needed

#### **Quality Assurance**
- **Validate before deployment**
- **Test with multiple browsers**
- **Check mobile compatibility**
- **Verify long-term accessibility**

---

## Integration Guidelines

### 🔗 **For Developers**

#### **Embedding Viewers**
Each viewer can be embedded using iframe:
```html
<!-- Mirador 3 -->
<iframe src="https://projectmirador.org/embed/?iiif-content=MANIFEST_URL"></iframe>

<!-- TheseusViewer -->
<iframe src="https://theseusviewer.org/?manifest=MANIFEST_URL"></iframe>
```

#### **API Integration**
- **Validation API**: Use validation logic in your applications
- **Compatibility checking**: Integrate compatibility tests
- **Manifest parsing**: Reuse manifest analysis code

### 📊 **For Content Creators**

#### **Manifest Optimization**
- **Test early and often** during development
- **Use cookbook formats** for maximum compatibility
- **Validate before publication**
- **Monitor service availability**

#### **Viewer Selection**
- **Mirador 3**: For complex scholarly applications
- **TheseusViewer**: For academic image comparison
- **Multi-viewer**: For maximum compatibility across both

---

## Technical Specifications

### 🔧 **Supported Formats**
- **IIIF Presentation API 3.0**
- **IIIF Image API 2.0/3.0**
- **JSON-LD with IIIF context**
- **Cookbook-format manifests**

### 📐 **Testing Capabilities**
- **Manifest validation** against IIIF 3.0 specification
- **Cross-viewer compatibility** analysis
- **Performance evaluation**
- **Accessibility testing**

### 🖥️ **Browser Requirements**
- **Modern browsers**: Chrome, Firefox, Safari, Edge
- **JavaScript enabled**: Required for all functionality
- **Internet connection**: Required for manifest loading
- **Local storage**: Optional, for caching

---

## Keyboard Shortcuts

### ⌨️ **Navigation**
- **Tab**: Switch between form fields
- **Enter**: Load manifest (when in URL field)
- **Escape**: Close validation results
- **F5**: Refresh current viewer

### 🔄 **Viewer-Specific**
Each viewer maintains its own keyboard shortcuts:
- **Mirador 3**: Standard Mirador shortcuts
- **TheseusViewer**: Viewer-specific controls

---

## FAQ

### ❓ **Frequently Asked Questions**

**Q: Can I test local manifests?**
A: The tool loads manifests by URL only (into an iframe pointing at the Mirador/TheseusViewer embed service), so a local manifest needs to be reachable at a public URL first — for example via GitHub Pages (see the [GitHub Pages guide](./github_pages_guide.md)).

**Q: How do I report compatibility issues?**
A: Use the validation feature first, then test with sample manifests to isolate the issue.

**Q: Can I save test results?**
A: Currently, the tool doesn't save results. Use screenshots or notes for documentation.

**Q: What's the best viewer for my use case?**
A: Use the compatibility testing feature to determine which viewer works best for your specific manifests.

---

## Support Resources

### 📖 **Documentation**
- [IIIF Presentation API 3.0](https://iiif.io/api/presentation/3.0/)
- [IIIF Cookbook](https://iiif.io/api/cookbook/)
- [Mirador 3 Documentation](https://mirador-dev.netlify.app/)

### 🧪 **Testing Resources**
- [IIIF Validator](https://iiif.io/api/validator/)
- [Manifest Examples](https://iiif.io/api/cookbook/)
- [IIIF Community](https://iiif.io/community/)

### 💡 **Best Practices**
- Always validate manifests before testing
- Test in multiple browsers for compatibility
- Document viewer-specific behaviors
- Keep IIIF services accessible and performant

---

## Troubleshooting Quick Reference

### 🚨 **Error Messages**

| Error | Cause | Solution |
|-------|-------|----------|
| "Failed to load manifest" | Invalid URL or CORS | Check URL and service availability |
| "Invalid JSON format" | Malformed JSON | Validate JSON syntax |
| "Missing required fields" | Incomplete manifest | Add required IIIF fields |
| "No items found" | Empty manifest | Verify manifest structure |

### 🔧 **Quick Fixes**

1. **Refresh the page** if viewer becomes unresponsive
2. **Clear browser cache** if loading issues persist
3. **Test with sample manifests** to verify tool functionality
4. **Check browser console** for detailed error messages

---

*User Manual last updated: 15/07/2025*
