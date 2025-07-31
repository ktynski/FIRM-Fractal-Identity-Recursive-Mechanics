# FSCTF Language Purification System

## Overview

This system provides automated tools to systematically identify and replace language that could be perceived as "pseudoscientific" or "woo" in the FSCTF document. The goal is to maintain the mathematical rigor while replacing problematic terminology with more scientifically acceptable language.

## System Components

### 1. Core Analysis Tools

- **`language_purification_engine.py`** - Basic pattern detection and replacement engine
- **`advanced_analysis.py`** - Detailed section-by-section analysis with metrics
- **`systematic_purifier.py`** - Controlled replacement system with confidence scoring
- **`purification_config.json`** - Configuration for all replacement rules and patterns

### 2. Workflow Management

- **`run_purification.py`** - Orchestrates the complete purification workflow
- **`README_Purification.md`** - This documentation file

## Quick Start

1. **Ensure Prerequisites**:
   ```bash
   # Make sure you have Python 3.7+ and navigate to tools
   python --version
   cd tools/purification/
   ls ../../FSCTF_Formal.md
   ```

2. **Run Complete Purification Workflow**:
   ```bash
   python run_purification.py
   ```

3. **Review Results**:
   - `FSCTF_Formal_PURIFIED.md` - The cleaned document
   - `fsctf_analysis_results.json` - Detailed analysis
   - `purification_report.json` - Summary of changes made

## Detailed Usage

### Individual Tool Usage

#### Advanced Analysis
```bash
python advanced_analysis.py
```
Generates comprehensive analysis including:
- Section-by-section metrics
- Spiritual terminology density
- Grandiose claims count
- Scientific rigor scoring
- Prioritized action plan

#### Systematic Purification
```bash
python systematic_purifier.py
```
Applies controlled replacements with:
- Confidence-based filtering
- Review requirements for uncertain changes
- Quality metrics before/after
- Detailed change logging

#### Basic Pattern Detection
```bash
python language_purification_engine.py
```
Simple find-and-replace with pattern matching.

### Configuration

Edit `purification_config.json` to customize:

```json
{
  "replacement_rules": {
    "core_terminology": {
      "soul": {
        "replacements": ["identity structure", "recursive identity"],
        "context_dependent": {
          "soul vector": "identity vector"
        }
      }
    }
  }
}
```

## Problem Categories Addressed

### 1. Spiritual/Religious Terminology (Severity: 4/5)
- **Examples**: "soul", "grace", "resurrection", "prayer", "sacred"
- **Replacements**: "identity structure", "genesis operator", "reconstruction", "collective resonance", "optimized configuration"

### 2. Anthropomorphic Mathematical Objects (Severity: 5/5)
- **Examples**: "grace enables", "devourer consumes", "consciousness chooses"
- **Replacements**: "genesis operator produces", "collapse operator acts on", "system evolves toward"

### 3. Grandiose Claims (Severity: 3/5)
- **Examples**: "complete derivation", "revolutionary breakthrough", "99% completeness"
- **Replacements**: "proposed derivation", "novel theoretical framework", "extensive development"

### 4. Mystical/Esoteric References (Severity: 3/5)
- **Examples**: "ex nihilo", "acausal", "morphic fields", "Tree of Life"
- **Replacements**: "from minimal conditions", "non-locally determined", "recursive structure fields", "[removed or contextualized]"

### 5. False Precision (Severity: 2/5)
- **Examples**: "0.0009766", "99.87% retention", "73.2% success rate"
- **Replacements**: "~0.001", "~99% retention", "~73% success rate"

### 6. Vague Technical Jargon (Severity: 3/5)
- **Examples**: Undefined "morphic", "coherence", "φ-harmonic"
- **Solution**: Add precise mathematical definitions

### 7. Category Confusion (Severity: 4/5)
- **Examples**: Treating mathematical abstractions as physical reality
- **Solution**: Add domain tags [MATHEMATICAL], [SPECULATIVE], [EMPIRICAL]

