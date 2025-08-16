#!/usr/bin/env python3
"""
Falsification Framework Visualization for Skeptics Section
Generates figures showing systematic falsification protocols and decision trees
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, ConnectionPatch
import seaborn as sns
from pathlib import Path

# Set style
plt.style.use('seaborn-v0_8-whitegrid')
sns.set_palette("husl")

def create_falsification_decision_tree():
    """Create decision tree showing falsification criteria"""
    fig, ax = plt.subplots(figsize=(14, 10))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis('off')
    
    # Define colors
    colors = {
        'test': '#3498db',      # Blue for tests
        'pass': '#27ae60',      # Green for pass
        'fail': '#e74c3c',      # Red for fail
        'action': '#f39c12'     # Orange for actions
    }
    
    # Root node
    root = FancyBboxPatch((4, 8.5), 2, 0.8, boxstyle="round,pad=0.1", 
                         facecolor=colors['test'], edgecolor='black', linewidth=2)
    ax.add_patch(root)
    ax.text(5, 8.9, 'FIRM Prediction\nTest', ha='center', va='center', 
            fontsize=12, fontweight='bold', color='white')
    
    # Level 1: Fixed point test
    fixed_point = FancyBboxPatch((1, 6.5), 2.5, 0.8, boxstyle="round,pad=0.1",
                                facecolor=colors['test'], edgecolor='black')
    ax.add_patch(fixed_point)
    ax.text(2.25, 6.9, 'Grace Operator\nFixed Point Unique?', ha='center', va='center',
            fontsize=10, fontweight='bold', color='white')
    
    pre_registered = FancyBboxPatch((4, 6.5), 2, 0.8, boxstyle="round,pad=0.1",
                                   facecolor=colors['test'], edgecolor='black')
    ax.add_patch(pre_registered)
    ax.text(5, 6.9, 'Pre-registered\nPrediction Match?', ha='center', va='center',
            fontsize=10, fontweight='bold', color='white')
    
    simpler_alt = FancyBboxPatch((6.5, 6.5), 2.5, 0.8, boxstyle="round,pad=0.1",
                                facecolor=colors['test'], edgecolor='black')
    ax.add_patch(simpler_alt)
    ax.text(7.75, 6.9, 'Simpler Alternative\nExists?', ha='center', va='center',
            fontsize=10, fontweight='bold', color='white')
    
    # Level 2: Outcomes
    # Fixed point outcomes
    fp_pass = FancyBboxPatch((0.5, 4.5), 1.5, 0.6, boxstyle="round,pad=0.1",
                            facecolor=colors['pass'], edgecolor='black')
    ax.add_patch(fp_pass)
    ax.text(1.25, 4.8, 'Continue\nTesting', ha='center', va='center',
            fontsize=9, color='white')
    
    fp_fail = FancyBboxPatch((2.5, 4.5), 1.5, 0.6, boxstyle="round,pad=0.1",
                            facecolor=colors['fail'], edgecolor='black')
    ax.add_patch(fp_fail)
    ax.text(3.25, 4.8, 'Revise\nAxioms', ha='center', va='center',
            fontsize=9, color='white')
    
    # Prediction outcomes
    pred_pass = FancyBboxPatch((4.25, 4.5), 1.5, 0.6, boxstyle="round,pad=0.1",
                              facecolor=colors['pass'], edgecolor='black')
    ax.add_patch(pred_pass)
    ax.text(5, 4.8, 'Theory\nSupported', ha='center', va='center',
            fontsize=9, color='white')
    
    pred_fail = FancyBboxPatch((4.25, 3.5), 1.5, 0.6, boxstyle="round,pad=0.1",
                              facecolor=colors['fail'], edgecolor='black')
    ax.add_patch(pred_fail)
    ax.text(5, 3.8, 'Theory\nFalsified', ha='center', va='center',
            fontsize=9, color='white')
    
    # Alternative outcomes
    alt_no = FancyBboxPatch((7, 4.5), 1.5, 0.6, boxstyle="round,pad=0.1",
                           facecolor=colors['pass'], edgecolor='black')
    ax.add_patch(alt_no)
    ax.text(7.75, 4.8, 'FIRM\nPreferred', ha='center', va='center',
            fontsize=9, color='white')
    
    alt_yes = FancyBboxPatch((7, 3.5), 1.5, 0.6, boxstyle="round,pad=0.1",
                            facecolor=colors['fail'], edgecolor='black')
    ax.add_patch(alt_yes)
    ax.text(7.75, 3.8, 'Adopt\nAlternative', ha='center', va='center',
            fontsize=9, color='white')
    
    # Level 3: Final actions
    abandon = FancyBboxPatch((3.5, 1.5), 3, 0.8, boxstyle="round,pad=0.1",
                            facecolor=colors['action'], edgecolor='black', linewidth=2)
    ax.add_patch(abandon)
    ax.text(5, 1.9, 'Complete Theory Abandonment\n"Truth over Success"', ha='center', va='center',
            fontsize=11, fontweight='bold', color='white')
    
    # Add arrows
    arrows = [
        # From root to level 1
        ((5, 8.5), (2.25, 7.3)),
        ((5, 8.5), (5, 7.3)),
        ((5, 8.5), (7.75, 7.3)),
        # From level 1 to level 2
        ((2.25, 6.5), (1.25, 5.1)),
        ((2.25, 6.5), (3.25, 5.1)),
        ((5, 6.5), (5, 5.1)),
        ((5, 6.5), (5, 4.1)),
        ((7.75, 6.5), (7.75, 5.1)),
        ((7.75, 6.5), (7.75, 4.1)),
        # To abandonment
        ((3.25, 4.5), (4.5, 2.3)),
        ((5, 3.5), (5, 2.3)),
        ((7.75, 3.5), (5.5, 2.3))
    ]
    
    for start, end in arrows:
        arrow = ConnectionPatch(start, end, "data", "data",
                              arrowstyle="->", shrinkA=5, shrinkB=5,
                              mutation_scale=20, fc="black", lw=1.5)
        ax.add_patch(arrow)
    
    # Add labels for Yes/No
    ax.text(1.5, 5.8, 'YES', ha='center', va='center', fontsize=9, 
            bbox=dict(boxstyle="round,pad=0.2", facecolor='lightgreen'))
    ax.text(3, 5.8, 'NO', ha='center', va='center', fontsize=9,
            bbox=dict(boxstyle="round,pad=0.2", facecolor='lightcoral'))
    ax.text(5, 5.8, 'YES', ha='center', va='center', fontsize=9,
            bbox=dict(boxstyle="round,pad=0.2", facecolor='lightgreen'))
    ax.text(5, 4.8, 'NO', ha='center', va='center', fontsize=9,
            bbox=dict(boxstyle="round,pad=0.2", facecolor='lightcoral'))
    ax.text(7.75, 5.8, 'NO', ha='center', va='center', fontsize=9,
            bbox=dict(boxstyle="round,pad=0.2", facecolor='lightgreen'))
    ax.text(7.75, 4.8, 'YES', ha='center', va='center', fontsize=9,
            bbox=dict(boxstyle="round,pad=0.2", facecolor='lightcoral'))
    
    plt.title('FIRM Falsification Decision Tree\nSystematic Criteria for Theory Rejection', 
              fontsize=16, fontweight='bold', pad=20)
    
    # Add legend
    legend_elements = [
        mpatches.Patch(color=colors['test'], label='Falsification Test'),
        mpatches.Patch(color=colors['pass'], label='Continue/Accept'),
        mpatches.Patch(color=colors['fail'], label='Reject/Revise'),
        mpatches.Patch(color=colors['action'], label='Final Action')
    ]
    ax.legend(handles=legend_elements, loc='upper right', bbox_to_anchor=(0.98, 0.98))
    
    plt.tight_layout()
    return fig

def create_statistical_protocol_flowchart():
    """Create flowchart showing statistical validation protocols"""
    fig, ax = plt.subplots(figsize=(12, 14))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 14)
    ax.axis('off')
    
    # Define protocol steps
    steps = [
        {'pos': (5, 12.5), 'text': 'Pre-register\nPrediction', 'color': '#3498db'},
        {'pos': (5, 11), 'text': 'Specify Search Space\n(N candidate forms)', 'color': '#3498db'},
        {'pos': (5, 9.5), 'text': 'Partition Constants\n60% train, 20% val, 20% test', 'color': '#9b59b6'},
        {'pos': (2.5, 8), 'text': 'Develop φ-forms\n(training data only)', 'color': '#e67e22'},
        {'pos': (7.5, 8), 'text': 'Select best model\n(validation data)', 'color': '#e67e22'},
        {'pos': (5, 6.5), 'text': 'Apply Bonferroni\nCorrection: p < α/N', 'color': '#e74c3c'},
        {'pos': (5, 5), 'text': 'Test on held-out data\n(one time only)', 'color': '#27ae60'},
        {'pos': (2.5, 3.5), 'text': 'Significant?\nReport success', 'color': '#27ae60'},
        {'pos': (7.5, 3.5), 'text': 'Not significant?\nReport null result', 'color': '#95a5a6'},
        {'pos': (5, 2), 'text': 'Publish complete\nsearch history', 'color': '#34495e'}
    ]
    
    # Draw boxes
    for step in steps:
        box = FancyBboxPatch((step['pos'][0]-0.8, step['pos'][1]-0.4), 1.6, 0.8,
                            boxstyle="round,pad=0.1", facecolor=step['color'],
                            edgecolor='black', linewidth=1)
        ax.add_patch(box)
        ax.text(step['pos'][0], step['pos'][1], step['text'], 
                ha='center', va='center', fontsize=10, fontweight='bold', 
                color='white')
    
    # Add arrows
    arrows = [
        ((5, 12.1), (5, 11.4)),
        ((5, 10.6), (5, 9.9)),
        ((5, 9.1), (2.5, 8.4)),
        ((5, 9.1), (7.5, 8.4)),
        ((2.5, 7.6), (5, 6.9)),
        ((7.5, 7.6), (5, 6.9)),
        ((5, 6.1), (5, 5.4)),
        ((5, 4.6), (2.5, 3.9)),
        ((5, 4.6), (7.5, 3.9)),
        ((2.5, 3.1), (5, 2.4)),
        ((7.5, 3.1), (5, 2.4))
    ]
    
    for start, end in arrows:
        arrow = ConnectionPatch(start, end, "data", "data",
                              arrowstyle="->", shrinkA=5, shrinkB=5,
                              mutation_scale=20, fc="black", lw=1.5)
        ax.add_patch(arrow)
    
    # Add side annotations
    ax.text(0.5, 8, 'Model\nDevelopment\nPhase', ha='center', va='center',
            fontsize=12, fontweight='bold', rotation=90,
            bbox=dict(boxstyle="round,pad=0.3", facecolor='lightblue', alpha=0.7))
    
    ax.text(9.5, 5, 'Validation\nPhase', ha='center', va='center',
            fontsize=12, fontweight='bold', rotation=90,
            bbox=dict(boxstyle="round,pad=0.3", facecolor='lightgreen', alpha=0.7))
    
    ax.text(0.5, 2, 'Transparency\nPhase', ha='center', va='center',
            fontsize=12, fontweight='bold', rotation=90,
            bbox=dict(boxstyle="round,pad=0.3", facecolor='lightgray', alpha=0.7))
    
    plt.title('Statistical Validation Protocol\nPreventing P-hacking and Multiple Testing Bias', 
              fontsize=16, fontweight='bold', pad=20)
    
    plt.tight_layout()
    return fig

def create_historical_comparison_chart():
    """Create comparison chart of failed TOEs vs FIRM"""
    theories = ['Pythagorean\nNumerology', 'Kepler\nPolyhedra', 'Eddington\nFundamental', 'String Theory\nLandscape', 'FIRM\nφ-Recursive']
    
    # Criteria scores (0-10 scale)
    criteria = {
        'Mathematical\nRigor': [2, 7, 8, 9, 8],
        'Empirical\nPredictions': [1, 4, 6, 3, 7],
        'Falsifiability': [2, 8, 9, 2, 9],
        'Uniqueness': [3, 6, 7, 1, 8],
        'Experimental\nAgreement': [1, 2, 3, 5, 7]
    }
    
    fig, ax = plt.subplots(figsize=(14, 8))
    
    x = np.arange(len(theories))
    width = 0.15
    colors = ['#e74c3c', '#f39c12', '#f1c40f', '#27ae60', '#3498db']
    
    for i, (criterion, scores) in enumerate(criteria.items()):
        offset = (i - 2) * width
        bars = ax.bar(x + offset, scores, width, label=criterion, color=colors[i], alpha=0.8)
        
        # Add value labels on bars
        for bar, score in zip(bars, scores):
            height = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2., height + 0.1,
                   f'{score}', ha='center', va='bottom', fontsize=9)
    
    ax.set_xlabel('Theory', fontsize=12, fontweight='bold')
    ax.set_ylabel('Score (0-10)', fontsize=12, fontweight='bold')
    ax.set_title('Historical Comparison: Failed TOEs vs FIRM\nObjective Assessment Across Key Criteria', 
                 fontsize=14, fontweight='bold')
    ax.set_xticks(x)
    ax.set_xticklabels(theories, fontsize=10)
    ax.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
    ax.set_ylim(0, 10.5)
    ax.grid(True, alpha=0.3)
    
    # Add annotation
    ax.text(4, 9.5, 'FIRM scores shown\nare self-assessed\nand require\nindependent\nvalidation', 
            ha='center', va='center', fontsize=9, style='italic',
            bbox=dict(boxstyle="round,pad=0.3", facecolor='yellow', alpha=0.7))
    
    plt.tight_layout()
    return fig

def create_testability_timeline():
    """Create timeline showing testability of FIRM predictions"""
    fig, ax = plt.subplots(figsize=(14, 10))
    
    # Timeline data
    timeline_data = {
        'Currently Testable (2024-2029)': {
            'items': ['Fine structure constant α⁻¹', 'Proton-electron mass ratio', 
                     'Cosmological constant Λ', 'CMB acoustic peaks'],
            'color': '#27ae60',
            'y_pos': 8
        },
        'Challenging but Possible (2030-2044)': {
            'items': ['New particle masses at φⁿ scales', 'Gravitational wave signatures',
                     'Dark matter φ-coupling', 'Neutrino mass hierarchy'],
            'color': '#f39c12',
            'y_pos': 5.5
        },
        'Currently Untestable': {
            'items': ['Consciousness φ-thresholds', 'Direct φ-field detection',
                     'Multiverse φ-selection', 'Pre-Big Bang φ-structure'],
            'color': '#e74c3c',
            'y_pos': 3
        }
    }
    
    ax.set_xlim(2024, 2050)
    ax.set_ylim(0, 10)
    
    # Draw timeline categories
    for category, data in timeline_data.items():
        # Category header
        ax.text(2025, data['y_pos'] + 1, category, fontsize=14, fontweight='bold',
                bbox=dict(boxstyle="round,pad=0.3", facecolor=data['color'], alpha=0.8))
        
        # Items
        for i, item in enumerate(data['items']):
            x_pos = 2026 + i * 5
            ax.scatter(x_pos, data['y_pos'], s=200, color=data['color'], alpha=0.7, zorder=3)
            ax.text(x_pos, data['y_pos'] - 0.5, item, ha='center', va='top', 
                   fontsize=9, rotation=45, fontweight='bold')
    
    # Add uncertainty regions
    ax.axvspan(2030, 2044, alpha=0.2, color='orange', label='Uncertain timeline')
    ax.axvspan(2045, 2050, alpha=0.2, color='red', label='May require breakthroughs')
    
    # Add vertical lines for key dates
    ax.axvline(x=2029, color='green', linestyle='--', alpha=0.7, linewidth=2)
    ax.text(2029.2, 9, '5-year\nvalidation\ntarget', fontsize=10, fontweight='bold')
    
    ax.axvline(x=2044, color='orange', linestyle='--', alpha=0.7, linewidth=2)
    ax.text(2044.2, 9, '20-year\nfull test\ntarget', fontsize=10, fontweight='bold')
    
    ax.set_xlabel('Year', fontsize=12, fontweight='bold')
    ax.set_ylabel('Testability Category', fontsize=12, fontweight='bold')
    ax.set_title('FIRM Prediction Testability Timeline\nHonest Assessment of Experimental Accessibility', 
                 fontsize=14, fontweight='bold')
    
    # Remove y-axis ticks
    ax.set_yticks([])
    
    # Add grid
    ax.grid(True, alpha=0.3, axis='x')
    
    # Add legend
    ax.legend(loc='upper right')
    
    plt.tight_layout()
    return fig

def main():
    """Generate all skeptics figures"""
    output_dir = Path("figures/canonical_outputs")
    output_dir.mkdir(parents=True, exist_ok=True)
    
    print("Generating skeptics section figures...")
    
    # Generate figures
    figures = {
        'firm_falsification_decision_tree.png': create_falsification_decision_tree(),
        'firm_statistical_validation_protocol.png': create_statistical_protocol_flowchart(),
        'firm_historical_theory_comparison.png': create_historical_comparison_chart(),
        'firm_testability_timeline.png': create_testability_timeline()
    }
    
    # Save figures
    for filename, fig in figures.items():
        filepath = output_dir / filename
        fig.savefig(filepath, dpi=300, bbox_inches='tight', 
                   facecolor='white', edgecolor='none')
        print(f"Saved: {filepath}")
        plt.close(fig)
    
    print("All skeptics figures generated successfully!")

if __name__ == "__main__":
    main()
