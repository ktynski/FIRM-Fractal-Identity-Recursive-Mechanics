#!/usr/bin/env python3
"""
FIRM Test Quality Monitoring & Reporting System
Team 3 Integration & Production Testing

Generates comprehensive reports on test coverage, quality trends, and system health.
Monitors testing progress and provides actionable insights for reaching 95% coverage target.

Monitoring Coverage:
- Real-time test coverage analysis
- Test quality metrics and trends  
- Module-by-module coverage reporting
- Integration test effectiveness
- Performance benchmarks
- Mathematical consistency verification

Production Features:
- Automated daily/weekly reports
- Coverage trend analysis
- Quality gate enforcement
- CI/CD integration metrics
- Team progress tracking
"""

import os
import sys
import json
import time
import subprocess
import argparse
from pathlib import Path
from datetime import datetime, timedelta
from typing import Dict, List, Any, Optional, Tuple
from dataclasses import dataclass, asdict
import numpy as np

# Add project root to path
PROJECT_ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

@dataclass
class CoverageMetrics:
    """Coverage metrics for a module or system."""
    lines_covered: int
    lines_total: int
    coverage_percentage: float
    missing_lines: List[int]
    branch_coverage: Optional[float] = None
    
@dataclass(frozen=True)
class TestQualityMetrics:
    """Test quality metrics."""
    __test__ = False  # Prevent pytest from collecting this as a test class
    total_tests: int
    passed_tests: int
    failed_tests: int
    skipped_tests: int
    execution_time: float
    success_rate: float
    
@dataclass
class ModuleReport:
    """Report for a single module."""
    module_name: str
    coverage_metrics: CoverageMetrics
    test_metrics: TestQualityMetrics
    test_files: List[str]
    priority_score: float  # Priority for coverage improvement
    
@dataclass
class SystemReport:
    """Complete system test quality report."""
    timestamp: str
    overall_coverage: CoverageMetrics
    overall_test_metrics: TestQualityMetrics
    module_reports: Dict[str, ModuleReport]
    coverage_trend: List[Tuple[str, float]]  # (date, coverage_percentage)
    quality_gates: Dict[str, bool]
    recommendations: List[str]


