# Examples

Illustrative example manifests and workflows for common editorial scenarios, built with the tools described in the [Generator Guide](./generator_guide.md). The JSON below is representative of the shapes each workflow produces — it is not captured output from a real run, and the institutions, artworks, and identifiers are fictional.

## Art History Use Cases

### 1. Stylistic Comparison: Renaissance Masters

**Scenario**: Compare three Renaissance paintings to analyze stylistic evolution.

#### Step-by-Step Workflow

**1. Create Individual Manifests**
```json
{
  "@context": ["http://iiif.io/api/presentation/3/context.json"],
  "id": "https://example.com/leonardo-last-supper.json",
  "type": "Manifest",
  "label": {
    "it": ["Leonardo da Vinci, L'Ultima Cena, 1495-1498"],
    "en": ["Leonardo da Vinci, The Last Supper, 1495-1498"]
  },
  "summary": {
    "it": ["Affresco parietale nel refettorio di Santa Maria delle Grazie"],
    "en": ["Wall fresco in the refectory of Santa Maria delle Grazie"]
  },
  "metadata": [
    {
      "label": {"it": ["Artista"], "en": ["Artist"]},
      "value": {"it": ["Leonardo da Vinci"], "en": ["Leonardo da Vinci"]}
    },
    {
      "label": {"it": ["Data"], "en": ["Date"]},
      "value": {"it": ["1495-1498"], "en": ["1495-1498"]}
    },
    {
      "label": {"it": ["Tecnica"], "en": ["Technique"]},
      "value": {"it": ["Tempera e olio su intonaco"], "en": ["Tempera and oil on plaster"]}
    }
  ],
  "items": [...]
}
```

**2. Build Comparison Layout**
- Layout: "Horizontal Row (Balanced Heights)"
- Target height: 600px
- Padding: 100px
- Images: Leonardo, Raphael, Michelangelo

**3. Generated Comparison Structure**
```json
{
  "items": [{
    "id": "https://example.com/comparison/canvas/layout",
    "type": "Canvas",
    "width": 1800,
    "height": 800,
    "items": [{
      "type": "AnnotationPage",
      "items": [
        {
          "id": "annotation/leonardo",
          "type": "Annotation",
          "motivation": "painting",
          "target": "canvas/layout#xywh=100,100,533,600",
          "body": {
            "id": "https://leonardo-service.com/image.jpg",
            "type": "Image",
            "service": [...]
          }
        },
        {
          "id": "annotation/raphael",
          "type": "Annotation",
          "motivation": "painting",
          "target": "canvas/layout#xywh=733,100,400,600",
          "body": {
            "id": "https://raphael-service.com/image.jpg",
            "type": "Image",
            "service": [...]
          }
        },
        {
          "id": "annotation/michelangelo",
          "type": "Annotation",
          "motivation": "painting",
          "target": "canvas/layout#xywh=1233,100,467,600",
          "body": {
            "id": "https://michelangelo-service.com/image.jpg",
            "type": "Image",
            "service": [...]
          }
        }
      ]
    }]
  }]
}
```

**4. Viewing Experience**
- Load in Mirador 3 for annotation capabilities
- Open in TheseusViewer for deep-zoom inspection of the composited canvas
- Test both from the Validation & Testing tab's "Test viewer compatibility" links
- Export for publication integration

### 2. Conservation Study: Before/After Treatment

**Scenario**: Document conservation treatment with before/after images.

#### Workflow
1. **Main + Derivatives Layout**
   - Main image: Painting before treatment
   - Derivatives: After treatment, X-ray, UV photos

2. **Metadata Structure**
```json
{
  "metadata": [
    {
      "label": {"en": ["Conservation Status"]},
      "value": {"en": ["Before treatment - extensive damage visible"]}
    },
    {
      "label": {"en": ["Treatment Date"]},
      "value": {"en": ["2023-06-15"]}
    },
    {
      "label": {"en": ["Conservator"]},
      "value": {"en": ["Dr. Maria Rossi"]}
    }
  ]
}
```

3. **Layout Positioning**
```javascript
// Main image (before treatment)
{
  "target": "canvas#xywh=100,100,800,600",
  "body": {
    "id": "before-treatment.jpg",
    "service": [{"id": "iiif-service/before"}]
  }
}

// Derivatives (after, x-ray, UV)
{
  "target": "canvas#xywh=100,750,200,150", // After treatment
  "body": {"id": "after-treatment.jpg"}
},
{
  "target": "canvas#xywh=350,750,200,150", // X-ray
  "body": {"id": "xray-image.jpg"}
},
{
  "target": "canvas#xywh=600,750,200,150", // UV
  "body": {"id": "uv-image.jpg"}
}
```

## Manuscript Studies

### 1. Paleographic Analysis: Script Evolution

**Scenario**: Compare manuscript pages showing evolution of Gothic script.

