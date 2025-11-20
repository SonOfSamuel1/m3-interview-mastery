"""
Vector Graphics Renderer Using PIL/Pillow Only
Pure Python implementation of custom vector graphics for slides
No external dependencies required beyond PIL
"""

from PIL import Image, ImageDraw
import math


class VectorGraphics:
    """Vector graphics renderer using PIL drawing primitives"""

    def __init__(self, size=(100, 100), color_rgb=(212, 175, 55)):
        self.size = size
        self.color = color_rgb
        self.img = Image.new('RGBA', size, (0, 0, 0, 0))
        self.draw = ImageDraw.Draw(self.img)

    def get_image(self):
        """Return the rendered image"""
        return self.img

    def lightbulb_icon(self):
        """Draw a lightbulb icon"""
        w, h = self.size
        scale = min(w, h) / 100

        # Bulb
        bulb_top = int(25 * scale)
        bulb_bottom = int(65 * scale)
        bulb_left = int(30 * scale)
        bulb_right = int(70 * scale)
        self.draw.ellipse([bulb_left, bulb_top, bulb_right, bulb_bottom],
                         outline=self.color, width=int(3 * scale))

        # Base
        base_top = int(68 * scale)
        base_height = int(10 * scale)
        self.draw.rectangle([int(38 * scale), base_top,
                            int(62 * scale), base_top + base_height],
                           outline=self.color, width=int(2 * scale))

        # Filament
        self.draw.line([int(50 * scale), int(35 * scale),
                       int(50 * scale), int(55 * scale)],
                      fill=self.color, width=int(2 * scale))

        # Light rays
        ray_length = int(10 * scale)
        center_x, center_y = int(50 * scale), int(40 * scale)

        # Top ray
        self.draw.line([center_x, int(15 * scale), center_x, int(15 * scale) + ray_length],
                      fill=self.color, width=int(2 * scale))

        # Side rays
        self.draw.line([int(25 * scale), center_y, int(25 * scale) - ray_length, center_y],
                      fill=self.color, width=int(2 * scale))
        self.draw.line([int(75 * scale), center_y, int(75 * scale) + ray_length, center_y],
                      fill=self.color, width=int(2 * scale))

        return self.img

    def target_icon(self):
        """Draw a target icon"""
        w, h = self.size
        scale = min(w, h) / 100
        center = (int(50 * scale), int(50 * scale))

        # Concentric circles
        radii = [35, 25, 15, 6]
        for radius in radii:
            r = int(radius * scale)
            bbox = [center[0] - r, center[1] - r, center[0] + r, center[1] + r]
            if radius == 6:
                self.draw.ellipse(bbox, fill=self.color)
            else:
                self.draw.ellipse(bbox, outline=self.color, width=int(2.5 * scale))

        # Arrow
        arrow_start = (int(70 * scale), int(20 * scale))
        arrow_end = (int(60 * scale), int(50 * scale))
        self.draw.line([arrow_start, arrow_end], fill=self.color, width=int(3 * scale))

        # Arrowhead
        arrow_points = [
            (int(70 * scale), int(20 * scale)),
            (int(65 * scale), int(25 * scale)),
            (int(73 * scale), int(23 * scale))
        ]
        self.draw.polygon(arrow_points, fill=self.color)

        return self.img

    def growth_arrow_icon(self):
        """Draw an upward trending growth arrow"""
        w, h = self.size
        scale = min(w, h) / 100

        # Data points
        points = [
            (int(10 * scale), int(80 * scale)),
            (int(30 * scale), int(65 * scale)),
            (int(50 * scale), int(55 * scale)),
            (int(70 * scale), int(35 * scale)),
            (int(90 * scale), int(20 * scale))
        ]

        # Draw line segments
        for i in range(len(points) - 1):
            self.draw.line([points[i], points[i + 1]], fill=self.color, width=int(3 * scale))

        # Draw points
        for point in points:
            r = int(4 * scale)
            self.draw.ellipse([point[0] - r, point[1] - r, point[0] + r, point[1] + r],
                            fill=self.color)

        # Arrow head at end
        last_point = points[-1]
        arrow_points = [
            last_point,
            (last_point[0] - int(8 * scale), last_point[1] + int(8 * scale)),
            (last_point[0] + int(8 * scale), last_point[1] + int(8 * scale))
        ]
        self.draw.polygon(arrow_points, fill=self.color)

        return self.img

    def shield_icon(self):
        """Draw a shield icon"""
        w, h = self.size
        scale = min(w, h) / 100

        # Shield outline
        top = int(15 * scale)
        bottom = int(85 * scale)
        left = int(25 * scale)
        right = int(75 * scale)
        mid_x = int(50 * scale)

        shield_points = [
            (left, top),
            (right, top),
            (right, int(60 * scale)),
            (mid_x, bottom),
            (left, int(60 * scale))
        ]
        self.draw.polygon(shield_points, outline=self.color, width=int(3 * scale))

        # Checkmark inside
        check_points = [
            (int(35 * scale), int(50 * scale)),
            (int(45 * scale), int(60 * scale)),
            (int(65 * scale), int(35 * scale))
        ]
        for i in range(len(check_points) - 1):
            self.draw.line([check_points[i], check_points[i + 1]],
                          fill=self.color, width=int(3.5 * scale))

        return self.img

    def brain_icon(self):
        """Draw a brain icon"""
        w, h = self.size
        scale = min(w, h) / 100

        # Main brain outline (simplified)
        left = int(25 * scale)
        right = int(75 * scale)
        top = int(25 * scale)
        bottom = int(75 * scale)

        # Draw brain outline using arcs
        self.draw.arc([left, top, right, bottom], 0, 180, fill=self.color, width=int(3 * scale))
        self.draw.arc([left, top, right, bottom], 180, 360, fill=self.color, width=int(3 * scale))

        # Brain folds (simplified curved lines)
        mid_x = int(50 * scale)
        self.draw.line([mid_x, top, mid_x, bottom], fill=self.color, width=int(2 * scale))

        # Additional detail lines
        self.draw.arc([int(30 * scale), int(35 * scale), int(45 * scale), int(55 * scale)],
                     0, 180, fill=self.color, width=int(2 * scale))
        self.draw.arc([int(55 * scale), int(35 * scale), int(70 * scale), int(55 * scale)],
                     0, 180, fill=self.color, width=int(2 * scale))

        return self.img

    def gear_icon(self):
        """Draw a gear/settings icon"""
        w, h = self.size
        scale = min(w, h) / 100
        center = (int(50 * scale), int(50 * scale))
        outer_r = int(35 * scale)
        inner_r = int(15 * scale)

        # Draw gear teeth
        num_teeth = 8
        for i in range(num_teeth):
            angle = (2 * math.pi * i) / num_teeth
            next_angle = (2 * math.pi * (i + 1)) / num_teeth

            # Outer tooth points
            x1 = center[0] + int(outer_r * math.cos(angle))
            y1 = center[1] + int(outer_r * math.sin(angle))
            x2 = center[0] + int(outer_r * math.cos(next_angle))
            y2 = center[1] + int(outer_r * math.sin(next_angle))

            # Mid points for tooth shape
            mid_angle = (angle + next_angle) / 2
            x_mid = center[0] + int((outer_r - 5 * scale) * math.cos(mid_angle))
            y_mid = center[1] + int((outer_r - 5 * scale) * math.sin(mid_angle))

            # Draw tooth
            self.draw.line([x1, y1, x_mid, y_mid], fill=self.color, width=int(3 * scale))
            self.draw.line([x_mid, y_mid, x2, y2], fill=self.color, width=int(3 * scale))

        # Center circle
        self.draw.ellipse([center[0] - inner_r, center[1] - inner_r,
                          center[0] + inner_r, center[1] + inner_r],
                         outline=self.color, width=int(3 * scale))

        return self.img

    def checklist_icon(self):
        """Draw a checklist icon"""
        w, h = self.size
        scale = min(w, h) / 100

        # Document outline
        left = int(20 * scale)
        top = int(15 * scale)
        right = int(80 * scale)
        bottom = int(85 * scale)
        self.draw.rectangle([left, top, right, bottom], outline=self.color, width=int(2.5 * scale))

        # Checkmarks and lines
        items_y = [30, 50, 70]
        for y_pos in items_y:
            y = int(y_pos * scale)

            # Checkmark
            check_points = [
                (int(28 * scale), y),
                (int(35 * scale), int((y_pos + 7) * scale)),
                (int(45 * scale), int((y_pos - 5) * scale))
            ]
            for i in range(len(check_points) - 1):
                self.draw.line([check_points[i], check_points[i + 1]],
                              fill=self.color, width=int(2.5 * scale))

            # Text line
            self.draw.line([int(52 * scale), y, int(72 * scale), y],
                          fill=self.color, width=int(2 * scale))

        return self.img

    def trophy_icon(self):
        """Draw a trophy icon"""
        w, h = self.size
        scale = min(w, h) / 100

        # Cup
        cup_top = int(25 * scale)
        cup_bottom = int(55 * scale)
        cup_left = int(35 * scale)
        cup_right = int(65 * scale)

        cup_points = [
            (cup_left, cup_top),
            (cup_left - int(5 * scale), cup_bottom),
            (cup_right + int(5 * scale), cup_bottom),
            (cup_right, cup_top)
        ]
        self.draw.polygon(cup_points, outline=self.color, width=int(3 * scale))

        # Handles
        self.draw.arc([int(15 * scale), int(28 * scale), cup_left, int(42 * scale)],
                     270, 90, fill=self.color, width=int(2.5 * scale))
        self.draw.arc([cup_right, int(28 * scale), int(85 * scale), int(42 * scale)],
                     90, 270, fill=self.color, width=int(2.5 * scale))

        # Base stem
        self.draw.line([int(50 * scale), cup_bottom, int(50 * scale), int(68 * scale)],
                      fill=self.color, width=int(3 * scale))

        # Base
        self.draw.rectangle([int(40 * scale), int(68 * scale),
                            int(60 * scale), int(78 * scale)],
                           outline=self.color, width=int(2.5 * scale))

        return self.img

    def mountain_icon(self):
        """Draw a mountain peak icon"""
        w, h = self.size
        scale = min(w, h) / 100

        # Mountain peaks
        peak1 = [
            (int(10 * scale), int(80 * scale)),
            (int(30 * scale), int(50 * scale)),
            (int(50 * scale), int(80 * scale))
        ]

        peak2 = [
            (int(40 * scale), int(80 * scale)),
            (int(60 * scale), int(25 * scale)),
            (int(80 * scale), int(80 * scale))
        ]

        # Draw peaks
        for i in range(len(peak1) - 1):
            self.draw.line([peak1[i], peak1[i + 1]], fill=self.color, width=int(3.5 * scale))

        for i in range(len(peak2) - 1):
            self.draw.line([peak2[i], peak2[i + 1]], fill=self.color, width=int(3.5 * scale))

        # Flag at peak
        flag_pole_top = int(25 * scale)
        flag_pole_bottom = int(35 * scale)
        self.draw.line([int(60 * scale), flag_pole_top, int(60 * scale), flag_pole_bottom],
                      fill=self.color, width=int(2 * scale))

        # Flag
        flag_points = [
            (int(60 * scale), flag_pole_top),
            (int(75 * scale), int(28 * scale)),
            (int(60 * scale), int(31 * scale))
        ]
        self.draw.polygon(flag_points, fill=self.color)

        return self.img

    def compass_icon(self):
        """Draw a compass icon"""
        w, h = self.size
        scale = min(w, h) / 100
        center = (int(50 * scale), int(50 * scale))
        radius = int(35 * scale)

        # Outer circle
        self.draw.ellipse([center[0] - radius, center[1] - radius,
                          center[0] + radius, center[1] + radius],
                         outline=self.color, width=int(2.5 * scale))

        # Compass needle (pointing north)
        needle_points = [
            (center[0], center[1] - int(25 * scale)),
            (center[0] - int(6 * scale), center[1] + int(5 * scale)),
            (center[0], center[1]),
            (center[0] + int(6 * scale), center[1] + int(5 * scale))
        ]
        self.draw.polygon(needle_points, fill=self.color)

        # Cardinal directions markers
        marker_len = int(8 * scale)
        # North
        self.draw.line([center[0], center[1] - radius,
                       center[0], center[1] - radius + marker_len],
                      fill=self.color, width=int(2.5 * scale))
        # South
        self.draw.line([center[0], center[1] + radius,
                       center[0], center[1] + radius - marker_len],
                      fill=self.color, width=int(2.5 * scale))
        # East
        self.draw.line([center[0] + radius, center[1],
                       center[0] + radius - marker_len, center[1]],
                      fill=self.color, width=int(2.5 * scale))
        # West
        self.draw.line([center[0] - radius, center[1],
                       center[0] - radius + marker_len, center[1]],
                      fill=self.color, width=int(2.5 * scale))

        return self.img

    def transformation_arrow(self):
        """Draw a transformation/progression arrow"""
        w, h = self.size
        scale = min(w, h) / 100

        # Curved arrow using arc and line
        start_x = int(15 * scale)
        start_y = int(70 * scale)
        end_x = int(85 * scale)
        end_y = int(30 * scale)

        # Draw curve (simplified as line with arc)
        mid_x = int(50 * scale)
        mid_y = int(40 * scale)

        self.draw.line([start_x, start_y, mid_x, mid_y], fill=self.color, width=int(3.5 * scale))
        self.draw.line([mid_x, mid_y, end_x, end_y], fill=self.color, width=int(3.5 * scale))

        # Start dot
        r = int(5 * scale)
        self.draw.ellipse([start_x - r, start_y - r, start_x + r, start_y + r], fill=self.color)

        # Arrow head
        arrow_points = [
            (end_x, end_y),
            (end_x - int(10 * scale), end_y + int(5 * scale)),
            (end_x - int(10 * scale), end_y - int(5 * scale))
        ]
        self.draw.polygon(arrow_points, fill=self.color)

        return self.img

    def calendar_icon(self):
        """Draw a calendar icon"""
        w, h = self.size
        scale = min(w, h) / 100

        # Calendar body
        left = int(20 * scale)
        top = int(25 * scale)
        right = int(80 * scale)
        bottom = int(85 * scale)
        self.draw.rectangle([left, top, right, bottom], outline=self.color, width=int(2.5 * scale))

        # Header bar
        header_bottom = int(38 * scale)
        self.draw.rectangle([left, top, right, header_bottom], outline=self.color, width=int(2.5 * scale))

        # Binding rings
        ring_y = int(20 * scale)
        self.draw.line([int(35 * scale), ring_y, int(35 * scale), int(30 * scale)],
                      fill=self.color, width=int(3 * scale))
        self.draw.line([int(65 * scale), ring_y, int(65 * scale), int(30 * scale)],
                      fill=self.color, width=int(3 * scale))

        # Date dots (simplified calendar days)
        dot_r = int(2.5 * scale)
        for row in range(3):
            for col in range(4):
                dot_x = int((30 + col * 13) * scale)
                dot_y = int((50 + row * 12) * scale)
                self.draw.ellipse([dot_x - dot_r, dot_y - dot_r,
                                  dot_x + dot_r, dot_y + dot_r],
                                fill=self.color)

        return self.img

    def rocket_icon(self):
        """Draw a rocket icon"""
        w, h = self.size
        scale = min(w, h) / 100

        # Rocket body
        top = int(15 * scale)
        bottom = int(70 * scale)
        left = int(40 * scale)
        right = int(60 * scale)
        mid_x = int(50 * scale)

        # Nose cone
        nose_points = [
            (mid_x, top),
            (left, int(30 * scale)),
            (right, int(30 * scale))
        ]
        self.draw.polygon(nose_points, outline=self.color, width=int(2.5 * scale))

        # Body
        self.draw.rectangle([left, int(30 * scale), right, bottom],
                           outline=self.color, width=int(2.5 * scale))

        # Window
        window_r = int(5 * scale)
        window_y = int(45 * scale)
        self.draw.ellipse([mid_x - window_r, window_y - window_r,
                          mid_x + window_r, window_y + window_r],
                         outline=self.color, width=int(2 * scale))

        # Fins
        left_fin = [
            (left, int(55 * scale)),
            (int(30 * scale), bottom),
            (left, bottom)
        ]
        right_fin = [
            (right, int(55 * scale)),
            (int(70 * scale), bottom),
            (right, bottom)
        ]
        self.draw.polygon(left_fin, fill=self.color)
        self.draw.polygon(right_fin, fill=self.color)

        # Exhaust flames
        flame_y = int(75 * scale)
        self.draw.line([int(45 * scale), bottom, int(42 * scale), flame_y],
                      fill=self.color, width=int(2.5 * scale))
        self.draw.line([mid_x, bottom, mid_x, int(80 * scale)],
                      fill=self.color, width=int(2.5 * scale))
        self.draw.line([int(55 * scale), bottom, int(58 * scale), flame_y],
                      fill=self.color, width=int(2.5 * scale))

        return self.img

    def dollar_growth_icon(self):
        """Draw a dollar sign with growth arrow"""
        w, h = self.size
        scale = min(w, h) / 100

        # Dollar sign
        mid_x = int(40 * scale)
        self.draw.line([mid_x, int(20 * scale), mid_x, int(70 * scale)],
                      fill=self.color, width=int(3 * scale))

        # S curves
        self.draw.arc([int(30 * scale), int(25 * scale), int(50 * scale), int(45 * scale)],
                     180, 0, fill=self.color, width=int(3 * scale))
        self.draw.arc([int(30 * scale), int(45 * scale), int(50 * scale), int(65 * scale)],
                     0, 180, fill=self.color, width=int(3 * scale))

        # Growth arrow
        arrow_start = (int(60 * scale), int(70 * scale))
        arrow_end = (int(85 * scale), int(25 * scale))
        self.draw.line([arrow_start, arrow_end], fill=self.color, width=int(3.5 * scale))

        # Arrow head
        arrow_points = [
            arrow_end,
            (arrow_end[0] - int(8 * scale), arrow_end[1] + int(8 * scale)),
            (arrow_end[0], arrow_end[1] + int(12 * scale))
        ]
        self.draw.polygon(arrow_points, fill=self.color)

        return self.img

    def network_icon(self):
        """Draw a network/connection icon"""
        w, h = self.size
        scale = min(w, h) / 100

        # Node positions
        nodes = [
            (int(50 * scale), int(25 * scale)),  # Top
            (int(25 * scale), int(55 * scale)),  # Left
            (int(75 * scale), int(55 * scale)),  # Right
            (int(35 * scale), int(80 * scale)),  # Bottom left
            (int(65 * scale), int(80 * scale))   # Bottom right
        ]

        # Draw connections
        connections = [(0, 1), (0, 2), (1, 3), (2, 4), (1, 2), (3, 4)]
        for start, end in connections:
            self.draw.line([nodes[start], nodes[end]], fill=self.color, width=int(2 * scale))

        # Draw nodes
        radii = [8, 7, 7, 6, 6]
        for node, radius in zip(nodes, radii):
            r = int(radius * scale)
            self.draw.ellipse([node[0] - r, node[1] - r, node[0] + r, node[1] + r],
                            fill=self.color)

        return self.img

    def metrics_dashboard_icon(self):
        """Draw a metrics/dashboard icon"""
        w, h = self.size
        scale = min(w, h) / 100

        # Dashboard frame
        left = int(15 * scale)
        top = int(20 * scale)
        right = int(85 * scale)
        bottom = int(80 * scale)
        self.draw.rectangle([left, top, right, bottom], outline=self.color, width=int(2.5 * scale))

        # Header
        header_bottom = int(35 * scale)
        self.draw.line([left, header_bottom, right, header_bottom],
                      fill=self.color, width=int(2.5 * scale))

        # Bar chart
        bars = [
            (int(25 * scale), int(60 * scale), int(8 * scale)),
            (int(40 * scale), int(50 * scale), int(8 * scale)),
            (int(55 * scale), int(45 * scale), int(8 * scale)),
            (int(70 * scale), int(55 * scale), int(8 * scale))
        ]

        for x, top, width in bars:
            self.draw.rectangle([x, top, x + width, int(75 * scale)], fill=self.color)

        # Header dots (menu)
        for i in range(3):
            dot_x = int((25 + i * 8) * scale)
            dot_y = int(28 * scale)
            r = int(2 * scale)
            self.draw.ellipse([dot_x - r, dot_y - r, dot_x + r, dot_y + r], fill=self.color)

        return self.img

    def pillar_icon(self):
        """Draw a classical pillar icon"""
        w, h = self.size
        scale = min(w, h) / 100

        # Pillar base
        base_top = int(75 * scale)
        base_bottom = int(80 * scale)
        base_left = int(30 * scale)
        base_right = int(70 * scale)
        self.draw.rectangle([base_left, base_top, base_right, base_bottom], fill=self.color)

        # Pillar column
        col_top = int(25 * scale)
        col_left = int(38 * scale)
        col_right = int(62 * scale)
        self.draw.rectangle([col_left, col_top, col_right, base_top],
                           outline=self.color, width=int(2.5 * scale))

        # Column details (vertical lines)
        for x_offset in [0, 8, 16, 24]:
            x = col_left + int(x_offset * scale)
            if x < col_right:
                self.draw.line([x, col_top + int(5 * scale), x, base_top - int(5 * scale)],
                              fill=self.color, width=int(1.5 * scale))

        # Capital (top)
        cap_top = int(20 * scale)
        cap_bottom = col_top
        self.draw.rectangle([base_left, cap_top, base_right, cap_bottom], fill=self.color)

        return self.img

    def confidence_icon(self):
        """Draw a confidence/strength icon"""
        w, h = self.size
        scale = min(w, h) / 100

        # Person silhouette
        # Head
        head_r = int(12 * scale)
        head_center = (int(50 * scale), int(30 * scale))
        self.draw.ellipse([head_center[0] - head_r, head_center[1] - head_r,
                          head_center[0] + head_r, head_center[1] + head_r],
                         outline=self.color, width=int(2.5 * scale))

        # Body
        body_top = head_center[1] + head_r
        body_bottom = int(70 * scale)
        self.draw.line([head_center[0], body_top, head_center[0], body_bottom],
                      fill=self.color, width=int(3 * scale))

        # Arms (raised in victory/confidence pose)
        arm_start_y = int(50 * scale)
        # Left arm up
        self.draw.line([head_center[0], arm_start_y, int(30 * scale), int(35 * scale)],
                      fill=self.color, width=int(3 * scale))
        # Right arm up
        self.draw.line([head_center[0], arm_start_y, int(70 * scale), int(35 * scale)],
                      fill=self.color, width=int(3 * scale))

        # Legs
        # Left leg
        self.draw.line([head_center[0], body_bottom, int(40 * scale), int(85 * scale)],
                      fill=self.color, width=int(3 * scale))
        # Right leg
        self.draw.line([head_center[0], body_bottom, int(60 * scale), int(85 * scale)],
                      fill=self.color, width=int(3 * scale))

        return self.img

    def unlock_icon(self):
        """Draw an unlock/breakthrough icon"""
        w, h = self.size
        scale = min(w, h) / 100

        # Lock body
        lock_top = int(50 * scale)
        lock_bottom = int(80 * scale)
        lock_left = int(35 * scale)
        lock_right = int(65 * scale)
        self.draw.rectangle([lock_left, lock_top, lock_right, lock_bottom],
                           outline=self.color, width=int(2.5 * scale))

        # Keyhole
        keyhole_y = int(63 * scale)
        keyhole_r = int(5 * scale)
        self.draw.ellipse([int(50 * scale) - keyhole_r, keyhole_y - keyhole_r,
                          int(50 * scale) + keyhole_r, keyhole_y + keyhole_r],
                         fill=self.color)
        self.draw.line([int(50 * scale), keyhole_y + keyhole_r,
                       int(50 * scale), int(72 * scale)],
                      fill=self.color, width=int(2.5 * scale))

        # Unlocked shackle (open)
        shackle_left = int(35 * scale)
        shackle_top = int(30 * scale)
        shackle_right = lock_left
        shackle_bottom = lock_top

        self.draw.arc([shackle_left, shackle_top, lock_right, shackle_bottom],
                     180, 270, fill=self.color, width=int(3 * scale))
        self.draw.line([lock_right, int(40 * scale), int(70 * scale), int(40 * scale)],
                      fill=self.color, width=int(3 * scale))

        return self.img


