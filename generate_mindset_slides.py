#!/usr/bin/env python3
"""
Generate professional slides for Active Offer M0- Mindset Module (Expanded)
Brand Style: Minimalist, clean, black text on light gray background
Output: 1920x1080 PNG files at 16:9 aspect ratio
"""

from PIL import Image, ImageDraw, ImageFont
import textwrap
import os

# Brand Colors
BACKGROUND_COLOR = "#F5F5F5"
TEXT_COLOR = "#000000"

# Slide dimensions (1920x1080 - 16:9 aspect ratio)
SLIDE_WIDTH = 1920
SLIDE_HEIGHT = 1080

# Typography settings
TITLE_FONT_SIZE = 120
SUBTITLE_FONT_SIZE = 80
BODY_FONT_SIZE = 52
SMALL_FONT_SIZE = 44

# Layout settings
LEFT_MARGIN = 100
RIGHT_MARGIN = 100
TOP_MARGIN = 80
BULLET_INDENT = 60
LINE_SPACING = 1.4

def wrap_text(text, font, max_width):
    """Wrap text to fit within max_width"""
    lines = []
    words = text.split()
    current_line = []

    for word in words:
        test_line = ' '.join(current_line + [word])
        bbox = font.getbbox(test_line)
        width = bbox[2] - bbox[0]

        if width <= max_width:
            current_line.append(word)
        else:
            if current_line:
                lines.append(' '.join(current_line))
            current_line = [word]

    if current_line:
        lines.append(' '.join(current_line))

    return lines

def create_title_slide(title, subtitle=None):
    """Create a centered title slide"""
    img = Image.new('RGB', (SLIDE_WIDTH, SLIDE_HEIGHT), BACKGROUND_COLOR)
    draw = ImageDraw.Draw(img)

    # Load fonts (using system fonts)
    try:
        title_font = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", TITLE_FONT_SIZE)
    except:
        title_font = ImageFont.load_default()

    # Draw title (centered)
    title_lines = wrap_text(title, title_font, SLIDE_WIDTH - 200)

    # Calculate total height for vertical centering
    line_height = int(TITLE_FONT_SIZE * LINE_SPACING)
    total_height = len(title_lines) * line_height

    if subtitle:
        try:
            subtitle_font = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", SUBTITLE_FONT_SIZE)
        except:
            subtitle_font = ImageFont.load_default()
        subtitle_lines = wrap_text(subtitle, subtitle_font, SLIDE_WIDTH - 200)
        total_height += len(subtitle_lines) * int(SUBTITLE_FONT_SIZE * LINE_SPACING) + 60

    # Start position for centered text
    y = (SLIDE_HEIGHT - total_height) // 2

    # Draw title lines
    for line in title_lines:
        bbox = title_font.getbbox(line)
        text_width = bbox[2] - bbox[0]
        x = (SLIDE_WIDTH - text_width) // 2
        draw.text((x, y), line, fill=TEXT_COLOR, font=title_font)
        y += line_height

    # Draw subtitle if provided
    if subtitle:
        y += 60
        for line in subtitle_lines:
            bbox = subtitle_font.getbbox(line)
            text_width = bbox[2] - bbox[0]
            x = (SLIDE_WIDTH - text_width) // 2
            draw.text((x, y), line, fill=TEXT_COLOR, font=subtitle_font)
            y += int(SUBTITLE_FONT_SIZE * LINE_SPACING)

    return img