#### Individual Manifest Example
```json
{
  "@context": ["http://iiif.io/api/presentation/3/context.json"],
  "id": "https://manuscripts.edu/gothic-script-1250.json",
  "type": "Manifest",
  "label": {
    "en": ["Gothic Script Sample, c. 1250"],
    "la": ["Scriptura Gothica, c. MCCL"]
  },
  "summary": {
    "en": ["Page from Book of Hours showing early Gothic script characteristics"]
  },
  "metadata": [
    {
      "label": {"en": ["Scribe"]},
      "value": {"en": ["Anonymous"]}
    },
    {
      "label": {"en": ["Repository"]},
      "value": {"en": ["Biblioteca Vaticana, MS Lat. 1234"]}
    },
    {
      "label": {"en": ["Script Type"]},
      "value": {"en": ["Gothic Textualis"]}
    },
    {
      "label": {"en": ["Date"]},
      "value": {"en": ["c. 1250"]}
    }
  ],
  "behavior": ["paged"],
  "viewingDirection": "left-to-right",
  "items": [...]
}
```

#### Comparison Layout: Storyboard
```json
{
  "items": [{
    "id": "paleographic-comparison/canvas",
    "type": "Canvas",
    "label": {"en": ["Gothic Script Evolution"]},
    "width": 1600,
    "height": 700,
    "items": [{
      "type": "AnnotationPage",
      "items": [
        {
          "target": "canvas#xywh=50,100,300,500",
          "body": {
            "id": "gothic-1250.jpg",
            "service": [{"id": "iiif/gothic-1250"}]
          }
        },
        {
          "target": "canvas#xywh=400,100,300,500",
          "body": {
            "id": "gothic-1300.jpg",
            "service": [{"id": "iiif/gothic-1300"}]
          }
        },
        {
          "target": "canvas#xywh=750,100,300,500",
          "body": {
            "id": "gothic-1350.jpg",
            "service": [{"id": "iiif/gothic-1350"}]
          }
        },
        {
          "target": "canvas#xywh=1100,100,300,500",
          "body": {
            "id": "gothic-1400.jpg",
            "service": [{"id": "iiif/gothic-1400"}]
          }
        }
      ]
    }]
  }]
}
```

### 2. Parallel Text Comparison

**Scenario**: Compare the same text in different manuscript traditions.

#### Multi-Canvas Approach
```json
{
  "items": [
    {
      "id": "canvas/manuscript-a",
      "type": "Canvas",
      "label": {"en": ["Manuscript A - Oxford, Bodleian Library"]},
      "width": 1200,
      "height": 1600,
      "items": [...]
    },
    {
      "id": "canvas/manuscript-b",
      "type": "Canvas",
      "label": {"en": ["Manuscript B - Paris, BnF"]},
      "width": 1200,
      "height": 1600,
      "items": [...]
    },
    {
      "id": "canvas/manuscript-c",
      "type": "Canvas",
      "label": {"en": ["Manuscript C - Vatican Library"]},
      "width": 1200,
      "height": 1600,
      "items": [...]
    }
  ]
}
```

## Digital Humanities Projects

### 1. Archaeological Site Documentation

**Scenario**: Document excavation layers with temporal sequencing.

#### Vertical Stack Layout
```json
{
  "label": {"en": ["Archaeological Stratigraphy - Site XYZ"]},
  "summary": {"en": ["Vertical sequence showing chronological layers"]},
  "items": [{
    "id": "stratigraphy/canvas",
    "type": "Canvas",
    "width": 1000,
    "height": 2000,
    "items": [{
      "type": "AnnotationPage",
      "items": [
        {
          "target": "canvas#xywh=100,100,800,300",
          "body": {
            "id": "layer-1-modern.jpg",
            "service": [{"id": "iiif/layer-1"}]
          }
        },
        {
          "target": "canvas#xywh=100,450,800,300",
          "body": {
            "id": "layer-2-medieval.jpg",
            "service": [{"id": "iiif/layer-2"}]
          }
        },
        {
          "target": "canvas#xywh=100,800,800,300",
          "body": {
            "id": "layer-3-roman.jpg",
            "service": [{"id": "iiif/layer-3"}]
          }
        },
        {
          "target": "canvas#xywh=100,1150,800,300",
          "body": {
            "id": "layer-4-prehistoric.jpg",
            "service": [{"id": "iiif/layer-4"}]
          }
        }
      ]
    }]
  }]
}
```

### 2. Cultural Heritage Exhibition

**Scenario**: Create virtual exhibition with thematic groupings.

#### 2×2 Grid Layout for Overview
```json
{
  "label": {"en": ["Medieval Illuminated Manuscripts"]},
  "summary": {"en": ["Thematic exhibition of illuminated manuscripts"]},
  "items": [{
    "id": "exhibition/overview",
    "type": "Canvas",
    "width": 1600,
    "height": 1200,
    "items": [{
      "type": "AnnotationPage",
      "items": [
        {
          "target": "canvas#xywh=50,50,725,525",
          "body": {"id": "religious-manuscripts.jpg"}
        },
        {
          "target": "canvas#xywh=825,50,725,525",
          "body": {"id": "secular-manuscripts.jpg"}
        },
        {
          "target": "canvas#xywh=50,625,725,525",
          "body": {"id": "scientific-manuscripts.jpg"}
        },
        {
          "target": "canvas#xywh=825,625,725,525",
          "body": {"id": "literary-manuscripts.jpg"}
        }
      ]
    }]
  }]
}
```