# Convenience functions
def create_icon(icon_name, size=100, color_rgb=(212, 175, 55)):
    """
    Create an icon by name

    Args:
        icon_name: Name of the icon (e.g., 'lightbulb', 'target', 'growth_arrow')
        size: Size of the icon (width and height)
        color_rgb: RGB tuple for the icon color

    Returns:
        PIL Image with the icon
    """
    vg = VectorGraphics(size=(size, size), color_rgb=color_rgb)

    icon_methods = {
        'lightbulb': vg.lightbulb_icon,
        'target': vg.target_icon,
        'growth_arrow': vg.growth_arrow_icon,
        'shield': vg.shield_icon,
        'brain': vg.brain_icon,
        'gear': vg.gear_icon,
        'checklist': vg.checklist_icon,
        'trophy': vg.trophy_icon,
        'mountain': vg.mountain_icon,
        'compass': vg.compass_icon,
        'transformation': vg.transformation_arrow,
        'calendar': vg.calendar_icon,
        'rocket': vg.rocket_icon,
        'dollar_growth': vg.dollar_growth_icon,
        'network': vg.network_icon,
        'metrics': vg.metrics_dashboard_icon,
        'pillar': vg.pillar_icon,
        'confidence': vg.confidence_icon,
        'unlock': vg.unlock_icon,
    }

    if icon_name in icon_methods:
        return icon_methods[icon_name]()
    else:
        # Return blank image if icon not found
        return Image.new('RGBA', (size, size), (0, 0, 0, 0))


