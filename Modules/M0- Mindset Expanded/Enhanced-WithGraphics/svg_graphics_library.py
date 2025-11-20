"""
SVG Graphics Library for M0- Mindset Module
Creates custom vector graphics in navy and gold colors
All graphics are designed to match Executive Minimalism aesthetic
"""

# Concept A Colors
NAVY = "#1A1F2E"
GOLD = "#D4AF37"
WHITE = "#FFFFFF"


def target_icon(size=100):
    """Concentric circles target/bullseye - for vision, goals"""
    svg = f'''<svg width="{size}" height="{size}" viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg">
        <circle cx="50" cy="50" r="40" fill="none" stroke="{GOLD}" stroke-width="3"/>
        <circle cx="50" cy="50" r="28" fill="none" stroke="{GOLD}" stroke-width="3"/>
        <circle cx="50" cy="50" r="16" fill="none" stroke="{GOLD}" stroke-width="3"/>
        <circle cx="50" cy="50" r="5" fill="{GOLD}"/>
    </svg>'''
    return svg


def growth_curve_icon(size=300):
    """Exponential growth curve - for compound effect"""
    width = int(size * 4/3)  # 4:3 aspect ratio
    height = size
    svg = f'''<svg width="{width}" height="{height}" viewBox="0 0 400 300" xmlns="http://www.w3.org/2000/svg">
        <!-- Exponential curve -->
        <path d="M 20 280 Q 80 260, 120 220 T 200 140 T 280 40 T 380 10"
              fill="none" stroke="{GOLD}" stroke-width="4" stroke-linecap="round"/>

        <!-- Dots along curve -->
        <circle cx="20" cy="280" r="5" fill="{GOLD}"/>
        <circle cx="120" cy="220" r="5" fill="{GOLD}"/>
        <circle cx="200" cy="140" r="5" fill="{GOLD}"/>
        <circle cx="280" cy="40" r="5" fill="{GOLD}"/>
        <circle cx="380" cy="10" r="5" fill="{GOLD}"/>

        <!-- Labels -->
        <text x="20" y="295" font-family="Arial" font-size="14" fill="{NAVY}" text-anchor="middle">Day 1</text>
        <text x="380" y="5" font-family="Arial" font-size="14" fill="{GOLD}" text-anchor="end" font-weight="bold">6 Months</text>
    </svg>'''
    return svg


def cycle_arrows_icon(size=200):
    """Circular arrows showing cycle - for Action→Results→Confidence"""
    svg = f'''<svg width="{size}" height="{size}" viewBox="0 0 200 200" xmlns="http://www.w3.org/2000/svg">
        <!-- Circular arrows -->
        <path d="M 100 30 A 70 70 0 0 1 170 100"
              fill="none" stroke="{GOLD}" stroke-width="4" stroke-linecap="round"/>
        <polygon points="175,95 165,105 170,110" fill="{GOLD}"/>

        <path d="M 170 100 A 70 70 0 0 1 100 170"
              fill="none" stroke="{GOLD}" stroke-width="4" stroke-linecap="round"/>
        <polygon points="105,175 95,165 90,170" fill="{GOLD}"/>

        <path d="M 100 170 A 70 70 0 0 1 30 100"
              fill="none" stroke="{GOLD}" stroke-width="4" stroke-linecap="round"/>
        <polygon points="25,105 35,95 30,90" fill="{GOLD}"/>

        <path d="M 30 100 A 70 70 0 0 1 100 30"
              fill="none" stroke="{GOLD}" stroke-width="4" stroke-linecap="round"/>
        <polygon points="95,25 105,35 110,30" fill="{GOLD}"/>

        <!-- Center circle -->
        <circle cx="100" cy="100" r="25" fill="none" stroke="{GOLD}" stroke-width="2"/>
    </svg>'''
    return svg