## Academic Publishing

### 1. Journal Article with Interactive Figures

**Scenario**: Art history article with comparative analysis.

#### HTML Integration

The Clean Viewer (`minimal_iiif_viewer.html`, in `src/contentstate/`) takes a `?manifest=` parameter for a plain manifest URL like the comparison manifest below. (Use `?content=` instead only when embedding a base64-encoded Content State that highlights a specific canvas region — see the [Content State guide](./contentstate_guide.md).)

```html
<figure>
  <iframe 
    src="https://your-domain.com/minimal_iiif_viewer.html?manifest=https://example.com/comparison-manifest.json"
    width="800" 
    height="600"
    title="Interactive Comparison of Renaissance Paintings">
  </iframe>
  <figcaption>
    Figure 1: Comparative analysis of perspective techniques in Renaissance painting.
    <a href="https://example.com/comparison-manifest.json">View manifest</a>
  </figcaption>
</figure>
```

#### Manifest Structure for Publication
```json
{
  "label": {"en": ["Figure 1: Perspective Techniques Comparison"]},
  "summary": {"en": ["Supporting material for 'Innovation in Renaissance Perspective' by Dr. Smith"]},
  "metadata": [
    {
      "label": {"en": ["Publication"]},
      "value": {"en": ["Journal of Art History, Vol. 45, No. 2"]}
    },
    {
      "label": {"en": ["Author"]},
      "value": {"en": ["Dr. Jane Smith"]}
    },
    {
      "label": {"en": ["DOI"]},
      "value": {"en": ["10.1000/182"]}
    }
  ],
  "rights": "http://creativecommons.org/licenses/by/4.0/",
  "requiredStatement": {
    "label": {"en": ["Attribution"]},
    "value": {"en": ["Images courtesy of respective institutions"]}
  }
}
```

### 2. Digital Edition with Apparatus

**Scenario**: Critical edition with textual variants.

#### Multi-Canvas for Witnesses
```json
{
  "label": {"en": ["Critical Edition - Manuscript Witnesses"]},
  "behavior": ["paged"],
  "items": [
    {
      "id": "witness-a/folio-1r",
      "type": "Canvas",
      "label": {"en": ["Witness A, folio 1r"]},
      "items": [...]
    },
    {
      "id": "witness-a/folio-1v",
      "type": "Canvas",
      "label": {"en": ["Witness A, folio 1v"]},
      "items": [...]
    },
    {
      "id": "witness-b/folio-1r",
      "type": "Canvas",
      "label": {"en": ["Witness B, folio 1r"]},
      "items": [...]
    }
  ]
}
```

## Educational Use Cases

### 1. Art History Survey Course

**Scenario**: Comparative slides for lecture.

#### Horizontal Row (Balanced Heights) Layout
```json
{
  "label": {"en": ["Lecture 5: Gothic vs Renaissance Architecture"]},
  "items": [{
    "id": "lecture-5/comparison",
    "type": "Canvas",
    "width": 1600,
    "height": 800,
    "items": [{
      "type": "AnnotationPage",
      "items": [
        {
          "target": "canvas#xywh=100,100,600,600",
          "body": {
            "id": "gothic-cathedral.jpg",
            "service": [{"id": "iiif/gothic-cathedral"}]
          }
        },
        {
          "target": "canvas#xywh=800,100,600,600",
          "body": {
            "id": "renaissance-palace.jpg",
            "service": [{"id": "iiif/renaissance-palace"}]
          }
        }
      ]
    }]
  }]
}
```

### 2. Student Assignment Platform

**Scenario**: Students compare artworks for analysis assignment.

#### Assignment Structure
```json
{
  "label": {"en": ["Assignment 3: Iconographic Analysis"]},
  "summary": {"en": ["Compare these three depictions of the Annunciation"]},
  "metadata": [
    {
      "label": {"en": ["Course"]},
      "value": {"en": ["ART 101 - Introduction to Art History"]}
    },
    {
      "label": {"en": ["Due Date"]},
      "value": {"en": ["2024-03-15"]}
    },
    {
      "label": {"en": ["Assignment Type"]},
      "value": {"en": ["Comparative Analysis"]}
    }
  ],
  "items": [...]
}
```

---

## See also

- [Generator Guide](./generator_guide.md)
- [Comparison Layout Algorithms](./layout_algorithms.md)
- [IIIF Compliance](./iiif_compliance.md)
- [Content State guide](./contentstate_guide.md)

---

Last updated: 2026-07-30