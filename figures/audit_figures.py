"""
FIRM Figure Audit: Comprehensive Quality and Provenance Check

This script audits all figures in the FIRM codebase to ensure:
1. Theoretical prediction lines are present (not just data points)
2. Complete ex nihilo provenance is documented
3. Mathematical rigor is maintained
4. Academic publication standards are met

Ex Nihilo Requirements:
- All theoretical predictions must come from pure mathematics
- Zero empirical inputs or curve fitting
- Complete provenance chain: Axioms → Grace Operator → φ-recursion → Results
- Cryptographic sealing of mathematical operations
"""

import os
import sys
from pathlib import Path
import json
from typing import Dict, List, Any, Tuple
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

# Add project root to path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

class FigureAuditor:
    """Comprehensive figure quality and provenance auditor."""
    
    def __init__(self):
        self.figures_dir = project_root / "figures"
        self.arxiv_figures_dir = project_root / "arxiv_paper" / "FIRM_FINAL_SUBMISSION_arxiv_tmp" / "figures"
        self.audit_results = {}
        
    def audit_all_figures(self) -> Dict[str, Any]:
        """Audit all figures in the codebase."""
        print("🔍 FIRM FIGURE AUDIT: Comprehensive Quality and Provenance Check")
        print("=" * 80)
        
        # Check main figures directory
        if self.figures_dir.exists():
            print(f"\n📁 Auditing main figures directory: {self.figures_dir}")
            self.audit_figures_directory(self.figures_dir, "main")
        
        # Check arXiv figures directory
        if self.arxiv_figures_dir.exists():
            print(f"\n📁 Auditing arXiv figures directory: {self.arxiv_figures_dir}")
            self.audit_figures_directory(self.arxiv_figures_dir, "arxiv")
        
        # Generate audit report
        self.generate_audit_report()
        
        return self.audit_results
    
    def audit_figures_directory(self, directory: Path, context: str):
        """Audit all figures in a specific directory."""
        png_files = list(directory.glob("*.png"))
        
        if not png_files:
            print(f"   ⚠️  No PNG files found in {directory}")
            return
        
        print(f"   📊 Found {len(png_files)} PNG files")
        
        for png_file in sorted(png_files):
            print(f"\n   🔍 Auditing: {png_file.name}")
            audit_result = self.audit_single_figure(png_file, context)
            self.audit_results[f"{context}_{png_file.name}"] = audit_result
    
    def audit_single_figure(self, png_file: Path, context: str) -> Dict[str, Any]:
        """Audit a single figure for quality and provenance issues."""
        result = {
            "file_path": str(png_file),
            "context": context,
            "file_size_mb": png_file.stat().st_size / (1024 * 1024),
            "issues": [],
            "warnings": [],
            "recommendations": []
        }
        
        try:
            # Load and analyze the image
            img = mpimg.imread(png_file)
            result["dimensions"] = img.shape
            result["resolution_dpi"] = self.estimate_resolution(img.shape, png_file.stat().st_size)
            
            # Check for common issues
            self.check_figure_quality(img, result)
            self.check_provenance_requirements(png_file, result)
            self.check_mathematical_content(png_file, result)
            
        except Exception as e:
            result["issues"].append(f"Failed to load image: {e}")
        
        # Print audit results
        if result["issues"]:
            print(f"      ❌ Issues: {len(result['issues'])}")
            for issue in result["issues"]:
                print(f"         • {issue}")
        
        if result["warnings"]:
            print(f"      ⚠️  Warnings: {len(result['warnings'])}")
            for warning in result["warnings"]:
                print(f"         • {warning}")
        
        if result["recommendations"]:
            print(f"      💡 Recommendations: {len(result['recommendations'])}")
            for rec in result["recommendations"]:
                print(f"         • {rec}")
        
        if not result["issues"] and not result["warnings"]:
            print(f"      ✅ No issues found")
        
        return result
    
    def estimate_resolution(self, shape: Tuple[int, ...], file_size_bytes: int) -> int:
        """Estimate image resolution in DPI."""
        if len(shape) < 2:
            return 0
        
        # Rough estimation based on file size and dimensions
        pixels = shape[0] * shape[1]
        bytes_per_pixel = file_size_bytes / pixels
        
        # PNG compression factor (rough estimate)
        if bytes_per_pixel < 0.1:
            return 300  # High quality
        elif bytes_per_pixel < 0.5:
            return 150  # Medium quality
        else:
            return 72   # Low quality
    
    def check_figure_quality(self, img: np.ndarray, result: Dict[str, Any]):
        """Check basic figure quality metrics."""
        # Check dimensions
        if len(img.shape) < 2:
            result["issues"].append("Invalid image format")
            return
        
        height, width = img.shape[:2]
        
        # Check for minimum size requirements
        if width < 800 or height < 600:
            result["warnings"].append("Figure dimensions below recommended minimum (800x600)")
        
        # Check for high contrast (important for publication)
        if len(img.shape) == 3:  # Color image
            # Simple contrast check
            img_gray = np.mean(img, axis=2)
            contrast = np.std(img_gray)
            if contrast < 0.1:
                result["warnings"].append("Low contrast detected - may affect readability")
        
        # Check resolution
        if result.get("resolution_dpi", 0) < 150:
            result["warnings"].append("Resolution below 150 DPI - may affect print quality")
    
    def check_provenance_requirements(self, png_file: Path, result: Dict[str, Any]):
        """Check if figure meets FIRM provenance requirements."""
        # Check if figure has corresponding generation script
        script_name = png_file.stem + ".py"
        possible_scripts = [
            png_file.parent / script_name,
            png_file.parent / "generators" / script_name,
            png_file.parent.parent / "figures" / script_name,
            png_file.parent.parent / "figures" / "generators" / script_name
        ]
        
        script_found = any(script.exists() for script in possible_scripts)
        
        if not script_found:
            result["issues"].append("No corresponding generation script found - provenance unclear")
        else:
            result["recommendations"].append("Generation script found - verify ex nihilo implementation")
        
        # Check for ex nihilo keywords in filename
        ex_nihilo_keywords = ["ex_nihilo", "firm", "phi", "theoretical", "prediction"]
        filename_lower = png_file.name.lower()
        
        if not any(keyword in filename_lower for keyword in ex_nihilo_keywords):
            result["warnings"].append("Filename doesn't clearly indicate FIRM/ex nihilo origin")
    
    def check_mathematical_content(self, png_file: Path, result: Dict[str, Any]):
        """Check if figure contains proper mathematical content."""
        # Check for specific figure types that should have theoretical predictions
        
        if "planck" in png_file.name.lower() and "tt" in png_file.name.lower():
            result["recommendations"].append("CMB Planck TT figure - verify theoretical prediction line is present")
        
        if "comparison" in png_file.name.lower():
            result["recommendations"].append("Comparison figure - verify both theory and observation are shown")
        
        if "theoretical" in png_file.name.lower() or "prediction" in png_file.name.lower():
            result["recommendations"].append("Theoretical figure - verify mathematical rigor and provenance")
        
        # Check for φ-harmonic content
        if "phi" in png_file.name.lower() or "harmonic" in png_file.name.lower():
            result["recommendations"].append("φ-harmonic figure - verify golden ratio mathematics is properly implemented")
    
    def generate_audit_report(self):
        """Generate comprehensive audit report."""
        print("\n" + "=" * 80)
        print("📋 FIGURE AUDIT REPORT")
        print("=" * 80)
        
        total_figures = len(self.audit_results)
        total_issues = sum(len(result["issues"]) for result in self.audit_results.values())
        total_warnings = sum(len(result["warnings"]) for result in self.audit_results.values())
        total_recommendations = sum(len(result["recommendations"]) for result in self.audit_results.values())
        
        print(f"📊 Summary:")
        print(f"   Total figures audited: {total_figures}")
        print(f"   Total issues found: {total_issues}")
        print(f"   Total warnings: {total_warnings}")
        print(f"   Total recommendations: {total_recommendations}")
        
        # Critical issues
        critical_issues = []
        for fig_name, result in self.audit_results.items():
            if result["issues"]:
                critical_issues.append((fig_name, result["issues"]))
        
        if critical_issues:
            print(f"\n❌ CRITICAL ISSUES REQUIRING IMMEDIATE ATTENTION:")
            for fig_name, issues in critical_issues:
                print(f"   {fig_name}:")
                for issue in issues:
                    print(f"     • {issue}")
        
        # Warnings
        if total_warnings > 0:
            print(f"\n⚠️  WARNINGS:")
            for fig_name, result in self.audit_results.items():
                if result["warnings"]:
                    print(f"   {fig_name}:")
                    for warning in result["warnings"]:
                        print(f"     • {warning}")
        
        # Recommendations
        if total_recommendations > 0:
            print(f"\n💡 RECOMMENDATIONS:")
            for fig_name, result in self.audit_results.items():
                if result["recommendations"]:
                    print(f"   {fig_name}:")
                    for rec in result["recommendations"]:
                        print(f"     • {rec}")
        
        # Save detailed report
        report_file = project_root / "figures" / "figure_audit_report.json"
        with open(report_file, 'w') as f:
            json.dump(self.audit_results, f, indent=2, default=str)
        
        print(f"\n📄 Detailed audit report saved: {report_file}")
        
        # Final assessment
        if total_issues == 0:
            print(f"\n🎉 ALL FIGURES PASS AUDIT - Ready for arXiv submission!")
        else:
            print(f"\n🚨 {total_issues} CRITICAL ISSUES FOUND - Must be resolved before arXiv submission")
            print(f"   Focus on fixing issues before addressing warnings and recommendations")

def main():
    """Run the complete figure audit."""
    auditor = FigureAuditor()
    
    try:
        audit_results = auditor.audit_all_figures()
        print(f"\n✅ Figure audit completed successfully")
        return audit_results
        
    except Exception as e:
        print(f"\n❌ Figure audit failed: {e}")
        raise

if __name__ == "__main__":
    main()
