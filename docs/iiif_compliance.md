# IIIF Compliance

Guide to IIIF standards compliance and best practices for academic manifests.

## 📜 IIIF Standards Overview

The International Image Interoperability Framework (IIIF) provides standardized APIs for sharing and viewing images across institutions and platforms.

### Core APIs
- **Presentation API 3.0**: Describes how images and their metadata are presented
- **Image API 3.0**: Defines how images are requested and delivered
- **Authentication API 1.0**: Handles access control (future implementation)
- **Search API 1.0**: Enables content search (future implementation)

## 🎯 Presentation API 3.0 Compliance

### Required Fields

#### Manifest Level
```json
{
  "@context": ["http://iiif.io/api/presentation/3/context.json"],
  "id": "https://example.com/manifest.json",
  "type": "Manifest",
  "label": { "en": ["Title"] }
}
```

**Validation Points**:
- ✅ `@context` must reference IIIF 3.0 context
- ✅ `id` must be a valid URI
- ✅ `type` must be "Manifest"
- ✅ `label` must be a language map

#### Canvas Level
```json
{
  "id": "https://example.com/canvas/1",
  "type": "Canvas",
  "width": 1000,
  "height": 693,
  "items": [...]
}
```

**Validation Points**:
- ✅ `id` must be unique URI
- ✅ `type` must be "Canvas"
- ✅ `width` and `height` must be integers
- ✅ `items` must contain AnnotationPage

#### Annotation Level
```json
{
  "id": "https://example.com/annotation/1",
  "type": "Annotation",
  "motivation": "painting",
  "target": "https://example.com/canvas/1",
  "body": {
    "id": "https://example.com/image.jpg",
    "type": "Image",
    "format": "image/jpeg",
    "service": [...]
  }
}
```

**Validation Points**:
- ✅ `id` must be unique URI
- ✅ `type` must be "Annotation"
- ✅ `motivation` should be "painting" for images
- ✅ `target` must reference canvas or region
- ✅ `body` must describe image resource

### Optional but Recommended Fields

#### Metadata Enhancement
```json
{
  "summary": { "en": ["Description of the manifest"] },
  "metadata": [
    {
      "label": { "en": ["Artist"] },
      "value": { "en": ["Leonardo da Vinci"] }
    }
  ],
  "rights": "http://creativecommons.org/licenses/by/4.0/",
  "requiredStatement": {
    "label": { "en": ["Attribution"] },
    "value": { "en": ["Provided by Example Institution"] }
  }
}
```

#### Behavioral Hints
```json
{
  "behavior": ["individuals", "facing-pages"],
  "viewingDirection": "left-to-right",
  "viewingHint": "paged"
}
```

## 🔧 Toolkit Compliance Features

### Automatic Validation

#### Generated Manifests Include:
- ✅ Complete IIIF 3.0 context
- ✅ Valid URI patterns
- ✅ Proper type declarations
- ✅ Required dimensional data
- ✅ Complete annotation structure
- ✅ Proper target formatting

#### Built-in Validation Checks:
```javascript
function validateManifest(manifest) {
  const results = [];
  
  // Context validation
  if (manifest['@context'] && 
      manifest['@context'].includes('http://iiif.io/api/presentation/3/context.json')) {
    results.push({valid: true, message: 'Valid IIIF 3.0 context'});
  } else {
    results.push({valid: false, message: 'Missing or invalid @context'});
  }
  
  // ID validation
  if (manifest.id && isValidURI(manifest.id)) {
    results.push({valid: true, message: 'Valid id'});
  } else {
    results.push({valid: false, message: 'Missing or invalid id'});
  }
  
  // Type validation
  if (manifest.type === 'Manifest') {
    results.push({valid: true, message: 'Valid type'});
  } else {
    results.push({valid: false, message: 'Invalid type'});
  }
  
  return results;
}
```

### Target Format Compatibility

#### String Targets (Cookbook Style)
```json
{
  "target": "https://example.com/canvas/1#xywh=100,100,400,300"
}
```

**Advantages**:
- ✅ Simple and readable
- ✅ Wide viewer support
- ✅ Easy to parse
- ✅ Mirador 3 compatible

#### Object Targets (Structured)
```json
{
  "target": {
    "id": "https://example.com/canvas/1#xywh=100,100,400,300",
    "type": "SpecificResource",
    "source": "https://example.com/canvas/1"
  }
}
```

**Advantages**:
- ✅ More semantic
- ✅ Better for complex selections
- ✅ Future-proof
- ✅ Standards compliant

## 🏛️ Image API Compliance

### Service Declaration
```json
{
  "service": [
    {
      "id": "https://example.com/iiif/image1",
      "type": "ImageService3",
      "profile": "level2"
    }
  ]
}
```

### Profile Levels

#### Level 0 (Basic)
- Required: `info.json`, basic image serving
- Optional: Size and format restrictions

#### Level 1 (Enhanced)
- Required: Size parameters, region extraction
- Optional: Rotation, quality levels

#### Level 2 (Full)
- Required: All level 1 features plus rotation
- Optional: Mirroring, advanced features

### Toolkit Image Service Support

