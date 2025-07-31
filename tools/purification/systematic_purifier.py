#!/usr/bin/env python3
"""
Systematic FSCTF Document Purifier
Applies controlled, reviewable replacements with validation
"""

import re
import json
from typing import Dict, List, Tuple, Optional
from dataclasses import dataclass
from pathlib import Path

@dataclass
class ReplacementRule:
    pattern: str
    replacement: str
    description: str
    category: str
    confidence: float  # 0.0-1.0, how confident we are in this replacement
    requires_review: bool = False

class SystematicPurifier:
    def __init__(self, config_path: str = "purification_config.json"):
        self.config_path = config_path
        self.replacement_rules = self._load_replacement_rules()
        self.changes_log = []
        
    def _load_replacement_rules(self) -> List[ReplacementRule]:
        """Load and compile replacement rules"""
        rules = []
        
        # Core terminology replacements (high confidence)
        core_replacements = {
            r'\bsoul\b(?!\s+(?:space|vector|field))': {
                'replacement': 'identity structure',
                'description': 'Replace spiritual "soul" with mathematical "identity structure"',
                'confidence': 0.9
            },
            r'\bgrace\b(?!\s+(?:operator|field|dynamics))': {
                'replacement': 'genesis',
                'description': 'Replace spiritual "grace" with mathematical "genesis"',
                'confidence': 0.9
            },
            r'\bdevourer\b(?!\s+(?:operator|algebra|field))': {
                'replacement': 'collapse operator',
                'description': 'Replace anthropomorphic "devourer" with mathematical "collapse operator"',
                'confidence': 0.95
            },
            r'\bresurrection\b': {
                'replacement': 'reconstruction',
                'description': 'Replace spiritual "resurrection" with "reconstruction"',
                'confidence': 0.9
            },
            r'\bprayer\b': {
                'replacement': 'collective resonance',
                'description': 'Replace spiritual "prayer" with "collective resonance"',
                'confidence': 0.8
            },
            r'\bsacred\s+space\b': {
                'replacement': 'optimized configuration',
                'description': 'Replace spiritual "sacred space" with "optimized configuration"',
                'confidence': 0.85
            }
        }
        
        for pattern, info in core_replacements.items():
            rules.append(ReplacementRule(
                pattern=pattern,
                replacement=info['replacement'],
                description=info['description'],
                category="core_terminology",
                confidence=info['confidence'],
                requires_review=info['confidence'] < 0.9
            ))
        
        # Grandiose claims (medium confidence, requires review)
        grandiose_replacements = {
            r'\bcomplete\s+derivation\b': {
                'replacement': 'proposed derivation',
                'description': 'Hedge grandiose claim "complete derivation"',
                'confidence': 0.8
            },
            r'\brevolutionary\s+breakthrough\b': {
                'replacement': 'significant theoretical development',
                'description': 'Moderate grandiose claim "revolutionary breakthrough"',
                'confidence': 0.75
            },
            r'\bparadigm\s+shift\b': {
                'replacement': 'theoretical framework',
                'description': 'Moderate claim "paradigm shift"',
                'confidence': 0.7
            },
            r'\bfirst\s+complete\b': {
                'replacement': 'proposed complete',
                'description': 'Add hedging to uniqueness claim',
                'confidence': 0.8
            },
            r'\b(?:99|100)%\s+completeness\b': {
                'replacement': 'extensive development',
                'description': 'Remove false precision in completeness claims',
                'confidence': 0.9
            }
        }
        
        for pattern, info in grandiose_replacements.items():
            rules.append(ReplacementRule(
                pattern=pattern,
                replacement=info['replacement'],
                description=info['description'],
                category="grandiose_claims",
                confidence=info['confidence'],
                requires_review=True
            ))
        
        # Anthropomorphic language (high confidence)
        anthropomorphic_patterns = [
            (r'(\w+)\s+enables\b', r'\1 produces', 'Remove anthropomorphic "enables"'),
            (r'(\w+)\s+chooses\b', r'\1 determines', 'Remove anthropomorphic "chooses"'),
            (r'(\w+)\s+decides\b', r'\1 results in', 'Remove anthropomorphic "decides"'),
            (r'(\w+)\s+consumes\b', r'\1 acts on', 'Remove anthropomorphic "consumes"'),
            (r'(\w+)\s+attacks\b', r'\1 affects', 'Remove anthropomorphic "attacks"'),
        ]
        
        for pattern, replacement, description in anthropomorphic_patterns:
            rules.append(ReplacementRule(
                pattern=pattern,
                replacement=replacement,
                description=description,
                category="anthropomorphic",
                confidence=0.95,
                requires_review=False
            ))
        
        # False precision (high confidence)
        rules.append(ReplacementRule(
            pattern=r'\b(\d+\.\d{4,})\b(?!\s*(?:×|e[+-]?\d+))',
            replacement=r'~\1',
            description='Add approximation symbol to excessive precision',
            category="false_precision",
            confidence=0.9,
            requires_review=False
        ))
        
        # Mystical terms (medium confidence)
        mystical_replacements = {
            r'\bex\s+nihilo\b': {
                'replacement': 'from minimal initial conditions',
                'description': 'Replace mystical "ex nihilo"',
                'confidence': 0.8
            },
            r'\bacausal\b': {
                'replacement': 'non-locally determined',
                'description': 'Replace mystical "acausal"',
                'confidence': 0.75
            },
            r'\bmorphic\s+fields?\b(?!\s+(?:mathematics|algebra|equation))': {
                'replacement': 'recursive structure fields',
                'description': 'Clarify vague "morphic fields"',
                'confidence': 0.7
            }
        }
        
        for pattern, info in mystical_replacements.items():
            rules.append(ReplacementRule(
                pattern=pattern,
                replacement=info['replacement'],
                description=info['description'],
                category="mystical_terms",
                confidence=info['confidence'],
                requires_review=True
            ))
        
        return rules
    
    def preview_replacements(self, text: str, category: Optional[str] = None) -> List[Dict]:
        """Preview what replacements would be made without applying them"""
        previews = []
        
        for rule in self.replacement_rules:
            if category and rule.category != category:
                continue
                
            matches = list(re.finditer(rule.pattern, text, re.IGNORECASE))
            for match in matches:
                # Get context
                start, end = max(0, match.start() - 50), min(len(text), match.end() + 50)
                context = text[start:end]
                
                previews.append({
                    'rule_description': rule.description,
                    'category': rule.category,
                    'confidence': rule.confidence,
                    'requires_review': rule.requires_review,
                    'original': match.group(),
                    'replacement': re.sub(rule.pattern, rule.replacement, match.group(), flags=re.IGNORECASE),
                    'context': context,
                    'position': match.start(),
                    'line_number': text[:match.start()].count('\n') + 1
                })
        
        return sorted(previews, key=lambda x: x['position'])
    
    def apply_replacements(self, text: str, category: Optional[str] = None, min_confidence: float = 0.8) -> Tuple[str, List[Dict]]:
        """Apply replacements with specified confidence threshold"""
        modified_text = text
        changes_made = []
        
        for rule in self.replacement_rules:
            if category and rule.category != category:
                continue
            if rule.confidence < min_confidence:
                continue
                
            original_text = modified_text
            modified_text = re.sub(rule.pattern, rule.replacement, modified_text, flags=re.IGNORECASE)
            
            # Count changes
            original_matches = len(re.findall(rule.pattern, original_text, re.IGNORECASE))
            remaining_matches = len(re.findall(rule.pattern, modified_text, re.IGNORECASE))
            changes_count = original_matches - remaining_matches
            
            if changes_count > 0:
                changes_made.append({
                    'rule': rule.description,
                    'category': rule.category,
                    'confidence': rule.confidence,
                    'changes_count': changes_count,
                    'pattern': rule.pattern,
                    'replacement': rule.replacement
                })
        
        return modified_text, changes_made
    
    def add_scientific_hedging(self, text: str) -> str:
        """Add appropriate scientific hedging to claims"""
        hedging_patterns = [
            # Strong claims → hedged claims
            (r'\b(This proves|This demonstrates|This shows)\b', r'This suggests'),
            (r'\b(We prove|We demonstrate|We show)\b', r'We propose'),
            (r'\b(It is clear that|Obviously|Clearly)\b', r'Evidence suggests that'),
            (r'\b(must be|will be|cannot be)\b', r'appears to be'),
            (r'\b(always|never|all|none)\b(?=\s+(?:systems?|theories?|models?))', r'typically'),
        ]
        
        modified_text = text
        for pattern, replacement in hedging_patterns:
            modified_text = re.sub(pattern, replacement, modified_text, flags=re.IGNORECASE)
        
        return modified_text
    
    def add_domain_tags(self, text: str) -> str:
        """Add appropriate domain tags to sections"""
        # This is a simplified version - in practice, this would be more sophisticated
        sections = text.split('\n## ')
        tagged_sections = []
        
        for section in sections:
            if 'equation' in section.lower() or 'theorem' in section.lower():
                section = '[MATHEMATICAL] ' + section
            elif 'consciousness' in section.lower() or 'soul' in section.lower():
                section = '[SPECULATIVE] ' + section
            elif 'prediction' in section.lower() or 'experimental' in section.lower():
                section = '[EMPIRICAL] ' + section
            
            tagged_sections.append(section)
        
        return '\n## '.join(tagged_sections)
    
    def generate_purification_report(self, original_text: str, purified_text: str) -> Dict:
        """Generate comprehensive report of purification changes"""
        report = {
            'summary': {
                'original_length': len(original_text),
                'purified_length': len(purified_text),
                'total_changes': len(self.changes_log),
                'changes_by_category': {}
            },
            'changes_detail': self.changes_log,
            'quality_metrics': self._calculate_quality_metrics(purified_text)
        }
        
        # Count changes by category
        for change in self.changes_log:
            category = change.get('category', 'unknown')
            if category not in report['summary']['changes_by_category']:
                report['summary']['changes_by_category'][category] = 0
            report['summary']['changes_by_category'][category] += change.get('changes_count', 1)
        
        return report
    
    def _calculate_quality_metrics(self, text: str) -> Dict:
        """Calculate quality metrics for purified text"""
        words = text.split()
        word_count = len(words)
        
        # Count remaining problematic terms
        spiritual_terms = len(re.findall(r'\b(?:soul|grace|devourer|resurrection|prayer|sacred|spiritual|divine)\b', text, re.IGNORECASE))
        grandiose_claims = len(re.findall(r'\b(?:complete|perfect|ultimate|absolute|revolutionary)\s+(?:solution|breakthrough|derivation)\b', text, re.IGNORECASE))
        anthropomorphic = len(re.findall(r'\b\w+\s+(?:enables|chooses|decides|wants|consumes|attacks)\b', text, re.IGNORECASE))
        
        # Count scientific terms
        scientific_terms = len(re.findall(r'\b(?:theorem|hypothesis|empirical|systematic|quantitative|measurement|analysis|validation)\b', text, re.IGNORECASE))
        
        return {
            'spiritual_density': (spiritual_terms / word_count) * 1000 if word_count > 0 else 0,
            'grandiose_density': (grandiose_claims / word_count) * 1000 if word_count > 0 else 0,
            'anthropomorphic_density': (anthropomorphic / word_count) * 1000 if word_count > 0 else 0,
            'scientific_density': (scientific_terms / word_count) * 1000 if word_count > 0 else 0,
            'quality_score': max(0, 100 - spiritual_terms - grandiose_claims*2 - anthropomorphic*3 + scientific_terms)
        }

