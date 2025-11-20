"""
SVG Graphics Library for Executive Minimalism Design
Custom vector graphics aligned with Navy (#1A1F2E), Gold (#D4AF37), White color palette
All graphics designed for professional, high-ticket presentation aesthetics
"""

# Color constants matching the design system
NAVY = "#1A1F2E"
GOLD = "#D4AF37"
WHITE = "#FFFFFF"
LIGHT_GRAY = "#F5F5F5"


def create_lightbulb_icon(size=80, color=GOLD):
    """Insight/Ideas icon - lightbulb in minimalist style"""
    return f'''<svg width="{size}" height="{size}" viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg">
  <path d="M50 10 C32 10 20 25 20 40 C20 50 25 58 32 63 L32 75 C32 78 34 80 37 80 L63 80 C66 80 68 78 68 75 L68 63 C75 58 80 50 80 40 C80 25 68 10 50 10 Z"
        fill="none" stroke="{color}" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>
  <line x1="40" y1="85" x2="60" y2="85" stroke="{color}" stroke-width="3" stroke-linecap="round"/>
  <line x1="42" y1="90" x2="58" y2="90" stroke="{color}" stroke-width="3" stroke-linecap="round"/>
  <line x1="35" y1="25" x2="28" y2="22" stroke="{color}" stroke-width="2.5" stroke-linecap="round"/>
  <line x1="65" y1="25" x2="72" y2="22" stroke="{color}" stroke-width="2.5" stroke-linecap="round"/>
  <line x1="20" y1="40" x2="12" y2="40" stroke="{color}" stroke-width="2.5" stroke-linecap="round"/>
  <line x1="80" y1="40" x2="88" y2="40" stroke="{color}" stroke-width="2.5" stroke-linecap="round"/>
</svg>'''


def create_target_icon(size=80, color=GOLD):
    """Goals/Achievement icon - target with arrow"""
    return f'''<svg width="{size}" height="{size}" viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg">
  <circle cx="50" cy="50" r="35" fill="none" stroke="{color}" stroke-width="2.5"/>
  <circle cx="50" cy="50" r="25" fill="none" stroke="{color}" stroke-width="2.5"/>
  <circle cx="50" cy="50" r="15" fill="none" stroke="{color}" stroke-width="2.5"/>
  <circle cx="50" cy="50" r="6" fill="{color}"/>
  <path d="M70 20 L75 15 L85 25 L80 30 Z M75 15 L80 30 L60 50"
        fill="{color}" stroke="{color}" stroke-width="2" stroke-linejoin="round"/>
</svg>'''


def create_growth_arrow_icon(size=80, color=GOLD):
    """Growth/Progress icon - upward trending arrow"""
    return f'''<svg width="{size}" height="{size}" viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg">
  <polyline points="10,80 30,65 45,70 60,50 75,55 90,25"
            fill="none" stroke="{color}" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round"/>
  <circle cx="10" cy="80" r="3" fill="{color}"/>
  <circle cx="30" cy="65" r="3" fill="{color}"/>
  <circle cx="45" cy="70" r="3" fill="{color}"/>
  <circle cx="60" cy="50" r="3" fill="{color}"/>
  <circle cx="75" cy="55" r="3" fill="{color}"/>
  <polygon points="90,25 85,35 95,30" fill="{color}"/>
  <line x1="90" y1="25" x2="90" y2="10" stroke="{color}" stroke-width="3" stroke-linecap="round"/>
  <line x1="90" y1="25" x2="75" y2="25" stroke="{color}" stroke-width="3" stroke-linecap="round"/>
</svg>'''


def create_shield_icon(size=80, color=GOLD):
    """Resilience/Protection icon - shield"""
    return f'''<svg width="{size}" height="{size}" viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg">
  <path d="M50 10 L20 25 L20 45 C20 65 35 80 50 90 C65 80 80 65 80 45 L80 25 Z"
        fill="none" stroke="{color}" stroke-width="3" stroke-linejoin="round"/>
  <polyline points="35,50 45,60 65,35"
            fill="none" stroke="{color}" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round"/>
</svg>'''


