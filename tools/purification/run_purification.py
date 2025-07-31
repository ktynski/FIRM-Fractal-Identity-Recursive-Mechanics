#!/usr/bin/env python3
"""
FSCTF Document Purification Workflow
Orchestrates the complete language purification process
"""

import subprocess
import sys
from pathlib import Path

def run_command(command, description):
    """Run a command and handle errors"""
    print(f"\n🔄 {description}")
    print("-" * 50)
    
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        
        if result.returncode == 0:
            print(result.stdout)
            if result.stderr:
                print("Warnings:", result.stderr)
            return True
        else:
            print(f"❌ Error running command: {command}")
            print(f"Error output: {result.stderr}")
            return False
    except Exception as e:
        print(f"❌ Exception running command: {e}")
        return False

def check_prerequisites():
    """Check if all required files exist"""
    required_files = [
        'FSCTF_Formal.md',
        'language_purification_engine.py',
        'advanced_analysis.py', 
        'systematic_purifier.py',
        'purification_config.json'
    ]
    
    missing_files = []
    for file in required_files:
        if not Path(file).exists():
            missing_files.append(file)
    
    if missing_files:
        print(f"❌ Missing required files: {', '.join(missing_files)}")
        return False
    
    print("✅ All required files found")
    return True

def main():
    """Main purification workflow"""
    print("🧹 FSCTF DOCUMENT PURIFICATION WORKFLOW")
    print("=" * 60)
    
    # Check prerequisites
    if not check_prerequisites():
        sys.exit(1)
    
    # Step 1: Run initial language analysis
    success = run_command(
        "python advanced_analysis.py ../../FSCTF_Formal.md",
        "Step 1: Comprehensive Language Analysis"
    )
    if not success:
        print("❌ Analysis failed, stopping workflow")
        sys.exit(1)
    
    # Step 2: Run basic pattern detection
    success = run_command(
        "python language_purification_engine.py ../../FSCTF_Formal.md",
        "Step 2: Pattern Detection & Basic Purification"
    )
    if not success:
        print("⚠️ Basic purification had issues, continuing...")
    
    # Step 3: Run systematic purification
    success = run_command(
        "python systematic_purifier.py ../../FSCTF_Formal.md",
        "Step 3: Systematic Document Purification"
    )
    if not success:
        print("❌ Systematic purification failed")
        sys.exit(1)
    
    # Step 4: Generate final summary
    print(f"\n📋 PURIFICATION WORKFLOW COMPLETE")
    print("=" * 60)
    
    # Check if outputs were created
    outputs = [
        'FSCTF_Formal_PURIFIED.md',
        'fsctf_analysis_results.json',
        'purification_report.json'
    ]
    
    print(f"\n📁 Generated Files:")
    for output in outputs:
        if Path(output).exists():
            size = Path(output).stat().st_size
            print(f"  ✅ {output} ({size:,} bytes)")
        else:
            print(f"  ❌ {output} (missing)")
    
    print(f"\n🎯 NEXT STEPS:")
    print(f"  1. Review the purified document: FSCTF_Formal_PURIFIED.md")
    print(f"  2. Check the analysis results: fsctf_analysis_results.json")
    print(f"  3. Review the purification report: purification_report.json")
    print(f"  4. Manually review any remaining high-risk changes")
    print(f"  5. Test that the mathematical content remains valid")
    
    print(f"\n✨ Purification workflow completed successfully!")

if __name__ == "__main__":
    main()