def create_content_slide(title, bullets, small_bullets=False):
    """Create a content slide with title and bullet points"""
    img = Image.new('RGB', (SLIDE_WIDTH, SLIDE_HEIGHT), BACKGROUND_COLOR)
    draw = ImageDraw.Draw(img)

    # Load fonts
    try:
        title_font = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", SUBTITLE_FONT_SIZE)
        bullet_font = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", SMALL_FONT_SIZE if small_bullets else BODY_FONT_SIZE)
    except:
        title_font = ImageFont.load_default()
        bullet_font = ImageFont.load_default()

    # Draw title
    y = TOP_MARGIN
    title_lines = wrap_text(title, title_font, SLIDE_WIDTH - LEFT_MARGIN - RIGHT_MARGIN)
    for line in title_lines:
        draw.text((LEFT_MARGIN, y), line, fill=TEXT_COLOR, font=title_font)
        y += int(SUBTITLE_FONT_SIZE * LINE_SPACING)

    y += 60  # Space after title

    # Draw bullets
    max_text_width = SLIDE_WIDTH - LEFT_MARGIN - RIGHT_MARGIN - BULLET_INDENT - 40
    font_size = SMALL_FONT_SIZE if small_bullets else BODY_FONT_SIZE
    line_height = int(font_size * LINE_SPACING)

    for bullet in bullets:
        # Draw bullet point
        draw.text((LEFT_MARGIN, y), "•", fill=TEXT_COLOR, font=bullet_font)

        # Wrap and draw bullet text
        bullet_lines = wrap_text(bullet, bullet_font, max_text_width)
        for i, line in enumerate(bullet_lines):
            x_offset = LEFT_MARGIN + BULLET_INDENT if i == 0 else LEFT_MARGIN + BULLET_INDENT
            draw.text((x_offset, y), line, fill=TEXT_COLOR, font=bullet_font)
            y += line_height

        y += 20  # Space between bullets

    return img