def winding_path_icon(size=300):
    """Non-linear winding path - for success journey"""
    width = int(size * 4/3)  # 4:3 aspect ratio
    height = size
    svg = f'''<svg width="{width}" height="{height}" viewBox="0 0 400 300" xmlns="http://www.w3.org/2000/svg">
        <!-- Winding path -->
        <path d="M 20 280 Q 80 260, 100 220 Q 120 180, 80 160 Q 40 140, 100 120
                 Q 160 100, 180 80 Q 200 60, 240 70 Q 280 80, 300 50 Q 320 20, 380 20"
              fill="none" stroke="{GOLD}" stroke-width="5" stroke-linecap="round"/>

        <!-- Start marker -->
        <circle cx="20" cy="280" r="8" fill="{NAVY}"/>
        <text x="20" y="298" font-family="Arial" font-size="12" fill="{NAVY}" text-anchor="middle" font-weight="bold">START</text>

        <!-- End marker -->
        <circle cx="380" cy="20" r="8" fill="{GOLD}"/>
        <text x="380" y="10" font-family="Arial" font-size="12" fill="{GOLD}" text-anchor="middle" font-weight="bold">SUCCESS</text>

        <!-- Waypoint dots -->
        <circle cx="100" cy="220" r="4" fill="{GOLD}"/>
        <circle cx="80" cy="160" r="4" fill="{GOLD}"/>
        <circle cx="180" cy="80" r="4" fill="{GOLD}"/>
        <circle cx="300" cy="50" r="4" fill="{GOLD}"/>
    </svg>'''
    return svg


def pillar_icon(size=80):
    """Greek column/pillar - for Three Pillars framework"""
    svg = f'''<svg width="{size}" height="{size}" viewBox="0 0 80 100" xmlns="http://www.w3.org/2000/svg">
        <!-- Capital -->
        <rect x="10" y="10" width="60" height="12" fill="{GOLD}"/>
        <rect x="5" y="18" width="70" height="4" fill="{GOLD}"/>

        <!-- Column -->
        <rect x="22" y="22" width="36" height="56" fill="none" stroke="{GOLD}" stroke-width="3"/>
        <line x1="28" y1="22" x2="28" y2="78" stroke="{GOLD}" stroke-width="1"/>
        <line x1="40" y1="22" x2="40" y2="78" stroke="{GOLD}" stroke-width="1"/>
        <line x1="52" y1="22" x2="52" y2="78" stroke="{GOLD}" stroke-width="1"/>

        <!-- Base -->
        <rect x="5" y="78" width="70" height="4" fill="{GOLD}"/>
        <rect x="10" y="82" width="60" height="8" fill="{GOLD}"/>
    </svg>'''
    return svg


def shark_icon(size=120):
    """Minimalist shark silhouette - for relentless execution"""
    svg = f'''<svg width="{size}" height="{size}" viewBox="0 0 120 80" xmlns="http://www.w3.org/2000/svg">
        <!-- Shark body -->
        <path d="M 10 40 Q 30 35, 50 35 Q 70 35, 85 38 Q 100 41, 110 40 Q 105 43, 95 44 Q 80 45, 50 45 Q 30 45, 10 40 Z"
              fill="{NAVY}"/>

        <!-- Dorsal fin -->
        <path d="M 55 35 L 60 10 L 65 35 Z" fill="{NAVY}"/>

        <!-- Tail fin -->
        <path d="M 10 40 L 5 30 L 8 40 L 5 50 Z" fill="{NAVY}"/>

        <!-- Pectoral fin -->
        <path d="M 45 45 L 40 60 L 50 45 Z" fill="{NAVY}"/>
    </svg>'''
    return svg


def gear_icon(size=100):
    """Gear/system icon - for systems thinking"""
    svg = f'''<svg width="{size}" height="{size}" viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg">
        <!-- Center circle -->
        <circle cx="50" cy="50" r="18" fill="none" stroke="{GOLD}" stroke-width="3"/>

        <!-- Gear teeth (8 teeth) -->
        <rect x="48" y="12" width="4" height="18" fill="{GOLD}"/>
        <rect x="70" y="22" width="18" height="4" fill="{GOLD}" transform="rotate(45 50 50)"/>
        <rect x="80" y="48" width="18" height="4" fill="{GOLD}"/>
        <rect x="70" y="74" width="18" height="4" fill="{GOLD}" transform="rotate(-45 50 50)"/>
        <rect x="48" y="70" width="4" height="18" fill="{GOLD}"/>
        <rect x="12" y="74" width="18" height="4" fill="{GOLD}" transform="rotate(45 50 50)"/>
        <rect x="2" y="48" width="18" height="4" fill="{GOLD}"/>
        <rect x="12" y="22" width="18" height="4" fill="{GOLD}" transform="rotate(-45 50 50)"/>
    </svg>'''
    return svg