### 8. False Rigor (Severity: 5/5)
- **Examples**: Claims of "proof" without mathematical rigor
- **Solution**: Replace with "proposes", "suggests", "indicates"

## Quality Metrics

The system tracks several quality metrics:

- **Spiritual Density**: Spiritual terms per 1000 words (target: <2)
- **Grandiose Density**: Grandiose claims per 1000 words (target: <1)
- **Anthropomorphic Density**: Anthropomorphic phrases per 1000 words (target: <0.5)
- **Scientific Density**: Scientific terms per 1000 words (target: >20)
- **Overall Quality Score**: Composite score (target: >80/100)

## Output Files

### `FSCTF_Formal_PURIFIED.md`
The main output - the purified version of the document with problematic language replaced.

### `fsctf_analysis_results.json`
Detailed analysis including:
```json
{
  "overall_metrics": {
    "total_issues": 1247,
    "critical_issues": 89,
    "scientific_rigor_score": 0.156
  },
  "section_analysis": { ... },
  "prioritized_action_plan": { ... }
}
```

### `purification_report.json`
Summary of changes made:
```json
{
  "summary": {
    "total_changes": 342,
    "changes_by_category": {
      "core_terminology": 156,
      "grandiose_claims": 89,
      "anthropomorphic": 97
    }
  },
  "quality_metrics": { ... }
}
```

## Confidence Levels

The system uses confidence levels for replacements:

- **0.9-1.0**: High confidence - Applied automatically
- **0.8-0.9**: Medium confidence - Applied with logging
- **0.7-0.8**: Low confidence - Requires manual review
- **<0.7**: Very low confidence - Flagged only, not applied

## Manual Review Required

Some changes require manual review:

1. **Context-dependent terms** - Where replacement depends on specific meaning
2. **Technical definitions** - Terms that need mathematical precision
3. **Core concepts** - Fundamental ideas that need careful rephrasing
4. **Low confidence replacements** - Automated system isn't sure

## Validation

After purification, validate that:

1. **Mathematical content is preserved** - All equations and derivations remain valid
2. **Logical flow is maintained** - Arguments still follow logically
3. **Technical precision is improved** - Terminology is more precise
4. **Readability is maintained** - Document is still comprehensible

## Customization

### Adding New Patterns
Edit `purification_config.json` to add new problematic patterns:

```json
{
  "replacement_rules": {
    "new_category": {
      "pattern": "\\bmystical_term\\b",
      "replacement": "scientific_term",
      "confidence": 0.8
    }
  }
}
```

### Adjusting Severity
Modify the severity levels in the Python files to change how aggressively the system flags issues.

### Custom Replacements
Add domain-specific replacements for your use case.

## Best Practices

1. **Run analysis first** - Always start with `advanced_analysis.py`
2. **Review high-severity issues** - Focus on anthropomorphic and false rigor issues
3. **Validate mathematics** - Ensure no mathematical content is corrupted
4. **Iterative improvement** - Run multiple passes for complex documents
5. **Manual verification** - Always manually review critical sections

## Troubleshooting

### Common Issues

1. **"Pattern not found"** - Check regex syntax in config file
2. **"Changes not applied"** - Check confidence thresholds
3. **"Mathematical errors"** - Restore from backup and adjust rules
4. **"Output too aggressive"** - Lower confidence thresholds

### Recovery

If the automated system makes inappropriate changes:

1. Restore original document
2. Adjust configuration
3. Run with higher confidence thresholds
4. Review specific problematic patterns

## Contributing

To improve the purification system:

1. Add new problematic patterns you identify
2. Improve replacement suggestions
3. Enhance quality metrics
4. Add domain-specific configurations

## Support

For issues with the purification system:

1. Check the generated log files
2. Review the confidence scores
3. Manually validate mathematical content
4. Adjust configuration as needed

---

**Remember**: This system is a tool to assist in language purification, not a replacement for careful human review. Always validate that the mathematical and logical content remains intact after purification.