# Define all slide content
slides_content = [
    # LESSON 1: The Psychology of High-Ticket Job Searches (8-10 slides)
    {
        "type": "title",
        "title": "The Psychology of High-Ticket Job Searches"
    },
    {
        "type": "content",
        "title": "Why Mindset Matters More Than Strategy",
        "bullets": [
            "Your mindset determines your actions, and your actions determine your results",
            "Most job seekers focus on tactics (resume, LinkedIn) but neglect the psychological foundation",
            "High-ticket roles ($200k-$500k+) require a different level of confidence and positioning",
            "Hiring managers can sense desperation, scarcity thinking, and lack of confidence immediately",
            "Premium positioning starts in your mind before it shows up in your messaging"
        ]
    },
    {
        "type": "content",
        "title": "The High-Ticket Job Search Mindset",
        "bullets": [
            "You are interviewing the company as much as they are interviewing you",
            "You bring valuable skills and expertise that solve expensive business problems",
            "Scarcity mindset: \"I hope they pick me\" vs. Abundance mindset: \"Is this the right fit?\"",
            "Your goal is not to get any job - it's to find the right high-value opportunity",
            "Confidence is not arrogance; it's knowing your worth and communicating it clearly"
        ]
    },
    {
        "type": "content",
        "title": "Common Psychological Barriers",
        "bullets": [
            "Imposter syndrome: Feeling you're not qualified for high-paying roles",
            "Fear of rejection: Avoiding opportunities because you might not get them",
            "Salary anxiety: Uncomfortable discussing compensation or negotiating",
            "Scarcity thinking: Taking the first offer instead of creating options",
            "Comparison trap: Measuring yourself against others instead of your own growth"
        ]
    },
    {
        "type": "content",
        "title": "The Cost of the Wrong Mindset",
        "bullets": [
            "Accepting roles below your market value can cost $50k-$200k+ per year",
            "Over a 5-year period, that's $250k-$1M in lost lifetime earnings",
            "Settling for the wrong company wastes 1-2 years of career momentum",
            "Poor negotiation due to fear leaves tens of thousands on the table",
            "Your mindset either compounds your success or your stagnation"
        ]
    },
    {
        "type": "content",
        "title": "Shifting to a High-Performer Mindset",
        "bullets": [
            "View yourself as a business solving problems, not an employee seeking permission",
            "Approach interviews as collaborative discovery, not interrogation",
            "See compensation as a reflection of value created, not a favor granted",
            "Embrace rejection as data and refinement, not personal failure",
            "Build evidence of your value through past results and future potential"
        ]
    },
    {
        "type": "content",
        "title": "The Abundance Mentality in Job Search",
        "bullets": [
            "There are thousands of companies hiring for high-ticket sales roles right now",
            "Multiple opportunities create leverage and confidence in negotiations",
            "You only need ONE great offer, but creating options gives you power",
            "Abundance thinking makes you more attractive to employers",
            "The right opportunity exists; your job is to position yourself to find it"
        ]
    },
    {
        "type": "content",
        "title": "Reframing Rejection and Setbacks",
        "bullets": [
            "Every \"no\" brings you closer to the right \"yes\"",
            "Rejection is feedback about fit, not a judgment of your worth",
            "Top performers get rejected often - they just don't let it stop them",
            "Use rejection to refine your approach, messaging, and target companies",
            "The company that rejects you might not be the right opportunity anyway"
        ]
    },
    {
        "type": "content",
        "title": "Building Psychological Resilience",
        "bullets": [
            "Separate your identity from your job search outcomes",
            "Celebrate small wins: applications submitted, connections made, interviews scheduled",
            "Develop a support system: mentors, peers, accountability partners",
            "Practice self-compassion during difficult moments",
            "Remember: You are building a career, not just finding a job"
        ]
    },

    # LESSON 2: Identifying Your Limiting Beliefs (7-9 slides)
    {
        "type": "title",
        "title": "Identifying Your Limiting Beliefs"
    },
    {
        "type": "content",
        "title": "What Are Limiting Beliefs?",
        "bullets": [
            "Subconscious assumptions about yourself, your capabilities, and what's possible",
            "Often formed from past experiences, family messages, or societal conditioning",
            "They feel like facts, but they're actually interpretations and stories",
            "Limiting beliefs create self-imposed ceilings on your potential and income",
            "Most people are completely unaware of the beliefs holding them back"
        ]
    },
    {
        "type": "content",
        "title": "Common Limiting Beliefs in Job Search",
        "bullets": [
            "\"I'm not qualified for roles at that level\"",
            "\"I don't have the right background or pedigree\"",
            "\"I'm too old/young for that type of opportunity\"",
            "\"Companies won't pay me that much\"",
            "\"I'm not good at interviews or selling myself\"",
            "\"I need more experience before I can make that move\""
        ]
    },
    {
        "type": "content",
        "title": "How Limiting Beliefs Sabotage Your Search",
        "bullets": [
            "You don't apply to roles you're actually qualified for",
            "You undersell yourself in interviews and negotiations",
            "You accept lower compensation than you deserve",
            "You avoid putting yourself in uncomfortable but growth-producing situations",
            "You create self-fulfilling prophecies: \"I knew they wouldn't hire me\""
        ]
    },
    {
        "type": "content",
        "title": "The Limiting Belief Identification Process",
        "bullets": [
            "Step 1: Notice areas where you hesitate or avoid taking action",
            "Step 2: Ask yourself: \"What would I have to believe to behave this way?\"",
            "Step 3: Write down the belief explicitly and examine the evidence",
            "Step 4: Challenge the belief with counter-evidence from your experience",
            "Step 5: Create a new empowering belief and find supporting evidence"
        ]
    },
    {
        "type": "content",
        "title": "Reframing Exercise: From Limiting to Empowering",
        "bullets": [
            "OLD: \"I'm not qualified\" → NEW: \"I bring unique value they can't find elsewhere\"",
            "OLD: \"I need more experience\" → NEW: \"I have transferable skills that apply immediately\"",
            "OLD: \"They won't pay me that much\" → NEW: \"I solve problems worth far more than my salary\"",
            "OLD: \"I'm bad at interviews\" → NEW: \"I'm learning and improving with each conversation\"",
            "OLD: \"I don't have connections\" → NEW: \"I'm building relationships strategically\""
        ]
    },
    {
        "type": "content",
        "title": "Evidence Collection: Building Your Case",
        "bullets": [
            "Document past wins: sales made, deals closed, problems solved",
            "Quantify your impact: revenue generated, money saved, efficiency gained",
            "Collect testimonials and recommendations from colleagues and clients",
            "Identify skills others pay you for advice on",
            "Notice when people come to you for help - that's evidence of expertise"
        ]
    },
    {
        "type": "content",
        "title": "The Power of Borrowed Belief",
        "bullets": [
            "If you don't believe in yourself yet, borrow belief from others who do",
            "Study people with your background who landed the roles you want",
            "Find mentors who see potential in you that you can't see yet",
            "Join communities of people pursuing similar goals",
            "Use their success as evidence of what's possible for you too"
        ]
    },
    {
        "type": "content",
        "title": "Daily Practice: Belief Reinforcement",
        "bullets": [
            "Morning: Review your empowering beliefs and supporting evidence",
            "During job search: Notice when limiting beliefs arise and reframe them",
            "After interactions: Collect evidence of your value and capability",
            "Evening: Reflect on moments you showed up despite fear or doubt",
            "Weekly: Update your evidence journal with new wins and insights"
        ]
    },

    # LESSON 3: Building Unshakeable Confidence (10-12 slides)
    {
        "type": "title",
        "title": "Building Unshakeable Confidence"
    },
    {
        "type": "content",
        "title": "What Is True Confidence?",
        "bullets": [
            "Confidence is not arrogance or bravado - it's quiet self-assurance",
            "It's the belief that you can handle whatever comes your way",
            "True confidence comes from evidence and preparation, not positive thinking alone",
            "It's being comfortable with uncertainty and embracing growth",
            "Confidence is a skill you build through action, not something you wait to feel"
        ]
    },
    {
        "type": "content",
        "title": "The Confidence-Action Cycle",
        "bullets": [
            "Most people think: Confidence → Action → Results",
            "Reality: Action → Results → Confidence",
            "You build confidence by taking action before you feel ready",
            "Each small action creates evidence that builds more confidence",
            "Waiting to feel confident before acting keeps you stuck forever"
        ]
    },
    {
        "type": "content",
        "title": "The Three Pillars of Career Confidence",
        "bullets": [
            "COMPETENCE: You have skills and knowledge that create value",
            "PREPARATION: You've done the work to be ready for opportunities",
            "EVIDENCE: You have proof of past successes and results",
            "When all three are strong, confidence becomes unshakeable",
            "Focus on building these systematically, not manufacturing fake confidence"
        ]
    },
    {
        "type": "content",
        "title": "Pillar 1: Building Competence",
        "bullets": [
            "Master the fundamentals of your craft (sales methodology, product knowledge)",
            "Develop expertise in specific areas (industry, buyer persona, solution selling)",
            "Stay current with trends and best practices in your field",
            "Invest in continuous learning: courses, certifications, mentorship",
            "Practice your skills deliberately and consistently"
        ]
    },
    {
        "type": "content",
        "title": "Pillar 2: Rigorous Preparation",
        "bullets": [
            "Research every company before you engage with them",
            "Prepare specific examples and stories for common interview questions",
            "Practice your pitch, story, and value proposition repeatedly",
            "Anticipate objections and prepare thoughtful responses",
            "Mock interviews, role plays, and feedback sessions build readiness"
        ]
    },
    {
        "type": "content",
        "title": "Pillar 3: Collecting Evidence",
        "bullets": [
            "Create a \"wins document\" tracking every success, big and small",
            "Quantify your achievements: revenue, quota attainment, deals closed",
            "Save testimonials, recommendations, and positive feedback",
            "Document problems you solved and value you created",
            "Review this evidence regularly to reinforce your capabilities"
        ]
    },
    {
        "type": "content",
        "title": "Confidence-Building Exercises",
        "bullets": [
            "Power posing: 2 minutes of confident body language before interviews",
            "Visualization: See yourself succeeding in interviews and negotiations",
            "Affirmations grounded in evidence: \"I closed $2M in revenue last year\"",
            "Recall past wins: Remember times you overcame challenges successfully",
            "Preparation rituals: Consistent routines that signal readiness to your brain"
        ]
    },
    {
        "type": "content",
        "title": "Overcoming Confidence Killers",
        "bullets": [
            "Comparison: Focus on your own progress, not others' highlight reels",
            "Perfectionism: Done is better than perfect; progress over perfection",
            "Negative self-talk: Catch it, challenge it, replace it with evidence-based truth",
            "Past failures: Reframe as learning experiences and data for improvement",
            "Fear of judgment: Most people are focused on themselves, not judging you"
        ]
    },
    {
        "type": "content",
        "title": "Confidence in High-Stakes Situations",
        "bullets": [
            "Nervousness is normal - even top performers feel it",
            "Channel nervous energy into enthusiasm and presence",
            "Focus on serving and helping, not proving yourself",
            "Remember: You're evaluating them as much as they're evaluating you",
            "Your preparation and competence will carry you through"
        ]
    },
    {
        "type": "content",
        "title": "The Compound Effect of Small Confidence Wins",
        "bullets": [
            "Send one message today, even if imperfect",
            "Schedule one informational interview this week",
            "Apply to one role that feels slightly out of reach",
            "Ask one question in an interview that shows your strategic thinking",
            "Each small action builds evidence and momentum",
            "Six months of small actions creates massive confidence transformation"
        ]
    },
    {
        "type": "content",
        "title": "Maintaining Confidence Through Challenges",
        "bullets": [
            "Setbacks don't erase your capabilities - they test your resilience",
            "Confidence fluctuates - that's normal; recommit to your foundation",
            "Return to your evidence journal when doubt creeps in",
            "Seek support from mentors and peers during difficult moments",
            "Remember: Your track record speaks louder than any single setback"
        ]
    },

    # LESSON 4: The 7 Success Habits Deep Dive (12-15 slides - incorporating existing content)
    {
        "type": "title",
        "title": "7 Success Habits to Develop Now"
    },
    {
        "type": "content",
        "title": "Success Habit #1: Have A Specific Vision",
        "bullets": [
            "Most people don't have a specific vision for their life or success",
            "What do you want? When do you want it by? And why do you want it?",
            "With clarity of vision, when things get hard... you have the ability to keep going and stay locked on target",
            "Vision isn't about what you are going to accomplish, its more about what you're EXCLUDING",
            "My Challenge To You: Think about and decide what your vision is for yourself and your business"
        ]
    },
    {
        "type": "content",
        "title": "Creating Your Career Vision",
        "bullets": [
            "Define your ideal role: responsibilities, company type, team structure",
            "Set specific income goals: base salary, OTE, equity targets",
            "Identify your timeline: 90 days, 6 months, 1 year milestones",
            "Clarify your why: What will this career success enable in your life?",
            "Write it down and review it daily to maintain focus and motivation"
        ]
    },
    {
        "type": "content",
        "title": "Success Habit #2: Stop Negotiating With Yourself",
        "bullets": [
            "How many times during the day do you negotiate with yourself?",
            "When the alarm goes off..do you wake up?",
            "When you say you are going to go to the gym... do you?",
            "When you write down your goals... do you accomplish them?",
            "When you say you are going to do more prospecting... do you?",
            "When you say you are going to give 100% every day... do you do it?"
        ]
    },
    {
        "type": "content",
        "title": "Building Non-Negotiable Standards",
        "bullets": [
            "Self-trust is built through keeping promises to yourself",
            "Every time you negotiate with yourself, you erode self-confidence",
            "Successful people eliminate decision fatigue with non-negotiable routines",
            "Your job search commitments: daily outreach, weekly applications, consistent follow-up",
            "The momentum from keeping promises compounds into career success"
        ]
    },
    {
        "type": "content",
        "title": "Success Habit #3: Soft Skills Vs. Hard Skills",
        "bullets": [
            "Hard skills are the actual tactical stuff you'd do to get sales, scale and grow your business. These are skills you CAN buy",
            "Soft skills are skills you CAN'T buy... you have to develop. Soft skills are things like your relationship with money, your emotional discipline, your ability to handle pressure, confidence and the ability to not sell sabotage",
            "Soft skills are always the limiting factor to your success",
            "Confidence is one of the biggest soft skills...start by stacking wins in your life"
        ]
    },
    {
        "type": "content",
        "title": "Developing Critical Soft Skills for Job Search",
        "bullets": [
            "Emotional regulation: Staying calm and confident during rejection",
            "Relationship building: Creating genuine connections with recruiters and hiring managers",
            "Communication: Articulating your value clearly and compellingly",
            "Resilience: Bouncing back from setbacks and maintaining momentum",
            "Strategic thinking: Positioning yourself as a problem-solver, not just a candidate"
        ]
    },
    {
        "type": "content",
        "title": "Success Habit #4: Take Extreme Ownership",
        "bullets": [
            "Most people place blame on everything and everyone else when it comes to lack of success in any area of your life",
            "The moment you stop that and come to realize that everything starts and stops with you...your success will explode",
            "Take accountability for your success",
            "Realize nobody is beyond suffering and setbacks"
        ]
    },
    {
        "type": "content",
        "title": "Extreme Ownership in Your Job Search",
        "bullets": [
            "Your results are a direct reflection of your actions and decisions",
            "Not getting interviews? Your resume, targeting, or outreach needs improvement",
            "Not getting offers? Your interview skills or positioning need refinement",
            "Not getting the salary you want? Your negotiation approach needs work",
            "Taking ownership gives you power to change your outcomes"
        ]
    },
    {
        "type": "content",
        "title": "Success Habit #5: Don't Think of Success as Linear",
        "bullets": [
            "Most people think of success as being a start and a finish. It's not.",
            "When people think like that...they end up starting many things and finishing nothing, but you'll feel like you've been doing everything possible to be successful",
            "For example, switching businesses, methods, courses, etc.",
            "What happens is that you end of starting a lot and finishing nothing",
            "Instead, think of success as planting seeds...then consistently watering them and eventually harvesting"
        ]
    },
    {
        "type": "content",
        "title": "The Non-Linear Path to Career Success",
        "bullets": [
            "Job search progress is not a straight line - expect ups and downs",
            "Weeks of silence can be followed by multiple opportunities at once",
            "Trust the process even when results aren't immediately visible",
            "Your consistent actions are accumulating - the compound effect takes time",
            "Stay committed to your strategy for at least 60-90 days before pivoting"
        ]
    },
    {
        "type": "content",
        "title": "Success Habit #6: Questions Not Statements",
        "bullets": [
            "Asking questions always opens the mind to solutions",
            "Statements always close the mind to the possibility of solutions",
            "Train yourself to say \"how can I?\" instead of \"I can't.\"",
            "\"How can I scale this offer up?\" instead of \"I can't scale this offer up.\""
        ]
    },
    {
        "type": "content",
        "title": "Empowering Questions for Job Search",
        "bullets": [
            "Instead of \"I can't get interviews\" → \"How can I improve my application approach?\"",
            "Instead of \"I'm not qualified\" → \"How can I position my experience to highlight relevant value?\"",
            "Instead of \"I won't get that salary\" → \"How can I negotiate for the compensation I deserve?\"",
            "Instead of \"I don't have connections\" → \"How can I strategically build relationships?\"",
            "Questions activate problem-solving; statements activate defensiveness"
        ]
    },
    {
        "type": "content",
        "title": "Success Habit #7: Be A Shark",
        "bullets": [
            "What do sharks do?",
            "Does the shark ever wake up and decide not to do shark things that day? No!",
            "Same goes for you as a salesperson and entrepreneur, get up every day and do whatever it takes to be successful",
            "Hunt down your goals with the same ferocity that a shark would"
        ]
    },
    {
        "type": "content",
        "title": "Relentless Execution in Your Job Search",
        "bullets": [
            "Show up every day with consistent effort regardless of how you feel",
            "Maintain your outreach and application rhythm even during slow periods",
            "Follow up persistently but professionally with opportunities",
            "Don't let rejection slow down your momentum - keep hunting",
            "Success comes to those who refuse to quit when things get hard"
        ]
    },

    # LESSON 5: Creating Your Personal Success System (8-10 slides)
    {
        "type": "title",
        "title": "Creating Your Personal Success System"
    },
    {
        "type": "content",
        "title": "Why Systems Beat Goals",
        "bullets": [
            "Goals tell you where you want to go; systems get you there",
            "You don't rise to the level of your goals - you fall to the level of your systems",
            "Relying on motivation alone leads to inconsistent effort and poor results",
            "Systems create automatic progress regardless of how you feel",
            "Winners and losers have the same goals; winners have better systems"
        ]
    },
    {
        "type": "content",
        "title": "The Components of a Success System",
        "bullets": [
            "DAILY HABITS: Non-negotiable actions you take every single day",
            "WEEKLY RHYTHMS: Recurring activities that move your job search forward",
            "TRACKING METRICS: Data that shows progress and identifies improvement areas",
            "FEEDBACK LOOPS: Regular review and adjustment of your approach",
            "ACCOUNTABILITY: People or systems that keep you honest and consistent"
        ]
    },
    {
        "type": "content",
        "title": "Your Daily Job Search System",
        "bullets": [
            "Morning: Review your vision and target company list (10 minutes)",
            "Mid-morning: 5 new LinkedIn connections or outreach messages (30 minutes)",
            "Afternoon: Research 2-3 target companies deeply (30 minutes)",
            "Evening: Update tracking spreadsheet and review progress (15 minutes)",
            "Total time investment: 85 minutes per day for career transformation"
        ]
    },
    {
        "type": "content",
        "title": "Your Weekly Job Search Rhythm",
        "bullets": [
            "Monday: Set weekly goals and priority target companies",
            "Tuesday-Thursday: Execute daily system + 3-5 applications to quality opportunities",
            "Friday: Review week's metrics, identify what worked, adjust approach",
            "Saturday: Interview preparation and skill development",
            "Sunday: Plan next week and recharge mentally",
            "Consistency over weeks and months compounds into major results"
        ]
    },
    {
        "type": "content",
        "title": "Essential Tracking Metrics",
        "bullets": [
            "Outreach: Connection requests sent, messages sent, response rate",
            "Applications: Jobs applied to, interviews secured, conversion rate",
            "Interviews: Interviews completed, offer rate, feedback received",
            "Network: New connections made, informational interviews conducted",
            "Learning: Skills practiced, feedback implemented, improvements made",
            "What gets measured gets managed - and improved"
        ]
    },
    {
        "type": "content",
        "title": "Building Feedback Loops",
        "bullets": [
            "Weekly self-review: What worked? What didn't? What will I test next?",
            "Track patterns: Which messages get responses? Which interviews go well?",
            "Seek external feedback: Mock interviews, message reviews, profile audits",
            "A/B test your approach: Try different headlines, messages, applications",
            "Iterate rapidly based on data, not assumptions"
        ]
    },
    {
        "type": "content",
        "title": "Accountability Systems That Work",
        "bullets": [
            "Find an accountability partner pursuing similar career goals",
            "Schedule weekly check-ins to report progress and commitments",
            "Join a community of job seekers for mutual support and motivation",
            "Share your goals with mentors who will hold you to high standards",
            "Use the Active Offer Accountability Log to track daily execution",
            "Public commitment increases follow-through significantly"
        ]
    },
    {
        "type": "content",
        "title": "Designing Your Environment for Success",
        "bullets": [
            "Remove distractions during your dedicated job search time",
            "Create a workspace that signals focus and professionalism",
            "Use tools that make execution easier: templates, trackers, calendars",
            "Eliminate friction: Have everything prepared and ready to go",
            "Your environment should make good behaviors easy and bad behaviors hard"
        ]
    },
    {
        "type": "content",
        "title": "The Power of Consistency Over Intensity",
        "bullets": [
            "Working 1 hour daily for 90 days beats working 10 hours in one weekend",
            "Consistency builds momentum, skills, and relationships over time",
            "Intense bursts of effort followed by inaction create poor results",
            "Your system should be sustainable long-term, not exhausting",
            "Small consistent actions compound into extraordinary outcomes"
        ]
    },
    {
        "type": "content",
        "title": "Your 90-Day Success System Implementation",
        "bullets": [
            "Days 1-30: Build the habit of daily execution, track everything, learn what works",
            "Days 31-60: Optimize based on data, increase volume, build momentum",
            "Days 61-90: Leverage your network and pipeline, multiple opportunities flowing",
            "This system, executed consistently, leads to interviews, offers, and career transformation",
            "Start today - your future self will thank you for the commitment"
        ]
    },
    {
        "type": "title",
        "title": "You Now Have the Mindset Foundation for Success"
    }
]

def generate_slides(output_dir):
    """Generate all slides and save as PNG files"""
    os.makedirs(output_dir, exist_ok=True)

    for i, slide_data in enumerate(slides_content, start=1):
        print(f"Generating slide {i}/{len(slides_content)}...")

        if slide_data["type"] == "title":
            img = create_title_slide(
                slide_data["title"],
                slide_data.get("subtitle")
            )
        else:  # content slide
            img = create_content_slide(
                slide_data["title"],
                slide_data["bullets"],
                slide_data.get("small_bullets", False)
            )

        # Save slide
        filename = f"{i}.png"
        filepath = os.path.join(output_dir, filename)
        img.save(filepath, "PNG", quality=95)
        print(f"  Saved: {filename}")

    print(f"\n✓ Successfully generated {len(slides_content)} slides")
    print(f"✓ Output directory: {output_dir}")

if __name__ == "__main__":
    output_directory = "/Users/terrancebrandon/Desktop/Active Offer/AO- Course Content/Active Offer- Course Material/M0- Mindset Expanded"
    generate_slides(output_directory)