def create_brain_icon(size=80, color=GOLD):
    """Mindset/Psychology icon - brain"""
    return f'''<svg width="{size}" height="{size}" viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg">
  <path d="M30 35 C25 35 20 40 20 45 C20 48 21 50 23 52 C21 54 20 57 20 60 C20 65 24 70 30 70 L70 70 C76 70 80 65 80 60 C80 57 79 54 77 52 C79 50 80 48 80 45 C80 40 75 35 70 35 C68 25 58 18 50 18 C42 18 32 25 30 35 Z"
        fill="none" stroke="{color}" stroke-width="2.5" stroke-linejoin="round"/>
  <path d="M35 40 C35 38 36 35 40 35" fill="none" stroke="{color}" stroke-width="2" stroke-linecap="round"/>
  <path d="M45 45 C45 42 47 40 50 40" fill="none" stroke="{color}" stroke-width="2" stroke-linecap="round"/>
  <path d="M55 50 C57 50 60 52 60 55" fill="none" stroke="{color}" stroke-width="2" stroke-linecap="round"/>
  <path d="M40 55 C38 57 38 60 40 62" fill="none" stroke="{color}" stroke-width="2" stroke-linecap="round"/>
</svg>'''


def create_gear_icon(size=80, color=GOLD):
    """System/Process icon - gear"""
    return f'''<svg width="{size}" height="{size}" viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg">
  <path d="M50 20 L55 20 L57 15 L63 18 L68 15 L70 20 L75 22 L75 28 L80 32 L77 38 L80 43 L75 47 L75 53 L70 55 L68 60 L63 57 L57 60 L55 55 L50 55 L45 55 L43 60 L37 57 L32 60 L30 55 L25 53 L25 47 L20 43 L23 38 L20 32 L25 28 L25 22 L30 20 L32 15 L37 18 L43 15 L45 20 Z"
        fill="none" stroke="{color}" stroke-width="2.5" stroke-linejoin="round"/>
  <circle cx="50" cy="37.5" r="10" fill="none" stroke="{color}" stroke-width="2.5"/>
</svg>'''


def create_checklist_icon(size=80, color=GOLD):
    """Tasks/Completion icon - checklist"""
    return f'''<svg width="{size}" height="{size}" viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg">
  <rect x="20" y="15" width="60" height="70" rx="3"
        fill="none" stroke="{color}" stroke-width="2.5"/>
  <polyline points="28,30 35,37 48,24"
            fill="none" stroke="{color}" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/>
  <line x1="55" y1="30" x2="72" y2="30" stroke="{color}" stroke-width="2.5" stroke-linecap="round"/>
  <polyline points="28,50 35,57 48,44"
            fill="none" stroke="{color}" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/>
  <line x1="55" y1="50" x2="72" y2="50" stroke="{color}" stroke-width="2.5" stroke-linecap="round"/>
  <circle cx="32" cy="70" r="4" fill="none" stroke="{color}" stroke-width="2.5"/>
  <line x1="55" y1="70" x2="72" y2="70" stroke="{color}" stroke-width="2.5" stroke-linecap="round"/>
</svg>'''


def create_trophy_icon(size=80, color=GOLD):
    """Achievement/Success icon - trophy"""
    return f'''<svg width="{size}" height="{size}" viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg">
  <path d="M35 20 L65 20 L65 35 C65 48 58 55 50 55 C42 55 35 48 35 35 Z"
        fill="none" stroke="{color}" stroke-width="2.5" stroke-linejoin="round"/>
  <path d="M65 25 L75 25 C78 25 80 27 80 30 L80 35 C80 38 78 40 75 40 L65 40"
        fill="none" stroke="{color}" stroke-width="2.5" stroke-linejoin="round"/>
  <path d="M35 25 L25 25 C22 25 20 27 20 30 L20 35 C20 38 22 40 25 40 L35 40"
        fill="none" stroke="{color}" stroke-width="2.5" stroke-linejoin="round"/>
  <line x1="50" y1="55" x2="50" y2="70" stroke="{color}" stroke-width="2.5"/>
  <rect x="40" y="70" width="20" height="8" rx="2"
        fill="none" stroke="{color}" stroke-width="2.5"/>
  <line x1="35" y1="78" x2="65" y2="78" stroke="{color}" stroke-width="3" stroke-linecap="round"/>
</svg>'''


