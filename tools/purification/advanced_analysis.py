#!/usr/bin/env python3
"""
Advanced FSCTF Language Analysis Tool
Provides detailed section-by-section analysis and specific recommendations
"""

import re
import json
from collections import defaultdict
from typing import Dict, List, Tuple, NamedTuple
from dataclasses import dataclass

class AnalysisResult(NamedTuple):
    section: str
    line_number: int
    issue_type: str
    problematic_text: str
    severity: int
    suggestion: str
    context: str

@dataclass
class SectionMetrics:
    spiritual_density: float  # spiritual terms per 100 words
    grandiose_claims: int
    false_precision_instances: int
    anthropomorphic_instances: int
    scientific_rigor_score: float  # 0-1, higher is better

class AdvancedFSCTFAnalyzer:
    def __init__(self, config_path: str = "purification_config.json"):
        with open(config_path, 'r') as f:
            self.config = json.load(f)
        
        self.problematic_patterns = self._compile_patterns()
        self.scientific_terms = self._load_scientific_vocabulary()
        
    def _compile_patterns(self) -> Dict[str, List[re.Pattern]]:
        """Compile all regex patterns from config"""
        patterns = {
            'spiritual': [
                re.compile(r'\b(?:soul|grace|devourer|resurrection|prayer|sacred|spiritual|divine|miracle)\b', re.IGNORECASE),
                re.compile(r'\b(?:eternal|transcendent|mystical|esoteric)\b', re.IGNORECASE)
            ],
            'grandiose': [
                re.compile(r'\b(?:complete|perfect|ultimate|absolute|revolutionary|paradigm-shifting)\s+(?:solution|breakthrough|derivation)\b', re.IGNORECASE),
                re.compile(r'\b(?:99|100)\.?\d*%\s+(?:completeness|success|accuracy)\b', re.IGNORECASE)
            ],
            'anthropomorphic': [
                re.compile(r'\b\w+\s+(?:enables|chooses|decides|wants|intends|consumes|attacks|hunts)\b', re.IGNORECASE)
            ],
            'false_precision': [
                re.compile(r'\b\d+\.\d{4,}\b(?!\s*(?:×|e[+-]?\d+))', re.IGNORECASE),
                re.compile(r'\b(?:99|100)\.\d+%\b', re.IGNORECASE)
            ],
            'mystical': [
                re.compile(r'\b(?:ex nihilo|acausal|morphic fields|Tree of Life|I Ching|kabbalah)\b', re.IGNORECASE)
            ]
        }
        return patterns
    
    def _load_scientific_vocabulary(self) -> set:
        """Load scientific terminology for rigor scoring"""
        return {
            'theorem', 'proof', 'axiom', 'hypothesis', 'empirical', 'experimental',
            'statistical', 'quantitative', 'measurement', 'observation', 'data',
            'analysis', 'methodology', 'systematic', 'rigorous', 'validation',
            'falsifiable', 'testable', 'reproducible', 'peer-reviewed'
        }
    
    def extract_sections(self, text: str) -> Dict[str, Tuple[str, int]]:
        """Extract document sections with their content and line numbers"""
        sections = {}
        current_section = "Introduction"
        current_content = []
        line_num = 0
        
        for line in text.split('\n'):
            line_num += 1
            
            # Check for new section headers
            if re.match(r'^#+\s+(.+)', line):
                # Save previous section
                if current_content:
                    sections[current_section] = ('\n'.join(current_content), line_num - len(current_content))
                
                # Start new section
                current_section = re.match(r'^#+\s+(.+)', line).group(1)
                current_content = []
            else:
                current_content.append(line)
        
        # Save final section
        if current_content:
            sections[current_section] = ('\n'.join(current_content), line_num - len(current_content))
        
        return sections
    
    def analyze_section(self, section_name: str, content: str, start_line: int) -> Tuple[SectionMetrics, List[AnalysisResult]]:
        """Perform detailed analysis of a single section"""
        words = content.split()
        word_count = len(words)
        
        issues = []
        
        # Count spiritual terms
        spiritual_count = 0
        for pattern in self.problematic_patterns['spiritual']:
            matches = list(pattern.finditer(content))
            spiritual_count += len(matches)
            for match in matches:
                line_offset = content[:match.start()].count('\n')
                issues.append(AnalysisResult(
                    section=section_name,
                    line_number=start_line + line_offset,
                    issue_type="spiritual_terminology",
                    problematic_text=match.group(),
                    severity=4,
                    suggestion=f"Replace '{match.group()}' with mathematical terminology",
                    context=self._get_context(content, match.start(), match.end())
                ))
        
        # Count grandiose claims
        grandiose_count = 0
        for pattern in self.problematic_patterns['grandiose']:
            matches = list(pattern.finditer(content))
            grandiose_count += len(matches)
            for match in matches:
                line_offset = content[:match.start()].count('\n')
                issues.append(AnalysisResult(
                    section=section_name,
                    line_number=start_line + line_offset,
                    issue_type="grandiose_claim",
                    problematic_text=match.group(),
                    severity=3,
                    suggestion=f"Add appropriate hedging: 'proposed {match.group().lower()}'",
                    context=self._get_context(content, match.start(), match.end())
                ))
        
        # Count false precision
        false_precision_count = 0
        for pattern in self.problematic_patterns['false_precision']:
            matches = list(pattern.finditer(content))
            false_precision_count += len(matches)
            for match in matches:
                line_offset = content[:match.start()].count('\n')
                issues.append(AnalysisResult(
                    section=section_name,
                    line_number=start_line + line_offset,
                    issue_type="false_precision",
                    problematic_text=match.group(),
                    severity=2,
                    suggestion=f"Replace with appropriate uncertainty: '~{match.group()}'",
                    context=self._get_context(content, match.start(), match.end())
                ))
        
        # Count anthropomorphic language
        anthropomorphic_count = 0
        for pattern in self.problematic_patterns['anthropomorphic']:
            matches = list(pattern.finditer(content))
            anthropomorphic_count += len(matches)
            for match in matches:
                line_offset = content[:match.start()].count('\n')
                issues.append(AnalysisResult(
                    section=section_name,
                    line_number=start_line + line_offset,
                    issue_type="anthropomorphic",
                    problematic_text=match.group(),
                    severity=5,
                    suggestion="Remove anthropomorphic agency from mathematical objects",
                    context=self._get_context(content, match.start(), match.end())
                ))
        
        # Calculate scientific rigor score
        scientific_words = sum(1 for word in words if word.lower() in self.scientific_terms)
        rigor_score = scientific_words / max(word_count, 1) if word_count > 0 else 0
        
        # Calculate metrics
        metrics = SectionMetrics(
            spiritual_density=(spiritual_count / max(word_count, 1)) * 100,
            grandiose_claims=grandiose_count,
            false_precision_instances=false_precision_count,
            anthropomorphic_instances=anthropomorphic_count,
            scientific_rigor_score=rigor_score
        )
        
        return metrics, issues
    
    def _get_context(self, text: str, start: int, end: int, context_size: int = 50) -> str:
        """Get surrounding context for a match"""
        context_start = max(0, start - context_size)
        context_end = min(len(text), end + context_size)
        return text[context_start:context_end].strip()
    
    def generate_prioritized_action_plan(self, analysis_results: List[AnalysisResult]) -> Dict[str, List[str]]:
        """Generate prioritized action plan based on analysis"""
        action_plan = {
            "immediate_critical": [],  # Severity 5
            "high_priority": [],       # Severity 4
            "medium_priority": [],     # Severity 3
            "low_priority": []         # Severity 1-2
        }
        
        # Group by severity
        for result in analysis_results:
            action_item = f"Line {result.line_number}: {result.suggestion} ('{result.problematic_text}')"
            
            if result.severity == 5:
                action_plan["immediate_critical"].append(action_item)
            elif result.severity == 4:
                action_plan["high_priority"].append(action_item)
            elif result.severity == 3:
                action_plan["medium_priority"].append(action_item)
            else:
                action_plan["low_priority"].append(action_item)
        
        return action_plan
    
    def analyze_full_document(self, filepath: str) -> Dict:
        """Perform comprehensive analysis of entire document"""
        with open(filepath, 'r', encoding='utf-8') as f:
            text = f.read()
        
        sections = self.extract_sections(text)
        all_issues = []
        section_summaries = {}
        
        print(f"Analyzing {len(sections)} sections...")
        
        for section_name, (content, start_line) in sections.items():
            print(f"  Analyzing: {section_name}")
            metrics, issues = self.analyze_section(section_name, content, start_line)
            all_issues.extend(issues)
            section_summaries[section_name] = metrics
        
        # Generate action plan
        action_plan = self.generate_prioritized_action_plan(all_issues)
        
        # Calculate overall document metrics
        total_issues = len(all_issues)
        critical_issues = len(action_plan["immediate_critical"])
        high_priority_issues = len(action_plan["high_priority"])
        
        return {
            "overall_metrics": {
                "total_issues": total_issues,
                "critical_issues": critical_issues,
                "high_priority_issues": high_priority_issues,
                "sections_analyzed": len(sections),
                "average_rigor_score": sum(m.scientific_rigor_score for m in section_summaries.values()) / len(section_summaries)
            },
            "section_analysis": section_summaries,
            "all_issues": all_issues,
            "prioritized_action_plan": action_plan,
            "recommendations": self._generate_recommendations(section_summaries, all_issues)
        }
    
    def _generate_recommendations(self, section_summaries: Dict, all_issues: List[AnalysisResult]) -> List[str]:
        """Generate high-level recommendations"""
        recommendations = []
        
        # Check for patterns across sections
        spiritual_sections = [name for name, metrics in section_summaries.items() 
                            if metrics.spiritual_density > 5.0]
        if spiritual_sections:
            recommendations.append(f"HIGH PRIORITY: {len(spiritual_sections)} sections have excessive spiritual terminology. Focus purification efforts on: {', '.join(spiritual_sections[:3])}")
        
        anthropomorphic_sections = [name for name, metrics in section_summaries.items()
                                  if metrics.anthropomorphic_instances > 3]
        if anthropomorphic_sections:
            recommendations.append(f"CRITICAL: {len(anthropomorphic_sections)} sections use anthropomorphic language for mathematical objects")
        
        grandiose_sections = [name for name, metrics in section_summaries.items()
                            if metrics.grandiose_claims > 2]
        if grandiose_sections:
            recommendations.append(f"MODERATE: {len(grandiose_sections)} sections contain excessive grandiose claims")
        
        # Overall document recommendations
        avg_rigor = sum(m.scientific_rigor_score for m in section_summaries.values()) / len(section_summaries)
        if avg_rigor < 0.1:
            recommendations.append("CRITICAL: Overall scientific rigor score is very low. Increase use of precise scientific terminology.")
        
        return recommendations

