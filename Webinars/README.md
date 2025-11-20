# Webinars

This directory contains all webinar scripts, slide decks, and evaluation reports for the **Active Offer** sales webinar.

## Directory Structure

```
Webinars/
├── Current/              # Active webinar version
├── Archive/              # Historical versions
│   ├── v1/
│   ├── v2.1/
│   ├── v2.2/
│   ├── v3.0/
│   ├── v4.0/
│   └── v4.1/
└── Evaluations/          # Performance analysis reports
```

## Current Version

**Location**: `Current/`

The current production webinar version includes:
- **Script**: Markdown file with slide-by-slide talking points
- **Slides**: PNG slide deck directory

## Webinar Evolution

### Version History

- **v1**: Initial complete talking points
- **v2.1**: Multiple iterations with enhanced future pacing
- **v2.2**: Enhanced future pacing refinement
- **v3.0**: Positioning principle framework
- **v4.0**: Russell Brunson's "Perfect Webinar" Three Secrets Framework
- **v4.1**: Bold promise enhancement
- **v4.2**: Optimized version (current)

### Framework: Three Secrets Structure

Current webinars use Russell Brunson's proven framework:
1. **Origin Story**: Establish authority and relatability
2. **Secret #1**: Internal belief shift (Vehicle)
3. **Secret #2**: External methodology (Internal Beliefs)
4. **Secret #3**: Implementation framework (External Beliefs)
5. **Stack & Close**: Value demonstration and offer

## Evaluation Reports

**Location**: `Evaluations/`

Performance analysis tracking:
- Conversion metrics
- Engagement data
- A/B test results
- Optimization recommendations

See individual evaluation reports for detailed analytics.

## Generating Webinar Slides

Use the slide generation script:

```bash
source .venv/bin/activate
python3 Scripts/generate_webinar_slides.py
```

Output location: `Current/` or version-specific archive directory

## Naming Conventions

**Scripts**: `Webinar-Script-v[X.Y]-[Description].md`
**Slide Directories**: `Webinar-v[X.Y]-Slides-[Description]/`
**Evaluations**: `Webinar-Evaluation-Report-v[X.Y].md`

## Working with Webinar Content

### Creating New Version

1. Copy current version to `Archive/v[X.Y]/`
2. Update script in `Current/`
3. Regenerate slides using generation script
4. Document changes in version history above
5. Create evaluation report after testing

### Best Practices

- Never overwrite production versions - always create new versions
- Document rationale for major changes
- Track performance metrics for each iteration
- Archive old slide directories with clear version labels