class FIRMTestQualityMonitor:
    """
    Comprehensive test quality monitoring system for FIRM.
    
    Tracks coverage, quality trends, and provides actionable insights
    for reaching the 95% coverage target.
    """
    
    def __init__(self, project_root: Optional[Path] = None):
        self.project_root = project_root or PROJECT_ROOT
        self.reports_dir = self.project_root / "reports" / "test_quality"
        self.reports_dir.mkdir(parents=True, exist_ok=True)
        
        # Coverage targets
        self.target_coverage = 95.0
        self.warning_coverage = 80.0
        
        # Quality gates thresholds
        self.quality_gates = {
            "minimum_coverage": 50.0,
            "maximum_failure_rate": 5.0,  # 5% max test failure rate
            "maximum_execution_time": 300.0,  # 5 minutes max
            "integration_tests_required": True,
            "mathematical_consistency_required": True
        }
        
    def run_coverage_analysis(self, modules: Optional[List[str]] = None) -> Dict[str, CoverageMetrics]:
        """Run comprehensive coverage analysis."""
        print("📊 Running coverage analysis...")
        
        if modules is None:
            modules = ["foundation", "constants", "structures", "cosmology", 
                      "validation", "provenance", "theory", "applications"]
        
        coverage_results = {}
        
        for module in modules:
            module_path = self.project_root / module
            if not module_path.exists():
                continue
                
            try:
                # Run pytest with coverage for this module
                cmd = [
                    sys.executable, "-m", "pytest", 
                    f"--cov={module}",
                    "--cov-report=json",
                    f"testing/{module}/",
                    "--tb=no", "-q"
                ]
                
                result = subprocess.run(
                    cmd, 
                    capture_output=True, 
                    text=True,
                    cwd=self.project_root,
                    timeout=60
                )
                
                # Parse coverage data
                coverage_file = self.project_root / ".coverage"
                if coverage_file.exists():
                    coverage_metrics = self._parse_coverage_data(module, result.stdout)
                    coverage_results[module] = coverage_metrics
                    
            except subprocess.TimeoutExpired:
                print(f"   ⚠️  Coverage analysis timeout for {module}")
            except Exception as e:
                print(f"   ⚠️  Coverage analysis failed for {module}: {e}")
                
        return coverage_results
        
    def _parse_coverage_data(self, module: str, coverage_output: str) -> CoverageMetrics:
        """Parse coverage data from pytest output."""
        lines = coverage_output.split('\n')
        
        # Look for coverage line
        for line in lines:
            if module in line and '%' in line:
                parts = line.split()
                for i, part in enumerate(parts):
                    if '%' in part:
                        coverage_pct = float(part.replace('%', ''))
                        
                        # Extract covered/total lines (simplified)
                        lines_total = 100  # Placeholder
                        lines_covered = int(coverage_pct * lines_total / 100)
                        
                        return CoverageMetrics(
                            lines_covered=lines_covered,
                            lines_total=lines_total,
                            coverage_percentage=coverage_pct,
                            missing_lines=[]
                        )
                        
        # Default if parsing fails
        return CoverageMetrics(
            lines_covered=0,
            lines_total=100,
            coverage_percentage=0.0,
            missing_lines=[]
        )
        
    def run_test_quality_analysis(self, test_pattern: str = "testing/") -> TestQualityMetrics:
        """Run comprehensive test quality analysis."""
        print("🧪 Running test quality analysis...")
        
        start_time = time.time()
        
        try:
            # Run pytest with detailed output
            cmd = [
                sys.executable, "-m", "pytest",
                test_pattern,
                "--tb=short",
                "-v",
                "--durations=10"
            ]
            
            result = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                cwd=self.project_root,
                timeout=300  # 5 minute timeout
            )
            
            execution_time = time.time() - start_time
            
            # Parse test results
            test_metrics = self._parse_test_results(result.stdout, execution_time)
            
            return test_metrics
            
        except subprocess.TimeoutExpired:
            execution_time = time.time() - start_time
            print(f"   ⚠️  Test execution timeout after {execution_time:.1f}s")
            
            return TestQualityMetrics(
                total_tests=0,
                passed_tests=0,
                failed_tests=0,
                skipped_tests=0,
                execution_time=execution_time,
                success_rate=0.0
            )
            
    def _parse_test_results(self, pytest_output: str, execution_time: float) -> TestQualityMetrics:
        """Parse test results from pytest output."""
        lines = pytest_output.split('\n')
        
        total_tests = 0
        passed_tests = 0
        failed_tests = 0
        skipped_tests = 0
        
        # Look for final test summary
        for line in lines:
            if " passed" in line or " failed" in line or " skipped" in line:
                # Parse test counts
                if "passed" in line:
                    for part in line.split():
                        if part.isdigit():
                            passed_tests = int(part)
                            break
                            
                if "failed" in line:
                    for part in line.split():
                        if part.isdigit():
                            failed_tests = int(part)
                            break
                            
                if "skipped" in line:
                    for part in line.split():
                        if part.isdigit():
                            skipped_tests = int(part)
                            break
        
        total_tests = passed_tests + failed_tests + skipped_tests
        success_rate = passed_tests / max(total_tests, 1) * 100.0
        
        return TestQualityMetrics(
            total_tests=total_tests,
            passed_tests=passed_tests,
            failed_tests=failed_tests,
            skipped_tests=skipped_tests,
            execution_time=execution_time,
            success_rate=success_rate
        )
        
    def analyze_module_priority(self, coverage_results: Dict[str, CoverageMetrics]) -> Dict[str, float]:
        """Analyze module priority for coverage improvement."""
        priorities = {}
        
        for module, metrics in coverage_results.items():
            # Priority factors:
            # 1. Low coverage (higher priority)
            # 2. Large number of uncovered lines 
            # 3. Module importance (foundation > theory > applications)
            
            coverage_factor = max(0, 100 - metrics.coverage_percentage) / 100
            lines_factor = min(1.0, metrics.lines_total / 200)  # Normalize by typical module size
            
            # Module importance weights
            importance_weights = {
                "foundation": 1.0,
                "constants": 0.9,
                "structures": 0.8,
                "cosmology": 0.7,
                "validation": 0.8,
                "provenance": 0.6,
                "theory": 0.7,
                "applications": 0.5
            }
            
            importance_factor = importance_weights.get(module, 0.5)
            
            priority_score = (coverage_factor * 0.5 + lines_factor * 0.3 + importance_factor * 0.2) * 100
            priorities[module] = priority_score
            
        return priorities
        
    def generate_recommendations(self, system_report: SystemReport) -> List[str]:
        """Generate actionable recommendations for test improvement."""
        recommendations = []
        
        overall_coverage = system_report.overall_coverage.coverage_percentage
        
        # Coverage recommendations
        if overall_coverage < self.target_coverage:
            gap = self.target_coverage - overall_coverage
            recommendations.append(f"📈 PRIORITY: Increase coverage by {gap:.1f}% to reach 95% target")
            
            # Find top priority modules
            sorted_modules = sorted(
                system_report.module_reports.items(),
                key=lambda x: x[1].priority_score,
                reverse=True
            )
            
            top_3_modules = sorted_modules[:3]
            for module_name, report in top_3_modules:
                if report.coverage_metrics.coverage_percentage < 80:
                    recommendations.append(
                        f"🎯 Focus on {module_name}: {report.coverage_metrics.coverage_percentage:.1f}% coverage, "
                        f"{report.coverage_metrics.lines_total - report.coverage_metrics.lines_covered} lines uncovered"
                    )
        
        # Test quality recommendations
        overall_success_rate = system_report.overall_test_metrics.success_rate
        if overall_success_rate < 95:
            recommendations.append(
                f"🔧 Fix failing tests: {100-overall_success_rate:.1f}% failure rate "
                f"({system_report.overall_test_metrics.failed_tests} failed tests)"
            )
        
        # Performance recommendations
        execution_time = system_report.overall_test_metrics.execution_time
        if execution_time > 120:  # 2 minutes
            recommendations.append(f"⚡ Optimize test performance: {execution_time:.1f}s execution time")
            
        # Quality gates recommendations
        failed_gates = [gate for gate, passed in system_report.quality_gates.items() if not passed]
        for gate in failed_gates:
            recommendations.append(f"🚨 Quality gate failure: {gate}")
            
        # Team-specific recommendations
        if len(recommendations) == 0:
            recommendations.append("✅ All quality metrics look good! Continue maintaining high standards.")
        else:
            recommendations.append("📋 See Team 1 & 2 strategy documents for specific implementation guidance")
            
        return recommendations
        
    def generate_system_report(self) -> SystemReport:
        """Generate complete system test quality report."""
        print("📋 Generating comprehensive system report...")
        
        # Run analyses
        coverage_results = self.run_coverage_analysis()
        test_metrics = self.run_test_quality_analysis()
        priorities = self.analyze_module_priority(coverage_results)
        
        # Create module reports
        module_reports = {}
        for module, coverage in coverage_results.items():
            module_test_metrics = self.run_test_quality_analysis(f"testing/{module}/")
            
            test_files = list((self.project_root / "testing" / module).glob("test_*.py"))
            test_file_names = [f.name for f in test_files]
            
            module_report = ModuleReport(
                module_name=module,
                coverage_metrics=coverage,
                test_metrics=module_test_metrics,
                test_files=test_file_names,
                priority_score=priorities.get(module, 0.0)
            )
            
            module_reports[module] = module_report
        
        # Calculate overall coverage
        total_covered = sum(m.lines_covered for m in coverage_results.values())
        total_lines = sum(m.lines_total for m in coverage_results.values())
        overall_coverage_pct = (total_covered / max(total_lines, 1)) * 100
        
        overall_coverage = CoverageMetrics(
            lines_covered=total_covered,
            lines_total=total_lines,
            coverage_percentage=overall_coverage_pct,
            missing_lines=[]
        )
        
        # Evaluate quality gates
        quality_gates_status = {
            "minimum_coverage": overall_coverage_pct >= self.quality_gates["minimum_coverage"],
            "maximum_failure_rate": test_metrics.success_rate >= (100 - self.quality_gates["maximum_failure_rate"]),
            "maximum_execution_time": test_metrics.execution_time <= self.quality_gates["maximum_execution_time"],
            "integration_tests_required": (self.project_root / "testing" / "integration").exists(),
            "mathematical_consistency_required": (self.project_root / "testing" / "integration" / "test_mathematical_consistency.py").exists()
        }
        
        # Create system report
        system_report = SystemReport(
            timestamp=datetime.now().isoformat(),
            overall_coverage=overall_coverage,
            overall_test_metrics=test_metrics,
            module_reports=module_reports,
            coverage_trend=[],  # Would be populated from historical data
            quality_gates=quality_gates_status,
            recommendations=[]
        )
        
        # Generate recommendations
        system_report.recommendations = self.generate_recommendations(system_report)
        
        return system_report
        
    def save_report(self, report: SystemReport, filename: Optional[str] = None) -> Path:
        """Save report to file."""
        if filename is None:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"firm_test_quality_report_{timestamp}.json"
            
        report_path = self.reports_dir / filename
        
        # Convert to dict for JSON serialization
        report_dict = asdict(report)
        
        with open(report_path, 'w') as f:
            json.dump(report_dict, f, indent=2)
            
        return report_path
        
    def print_report_summary(self, report: SystemReport):
        """Print human-readable report summary."""
        print("\n" + "="*80)
        print("📊 FIRM TEST QUALITY REPORT SUMMARY")
        print("="*80)
        print(f"Generated: {report.timestamp}")
        print(f"Overall Coverage: {report.overall_coverage.coverage_percentage:.1f}% "
              f"({report.overall_coverage.lines_covered}/{report.overall_coverage.lines_total} lines)")
        print(f"Test Success Rate: {report.overall_test_metrics.success_rate:.1f}% "
              f"({report.overall_test_metrics.passed_tests}/{report.overall_test_metrics.total_tests} tests)")
        print(f"Execution Time: {report.overall_test_metrics.execution_time:.1f}s")
        
        print("\n📈 COVERAGE BY MODULE:")
        sorted_modules = sorted(
            report.module_reports.items(),
            key=lambda x: x[1].coverage_metrics.coverage_percentage
        )
        
        for module_name, module_report in sorted_modules:
            coverage_pct = module_report.coverage_metrics.coverage_percentage
            status_icon = "🟢" if coverage_pct >= 80 else "🟡" if coverage_pct >= 50 else "🔴"
            print(f"  {status_icon} {module_name:20}: {coverage_pct:5.1f}% "
                  f"({len(module_report.test_files)} test files)")
        
        print("\n🚨 QUALITY GATES STATUS:")
        for gate_name, status in report.quality_gates.items():
            status_icon = "✅" if status else "❌"
            print(f"  {status_icon} {gate_name.replace('_', ' ').title()}")
        
        print("\n💡 RECOMMENDATIONS:")
        for i, recommendation in enumerate(report.recommendations, 1):
            print(f"  {i}. {recommendation}")
        
        print("\n🎯 PROGRESS TO 95% TARGET:")
        progress = report.overall_coverage.coverage_percentage / 95.0 * 100
        remaining = 95.0 - report.overall_coverage.coverage_percentage
        print(f"  Progress: {progress:.1f}% complete")
        print(f"  Remaining: {remaining:.1f}% coverage needed")
        
        lines_needed = int(remaining * report.overall_coverage.lines_total / 100)
        print(f"  Estimated lines to test: ~{lines_needed}")
        
        print("="*80)


def main():
    """Main entry point for test quality monitoring."""
    parser = argparse.ArgumentParser(description="FIRM Test Quality Monitor")
    parser.add_argument("--save", action="store_true", help="Save report to file")
    parser.add_argument("--modules", nargs="*", help="Specific modules to analyze")
    parser.add_argument("--output", help="Output filename for saved report")
    
    args = parser.parse_args()
    
    print("🔍 FIRM Test Quality Monitor Starting...")
    
    monitor = FIRMTestQualityMonitor()
    
    # Generate report
    report = monitor.generate_system_report()
    
    # Print summary
    monitor.print_report_summary(report)
    
    # Save if requested
    if args.save:
        report_path = monitor.save_report(report, args.output)
        print(f"\n💾 Report saved to: {report_path}")
        
    print("\n🎉 Test Quality Monitoring Complete!")


if __name__ == "__main__":
    main()