def calendar_icon(size=80):
    """Calendar icon - for weekly rhythm"""
    svg = f'''<svg width="{size}" height="{size}" viewBox="0 0 80 80" xmlns="http://www.w3.org/2000/svg">
        <!-- Calendar outline -->
        <rect x="10" y="15" width="60" height="55" fill="none" stroke="{GOLD}" stroke-width="3" rx="3"/>

        <!-- Top bar -->
        <rect x="10" y="15" width="60" height="12" fill="{GOLD}" rx="3"/>

        <!-- Rings -->
        <line x1="25" y1="10" x2="25" y2="20" stroke="{GOLD}" stroke-width="3" stroke-linecap="round"/>
        <line x1="55" y1="10" x2="55" y2="20" stroke="{GOLD}" stroke-width="3" stroke-linecap="round"/>

        <!-- Date dots -->
        <circle cx="22" cy="38" r="3" fill="{GOLD}"/>
        <circle cx="40" cy="38" r="3" fill="{GOLD}"/>
        <circle cx="58" cy="38" r="3" fill="{GOLD}"/>
        <circle cx="22" cy="52" r="3" fill="{GOLD}"/>
        <circle cx="40" cy="52" r="3" fill="{GOLD}"/>
        <circle cx="58" cy="52" r="3" fill="{GOLD}"/>
    </svg>'''
    return svg


def dashboard_icon(size=100):
    """Dashboard/metrics gauge - for tracking"""
    svg = f'''<svg width="{size}" height="{size}" viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg">
        <!-- Gauge arc -->
        <path d="M 20 80 A 40 40 0 0 1 80 80"
              fill="none" stroke="{GOLD}" stroke-width="4" stroke-linecap="round"/>

        <!-- Tick marks -->
        <line x1="20" y1="80" x2="25" y2="75" stroke="{GOLD}" stroke-width="2"/>
        <line x1="30" y1="60" x2="35" y2="58" stroke="{GOLD}" stroke-width="2"/>
        <line x1="50" y1="50" x2="50" y2="45" stroke="{GOLD}" stroke-width="2"/>
        <line x1="70" y1="60" x2="65" y2="58" stroke="{GOLD}" stroke-width="2"/>
        <line x1="80" y1="80" x2="75" y2="75" stroke="{GOLD}" stroke-width="2"/>

        <!-- Needle -->
        <line x1="50" y1="80" x2="62" y2="58" stroke="{NAVY}" stroke-width="3" stroke-linecap="round"/>

        <!-- Center dot -->
        <circle cx="50" cy="80" r="4" fill="{NAVY}"/>
    </svg>'''
    return svg


def network_icon(size=100):
    """Network nodes - for opportunities/connections"""
    svg = f'''<svg width="{size}" height="{size}" viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg">
        <!-- Connection lines -->
        <line x1="50" y1="20" x2="20" y2="60" stroke="{GOLD}" stroke-width="2"/>
        <line x1="50" y1="20" x2="80" y2="60" stroke="{GOLD}" stroke-width="2"/>
        <line x1="50" y1="20" x2="50" y2="80" stroke="{GOLD}" stroke-width="2"/>
        <line x1="20" y1="60" x2="80" y2="60" stroke="{GOLD}" stroke-width="2"/>
        <line x1="20" y1="60" x2="50" y2="80" stroke="{GOLD}" stroke-width="2"/>
        <line x1="80" y1="60" x2="50" y2="80" stroke="{GOLD}" stroke-width="2"/>

        <!-- Nodes -->
        <circle cx="50" cy="20" r="8" fill="{GOLD}"/>
        <circle cx="20" cy="60" r="8" fill="{GOLD}"/>
        <circle cx="80" cy="60" r="8" fill="{GOLD}"/>
        <circle cx="50" cy="80" r="8" fill="{GOLD}"/>
    </svg>'''
    return svg


def checkmark_icon(size=60):
    """Checkmark - for completion, success"""
    svg = f'''<svg width="{size}" height="{size}" viewBox="0 0 60 60" xmlns="http://www.w3.org/2000/svg">
        <path d="M 10 30 L 25 45 L 50 15"
              fill="none" stroke="{GOLD}" stroke-width="6" stroke-linecap="round" stroke-linejoin="round"/>
    </svg>'''
    return svg