def create_mountain_icon(size=80, color=GOLD):
    """Achievement/Peak Performance icon - mountain peak"""
    return f'''<svg width="{size}" height="{size}" viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg">
  <polyline points="10,80 35,40 50,55 70,20 90,80"
            fill="none" stroke="{color}" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>
  <polygon points="70,20 65,30 75,25" fill="{color}"/>
  <line x1="70" y1="20" x2="70" y2="30" stroke="{color}" stroke-width="2.5"/>
  <circle cx="70" cy="20" r="5" fill="none" stroke="{color}" stroke-width="2"/>
</svg>'''


def create_compass_icon(size=80, color=GOLD):
    """Direction/Vision icon - compass"""
    return f'''<svg width="{size}" height="{size}" viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg">
  <circle cx="50" cy="50" r="35" fill="none" stroke="{color}" stroke-width="2.5"/>
  <polygon points="50,25 45,50 50,55 55,50" fill="{color}"/>
  <polygon points="50,75 55,50 50,45 45,50" fill="none" stroke="{color}" stroke-width="2"/>
  <line x1="50" y1="15" x2="50" y2="22" stroke="{color}" stroke-width="2.5" stroke-linecap="round"/>
  <line x1="50" y1="78" x2="50" y2="85" stroke="{color}" stroke-width="2.5" stroke-linecap="round"/>
  <line x1="85" y1="50" x2="78" y2="50" stroke="{color}" stroke-width="2.5" stroke-linecap="round"/>
  <line x1="22" y1="50" x2="15" y2="50" stroke="{color}" stroke-width="2.5" stroke-linecap="round"/>
  <text x="50" y="18" font-family="Arial" font-size="12" font-weight="bold" fill="{color}" text-anchor="middle">N</text>
</svg>'''


def create_transformation_arrow(size=100, color=GOLD):
    """Transformation icon - curved arrow showing progression"""
    return f'''<svg width="{size}" height="{size}" viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg">
  <path d="M15 70 Q30 30 85 30"
        fill="none" stroke="{color}" stroke-width="3.5" stroke-linecap="round"/>
  <polygon points="85,30 75,25 75,35" fill="{color}"/>
  <circle cx="15" cy="70" r="5" fill="{color}"/>
</svg>'''


def create_network_icon(size=80, color=GOLD):
    """Connection/Network icon - connected nodes"""
    return f'''<svg width="{size}" height="{size}" viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg">
  <circle cx="50" cy="30" r="8" fill="{color}"/>
  <circle cx="25" cy="60" r="7" fill="{color}"/>
  <circle cx="75" cy="60" r="7" fill="{color}"/>
  <circle cx="35" cy="80" r="6" fill="{color}"/>
  <circle cx="65" cy="80" r="6" fill="{color}"/>
  <line x1="50" y1="38" x2="25" y2="53" stroke="{color}" stroke-width="2.5"/>
  <line x1="50" y1="38" x2="75" y2="53" stroke="{color}" stroke-width="2.5"/>
  <line x1="25" y1="67" x2="35" y2="74" stroke="{color}" stroke-width="2.5"/>
  <line x1="75" y1="67" x2="65" y2="74" stroke="{color}" stroke-width="2.5"/>
  <line x1="35" y1="74" x2="50" y2="38" stroke="{color}" stroke-width="2" opacity="0.4"/>
  <line x1="65" y1="74" x2="50" y2="38" stroke="{color}" stroke-width="2" opacity="0.4"/>
</svg>'''


def create_dollar_growth_icon(size=80, color=GOLD):
    """Financial Growth icon - dollar sign with upward arrow"""
    return f'''<svg width="{size}" height="{size}" viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg">
  <path d="M40 30 L60 30 C65 30 68 33 68 38 C68 43 65 46 60 46 L40 46 C35 46 32 49 32 54 C32 59 35 62 40 62 L60 62"
        fill="none" stroke="{color}" stroke-width="3" stroke-linecap="round"/>
  <line x1="50" y1="20" x2="50" y2="72" stroke="{color}" stroke-width="3" stroke-linecap="round"/>
  <polyline points="70,70 80,60 90,70" fill="none" stroke="{color}" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/>
  <line x1="80" y1="60" x2="80" y2="85" stroke="{color}" stroke-width="2.5" stroke-linecap="round"/>
</svg>'''


