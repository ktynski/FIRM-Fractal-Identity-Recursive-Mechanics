#!/usr/bin/env python3
"""
FSCTF Language Purification Engine
Systematically identifies and replaces pseudoscientific language patterns
"""

import re
import json
from typing import Dict, List, Tuple, Set
from dataclasses import dataclass
from enum import Enum

class ProblemCategory(Enum):
    SPIRITUAL_RELIGIOUS = "spiritual_religious"
    ANTHROPOMORPHIC = "anthropomorphic" 
    GRANDIOSE_CLAIMS = "grandiose_claims"
    MYSTICAL_ESOTERIC = "mystical_esoteric"
    FALSE_PRECISION = "false_precision"
    VAGUE_JARGON = "vague_jargon"
    CATEGORY_CONFUSION = "category_confusion"
    FALSE_RIGOR = "false_rigor"

@dataclass
class LanguagePattern:
    pattern: str  # regex pattern
    category: ProblemCategory
    context_required: List[str]  # words that must appear nearby
    exceptions: List[str]  # contexts where this pattern is acceptable
    severity: int  # 1-5, how problematic this is

@dataclass
class Replacement:
    original: str
    replacement: str
    explanation: str
    preserve_meaning: bool

class FSCTFLanguagePurifier:
    def __init__(self):
        self.problematic_patterns = self._initialize_patterns()
        self.replacement_mappings = self._initialize_replacements()
        self.domain_tags = ["[MATHEMATICAL]", "[HYPOTHETICAL]", "[SPECULATIVE]", "[EMPIRICAL]"]
        
    def _initialize_patterns(self) -> List[LanguagePattern]:
        """Define all problematic language patterns"""
        patterns = []
        
        # Category 1: Spiritual/Religious Terms
        spiritual_terms = [
            r'\bsoul\b(?!.*space|.*vector)',  # soul but not "soul space" or "soul vector"
            r'\bgrace\b(?!.*operator|.*field)',  # grace but not "grace operator"
            r'\bresurrection\b',
            r'\bprayer\b',
            r'\bsacred\s+space\b',
            r'\bforgiveness\b',
            r'\beternal\s+rebirth\b',
            r'\bspiritual\b',
            r'\bdivine\b',
            r'\bmiracle\b(?!.*theorem)',
        ]
        
        for term in spiritual_terms:
            patterns.append(LanguagePattern(
                pattern=term,
                category=ProblemCategory.SPIRITUAL_RELIGIOUS,
                context_required=[],
                exceptions=["mathematical", "abstract", "formal"],
                severity=4
            ))
            
        # Category 2: Anthropomorphic Mathematical Objects
        anthropomorphic_patterns = [
            r'grace\s+(enables|chooses|decides|wants|intends)',
            r'devourer\s+(consumes|attacks|chooses|hunts)',
            r'consciousness\s+(decides|chooses|selects)',
            r'operator\s+(enables|wants|decides)',
            r'field\s+(chooses|decides|wants)',
        ]
        
        for pattern in anthropomorphic_patterns:
            patterns.append(LanguagePattern(
                pattern=pattern,
                category=ProblemCategory.ANTHROPOMORPHIC,
                context_required=[],
                exceptions=[],
                severity=5
            ))
            
        # Category 3: Grandiose Claims
        grandiose_patterns = [
            r'\b(?:complete|total|perfect|ultimate|absolute)\s+(?:derivation|solution|breakthrough)\b',
            r'\b(?:99|100)%\s+(?:completeness|success|accuracy)\b',
            r'\bfirst\s+(?:complete|total)\s+emergence\b',
            r'\brevolutionary\s+breakthrough\b',
            r'\bparadigm\s+shift\b',
            r'\bfundamental\s+breakthrough\b',
        ]
        
        for pattern in grandiose_patterns:
            patterns.append(LanguagePattern(
                pattern=pattern,
                category=ProblemCategory.GRANDIOSE_CLAIMS,
                context_required=[],
                exceptions=["proposed", "hypothetical", "if confirmed"],
                severity=4
            ))
            
        # Category 4: Mystical/Esoteric References
        mystical_patterns = [
            r'\bex\s+nihilo\b',
            r'\bmorphic\s+fields?\b(?!.*mathematics|.*algebra)',
            r'\bacausal\b',
            r'\bTree\s+of\s+Life\b',
            r'\bI\s+Ching\b',
            r'\bmythic\s+validation\b',
            r'\bkabbalah\b',
            r'\besoteric\b',
        ]
        
        for pattern in mystical_patterns:
            patterns.append(LanguagePattern(
                pattern=pattern,
                category=ProblemCategory.MYSTICAL_ESOTERIC,
                context_required=[],
                exceptions=["analogy", "metaphor", "comparison"],
                severity=3
            ))
            
        # Category 5: False Precision
        false_precision_patterns = [
            r'\b\d+\.\d{4,}\b(?!\s*(?:×|×10|e[+-]?\d+))',  # Many decimal places without scientific notation
            r'\b(?:99|100)\.(?:\d+)%\b',  # Overly precise percentages
            r'\b\d+\.\d+%\s+(?:success|accuracy|retention)\b',
        ]
        
        for pattern in false_precision_patterns:
            patterns.append(LanguagePattern(
                pattern=pattern,
                category=ProblemCategory.FALSE_PRECISION,
                context_required=[],
                exceptions=["fundamental constant", "mathematical constant"],
                severity=3
            ))
            
        return patterns
    
    def _initialize_replacements(self) -> Dict[str, Replacement]:
        """Define replacement mappings for problematic terms"""
        return {
            # Spiritual/Religious → Abstract Mathematical
            "soul": Replacement(
                "identity structure", 
                "Recursive identity structure in morphic space",
                True
            ),
            "grace": Replacement(
                "genesis operator", 
                "Mathematical operator for structure initiation",
                True
            ),
            "devourer": Replacement(
                "collapse operator",
                "Mathematical operator for coherence dissolution", 
                True
            ),
            "resurrection": Replacement(
                "reconstruction",
                "Mathematical reconstruction of identity structures",
                True
            ),
            "prayer": Replacement(
                "collective resonance",
                "Coordinated resonance between identity structures",
                True
            ),
            "sacred space": Replacement(
                "optimized field configuration",
                "Mathematically optimized field configuration",
                True
            ),
            
            # Grandiose Claims → Appropriately Hedged
            "complete derivation": Replacement(
                "proposed derivation",
                "Adds appropriate uncertainty",
                True
            ),
            "revolutionary breakthrough": Replacement(
                "novel theoretical framework",
                "More modest, accurate description",
                True
            ),
            "99% completeness": Replacement(
                "extensive theoretical development",
                "Removes false precision",
                True
            ),
            "first complete emergence": Replacement(
                "proposed emergence mechanism",
                "Removes grandiose uniqueness claims",
                True
            ),
            
            # Mystical → Mathematical
            "ex nihilo": Replacement(
                "from minimal initial conditions",
                "More precise mathematical description",
                True
            ),
            "acausal": Replacement(
                "non-locally determined",
                "More precise physical description", 
                True
            ),
            "morphic fields": Replacement(
                "recursive structure fields",
                "More precise mathematical terminology",
                True
            ),
            
            # Anthropomorphic → Mechanistic
            "grace enables": Replacement(
                "the genesis operator produces",
                "Removes anthropomorphic agency",
                True
            ),
            "devourer consumes": Replacement(
                "the collapse operator acts on",
                "Mechanistic description",
                True
            ),
            "consciousness chooses": Replacement(
                "the system evolves toward",
                "Removes implied agency",
                True
            ),
        }
    
    def scan_document(self, text: str) -> Dict[ProblemCategory, List[Tuple[str, int, int]]]:
        """Scan document and return all problematic patterns found"""
        findings = {category: [] for category in ProblemCategory}
        
        for pattern_obj in self.problematic_patterns:
            matches = re.finditer(pattern_obj.pattern, text, re.IGNORECASE)
            for match in matches:
                # Check for exceptions in context
                start, end = max(0, match.start() - 100), min(len(text), match.end() + 100)
                context = text[start:end].lower()
                
                is_exception = any(exc in context for exc in pattern_obj.exceptions)
                if not is_exception:
                    findings[pattern_obj.category].append((
                        match.group(),
                        match.start(),
                        match.end()
                    ))
        
        return findings
    
    def generate_purification_report(self, text: str) -> Dict:
        """Generate comprehensive report of issues found"""
        findings = self.scan_document(text)
        
        report = {
            "total_issues": sum(len(issues) for issues in findings.values()),
            "issues_by_category": {},
            "severity_breakdown": {1: 0, 2: 0, 3: 0, 4: 0, 5: 0},
            "recommendations": []
        }
        
        for category, issues in findings.items():
            if issues:
                report["issues_by_category"][category.value] = {
                    "count": len(issues),
                    "examples": issues[:5],  # First 5 examples
                }
                
        return report
    
    def apply_replacements(self, text: str, category_filter: Set[ProblemCategory] = None) -> Tuple[str, List[str]]:
        """Apply systematic replacements to text"""
        if category_filter is None:
            category_filter = set(ProblemCategory)
            
        modified_text = text
        changes_made = []
        
        for original, replacement in self.replacement_mappings.items():
            if replacement.preserve_meaning:
                # Use word boundaries to avoid partial replacements
                pattern = r'\b' + re.escape(original) + r'\b'
                matches = list(re.finditer(pattern, modified_text, re.IGNORECASE))
                
                if matches:
                    modified_text = re.sub(pattern, replacement.replacement, modified_text, flags=re.IGNORECASE)
                    changes_made.append(f"Replaced '{original}' → '{replacement.replacement}' ({len(matches)} instances)")
        
        return modified_text, changes_made

def main():
    """Main execution function"""
    purifier = FSCTFLanguagePurifier()
    
    # Read the FSCTF document
    with open('FSCTF_Formal.md', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Generate initial report
    print("Scanning FSCTF document for problematic language patterns...")
    report = purifier.generate_purification_report(content)
    
    print(f"\nFOUND {report['total_issues']} TOTAL ISSUES")
    print("\nIssues by category:")
    for category, details in report["issues_by_category"].items():
        print(f"  {category}: {details['count']} instances")
        for example in details['examples'][:3]:
            print(f"    - '{example[0]}'")
    
    # Apply purification
    print("\nApplying systematic language purification...")
    purified_content, changes = purifier.apply_replacements(content)
    
    print(f"\nCHANGES MADE:")
    for change in changes:
        print(f"  - {change}")
    
    # Save purified version
    with open('FSCTF_Formal_PURIFIED.md', 'w', encoding='utf-8') as f:
        f.write(purified_content)
    
    print(f"\nPurified document saved as: FSCTF_Formal_PURIFIED.md")
    
    # Generate final report
    final_report = purifier.generate_purification_report(purified_content)
    print(f"Remaining issues: {final_report['total_issues']}")

if __name__ == "__main__":
    main()