def main():
    analyzer = AdvancedFSCTFAnalyzer()
    
    print("🔍 Advanced FSCTF Language Analysis")
    print("=" * 50)
    
    results = analyzer.analyze_full_document('FSCTF_Formal.md')
    
    print(f"\n📊 OVERALL METRICS:")
    print(f"  Total Issues Found: {results['overall_metrics']['total_issues']}")
    print(f"  Critical Issues: {results['overall_metrics']['critical_issues']}")
    print(f"  High Priority Issues: {results['overall_metrics']['high_priority_issues']}")
    print(f"  Scientific Rigor Score: {results['overall_metrics']['average_rigor_score']:.3f}")
    
    print(f"\n🚨 TOP RECOMMENDATIONS:")
    for i, rec in enumerate(results['recommendations'][:5], 1):
        print(f"  {i}. {rec}")
    
    print(f"\n⚡ IMMEDIATE ACTION ITEMS:")
    for item in results['prioritized_action_plan']['immediate_critical'][:10]:
        print(f"  • {item}")
    
    print(f"\n📋 HIGH PRIORITY ITEMS:")
    for item in results['prioritized_action_plan']['high_priority'][:10]:
        print(f"  • {item}")
    
    # Save detailed results
    with open('fsctf_analysis_results.json', 'w') as f:
        # Convert NamedTuple to dict for JSON serialization
        serializable_results = {
            **results,
            'all_issues': [issue._asdict() for issue in results['all_issues']],
            'section_analysis': {name: {
                'spiritual_density': metrics.spiritual_density,
                'grandiose_claims': metrics.grandiose_claims,
                'false_precision_instances': metrics.false_precision_instances,
                'anthropomorphic_instances': metrics.anthropomorphic_instances,
                'scientific_rigor_score': metrics.scientific_rigor_score
            } for name, metrics in results['section_analysis'].items()}
        }
        json.dump(serializable_results, f, indent=2)
    
    print(f"\n💾 Detailed analysis saved to: fsctf_analysis_results.json")

if __name__ == "__main__":
    main()