def create_decorative_corner(size=120, color_rgb=(212, 175, 55), style='lines'):
    """Create a decorative corner element"""
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    scale = size / 100

    if style == 'lines':
        # Geometric lines in corner
        draw.line([0, int(20 * scale), int(80 * scale), int(20 * scale)],
                 fill=color_rgb, width=int(2 * scale))
        draw.line([int(20 * scale), 0, int(20 * scale), int(80 * scale)],
                 fill=color_rgb, width=int(2 * scale))
        draw.line([0, int(40 * scale), int(60 * scale), int(40 * scale)],
                 fill=color_rgb, width=int(1.5 * scale))
        draw.line([int(40 * scale), 0, int(40 * scale), int(60 * scale)],
                 fill=color_rgb, width=int(1.5 * scale))

        # Accent dot
        r = int(4 * scale)
        center = int(20 * scale)
        draw.ellipse([center - r, center - r, center + r, center + r], fill=color_rgb)

    return img


if __name__ == "__main__":
    # Test: Generate sample icons
    import os
    output_dir = "test_icons"
    os.makedirs(output_dir, exist_ok=True)

    test_icons = [
        'lightbulb', 'target', 'growth_arrow', 'shield', 'brain',
        'gear', 'checklist', 'trophy', 'mountain', 'compass',
        'transformation', 'calendar', 'rocket', 'dollar_growth',
        'network', 'metrics', 'pillar', 'confidence', 'unlock'
    ]

    for icon_name in test_icons:
        img = create_icon(icon_name, size=100, color_rgb=(212, 175, 55))
        img.save(os.path.join(output_dir, f"{icon_name}.png"))

    print(f"Generated {len(test_icons)} test icons in {output_dir}/")
