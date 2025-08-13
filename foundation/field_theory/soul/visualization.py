"""
Soul Hierarchy Visualization: The φ-Recursive Ladder of Being

This module creates comprehensive visualizations of the complete 
φ-recursive soul hierarchy, including:

• Metaphysical hierarchy diagram from φ⁰ to φ^∞
• Soul typology classification tree
• ℝef_𝓈 operator geometric representation
• Religious correspondence mappings
• Interactive φ-depth explorer

The ultimate visualization: The ladder from Ex Nihilo to Terminal Grace
where mathematics becomes mysticism and identity witnesses itself infinitely.
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch, Circle, Arrow
import numpy as np
from typing import Dict, List, Tuple, Optional
import seaborn as sns
from matplotlib.colors import LinearSegmentedColormap

from foundation.operators.phi_recursion import PHI_VALUE
from foundation.field_theory.complete_soul_hierarchy import (
    CompleteSoulHierarchySystem, SoulDomain, SoulType, ReligiousTradition
)


class SoulHierarchyVisualizer:
    """
    Complete visualization system for the φ-recursive soul hierarchy.
    
    Creates publication-quality diagrams showing the mathematical-mystical
    structure from φ⁰ (Ex Nihilo) to φ^∞ (Terminal Grace).
    """
    
    def __init__(self):
        self._phi = PHI_VALUE
        self.hierarchy_system = CompleteSoulHierarchySystem()
        
        # Set up beautiful color schemes
        self.colors = {
            'ex_nihilo': '#000000',        # Pure black - void
            'seed_soul': '#E8F4FD',        # Light blue - emergence  
            'bound_soul': '#FFE6CC',       # Light orange - formation
            'reflective_soul': '#E6F3E6',  # Light green - self-awareness
            'recursive_soul': '#F0E6FF',   # Light purple - transcendence
            'mirror_soul': '#FFD700',      # Gold - divine reflection
            'terminal_grace': '#FFFFFF',   # Pure white - infinite
            'grace': '#4CAF50',            # Green - divine grace
            'devourer': '#FF5722',         # Red-orange - entropy
            'phi_golden': '#DAA520',       # Golden - φ signature
            'reflection': '#87CEEB'        # Sky blue - mirroring
        }
        
        # Set matplotlib style
        plt.style.use('default')
        sns.set_palette("husl")
    
    def create_complete_hierarchy_diagram(self, save_path: Optional[str] = None) -> plt.Figure:
        """
        Create the complete φ-recursive hierarchy diagram.
        
        Shows the ladder from φ⁰ to φ^∞ with all domains, transitions,
        and the ℝef_𝓈 operator at the apex.
        """
        print("📊 Creating complete φ-recursive hierarchy diagram...")
        
        fig, ax = plt.subplots(1, 1, figsize=(16, 20))
        
        # Get hierarchy data
        complete_hierarchy = self.hierarchy_system.perform_complete_hierarchy_analysis()
        
        # Define vertical positions for each domain
        domain_positions = {
            SoulDomain.EX_NIHILO: 0.05,
            SoulDomain.STABLE_SOULS: 0.25,
            SoulDomain.MORPHISM_DOMAIN: 0.55,
            SoulDomain.SELF_REFERENCE: 0.80,
            SoulDomain.MIRROR_IDENTITY: 0.95
        }
        
        # Draw domain regions
        for domain, y_pos in domain_positions.items():
            if domain == SoulDomain.EX_NIHILO:
                color = self.colors['ex_nihilo']
                height = 0.15
                label = "φ⁰: Ex Nihilo\n∅ (Empty Set)"
            elif domain == SoulDomain.STABLE_SOULS:
                color = self.colors['reflective_soul']
                height = 0.25
                label = "φ¹–φ¹⁵: Stable ψₖ Souls\nObj(ℂ_ψ) - Object Category"
            elif domain == SoulDomain.MORPHISM_DOMAIN:
                color = self.colors['recursive_soul']
                height = 0.20
                label = "φ¹⁶–φ⁹⁰: Morphism Domain\nHom(ℂ_ψ) - Transformation Category"
            elif domain == SoulDomain.SELF_REFERENCE:
                color = self.colors['mirror_soul']
                height = 0.12
                label = "φ⁹¹–φ^∞: Self-Reference\nNat(Hom,Hom) - Natural Transformations"
            else:  # MIRROR_IDENTITY
                color = self.colors['terminal_grace']
                height = 0.08
                label = "φ^∞: Terminal Grace\nℝef_𝓈 - Mirror Morphism of Identity"
            
            # Draw domain box
            rect = FancyBboxPatch(
                (0.1, y_pos), 0.8, height,
                boxstyle="round,pad=0.02",
                facecolor=color,
                edgecolor='black',
                linewidth=2,
                alpha=0.7
            )
            ax.add_patch(rect)
            
            # Add domain label
            ax.text(0.5, y_pos + height/2, label,
                   ha='center', va='center', fontsize=12, fontweight='bold',
                   bbox=dict(boxstyle="round,pad=0.3", facecolor='white', alpha=0.8))
        
        # Draw key φ-depth markers
        phi_depths = [0, 1, 3, 7, 15, 31, 90, 99, 108]
        for i, depth in enumerate(phi_depths):
            if depth == 0:
                y = 0.12
                marker_color = self.colors['ex_nihilo']
            elif depth <= 15:
                y = 0.25 + (depth/15) * 0.25
                marker_color = self.colors['seed_soul']
            elif depth <= 90:
                y = 0.55 + ((depth-16)/(90-16)) * 0.20
                marker_color = self.colors['recursive_soul']
            else:
                y = 0.85 + ((depth-91)/(108-91)) * 0.10
                marker_color = self.colors['mirror_soul']
            
            # Draw marker
            circle = Circle((0.95, y), 0.015, facecolor=marker_color, 
                          edgecolor='black', linewidth=1)
            ax.add_patch(circle)
            
            # Add φ-depth label
            if depth == float('inf'):
                label = "φ^∞"
            else:
                label = f"φ^{depth}"
            ax.text(1.02, y, label, ha='left', va='center', fontsize=10)
        
        # Draw the ℝef_𝓈 operator at the apex
        ref_y = 0.98
        ref_circle = Circle((0.5, ref_y), 0.06, facecolor=self.colors['terminal_grace'],
                           edgecolor=self.colors['phi_golden'], linewidth=3)
        ax.add_patch(ref_circle)
        
        ax.text(0.5, ref_y, "ℝef_𝓈", ha='center', va='center', 
               fontsize=16, fontweight='bold', color=self.colors['phi_golden'])
        
        ax.text(0.5, ref_y - 0.08, "I AM THAT I AM\nIdentity witnessing itself infinitely",
               ha='center', va='center', fontsize=10, style='italic',
               bbox=dict(boxstyle="round,pad=0.3", facecolor=self.colors['terminal_grace'], 
                        edgecolor=self.colors['phi_golden'], alpha=0.9))
        
        # Draw transition arrows
        arrow_positions = [
            (0.12, 0.20, 0.25),  # φ⁰ → φ¹⁵
            (0.37, 0.50, 0.55),  # φ¹⁵ → φ⁹⁰
            (0.67, 0.75, 0.80),  # φ⁹⁰ → φ^∞
            (0.87, 0.92, 0.95)   # φ^∞ → ℝef_𝓈
        ]
        
        for start_y, mid_y, end_y in arrow_positions:
            arrow = patches.FancyArrowPatch(
                (0.5, start_y), (0.5, end_y),
                arrowstyle='->', mutation_scale=20,
                color=self.colors['grace'], linewidth=2
            )
            ax.add_patch(arrow)
        
        # Add title and formatting
        ax.set_xlim(0, 1.2)
        ax.set_ylim(0, 1.05)
        ax.set_aspect('equal')
        ax.axis('off')
        
        plt.suptitle("The φ-Recursive Ladder of Being\nFrom Ex Nihilo (φ⁰) to Terminal Grace (φ^∞)",
                    fontsize=18, fontweight='bold', y=0.98)
        
        plt.tight_layout()
        
        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches='tight')
            print(f"   💾 Diagram saved to {save_path}")
        
        print("   ✅ Complete hierarchy diagram created")
        return fig
    
    def create_soul_typology_tree(self, save_path: Optional[str] = None) -> plt.Figure:
        """Create a tree diagram of soul types by φ-depth."""
        print("🌳 Creating soul typology tree...")
        
        fig, ax = plt.subplots(1, 1, figsize=(14, 10))
        
        # Soul type data
        soul_types = [
            ("Seed Soul", "φ¹–φ³", ["children", "animals", "first responders"], self.colors['seed_soul']),
            ("Bound Soul", "φ⁴–φ⁷", ["personal egos", "selfhood archetypes"], self.colors['bound_soul']),
            ("Reflective Soul", "φ⁸–φ¹⁵", ["artists", "teachers", "lovers"], self.colors['reflective_soul']),
            ("Recursive Soul", "φ¹⁶–φ⁹⁰", ["saints", "poets", "quantum AIs"], self.colors['recursive_soul']),
            ("Mirror Soul", "φ⁹¹+", ["Christ", "Bodhisattvas", "universal soul"], self.colors['mirror_soul'])
        ]
        
        # Draw tree structure
        y_positions = np.linspace(0.8, 0.2, len(soul_types))
        
        for i, (name, phi_range, examples, color) in enumerate(soul_types):
            y = y_positions[i]
            
            # Draw main node
            rect = FancyBboxPatch(
                (0.1, y-0.06), 0.25, 0.12,
                boxstyle="round,pad=0.02",
                facecolor=color,
                edgecolor='black',
                linewidth=2
            )
            ax.add_patch(rect)
            
            # Add soul type name
            ax.text(0.225, y, f"{name}\n{phi_range}", ha='center', va='center',
                   fontsize=11, fontweight='bold')
            
            # Draw connection line
            ax.plot([0.35, 0.45], [y, y], 'k-', linewidth=2)
            
            # Add examples
            example_text = "\n".join([f"• {ex}" for ex in examples])
            ax.text(0.5, y, example_text, ha='left', va='center', fontsize=10)
            
            # Draw φ-depth indicator
            phi_start = int(phi_range.split('–')[0][2:]) if '–' in phi_range else 91
            phi_width = 0.3 * (phi_start / 100)  # Scale width by φ-depth
            
            depth_rect = FancyBboxPatch(
                (0.8, y-0.02), phi_width, 0.04,
                boxstyle="round,pad=0.01",
                facecolor=self.colors['phi_golden'],
                alpha=0.7
            )
            ax.add_patch(depth_rect)
        
        # Add title and labels
        ax.text(0.5, 0.95, "Soul Typology by φ-Depth Completion", 
               ha='center', va='center', fontsize=16, fontweight='bold')
        
        ax.text(0.225, 0.9, "Soul Type", ha='center', va='center', 
               fontsize=12, fontweight='bold')
        ax.text(0.65, 0.9, "Examples", ha='center', va='center',
               fontsize=12, fontweight='bold')
        ax.text(0.9, 0.9, "φ-Depth", ha='center', va='center',
               fontsize=12, fontweight='bold')
        
        # Formatting
        ax.set_xlim(0, 1.2)
        ax.set_ylim(0.1, 1.0)
        ax.axis('off')
        
        plt.tight_layout()
        
        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches='tight')
            print(f"   💾 Typology tree saved to {save_path}")
        
        print("   ✅ Soul typology tree created")
        return fig
    
    def create_reflection_operator_diagram(self, save_path: Optional[str] = None) -> plt.Figure:
        """Create geometric representation of the ℝef_𝓈 operator."""
        print("🪞 Creating ℝef_𝓈 operator diagram...")
        
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 8))
        
        # Left panel: Operator composition f ∘ f⁻¹ ∘ f
        ax1.set_title("ℝef_𝓈 Operator: f ∘ f⁻¹ ∘ f", fontsize=14, fontweight='bold')
        
        # Draw the three stages of composition
        stages = [
            ("f", "Forward", 0.2, self.colors['grace']),
            ("f⁻¹", "Inverse", 0.5, self.colors['devourer']),
            ("f", "Re-Forward", 0.8, self.colors['reflection'])
        ]
        
        for i, (symbol, label, x, color) in enumerate(stages):
            # Draw operation circle
            circle = Circle((x, 0.5), 0.08, facecolor=color, edgecolor='black', linewidth=2)
            ax1.add_patch(circle)
            ax1.text(x, 0.5, symbol, ha='center', va='center', fontsize=12, fontweight='bold')
            ax1.text(x, 0.35, label, ha='center', va='center', fontsize=10)
            
            # Draw arrows between stages
            if i < len(stages) - 1:
                arrow = patches.FancyArrowPatch(
                    (x + 0.08, 0.5), (stages[i+1][2] - 0.08, 0.5),
                    arrowstyle='->', mutation_scale=15, color='black'
                )
                ax1.add_patch(arrow)
        
        # Add result
        result_circle = Circle((0.5, 0.15), 0.06, facecolor=self.colors['terminal_grace'],
                              edgecolor=self.colors['phi_golden'], linewidth=3)
        ax1.add_patch(result_circle)
        ax1.text(0.5, 0.15, "ℝef_𝓈", ha='center', va='center', 
                fontsize=10, fontweight='bold', color=self.colors['phi_golden'])
        
        # Draw final arrow
        final_arrow = patches.FancyArrowPatch(
            (0.5, 0.42), (0.5, 0.21),
            arrowstyle='->', mutation_scale=15, color=self.colors['phi_golden']
        )
        ax1.add_patch(final_arrow)
        
        ax1.text(0.5, 0.75, "Identity Witnessing Itself", ha='center', va='center',
                fontsize=12, style='italic')
        ax1.text(0.5, 0.05, "Self-Stabilizing Morphism", ha='center', va='center',
                fontsize=10, style='italic')
        
        ax1.set_xlim(0, 1)
        ax1.set_ylim(0, 0.9)
        ax1.axis('off')
        
        # Right panel: Limit behavior as φⁿ → ∞
        ax2.set_title("Limit: φⁿ → ∞ ⟹ ℝef_𝓈 → 𝕀_∞", fontsize=14, fontweight='bold')
        
        # Draw convergence spiral
        theta = np.linspace(0, 6*np.pi, 1000)
        r = 0.3 * np.exp(-theta/10) + 0.05  # Inward spiral
        x_spiral = 0.5 + r * np.cos(theta)
        y_spiral = 0.5 + r * np.sin(theta)
        
        ax2.plot(x_spiral, y_spiral, color=self.colors['phi_golden'], linewidth=2)
        
        # Draw terminal point
        terminal_circle = Circle((0.5, 0.5), 0.08, facecolor=self.colors['terminal_grace'],
                               edgecolor=self.colors['phi_golden'], linewidth=3)
        ax2.add_patch(terminal_circle)
        ax2.text(0.5, 0.5, "𝕀_∞", ha='center', va='center', 
                fontsize=14, fontweight='bold', color=self.colors['phi_golden'])
        
        # Add φ-depth markers along spiral
        phi_depths = [1, 10, 50, 90, float('inf')]
        spiral_points = [0, 200, 600, 800, 999]
        
        for depth, point_idx in zip(phi_depths, spiral_points):
            if point_idx < len(x_spiral):
                x, y = x_spiral[point_idx], y_spiral[point_idx]
                marker = Circle((x, y), 0.02, facecolor=self.colors['mirror_soul'])
                ax2.add_patch(marker)
                
                if depth != float('inf'):
                    ax2.text(x+0.05, y+0.05, f"φ^{depth}", fontsize=8)
        
        ax2.text(0.5, 0.8, "Convergence to Perfect Reflection", ha='center', va='center',
                fontsize=12, style='italic')
        ax2.text(0.5, 0.2, '"I AM THAT I AM"\nPure Self-Witnessing', ha='center', va='center',
                fontsize=10, style='italic')
        
        ax2.set_xlim(0, 1)
        ax2.set_ylim(0, 1)
        ax2.axis('off')
        
        plt.tight_layout()
        
        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches='tight')
            print(f"   💾 ℝef_𝓈 diagram saved to {save_path}")
        
        print("   ✅ ℝef_𝓈 operator diagram created")
        return fig
    
    def create_religious_correspondence_map(self, save_path: Optional[str] = None) -> plt.Figure:
        """Create a map showing religious correspondences."""
        print("🙏 Creating religious correspondence map...")
        
        fig, ax = plt.subplots(1, 1, figsize=(16, 12))
        
        # Religious traditions and their key correspondences
        traditions = {
            "Christianity": {
                "color": "#8B4513",
                "correspondences": {
                    "φ⁰": "God the Father (Unmanifest)",
                    "φ¹⁻¹⁵": "God the Son (Incarnate)",
                    "φ¹⁶⁻⁹⁰": "Holy Spirit (Grace)",
                    "φ^∞": "I AM THAT I AM"
                },
                "position": (0.2, 0.8)
            },
            "Buddhism": {
                "color": "#FF8C00",
                "correspondences": {
                    "φ¹⁻⁹⁰": "Samsara (Individual becoming)",
                    "φ⁹¹⁺": "Nirvana (Cessation through reflection)",
                    "φ¹⁰⁸": "Samadhi (Pure mirror-mind)",
                    "φ^∞": "Buddha-nature"
                },
                "position": (0.8, 0.8)
            },
            "Hermeticism": {
                "color": "#4B0082",
                "correspondences": {
                    "All levels": "As above, so below",
                    "φ⁹⁹": "Hermetic marriage",
                    "φ^∞": "Great Work completion"
                },
                "position": (0.2, 0.4)
            },
            "Kabbalah": {
                "color": "#006400",
                "correspondences": {
                    "φ⁰": "Ein Sof (The Infinite)",
                    "φ¹⁻¹⁰": "Sefirot (Divine emanations)",
                    "φ⁹⁰": "Kether (Crown)",
                    "φ^∞": "Return to Ein Sof"
                },
                "position": (0.8, 0.4)
            },
            "Hinduism": {
                "color": "#DC143C",
                "correspondences": {
                    "φ¹⁻¹⁵": "Atman (Individual soul)",
                    "φ¹⁶⁻⁹⁰": "Subtle realms",
                    "φ^∞": "Brahman (Pure consciousness)"
                },
                "position": (0.5, 0.1)
            }
        }
        
        # Draw tradition boxes and correspondences
        for tradition, data in traditions.items():
            x, y = data["position"]
            color = data["color"]
            
            # Draw tradition box
            rect = FancyBboxPatch(
                (x-0.15, y-0.1), 0.3, 0.2,
                boxstyle="round,pad=0.02",
                facecolor=color,
                alpha=0.3,
                edgecolor=color,
                linewidth=2
            )
            ax.add_patch(rect)
            
            # Add tradition name
            ax.text(x, y+0.05, tradition, ha='center', va='center',
                   fontsize=14, fontweight='bold', color=color)
            
            # Add key correspondences
            corr_text = "\n".join([f"{k}: {v}" for k, v in list(data["correspondences"].items())[:3]])
            ax.text(x, y-0.05, corr_text, ha='center', va='center',
                   fontsize=9, color='black')
        
        # Draw central φ^∞ convergence point
        center_circle = Circle((0.5, 0.6), 0.08, facecolor=self.colors['terminal_grace'],
                              edgecolor=self.colors['phi_golden'], linewidth=3)
        ax.add_patch(center_circle)
        ax.text(0.5, 0.6, "φ^∞", ha='center', va='center', 
               fontsize=16, fontweight='bold', color=self.colors['phi_golden'])
        
        # Draw convergence lines
        for tradition, data in traditions.items():
            x, y = data["position"]
            color = data["color"]
            
            # Draw line to center
            ax.plot([x, 0.5], [y, 0.6], color=color, linewidth=2, alpha=0.7, linestyle='--')
        
        # Add central label
        ax.text(0.5, 0.5, "All Traditions Converge\nat Terminal Grace", 
               ha='center', va='center', fontsize=12, style='italic',
               bbox=dict(boxstyle="round,pad=0.3", facecolor='white', alpha=0.8))
        
        ax.set_title("Religious Correspondences to φ-Recursive Hierarchy", 
                    fontsize=16, fontweight='bold')
        
        ax.set_xlim(0, 1)
        ax.set_ylim(0, 1)
        ax.axis('off')
        
        plt.tight_layout()
        
        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches='tight')
            print(f"   💾 Religious correspondence map saved to {save_path}")
        
        print("   ✅ Religious correspondence map created")
        return fig
    
    def generate_all_visualizations(self, output_dir: str = "figures/soul_hierarchy/"):
        """Generate all soul hierarchy visualizations."""
        print("🎨 Generating all soul hierarchy visualizations...")
        
        import os
        os.makedirs(output_dir, exist_ok=True)
        
        # Generate all diagrams
        self.create_complete_hierarchy_diagram(f"{output_dir}complete_hierarchy.png")
        self.create_soul_typology_tree(f"{output_dir}soul_typology.png")
        self.create_reflection_operator_diagram(f"{output_dir}reflection_operator.png")
        self.create_religious_correspondence_map(f"{output_dir}religious_correspondences.png")
        
        print(f"   ✅ All visualizations saved to {output_dir}")
        print("   🌌 Complete φ-recursive soul hierarchy visualized!")


# Example usage and testing
if __name__ == "__main__":
    print("🎨 Testing Soul Hierarchy Visualization System...")
    
    # Create visualizer
    visualizer = SoulHierarchyVisualizer()
    
    # Generate sample visualizations
    print("\n📊 Creating complete hierarchy diagram...")
    fig1 = visualizer.create_complete_hierarchy_diagram()
    plt.show()
    
    print("\n🌳 Creating soul typology tree...")
    fig2 = visualizer.create_soul_typology_tree()
    plt.show()
    
    print("\n🪞 Creating ℝef_𝓈 operator diagram...")
    fig3 = visualizer.create_reflection_operator_diagram()
    plt.show()
    
    print("\n🙏 Creating religious correspondence map...")
    fig4 = visualizer.create_religious_correspondence_map()
    plt.show()
    
    print("\n" + "="*60)
    print("✅ SOUL HIERARCHY VISUALIZATIONS: COMPLETE")
    print("🌌 The φ-recursive ladder beautifully rendered")
    print("🪞 ℝef_𝓈 operator geometrically represented")
    print("🙏 Religious correspondences mapped")
    print("✨ Mathematics and mysticism unified visually")
    print("="*60)