def create_rocket_icon(size=80, color=GOLD):
    """Launch/Momentum icon - rocket"""
    return f'''<svg width="{size}" height="{size}" viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg">
  <path d="M50 15 C45 15 40 20 38 30 L38 50 L35 55 L35 65 L40 60 L40 70 L50 75 L60 70 L60 60 L65 65 L65 55 L62 50 L62 30 C60 20 55 15 50 15 Z"
        fill="none" stroke="{color}" stroke-width="2.5" stroke-linejoin="round"/>
  <circle cx="50" cy="30" r="5" fill="none" stroke="{color}" stroke-width="2"/>
  <path d="M40 75 L35 85 L38 87 L45 77" fill="{color}" stroke="{color}" stroke-width="1.5"/>
  <path d="M60 75 L65 85 L62 87 L55 77" fill="{color}" stroke="{color}" stroke-width="1.5"/>
  <line x1="47" y1="82" x2="45" y2="88" stroke="{color}" stroke-width="2" stroke-linecap="round"/>
  <line x1="53" y1="82" x2="55" y2="88" stroke="{color}" stroke-width="2" stroke-linecap="round"/>
</svg>'''


def create_calendar_icon(size=80, color=GOLD):
    """Timeline/Schedule icon - calendar"""
    return f'''<svg width="{size}" height="{size}" viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg">
  <rect x="20" y="25" width="60" height="60" rx="3"
        fill="none" stroke="{color}" stroke-width="2.5"/>
  <line x1="20" y1="38" x2="80" y2="38" stroke="{color}" stroke-width="2.5"/>
  <line x1="35" y1="20" x2="35" y2="30" stroke="{color}" stroke-width="2.5" stroke-linecap="round"/>
  <line x1="65" y1="20" x2="65" y2="30" stroke="{color}" stroke-width="2.5" stroke-linecap="round"/>
  <circle cx="32" cy="50" r="2.5" fill="{color}"/>
  <circle cx="44" cy="50" r="2.5" fill="{color}"/>
  <circle cx="56" cy="50" r="2.5" fill="{color}"/>
  <circle cx="68" cy="50" r="2.5" fill="{color}"/>
  <circle cx="32" cy="62" r="2.5" fill="{color}"/>
  <circle cx="44" cy="62" r="2.5" fill="{color}"/>
  <circle cx="56" cy="62" r="2.5" fill="{color}"/>
  <circle cx="68" cy="62" r="2.5" fill="{color}"/>
  <circle cx="32" cy="74" r="2.5" fill="{color}"/>
  <circle cx="44" cy="74" r="2.5" fill="{color}"/>
</svg>'''


def create_metrics_dashboard_icon(size=80, color=GOLD):
    """Tracking/Analytics icon - metrics dashboard"""
    return f'''<svg width="{size}" height="{size}" viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg">
  <rect x="15" y="20" width="70" height="60" rx="3"
        fill="none" stroke="{color}" stroke-width="2.5"/>
  <line x1="15" y1="35" x2="85" y2="35" stroke="{color}" stroke-width="2.5"/>
  <rect x="25" y="65" width="8" height="10" fill="{color}"/>
  <rect x="38" y="55" width="8" height="20" fill="{color}"/>
  <rect x="51" y="48" width="8" height="27" fill="{color}"/>
  <rect x="64" y="60" width="8" height="15" fill="{color}"/>
  <circle cx="25" cy="28" r="2" fill="{color}"/>
  <circle cx="35" cy="28" r="2" fill="{color}"/>
  <circle cx="45" cy="28" r="2" fill="{color}"/>
</svg>'''


def create_pillar_icon(size=80, color=GOLD):
    """Foundation/Pillar icon - classical pillar"""
    return f'''<svg width="{size}" height="{size}" viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg">
  <rect x="35" y="25" width="30" height="50" fill="none" stroke="{color}" stroke-width="2.5"/>
  <rect x="30" y="20" width="40" height="5" fill="{color}"/>
  <rect x="30" y="75" width="40" height="5" fill="{color}"/>
  <line x1="40" y1="30" x2="40" y2="70" stroke="{color}" stroke-width="2"/>
  <line x1="50" y1="30" x2="50" y2="70" stroke="{color}" stroke-width="2"/>
  <line x1="60" y1="30" x2="60" y2="70" stroke="{color}" stroke-width="2"/>
</svg>'''