#### Auto-Detection
```javascript
async function fetchImageInfo(serviceId) {
  try {
    const response = await fetch(`${serviceId}/info.json`);
    const info = await response.json();
    
    return {
      width: info.width,
      height: info.height,
      profile: info.profile,
      protocol: info.protocol
    };
  } catch (error) {
    console.error('Image service detection failed:', error);
    return null;
  }
}
```

#### Profile Verification
```javascript
function validateImageService(service) {
  const requiredFields = ['id', 'type', 'profile'];
  const validTypes = ['ImageService3', 'ImageService2'];
  const validProfiles = ['level0', 'level1', 'level2'];
  
  return {
    hasRequiredFields: requiredFields.every(field => service[field]),
    hasValidType: validTypes.includes(service.type),
    hasValidProfile: validProfiles.some(profile => 
      service.profile.includes(profile)
    )
  };
}
```

## 🔍 Common Compliance Issues

### 1. Context Problems

#### Issue: Missing or Incorrect Context
```json
{
  "@context": "http://iiif.io/api/presentation/2/context.json" // ❌ Wrong version
}
```

#### Solution: Use IIIF 3.0 Context
```json
{
  "@context": ["http://iiif.io/api/presentation/3/context.json"] // ✅ Correct
}
```

### 2. URI Format Issues

#### Issue: Invalid ID Format
```json
{
  "id": "manifest1" // ❌ Not a valid URI
}
```

#### Solution: Full URI
```json
{
  "id": "https://example.com/manifest1.json" // ✅ Valid URI
}
```

### 3. Language Map Problems

#### Issue: String Instead of Language Map
```json
{
  "label": "My Title" // ❌ Should be language map
}
```

#### Solution: Proper Language Map
```json
{
  "label": { "en": ["My Title"] } // ✅ Language map
}
```

### 4. Canvas Dimension Issues

#### Issue: Missing Dimensions
```json
{
  "type": "Canvas" // ❌ Missing width/height
}
```

#### Solution: Include Dimensions
```json
{
  "type": "Canvas",
  "width": 1000,
  "height": 693 // ✅ Dimensions included
}
```

### 5. Annotation Structure Problems

#### Issue: Incomplete Annotation
```json
{
  "type": "Annotation",
  "target": "canvas1" // ❌ Missing motivation, body
}
```

#### Solution: Complete Annotation
```json
{
  "type": "Annotation",
  "motivation": "painting",
  "target": "canvas1",
  "body": {
    "id": "image.jpg",
    "type": "Image",
    "format": "image/jpeg"
  } // ✅ Complete annotation
}
```

## 📋 Validation Checklist

### Manifest Level
- [ ] Valid IIIF 3.0 context
- [ ] Unique, valid ID URI
- [ ] Correct type declaration
- [ ] Language map for label
- [ ] Optional: summary, metadata, rights

### Canvas Level
- [ ] Unique ID per canvas
- [ ] Correct type declaration
- [ ] Positive integer dimensions
- [ ] At least one AnnotationPage
- [ ] Optional: label, thumbnail

### Annotation Level
- [ ] Unique ID per annotation
- [ ] Correct type declaration
- [ ] Appropriate motivation
- [ ] Valid target reference
- [ ] Complete body description

### Service Level
- [ ] Valid service ID
- [ ] Correct service type
- [ ] Appropriate profile level
- [ ] Accessible info.json endpoint

## 🛠️ Testing Tools

### Built-in Validation
```javascript
// Use toolkit validation
const validation = validateIIIFManifest(manifest);
validation.forEach(result => {
  console.log(`${result.valid ? '✅' : '❌'} ${result.message}`);
});
```

### External Validators
- [IIIF Validator](https://iiif.io/api/presentation/validator/service/)
- [Presentation API Validator](https://presentation-validator.iiif.io/)
- [Manifest Editor](https://manifest-editor.digirati.services/)

### Cross-Viewer Testing
```javascript
// Test in multiple viewers
const viewers = [
  'https://projectmirador.org/embed/',
  'https://theseusviewer.org/',
  'https://universalviewer.io/'
];

viewers.forEach(viewer => {
  const testUrl = `${viewer}?manifest=${encodeURIComponent(manifestUrl)}`;
  console.log(`Test in: ${testUrl}`);
});
```

## 📊 Compliance Levels

### Level 1: Basic Compliance
- ✅ Valid IIIF 3.0 structure
- ✅ Required fields present
- ✅ Proper type declarations
- ✅ Basic viewing works

### Level 2: Enhanced Compliance
- ✅ Level 1 requirements
- ✅ Rich metadata included
- ✅ Proper language maps
- ✅ Thumbnail support
- ✅ Multi-viewer compatibility

### Level 3: Full Compliance
- ✅ Level 2 requirements
- ✅ Advanced features (behaviors, hints)
- ✅ Authentication support
- ✅ Search API integration
- ✅ Comprehensive testing

## 🔮 Future Considerations

### Upcoming Standards
- **IIIF 4.0**: Enhanced annotation support
- **Web Annotation**: W3C standard integration
- **Linked Data**: RDF/JSON-LD improvements
- **Authentication 2.0**: Enhanced access control

### Best Practices Evolution
- **Performance**: Optimize for mobile devices
- **Accessibility**: Screen reader compatibility
- **Internationalization**: Multi-language support
- **Preservation**: Long-term archival considerations

---

**Next:** [API Reference](./api-reference.md) | [Examples](./examples.md)