def main():
    """Interactive purification workflow"""
    purifier = SystematicPurifier()
    
    print("🧹 FSCTF Systematic Document Purifier")
    print("=" * 50)
    
    # Load document
    with open('FSCTF_Formal.md', 'r', encoding='utf-8') as f:
        original_text = f.read()
    
    print(f"📄 Loaded document: {len(original_text):,} characters")
    
    # Preview high-confidence replacements
    print("\n🔍 Previewing high-confidence replacements...")
    all_previews = purifier.preview_replacements(original_text)
    high_confidence_previews = [p for p in all_previews if p['confidence'] >= 0.9]
    
    print(f"Found {len(high_confidence_previews)} high-confidence replacements:")
    for i, preview in enumerate(high_confidence_previews[:10], 1):
        print(f"  {i}. Line {preview['line_number']}: '{preview['original']}' → '{preview['replacement']}'")
        print(f"     Category: {preview['category']} | Confidence: {preview['confidence']:.1%}")
    
    if len(high_confidence_previews) > 10:
        print(f"     ... and {len(high_confidence_previews) - 10} more")
    
    # Apply high-confidence replacements
    print(f"\n⚡ Applying high-confidence replacements (≥90% confidence)...")
    purified_text, changes = purifier.apply_replacements(original_text, min_confidence=0.9)
    purifier.changes_log.extend(changes)
    
    print(f"Applied {len(changes)} high-confidence changes:")
    for change in changes:
        print(f"  • {change['rule']}: {change['changes_count']} instances")
    
    # Add scientific hedging
    print(f"\n🎯 Adding scientific hedging...")
    purified_text = purifier.add_scientific_hedging(purified_text)
    
    # Generate quality report
    print(f"\n📊 Generating quality metrics...")
    report = purifier.generate_purification_report(original_text, purified_text)
    
    print(f"\nQUALITY METRICS:")
    metrics = report['quality_metrics']
    print(f"  Spiritual term density: {metrics['spiritual_density']:.1f} per 1000 words")
    print(f"  Grandiose claim density: {metrics['grandiose_density']:.1f} per 1000 words")
    print(f"  Anthropomorphic density: {metrics['anthropomorphic_density']:.1f} per 1000 words")
    print(f"  Scientific term density: {metrics['scientific_density']:.1f} per 1000 words")
    print(f"  Overall quality score: {metrics['quality_score']:.1f}/100")
    
    # Save results
    output_path = 'FSCTF_Formal_PURIFIED.md'
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(purified_text)
    
    report_path = 'purification_report.json'
    with open(report_path, 'w') as f:
        json.dump(report, f, indent=2)
    
    print(f"\n💾 Results saved:")
    print(f"  Purified document: {output_path}")
    print(f"  Detailed report: {report_path}")
    
    print(f"\n✅ Purification complete! Quality improvement: {metrics['quality_score']:.1f}%")

if __name__ == "__main__":
    main()