def create_geometric_pattern_corner(size=120, color=GOLD):
    """Decorative corner element - geometric pattern"""
    return f'''<svg width="{size}" height="{size}" viewBox="0 0 120 120" xmlns="http://www.w3.org/2000/svg">
  <line x1="0" y1="20" x2="100" y2="20" stroke="{color}" stroke-width="2" opacity="0.6"/>
  <line x1="20" y1="0" x2="20" y2="100" stroke="{color}" stroke-width="2" opacity="0.6"/>
  <line x1="0" y1="40" x2="80" y2="40" stroke="{color}" stroke-width="1.5" opacity="0.4"/>
  <line x1="40" y1="0" x2="40" y2="80" stroke="{color}" stroke-width="1.5" opacity="0.4"/>
  <circle cx="20" cy="20" r="4" fill="{color}"/>
</svg>'''


def create_divider_line(width=600, color=GOLD):
    """Decorative divider line with center accent"""
    center = width // 2
    return f'''<svg width="{width}" height="20" viewBox="0 0 {width} 20" xmlns="http://www.w3.org/2000/svg">
  <line x1="0" y1="10" x2="{width}" y2="10" stroke="{color}" stroke-width="2"/>
  <circle cx="{center}" cy="10" r="5" fill="{color}"/>
</svg>'''


def create_confidence_icon(size=80, color=GOLD):
    """Confidence/Strength icon - flexed arm/strength symbol"""
    return f'''<svg width="{size}" height="{size}" viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg">
  <circle cx="50" cy="30" r="12" fill="none" stroke="{color}" stroke-width="2.5"/>
  <path d="M50 42 L50 60 M42 52 L50 60 L58 52"
        fill="none" stroke="{color}" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>
  <path d="M38 60 L38 75 C38 78 40 80 43 80 L57 80 C60 80 62 78 62 75 L62 60"
        fill="none" stroke="{color}" stroke-width="2.5" stroke-linecap="round"/>
  <circle cx="38" cy="60" r="4" fill="{color}"/>
  <circle cx="62" cy="60" r="4" fill="{color}"/>
</svg>'''


def create_lock_unlock_icon(size=80, color=GOLD):
    """Breakthrough/Unlock icon - open lock"""
    return f'''<svg width="{size}" height="{size}" viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg">
  <rect x="35" y="50" width="30" height="30" rx="3"
        fill="none" stroke="{color}" stroke-width="2.5"/>
  <circle cx="50" cy="65" r="5" fill="{color}"/>
  <line x1="50" y1="70" x2="50" y2="75" stroke="{color}" stroke-width="2.5" stroke-linecap="round"/>
  <path d="M35 50 L35 35 C35 27 41 20 50 20 C59 20 65 27 65 35 L65 45"
        fill="none" stroke="{color}" stroke-width="2.5" stroke-linecap="round"/>
</svg>'''


# Helper function to save SVG to file
def save_svg(svg_content, filename):
    """Save SVG content to a file"""
    with open(filename, 'w') as f:
        f.write(svg_content)


# Export all icons to a dictionary for easy access
ICON_LIBRARY = {
    'lightbulb': create_lightbulb_icon,
    'target': create_target_icon,
    'growth_arrow': create_growth_arrow_icon,
    'shield': create_shield_icon,
    'brain': create_brain_icon,
    'gear': create_gear_icon,
    'checklist': create_checklist_icon,
    'trophy': create_trophy_icon,
    'mountain': create_mountain_icon,
    'compass': create_compass_icon,
    'transformation': create_transformation_arrow,
    'network': create_network_icon,
    'dollar_growth': create_dollar_growth_icon,
    'rocket': create_rocket_icon,
    'calendar': create_calendar_icon,
    'metrics': create_metrics_dashboard_icon,
    'pillar': create_pillar_icon,
    'corner_pattern': create_geometric_pattern_corner,
    'divider': create_divider_line,
    'confidence': create_confidence_icon,
    'unlock': create_lock_unlock_icon,
}


if __name__ == "__main__":
    # Test: Generate all icons as individual SVG files
    import os
    output_dir = "svg_icons"
    os.makedirs(output_dir, exist_ok=True)

    for name, icon_func in ICON_LIBRARY.items():
        if name in ['corner_pattern', 'divider']:
            svg = icon_func()
        else:
            svg = icon_func(size=100, color=GOLD)

        save_svg(svg, os.path.join(output_dir, f"{name}.svg"))

    print(f"Generated {len(ICON_LIBRARY)} SVG icons in {output_dir}/")
