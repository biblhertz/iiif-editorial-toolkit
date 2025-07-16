# IIIF Editorial Toolkit

A comprehensive suite of tools for creating, viewing, and managing IIIF (International Image Interoperability Framework) manifests in academic and scholarly contexts.

## The history Behind
This toolkit was created out of frustration in order to have a sensible way to generate multi-image IIIF manifests as a better solution than genrating a composition in Photoshop. Initially the idea was to use Openseadragon to view them and the solution provided by Claude 4 Sonnet worked, kinda. The viewer is a quick way to check the code, or even a draft for a display page, because I wanted a local Openseadragon with multi-image enabled. The problems started with more complex layout with different vertical alignment, because the coordinates made absolutely no sense. The other problem was that those manifest were not properly displayed in Mirador, even if the manifest and the layers were correctly loaded.

For this reason I double checked the IIIF Multi-Image cookbook and found that the OSD manifest had a totally different approach. I asked to rebuilt everything in a new version. if you think this might be interesting, you can read the full description below.

## 🚀 Quick Start

### Demo
Visit our [live demo](https://biblhertz.github.io/iiif-editorial-toolkit/) to try all tools without installation.

### Local Setup
```bash
git clone https://github.com/biblhertz/iiif-editorial-toolkit.git
cd iiif-editorial-toolkit
# Open any HTML file in your browser - no build step required!
```

## 📚 Project Structure

```
iiif-editorial-toolkit/
├── demo/                        # GitHub Pages demo site (TBD)
├── docs/                        # Documentation 
├── src/                         # The code 
│   ├── generator/               # Manifest generation tools
│   │   ├── iiif_generator.html  # Enhanced academic generator
│   │   └── osd_generator.html   # OpenSeadragon-focused generator
│   ├── openseadragon/           # OpenSeadragon viewer
│   │   └── osd_viewer.html      # Specialized OSD viewer
│   └── viewer/                  # Multi-viewer testing tools
│       └── iiif_viewer.html     # Multi-viewer comparison tool
└── README.md                    # This file
```

## 🛠️ Tools Overview

### 1. III Manifest Generator (`iiif_generator.html`)
**Best for:** Complex academic projects with multiple comparison layouts

**Features:**
- Dual manifest generation (Universal + Simple)
- Advanced layout algorithms (6 layout types)
- Viewer compatibility optimization
- Manifest library management
- Auto-fetch IIIF image information
- Validation and testing tools

**Use Cases:**
- Art history comparisons
- Manuscript analysis
- Multi-image scholarly publications
- Complex positioning requirements

### 2. OpenSeadragon Generator (`osd_generator.html`)
**Best for:** Single-canvas compositions optimized for OpenSeadragon

**Features:**
- OpenSeadragon-specific optimizations
- Simplified comparison layouts
- Canvas-based positioning
- Library management
- Clean, focused interface

**Use Cases:**
- Simple image comparisons
- OpenSeadragon-focused projects
- Quick manifest creation
- Teaching materials

### 3. OpenSeadragon Viewer (`osd_viewer.html`)
**Best for:** High-performance viewing with detailed navigation

**Features:**
- Multi-canvas navigation
- Positioned composition support
- Automatic manifest type detection
- Advanced zoom and pan controls
- Intelligent manifest parsing

**Use Cases:**
- Detailed image analysis
- High-resolution viewing
- Sequential image navigation
- Research presentations

### 4. Multi-Viewer Testing Tool (`iiif_viewer.html`)
**Best for:** Testing manifest compatibility across different viewers

**Features:**
- Mirador 3 integration
- TheseusViewer support
- Manifest validation
- Compatibility testing
- Quick viewer switching

**Use Cases:**
- Manifest validation
- Cross-viewer testing
- Compatibility verification
- Quality assurance

## 🔄 Workflows

### OpenSeadragon Workflow
Perfect for detailed image analysis and research:

1. **Generate Individual Manifests**
   - Use `osd_generator.html` 
   - Auto-fetch image dimensions
   - Save to library

2. **Create Comparisons**
   - Import from library
   - Choose layout type
   - Generate OpenSeadragon-optimized manifest

3. **View Results**
   - Use `osd_viewer.html`
   - Navigate with full OSD controls
   - Export or share manifest

### IIIF Cookbook Workflow
Ideal for complex academic publications:

1. **Generate Academic Manifests**
   - Use `iiif_generator.html`
   - Create individual image manifests
   - Build manifest library

2. **Create Advanced Comparisons**
   - Select viewer compatibility (Universal/Simple/Dual)
   - Choose from 6 layout algorithms
   - Fine-tune positioning

3. **Test Compatibility**
   - Use `iiif_viewer.html`
   - Test in Mirador 3 and TheseusViewer
   - Validate IIIF compliance

4. **Deploy**
   - Download manifests
   - Host on your server
   - Integrate with publication

## 📖 Detailed Documentation

- [Generator Guide](./docs/generator-guide.md) - Complete guide to manifest generation
- [Viewer Guide](./docs/viewer-guide.md) - Using the viewers effectively
- [Layout Algorithms](./docs/layout-algorithms.md) - Understanding positioning systems
- [IIIF Compliance](./docs/iiif-compliance.md) - Standards and best practices
- [API Reference](./docs/api-reference.md) - Technical specifications
- [Examples](./docs/examples.md) - Coded examples and use cases

## 🎯 Use Cases

### Art History Research
- Compare artistic works across collections
- Analyze details and variations
- Create scholarly annotations
- Present findings interactively

### Manuscript Studies
- Multi-page manuscript navigation
- Parallel text comparison
- Paleographic analysis
- Collaborative annotation

### Digital Humanities
- Cultural heritage preservation
- Interactive exhibitions
- Educational resources
- Research publications

### Academic Publishing
- Illustrated scholarly articles
- Interactive figures
- Comparative analysis
- Peer review materials

## 🔧 Technical Requirements

### Browser Support
- Chrome 70+ (recommended)
- Firefox 65+
- Safari 12+
- Edge 79+

### IIIF Compliance
- IIIF Presentation API 3.0
- IIIF Image API 2.1/3.0
- IIIF Authentication (planned)

### Dependencies
- OpenSeadragon 4.1.0 (CDN)
- No build process required
- Pure HTML/CSS/JavaScript

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [IIIF Community](https://iiif.io/) for standards and specifications
- [OpenSeadragon](https://openseadragon.github.io/) for the viewer library
- [Mirador](https://projectmirador.org/) for viewer integration
- [TheseusViewer](https://theseusviewer.org/) for comparison viewing

## 📞 Support

- Create an [issue](https://github.com/yourusername/iiif-editorial-toolkit/issues)
- Check the [documentation](./docs/)
- Join the [IIIF Community](https://iiif.io/community/)

---

**Made with ❤️ and Claude Sonnet 4 for the academic editorial community**