def arrow_up_icon(size=60):
    """Upward arrow - for growth, improvement"""
    svg = f'''<svg width="{size}" height="{size}" viewBox="0 0 60 60" xmlns="http://www.w3.org/2000/svg">
        <!-- Arrow shaft -->
        <rect x="26" y="15" width="8" height="35" fill="{GOLD}"/>

        <!-- Arrow head -->
        <path d="M 30 10 L 15 25 L 45 25 Z" fill="{GOLD}"/>
    </svg>'''
    return svg


def lightbulb_icon(size=80):
    """Lightbulb - for insights, ideas"""
    svg = f'''<svg width="{size}" height="{size}" viewBox="0 0 80 100" xmlns="http://www.w3.org/2000/svg">
        <!-- Bulb -->
        <circle cx="40" cy="35" r="20" fill="none" stroke="{GOLD}" stroke-width="3"/>

        <!-- Base -->
        <rect x="32" y="55" width="16" height="8" fill="none" stroke="{GOLD}" stroke-width="2"/>
        <rect x="30" y="63" width="20" height="4" fill="{GOLD}"/>

        <!-- Light rays -->
        <line x1="40" y1="10" x2="40" y2="2" stroke="{GOLD}" stroke-width="3" stroke-linecap="round"/>
        <line x1="60" y1="15" x2="66" y2="9" stroke="{GOLD}" stroke-width="3" stroke-linecap="round"/>
        <line x1="65" y1="35" x2="73" y2="35" stroke="{GOLD}" stroke-width="3" stroke-linecap="round"/>
        <line x1="20" y1="15" x2="14" y2="9" stroke="{GOLD}" stroke-width="3" stroke-linecap="round"/>
        <line x1="15" y1="35" x2="7" y2="35" stroke="{GOLD}" stroke-width="3" stroke-linecap="round"/>
    </svg>'''
    return svg


def shield_icon(size=80):
    """Shield - for barriers, protection"""
    svg = f'''<svg width="{size}" height="{size}" viewBox="0 0 80 100" xmlns="http://www.w3.org/2000/svg">
        <path d="M 40 10 L 10 25 L 10 50 Q 10 75, 40 90 Q 70 75, 70 50 L 70 25 Z"
              fill="none" stroke="{NAVY}" stroke-width="3"/>

        <!-- X mark -->
        <line x1="30" y1="40" x2="50" y2="60" stroke="{NAVY}" stroke-width="3" stroke-linecap="round"/>
        <line x1="50" y1="40" x2="30" y2="60" stroke="{NAVY}" stroke-width="3" stroke-linecap="round"/>
    </svg>'''
    return svg


def trophy_icon(size=80):
    """Trophy - for achievement, wins"""
    svg = f'''<svg width="{size}" height="{size}" viewBox="0 0 80 100" xmlns="http://www.w3.org/2000/svg">
        <!-- Cup -->
        <path d="M 25 20 L 30 50 Q 30 60, 40 60 Q 50 60, 50 50 L 55 20 Z"
              fill="none" stroke="{GOLD}" stroke-width="3"/>

        <!-- Handles -->
        <path d="M 25 25 Q 15 25, 15 35 Q 15 42, 25 42"
              fill="none" stroke="{GOLD}" stroke-width="2"/>
        <path d="M 55 25 Q 65 25, 65 35 Q 65 42, 55 42"
              fill="none" stroke="{GOLD}" stroke-width="2"/>

        <!-- Base -->
        <rect x="35" y="60" width="10" height="15" fill="{GOLD}"/>
        <rect x="25" y="75" width="30" height="5" fill="{GOLD}"/>
    </svg>'''
    return svg


# Export all SVG functions as a dictionary
SVG_LIBRARY = {
    'target': target_icon,
    'growth_curve': growth_curve_icon,
    'cycle_arrows': cycle_arrows_icon,
    'winding_path': winding_path_icon,
    'pillar': pillar_icon,
    'shark': shark_icon,
    'gear': gear_icon,
    'calendar': calendar_icon,
    'dashboard': dashboard_icon,
    'network': network_icon,
    'checkmark': checkmark_icon,
    'arrow_up': arrow_up_icon,
    'lightbulb': lightbulb_icon,
    'shield': shield_icon,
    'trophy': trophy_icon,
}

if __name__ == "__main__":
    print("SVG Graphics Library")
    print("=" * 50)
    print(f"Available graphics: {len(SVG_LIBRARY)}")
    print("\nGraphics:")
    for name in SVG_LIBRARY.keys():
        print(f"  - {name}")
