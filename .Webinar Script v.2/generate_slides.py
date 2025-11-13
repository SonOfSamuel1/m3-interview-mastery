#!/usr/bin/env python3
"""
Active Offer Webinar Slide Generator
Creates 120 professional PNG slides at 1920x1080 resolution
"""

from playwright.sync_api import sync_playwright
import os
import time

# Premium color palette - Professional blues and grays
COLORS = {
    'primary': '#1a365d',      # Deep blue
    'secondary': '#2c5282',    # Medium blue
    'accent': '#3182ce',       # Bright blue
    'text_dark': '#1a202c',    # Almost black
    'text_light': '#ffffff',   # White
    'gray_light': '#e2e8f0',   # Light gray
    'gray_medium': '#cbd5e0',  # Medium gray
    'gray_dark': '#4a5568',    # Dark gray
    'success': '#38a169',      # Green for checkmarks
    'warning': '#e53e3e',      # Red for X marks
}

def create_html_template(content, bg_color='#ffffff', text_color='#1a202c'):
    """Creates base HTML template for slides"""
    return f"""
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}

        body {{
            width: 1920px;
            height: 1080px;
            background: {bg_color};
            color: {text_color};
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Helvetica Neue', Arial, sans-serif;
            display: flex;
            align-items: center;
            justify-content: center;
            padding: 80px;
            overflow: hidden;
        }}

        .slide {{
            width: 100%;
            height: 100%;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            text-align: center;
        }}

        .slide-left {{
            text-align: left;
            align-items: flex-start;
        }}

        h1 {{
            font-size: 96px;
            font-weight: 700;
            line-height: 1.2;
            margin-bottom: 40px;
            color: {COLORS['primary']};
        }}

        h2 {{
            font-size: 72px;
            font-weight: 600;
            line-height: 1.3;
            margin-bottom: 30px;
            color: {COLORS['secondary']};
        }}

        h3 {{
            font-size: 56px;
            font-weight: 500;
            line-height: 1.4;
            margin-bottom: 24px;
            color: {COLORS['gray_dark']};
        }}

        p {{
            font-size: 42px;
            line-height: 1.6;
            margin-bottom: 20px;
            max-width: 1400px;
        }}

        .subhead {{
            font-size: 48px;
            color: {COLORS['gray_dark']};
            font-weight: 400;
            line-height: 1.5;
        }}

        .large-text {{
            font-size: 64px;
            font-weight: 600;
            line-height: 1.4;
            max-width: 1500px;
            margin: 40px 0;
        }}

        ul {{
            list-style: none;
            font-size: 42px;
            line-height: 1.8;
            text-align: left;
            max-width: 1400px;
        }}

        li {{
            margin-bottom: 24px;
            padding-left: 50px;
            position: relative;
        }}

        li:before {{
            content: "•";
            position: absolute;
            left: 0;
            color: {COLORS['accent']};
            font-weight: bold;
            font-size: 48px;
        }}

        .checkmark:before {{
            content: "✓";
            color: {COLORS['success']};
        }}

        .xmark:before {{
            content: "✗";
            color: {COLORS['warning']};
        }}

        .split {{
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 60px;
            width: 100%;
            align-items: start;
        }}

        .split h3 {{
            margin-bottom: 30px;
            font-size: 48px;
        }}

        .split ul {{
            font-size: 36px;
        }}

        .split li {{
            margin-bottom: 20px;
        }}

        .box {{
            background: {COLORS['gray_light']};
            padding: 40px;
            border-radius: 12px;
            margin: 20px 0;
        }}

        .box-dark {{
            background: {COLORS['primary']};
            color: {COLORS['text_light']};
            padding: 40px;
            border-radius: 12px;
            margin: 20px 0;
        }}

        .number-stat {{
            font-size: 120px;
            font-weight: 700;
            color: {COLORS['accent']};
            margin: 30px 0;
        }}

        .quote {{
            font-size: 48px;
            font-style: italic;
            line-height: 1.6;
            max-width: 1400px;
            padding: 40px;
            border-left: 8px solid {COLORS['accent']};
            background: {COLORS['gray_light']};
            border-radius: 8px;
            text-align: left;
        }}

        .cta {{
            background: {COLORS['accent']};
            color: {COLORS['text_light']};
            padding: 30px 60px;
            font-size: 56px;
            font-weight: 600;
            border-radius: 12px;
            margin: 40px 0;
            display: inline-block;
        }}

        .small-text {{
            font-size: 32px;
            color: {COLORS['gray_dark']};
            margin-top: 20px;
        }}

        .steps {{
            display: flex;
            justify-content: space-between;
            width: 100%;
            margin: 40px 0;
        }}

        .step {{
            flex: 1;
            padding: 30px;
            text-align: center;
        }}

        .step-number {{
            font-size: 72px;
            font-weight: 700;
            color: {COLORS['accent']};
            margin-bottom: 20px;
        }}

        .step-title {{
            font-size: 36px;
            font-weight: 600;
            color: {COLORS['primary']};
        }}
    </style>
</head>
<body>
    {content}
</body>
</html>
"""

# Slide definitions
SLIDES = [
    # PHASE 1: INTRODUCTION (Slides 1-15)
    {
        'num': 1,
        'html': create_html_template(f"""
            <div class="slide">
                <h1 style="color: {COLORS['primary']};">The Active Offer System</h1>
                <p class="subhead" style="max-width: 1300px;">How to Position Yourself So Hiring Managers Seek YOU Out<br>(And Double Your Income in 90 Days)</p>
            </div>
        """)
    },
    {
        'num': 2,
        'html': create_html_template(f"""
            <div class="slide">
                <h2>From $150K to $500K in One Year</h2>
                <p class="large-text">While Working LESS and From Home</p>
            </div>
        """)
    },
    {
        'num': 3,
        'html': create_html_template(f"""
            <div class="slide slide-left">
                <h2>Sound Familiar?</h2>
                <ul>
                    <li>Stuck at the same income level for years</li>
                    <li>Working 50-60+ hour weeks, constant travel</li>
                    <li>Watching others get promoted while you grind</li>
                    <li>Sending out resumes and getting nowhere</li>
                    <li>Feeling undervalued and overlooked</li>
                </ul>
            </div>
        """)
    },
    {
        'num': 4,
        'html': create_html_template(f"""
            <div class="slide slide-left">
                <h2>You've Tried Everything...</h2>
                <ul>
                    <li class="xmark">"Polish your resume"</li>
                    <li class="xmark">"Apply to 100+ jobs"</li>
                    <li class="xmark">"Network at events"</li>
                    <li class="xmark">"Work harder at current job"</li>
                </ul>
                <p style="margin-top: 60px; font-size: 52px; font-weight: 600;">Yet you're still stuck</p>
            </div>
        """)
    },
    {
        'num': 5,
        'html': create_html_template(f"""
            <div class="slide">
                <h2>It's Not Your Fault</h2>
                <p class="large-text">You've been following advice that was designed to keep you powerless</p>
                <p class="subhead" style="margin-top: 60px;">Let me explain...</p>
            </div>
        """)
    },
    {
        'num': 6,
        'html': create_html_template(f"""
            <div class="slide slide-left">
                <h2>I Was Just Like You</h2>
                <ul>
                    <li>10 years at AT&T</li>
                    <li>Never broke $150K despite being top performer</li>
                    <li>Working constantly, traveling every week</li>
                    <li>Missing family time, burning out</li>
                </ul>
            </div>
        """)
    },
    {
        'num': 7,
        'html': create_html_template(f"""
            <div class="slide">
                <h2>Then I Got Laid Off</h2>
                <p class="large-text">After giving everything to that company for a decade, I was just another number</p>
                <p class="subhead" style="margin-top: 60px;">Feeling lost, questioning everything</p>
            </div>
        """)
    },
    {
        'num': 8,
        'html': create_html_template(f"""
            <div class="slide">
                <h2>That's When I Discovered Something</h2>
                <p class="large-text">A friend asked me: "What if instead of chasing jobs, you made companies come to YOU?"</p>
                <p class="subhead" style="margin-top: 60px;">It sounded crazy... but I was desperate enough to try</p>
            </div>
        """)
    },
    {
        'num': 9,
        'html': create_html_template(f"""
            <div class="slide">
                <h2 style="margin-bottom: 80px;">Here's What Changed Everything</h2>
                <p class="large-text">Your income isn't determined by how hard you work...</p>
            </div>
        """)
    },
    {
        'num': 10,
        'html': create_html_template(f"""
            <div class="slide">
                <p class="large-text" style="font-size: 72px; font-weight: 700; color: {COLORS['primary']};">It's determined by WHO is hiring you and how you POSITION yourself before the conversation starts</p>
            </div>
        """)
    },
    {
        'num': 11,
        'html': create_html_template(f"""
            <div class="slide">
                <h2 style="margin-bottom: 60px;">OLD WAY vs. NEW WAY</h2>
                <div class="split">
                    <div>
                        <h3 style="color: {COLORS['warning']};">Old Way</h3>
                        <ul>
                            <li>Apply through job portals</li>
                            <li>Compete with 200+ candidates</li>
                            <li>Hope for callbacks</li>
                            <li>Accept lowball offers</li>
                            <li>Stay powerless</li>
                        </ul>
                    </div>
                    <div>
                        <h3 style="color: {COLORS['success']};">New Way</h3>
                        <ul>
                            <li>Target ideal companies</li>
                            <li>Hiring managers seek YOU</li>
                            <li>Multiple competing offers</li>
                            <li>Negotiate from strength</li>
                            <li>Control your income</li>
                        </ul>
                    </div>
                </div>
            </div>
        """)
    },
    {
        'num': 12,
        'html': create_html_template(f"""
            <div class="slide slide-left">
                <h2>Once I Applied This...</h2>
                <ul style="font-size: 48px;">
                    <li class="checkmark">3 competing offers in 8 weeks</li>
                    <li class="checkmark">Hired within 6 days</li>
                    <li class="checkmark">First year: $500K+</li>
                    <li class="checkmark">Working from home</li>
                    <li class="checkmark">Less than 45 hours/week</li>
                </ul>
            </div>
        """)
    },
    {
        'num': 13,
        'html': create_html_template(f"""
            <div class="slide slide-left">
                <h2>This Works For Others Too</h2>
                <ul style="font-size: 44px;">
                    <li>Darrel: $90K raise on first offer</li>
                    <li>Sarah: $514K → $1.08M in 2 years</li>
                    <li>Multiple students: $50K-$150K raises</li>
                    <li>Average: 30-90 days to results</li>
                </ul>
            </div>
        """)
    },
    {
        'num': 14,
        'html': create_html_template(f"""
            <div class="slide slide-left">
                <h2>In The Next 60 Minutes...</h2>
                <ul>
                    <li>The 3 secrets to commanding premium offers</li>
                    <li>Why traditional job search keeps you powerless</li>
                    <li>The exact 4-step system I used (and my students use)</li>
                    <li>How to implement this in 30 minutes/day while employed</li>
                </ul>
            </div>
        """)
    },
    {
        'num': 15,
        'html': create_html_template(f"""
            <div class="slide">
                <h2>Before We Start, One Request</h2>
                <p class="large-text">Keep an open mind. This is different from everything you've been taught about career advancement.</p>
                <p class="subhead" style="margin-top: 80px;">Sound good? Let's dive in...</p>
            </div>
        """)
    },

    # PHASE 2: SECRET #1 - THE VEHICLE (Slides 16-45)
    {
        'num': 16,
        'html': create_html_template(f"""
            <div class="slide">
                <h1 style="color: {COLORS['accent']};">Secret #1</h1>
            </div>
        """)
    },
    {
        'num': 17,
        'html': create_html_template(f"""
            <div class="slide">
                <h2>The Active Offer Methodology</h2>
                <p class="subhead">Why Traditional Job Search Keeps You Stuck (And What To Do Instead)</p>
            </div>
        """)
    },
    {
        'num': 18,
        'html': create_html_template(f"""
            <div class="slide">
                <h2 style="margin-bottom: 60px;">Most Salespeople Believe...</h2>
                <p class="large-text">"The way to advance is to work harder at my current job or apply to more positions"</p>
                <p class="small-text" style="margin-top: 60px; color: {COLORS['warning']}; font-size: 42px; font-weight: 600;">This is a lie</p>
            </div>
        """)
    },
    {
        'num': 19,
        'html': create_html_template(f"""
            <div class="slide">
                <h2 style="margin-bottom: 40px;">Here's The Problem With That Belief</h2>
                <p class="large-text" style="font-size: 48px;">Job portals are designed to commoditize you. You're one of 200+ applicants, and the hiring manager never sees what makes you special.</p>
            </div>
        """)
    },
    {
        'num': 20,
        'html': create_html_template(f"""
            <div class="slide">
                <h2 style="margin-bottom: 40px;">The Best Opportunities Never Get Posted</h2>
                <div class="number-stat">80%</div>
                <p class="large-text" style="font-size: 44px;">of executive sales roles are filled through referrals and direct outreach before they're ever posted</p>
                <p class="subhead" style="margin-top: 60px;">If you're applying online, you're already too late</p>
            </div>
        """)
    },
    {
        'num': 21,
        'html': create_html_template(f"""
            <div class="slide">
                <h2 style="margin-bottom: 40px;">Working Harder Doesn't Change WHO Is Hiring You</h2>
                <p class="large-text" style="font-size: 48px;">You can be the best salesperson in a $100K role... but that doesn't automatically qualify you for a $300K role at a different company. You need POSITIONING.</p>
            </div>
        """)
    },
    {
        'num': 22,
        'html': create_html_template(f"""
            <div class="slide">
                <h2>Let Me Tell You The Full Story</h2>
                <p class="large-text">For 10 years at AT&T, I gave everything...</p>
            </div>
        """)
    },
    {
        'num': 23,
        'html': create_html_template(f"""
            <div class="slide slide-left">
                <h2 style="margin-bottom: 50px;">The Grind</h2>
                <ul>
                    <li>Top performer every year</li>
                    <li>Working 60+ hour weeks</li>
                    <li>Constant travel (home 2 days/week)</li>
                    <li>Missing my kids growing up</li>
                    <li>Never broke $150K despite hitting quota 130%</li>
                </ul>
            </div>
        """)
    },
    {
        'num': 24,
        'html': create_html_template(f"""
            <div class="slide">
                <h2 style="margin-bottom: 60px;">Then In 2015...</h2>
                <p class="large-text">I got laid off. After everything I'd given, I was just another number on a spreadsheet.</p>
                <p class="subhead" style="margin-top: 80px;">Devastated, questioning everything</p>
            </div>
        """)
    },
    {
        'num': 25,
        'html': create_html_template(f"""
            <div class="slide">
                <h2 style="margin-bottom: 40px;">I Called My Friend Simon<br>(VP at a Tech Company)</h2>
                <div class="quote">"Why are you rowing so hard in the wrong boat?"</div>
                <p class="subhead" style="margin-top: 40px;">My reaction: "What do you mean?"</p>
            </div>
        """)
    },
    {
        'num': 26,
        'html': create_html_template(f"""
            <div class="slide">
                <h2 style="margin-bottom: 40px;">Simon's Response</h2>
                <p class="large-text" style="font-size: 48px;">"You're amazing at sales, but you're in a role that caps you. What if you could pick the BEST offer available for your skillset?"</p>
                <p class="subhead" style="margin-top: 60px;">I'd never thought of it that way</p>
            </div>
        """)
    },
    {
        'num': 27,
        'html': create_html_template(f"""
            <div class="slide">
                <h2 style="margin-bottom: 60px;">That's When It Hit Me</h2>
                <p class="large-text">I wasn't failing. I was just in the wrong POSITION. My skills were worth way more—I just needed to position myself correctly.</p>
            </div>
        """)
    },
    {
        'num': 28,
        'html': create_html_template(f"""
            <div class="slide">
                <h2 style="margin-bottom: 60px;">So I Created A System</h2>
                <p class="large-text">I reverse-engineered the exact role I wanted, identified the hiring managers, and positioned myself so THEY came to ME.</p>
            </div>
        """)
    },
    {
        'num': 29,
        'html': create_html_template(f"""
            <div class="slide slide-left">
                <h2 style="margin-bottom: 50px;">The Result</h2>
                <ul style="font-size: 48px;">
                    <li>8 weeks of implementation</li>
                    <li>3 competing offers</li>
                    <li>Hired within 6 days of interviews</li>
                    <li>First year: $500K+</li>
                    <li>Work from home, less than 45 hours/week</li>
                </ul>
            </div>
        """)
    },
    {
        'num': 30,
        'html': create_html_template(f"""
            <div class="slide">
                <h2 style="margin-bottom: 80px;">Here's The Truth</h2>
                <p class="large-text" style="font-size: 56px; font-weight: 700;">The fastest way to double your income is to strategically POSITION yourself so the right companies seek YOU out</p>
            </div>
        """)
    },
    {
        'num': 31,
        'html': create_html_template(f"""
            <div class="slide">
                <h2 style="margin-bottom: 50px;">The Active Offer System</h2>
                <div class="steps">
                    <div class="step">
                        <div class="step-number">1</div>
                        <div class="step-title">Profile<br>Matching</div>
                    </div>
                    <div class="step">
                        <div class="step-number">2</div>
                        <div class="step-title">Reverse<br>Attraction</div>
                    </div>
                    <div class="step">
                        <div class="step-number">3</div>
                        <div class="step-title">Interview<br>Mastery</div>
                    </div>
                    <div class="step">
                        <div class="step-number">4</div>
                        <div class="step-title">Negotiating<br>the Offer</div>
                    </div>
                </div>
            </div>
        """)
    },
    {
        'num': 32,
        'html': create_html_template(f"""
            <div class="slide slide-left">
                <h2 style="margin-bottom: 40px;">Step 1: Profile Matching</h2>
                <p style="margin-bottom: 30px;">Reverse-engineer your ideal role based on:</p>
                <ul>
                    <li>Income goals ($150K? $300K? $500K+?)</li>
                    <li>Lifestyle preferences (remote? travel? hours?)</li>
                    <li>Company type (startup? enterprise? Series B?)</li>
                    <li>Industry alignment (SaaS? Pharma? Manufacturing?)</li>
                </ul>
            </div>
        """)
    },
    {
        'num': 33,
        'html': create_html_template(f"""
            <div class="slide">
                <h2 style="margin-bottom: 60px;">Most People Skip This Step</h2>
                <p class="large-text">They apply to any "Senior Sales" role and wonder why nothing fits. You need to TARGET strategically.</p>
            </div>
        """)
    },
    {
        'num': 34,
        'html': create_html_template(f"""
            <div class="slide slide-left">
                <h2 style="margin-bottom: 40px;">Step 2: Reverse Attraction</h2>
                <p style="margin-bottom: 30px;">Instead of chasing hiring managers, make them come to YOU through:</p>
                <ul>
                    <li>Optimized LinkedIn presence</li>
                    <li>Strategic referral navigation</li>
                    <li>Direct outreach (the right way)</li>
                    <li>Positioning as the obvious choice</li>
                </ul>
            </div>
        """)
    },
    {
        'num': 35,
        'html': create_html_template(f"""
            <div class="slide">
                <h2 style="margin-bottom: 40px;">When They Come To You...</h2>
                <p class="large-text">You enter the conversation from a position of POWER, not desperation</p>
                <p class="subhead" style="margin-top: 60px;">Result: Better negotiation leverage, faster hiring process</p>
            </div>
        """)
    },
    {
        'num': 36,
        'html': create_html_template(f"""
            <div class="slide slide-left">
                <h2 style="margin-bottom: 40px;">Step 3: Interview Mastery</h2>
                <p style="margin-bottom: 30px;">This isn't about "performing well." It's about:</p>
                <ul>
                    <li>Evaluating THEM as much as they evaluate you</li>
                    <li>Positioning your value strategically</li>
                    <li>Creating urgency through other opportunities</li>
                    <li>Making them want to close YOU</li>
                </ul>
            </div>
        """)
    },
    {
        'num': 37,
        'html': create_html_template(f"""
            <div class="slide">
                <h2 style="margin-bottom: 60px;">Interviews Aren't Tests</h2>
                <p class="large-text">They're strategic conversations where you assess fit and position value</p>
                <p class="subhead" style="margin-top: 80px;">From "I hope they like me" → "Is this the right opportunity?"</p>
            </div>
        """)
    },
    {
        'num': 38,
        'html': create_html_template(f"""
            <div class="slide slide-left">
                <h2 style="margin-bottom: 40px;">Step 4: Negotiating the Offer</h2>
                <p style="margin-bottom: 30px;">With multiple competing offers, you negotiate from abundance:</p>
                <ul>
                    <li>Leveraging other offers</li>
                    <li>Structuring comp strategically</li>
                    <li>Getting more than they offered</li>
                    <li>Creating win-win scenarios</li>
                </ul>
            </div>
        """)
    },
    {
        'num': 39,
        'html': create_html_template(f"""
            <div class="slide">
                <h2 style="margin-bottom: 40px;">This Is Where Tens Of Thousands Get Added</h2>
                <p class="large-text">$50K-$150K raises don't happen by accepting the first offer</p>
                <p class="subhead" style="margin-top: 60px;">Example: One student got $90K more just by having 2 competing offers</p>
            </div>
        """)
    },
    {
        'num': 40,
        'html': create_html_template(f"""
            <div class="slide">
                <h2 style="margin-bottom: 50px;">Each Step Builds On The Last</h2>
                <div class="steps">
                    <div class="step">
                        <div class="step-number">1</div>
                        <div class="step-title">Profile<br>Matching</div>
                    </div>
                    <div style="font-size: 72px; color: {COLORS['accent']};">→</div>
                    <div class="step">
                        <div class="step-number">2</div>
                        <div class="step-title">Reverse<br>Attraction</div>
                    </div>
                    <div style="font-size: 72px; color: {COLORS['accent']};">→</div>
                    <div class="step">
                        <div class="step-number">3</div>
                        <div class="step-title">Interview<br>Mastery</div>
                    </div>
                    <div style="font-size: 72px; color: {COLORS['accent']};">→</div>
                    <div class="step">
                        <div class="step-number">4</div>
                        <div class="step-title">Negotiating</div>
                    </div>
                </div>
                <p class="subhead" style="margin-top: 40px;">This isn't 4 separate tactics. It's ONE unified system for commanding premium offers.</p>
            </div>
        """)
    },
    {
        'num': 41,
        'html': create_html_template(f"""
            <div class="slide slide-left">
                <h2 style="margin-bottom: 50px;">Meet Darrel</h2>
                <ul>
                    <li>Stuck at $130K for 3 years</li>
                    <li>Overworked, undervalued</li>
                    <li>Frustrated with career plateau</li>
                </ul>
            </div>
        """)
    },
    {
        'num': 42,
        'html': create_html_template(f"""
            <div class="slide slide-left">
                <h2 style="margin-bottom: 40px;">What Happened When Darrel Applied This</h2>
                <ul style="font-size: 40px;">
                    <li>Week 1-2: Profile matching (identified 12 target companies)</li>
                    <li>Week 3-6: Reverse attraction (5 hiring managers reached out)</li>
                    <li>Week 7-8: Interviews with 3 companies</li>
                    <li>Week 9: 2 competing offers</li>
                </ul>
            </div>
        """)
    },
    {
        'num': 43,
        'html': create_html_template(f"""
            <div class="slide">
                <h2 style="margin-bottom: 60px;">Darrel's Result</h2>
                <p style="font-size: 52px; margin-bottom: 30px;">First offer: <span style="color: {COLORS['accent']}; font-weight: 700;">$220K</span> ($90K raise)</p>
                <p style="font-size: 52px; margin-bottom: 30px;">One year later: <span style="color: {COLORS['accent']}; font-weight: 700;">$300K</span> ($80K raise + $70K stock)</p>
                <div class="number-stat" style="margin-top: 60px;">$170K+</div>
                <p class="subhead">Total increase in comp in 18 months</p>
            </div>
        """)
    },
    {
        'num': 44,
        'html': create_html_template(f"""
            <div class="slide slide-left">
                <h2 style="margin-bottom: 50px;">This Works Because...</h2>
                <ul>
                    <li>It's based on how hiring actually happens at senior levels</li>
                    <li>It positions you as sought-after, not desperate</li>
                    <li>It creates competition for your talents</li>
                    <li>It's repeatable (use it every career move)</li>
                </ul>
            </div>
        """)
    },
    {
        'num': 45,
        'html': create_html_template(f"""
            <div class="slide">
                <h2 style="margin-bottom: 60px;">Secret #1 Recap</h2>
                <p class="large-text">The Active Offer System: Position yourself strategically so hiring managers seek YOU out, creating multiple competing offers</p>
                <p class="subhead" style="margin-top: 80px;">Make sense?</p>
            </div>
        """)
    },

    # PHASE 3: SECRET #2 - INTERNAL BELIEF (Slides 46-70)
    {
        'num': 46,
        'html': create_html_template(f"""
            <div class="slide">
                <h1 style="color: {COLORS['accent']};">Secret #2</h1>
            </div>
        """)
    },
    {
        'num': 47,
        'html': create_html_template(f"""
            <div class="slide">
                <h2>Why YOU Are Qualified For These Roles</h2>
                <p class="subhead">(Even If You Don't Think So)</p>
            </div>
        """)
    },
    {
        'num': 48,
        'html': create_html_template(f"""
            <div class="slide">
                <h2 style="margin-bottom: 80px;">You Might Be Thinking...</h2>
                <p class="large-text">"I'm not qualified for $300K+ roles. Those are for people better than me."</p>
            </div>
        """)
    },
    {
        'num': 49,
        'html': create_html_template(f"""
            <div class="slide slide-left">
                <h2 style="margin-bottom: 50px;">Here's Why You Think That</h2>
                <ul>
                    <li>Job descriptions are intimidating</li>
                    <li>You focus on what you DON'T have</li>
                    <li>You compare yourself to others</li>
                    <li>Imposter syndrome kicks in</li>
                </ul>
            </div>
        """)
    },
    {
        'num': 50,
        'html': create_html_template(f"""
            <div class="slide">
                <h2 style="margin-bottom: 60px;">But Here's The Truth</h2>
                <p class="large-text">Companies don't pay $300K for perfect candidates. They pay $300K for people who can DELIVER results.</p>
                <p class="subhead" style="margin-top: 80px;">Can you deliver results?</p>
            </div>
        """)
    },
    {
        'num': 51,
        'html': create_html_template(f"""
            <div class="slide slide-left">
                <h2 style="margin-bottom: 40px;">What $300K Companies Actually Need</h2>
                <ul>
                    <li>Proven ability to close deals</li>
                    <li>Understanding of complex sales cycles</li>
                    <li>Relationship-building skills</li>
                    <li>Ability to navigate enterprise accounts</li>
                </ul>
                <p class="subhead" style="margin-top: 60px;">Notice: These are all TRANSFERABLE skills</p>
            </div>
        """)
    },
    {
        'num': 52,
        'html': create_html_template(f"""
            <div class="slide">
                <h2 style="margin-bottom: 60px;">If You Can Sell, You Can Sell</h2>
                <p class="large-text">Pharma → SaaS. Manufacturing → Tech. Insurance → Finance.</p>
                <p class="subhead" style="margin-top: 80px;">The fundamentals are the same. You just need to POSITION them correctly.</p>
            </div>
        """)
    },
    {
        'num': 53,
        'html': create_html_template(f"""
            <div class="slide">
                <h2 style="margin-bottom: 80px;">I Had The Same Doubt</h2>
                <p class="large-text">When I first looked at $400K+ tech sales roles, I thought "I'm a telecom guy. They won't want me."</p>
            </div>
        """)
    },
    {
        'num': 54,
        'html': create_html_template(f"""
            <div class="slide">
                <h2 style="margin-bottom: 60px;">I Almost Talked Myself Out Of It</h2>
                <p class="large-text">I was about to only apply to telecom companies (where comp caps at $180K)</p>
                <p class="subhead" style="margin-top: 80px;">But something told me to at least TRY</p>
            </div>
        """)
    },
    {
        'num': 55,
        'html': create_html_template(f"""
            <div class="slide slide-left">
                <h2 style="margin-bottom: 40px;">Then I Inventoried My Value</h2>
                <ul>
                    <li>10 years closing enterprise deals</li>
                    <li>Consistent quota attainment</li>
                    <li>Complex sales cycle experience</li>
                    <li>Team leadership</li>
                    <li>Account management</li>
                </ul>
            </div>
        """)
    },
    {
        'num': 56,
        'html': create_html_template(f"""
            <div class="slide">
                <h2 style="margin-bottom: 80px;">I Realized...</h2>
                <p class="large-text">These skills were worth $400K+ in the RIGHT market. I just needed to position them correctly for tech buyers.</p>
            </div>
        """)
    },
    {
        'num': 57,
        'html': create_html_template(f"""
            <div class="slide">
                <h2 style="margin-bottom: 60px;">When I Repositioned Myself</h2>
                <p class="large-text" style="font-size: 48px;">Hiring managers SAW the value. They didn't care I wasn't "from tech." They cared I could close deals.</p>
                <p class="subhead" style="margin-top: 60px;">Result: First year $500K+</p>
            </div>
        """)
    },
    {
        'num': 58,
        'html': create_html_template(f"""
            <div class="slide">
                <h2 style="margin-bottom: 80px;">Here's What You Need To Believe</h2>
                <p class="large-text" style="font-size: 56px; font-weight: 700;">Your skills ARE valuable. You just need to inventory them and position them for premium markets.</p>
            </div>
        """)
    },
    {
        'num': 59,
        'html': create_html_template(f"""
            <div class="slide slide-left">
                <h2 style="margin-bottom: 40px;">The Value Inventory Exercise</h2>
                <ul>
                    <li>Deal sizes you've closed</li>
                    <li>Sales cycle complexity</li>
                    <li>Industries served</li>
                    <li>Team leadership</li>
                    <li>Quota attainment %</li>
                    <li>Special certifications/skills</li>
                </ul>
            </div>
        """)
    },
    {
        'num': 60,
        'html': create_html_template(f"""
            <div class="slide">
                <h2 style="margin-bottom: 40px;">Then Position It For Premium Markets</h2>
                <div style="text-align: left; max-width: 1500px; margin: 40px auto;">
                    <p style="font-size: 38px; margin-bottom: 20px; color: {COLORS['warning']};">
                        <span style="font-weight: 700;">DON'T say:</span> "Sold telecom services"
                    </p>
                    <p style="font-size: 38px; margin-top: 40px; color: {COLORS['success']};">
                        <span style="font-weight: 700;">DO say:</span> "Closed $2M+ enterprise deals in 9-12 month sales cycles"
                    </p>
                </div>
                <p class="subhead" style="margin-top: 60px;">The difference: Transferable vs. industry-specific framing</p>
            </div>
        """)
    },
    {
        'num': 61,
        'html': create_html_template(f"""
            <div class="slide slide-left">
                <h2 style="margin-bottom: 40px;">Where The $300K+ Roles Are</h2>
                <ul>
                    <li>SaaS (especially enterprise)</li>
                    <li>Tech (cybersecurity, data, cloud)</li>
                    <li>Pharma/Biotech</li>
                    <li>Financial services</li>
                    <li>Manufacturing tech</li>
                </ul>
                <p class="subhead" style="margin-top: 50px;">Your skills transfer to ALL of these</p>
            </div>
        """)
    },
    {
        'num': 62,
        'html': create_html_template(f"""
            <div class="slide slide-left">
                <h2 style="margin-bottom: 50px;">Meet Jennifer</h2>
                <ul>
                    <li>8 years in pharmaceutical sales</li>
                    <li>Making $115K</li>
                    <li>Felt "stuck in pharma"</li>
                    <li>Scared to pivot to tech</li>
                </ul>
            </div>
        """)
    },
    {
        'num': 63,
        'html': create_html_template(f"""
            <div class="slide">
                <div class="quote">"I thought tech companies would laugh at my pharma background. I almost didn't even try."</div>
            </div>
        """)
    },
    {
        'num': 64,
        'html': create_html_template(f"""
            <div class="slide slide-left">
                <h2 style="margin-bottom: 40px;">What Happened When She Applied Profile Matching</h2>
                <p style="margin-bottom: 30px;">We inventoried her transferable skills:</p>
                <ul>
                    <li>Selling to C-suite in hospital systems</li>
                    <li>$5M+ territory management</li>
                    <li>Complex regulatory environment navigation</li>
                    <li>Team collaboration across functions</li>
                </ul>
            </div>
        """)
    },
    {
        'num': 65,
        'html': create_html_template(f"""
            <div class="slide">
                <h2 style="margin-bottom: 60px;">We Repositioned Her For Healthcare SaaS</h2>
                <p class="large-text" style="font-size: 48px;">"Enterprise sales professional with proven C-suite selling in highly regulated environments"</p>
                <p class="subhead" style="margin-top: 80px;">Health tech companies were VERY interested</p>
            </div>
        """)
    },
    {
        'num': 66,
        'html': create_html_template(f"""
            <div class="slide">
                <h2 style="margin-bottom: 60px;">Jennifer's Result</h2>
                <p style="font-size: 48px; margin-bottom: 25px;">4 interviews in 6 weeks</p>
                <p style="font-size: 48px; margin-bottom: 25px;">2 offers</p>
                <p style="font-size: 48px; margin-bottom: 25px;">Final comp: <span style="color: {COLORS['accent']}; font-weight: 700;">$245K</span> base + equity</p>
                <div class="number-stat" style="margin-top: 60px;">$130K</div>
                <p class="subhead">increase from pharma role</p>
            </div>
        """)
    },
    {
        'num': 67,
        'html': create_html_template(f"""
            <div class="slide">
                <div class="quote">"I can't believe I almost talked myself out of this. My skills were always valuable—I just needed to see them differently."</div>
            </div>
        """)
    },
    {
        'num': 68,
        'html': create_html_template(f"""
            <div class="slide">
                <h2 style="margin-bottom: 60px;">What About You?</h2>
                <p class="large-text" style="font-size: 48px;">What deals have you closed?<br>What complexity have you navigated?<br>What results have you delivered?</p>
                <p class="subhead" style="margin-top: 80px;">You're more qualified than you think</p>
            </div>
        """)
    },
    {
        'num': 69,
        'html': create_html_template(f"""
            <div class="slide">
                <h2 style="margin-bottom: 60px;">Secret #2 Recap</h2>
                <p class="large-text">Your skills ARE valuable and transferable. You just need to inventory them and position them for premium markets.</p>
            </div>
        """)
    },
    {
        'num': 70,
        'html': create_html_template(f"""
            <div class="slide">
                <h2>Still With Me?</h2>
                <p class="large-text">Two secrets down, one to go...</p>
                <p class="subhead" style="margin-top: 80px;">This last one is important</p>
            </div>
        """)
    },

    # PHASE 4: SECRET #3 - EXTERNAL BELIEF (Slides 71-95)
    {
        'num': 71,
        'html': create_html_template(f"""
            <div class="slide">
                <h1 style="color: {COLORS['accent']};">Secret #3</h1>
            </div>
        """)
    },
    {
        'num': 72,
        'html': create_html_template(f"""
            <div class="slide">
                <h2>How To Implement This While Working Full-Time</h2>
                <p class="subhead">(In Just 30 Minutes Per Day)</p>
            </div>
        """)
    },
    {
        'num': 73,
        'html': create_html_template(f"""
            <div class="slide slide-left">
                <h2 style="margin-bottom: 50px;">You Might Be Thinking...</h2>
                <ul>
                    <li>"I don't have time for this while working"</li>
                    <li>"My current employer will find out"</li>
                    <li>"This sounds like it takes months"</li>
                    <li>"This won't work in my industry"</li>
                </ul>
            </div>
        """)
    },
    {
        'num': 74,
        'html': create_html_template(f"""
            <div class="slide">
                <h2 style="margin-bottom: 60px;">These Are Valid Concerns</h2>
                <p class="large-text">You're busy. You're employed. You can't risk your current job.</p>
                <p class="subhead" style="margin-top: 80px;">I'm going to show you how to do this discreetly and efficiently</p>
            </div>
        """)
    },
    {
        'num': 75,
        'html': create_html_template(f"""
            <div class="slide">
                <h2 style="margin-bottom: 40px;">The Time Myth</h2>
                <p style="font-size: 48px; margin-bottom: 40px; color: {COLORS['warning']};">Myth: This takes hours per day</p>
                <p style="font-size: 48px; margin-bottom: 50px; color: {COLORS['success']}; font-weight: 600;">Reality: 30 minutes per day is enough</p>
                <div style="text-align: left; max-width: 1000px; margin: 0 auto;">
                    <p style="font-size: 38px; margin: 15px 0;">10 min: LinkedIn optimization/activity</p>
                    <p style="font-size: 38px; margin: 15px 0;">15 min: Strategic outreach</p>
                    <p style="font-size: 38px; margin: 15px 0;">5 min: Follow-ups</p>
                </div>
            </div>
        """)
    },
    {
        'num': 76,
        'html': create_html_template(f"""
            <div class="slide slide-left">
                <h2 style="margin-bottom: 40px;">How To Do This Without Your Employer Knowing</h2>
                <ul style="font-size: 38px;">
                    <li>Don't change your LinkedIn headline to "Open to opportunities"</li>
                    <li>Take calls before/after work or lunch</li>
                    <li>Use personal email only</li>
                    <li>Schedule interviews as "doctor appointments"</li>
                    <li>Never trash-talk current employer</li>
                </ul>
            </div>
        """)
    },
    {
        'num': 77,
        'html': create_html_template(f"""
            <div class="slide slide-left">
                <h2 style="margin-bottom: 40px;">Realistic Timeline</h2>
                <ul style="font-size: 38px;">
                    <li>Weeks 1-2: Profile matching (target companies)</li>
                    <li>Weeks 3-4: Optimize LinkedIn, gather referrals</li>
                    <li>Weeks 5-6: Outreach and initial conversations</li>
                    <li>Weeks 7-8: Interviews</li>
                    <li>Weeks 9-10: Offers and negotiation</li>
                </ul>
                <p class="subhead" style="margin-top: 50px;">Total: 60-90 days from start to hired</p>
            </div>
        """)
    },
    {
        'num': 78,
        'html': create_html_template(f"""
            <div class="slide slide-left">
                <h2 style="margin-bottom: 40px;">Does This Work In MY Industry?</h2>
                <p style="font-size: 48px; margin-bottom: 40px;">If you're in B2B sales, YES</p>
                <p style="margin-bottom: 30px;">Proven industries:</p>
                <ul>
                    <li class="checkmark">SaaS</li>
                    <li class="checkmark">Pharma</li>
                    <li class="checkmark">Manufacturing</li>
                    <li class="checkmark">Tech</li>
                    <li class="checkmark">Financial services</li>
                    <li class="checkmark">Healthcare</li>
                </ul>
            </div>
        """)
    },
    {
        'num': 79,
        'html': create_html_template(f"""
            <div class="slide slide-left">
                <h2 style="margin-bottom: 50px;">Let Me Tell You About Marcus</h2>
                <ul>
                    <li>Manufacturing sales, making $95K</li>
                    <li>Working 55 hours/week</li>
                    <li>Two young kids</li>
                    <li>Wife worked full-time too</li>
                </ul>
            </div>
        """)
    },
    {
        'num': 80,
        'html': create_html_template(f"""
            <div class="slide">
                <div class="quote">"This sounds great, but I barely have time to breathe. How am I supposed to add a job search on top of everything?"</div>
            </div>
        """)
    },
    {
        'num': 81,
        'html': create_html_template(f"""
            <div class="slide">
                <h2 style="margin-bottom: 60px;">I Told Him...</h2>
                <p class="large-text" style="font-size: 48px;">"You're right. If you do this the OLD way (applying to 100+ jobs), you don't have time."</p>
                <p class="subhead" style="margin-top: 60px;">"But if you do it strategically, 30 minutes per day is enough"</p>
            </div>
        """)
    },
    {
        'num': 82,
        'html': create_html_template(f"""
            <div class="slide slide-left">
                <h2 style="margin-bottom: 40px;">Here's What Marcus Did</h2>
                <p style="margin-bottom: 30px;">6:00-6:30am: Before kids woke up</p>
                <ul style="font-size: 38px;">
                    <li>Monday: Identify 3 target companies</li>
                    <li>Tuesday: Find hiring managers on LinkedIn</li>
                    <li>Wednesday: Craft outreach messages</li>
                    <li>Thursday: Send connection requests</li>
                    <li>Friday: Follow up on responses</li>
                </ul>
            </div>
        """)
    },
    {
        'num': 83,
        'html': create_html_template(f"""
            <div class="slide slide-left">
                <h2 style="margin-bottom: 40px;">For Calls and Interviews</h2>
                <ul>
                    <li>Scheduled as "client meetings" or "doctor appointments"</li>
                    <li>Took calls during lunch in car</li>
                    <li>1-2 interviews per week max</li>
                    <li>Never impacted work performance</li>
                </ul>
            </div>
        """)
    },
    {
        'num': 84,
        'html': create_html_template(f"""
            <div class="slide slide-left">
                <h2 style="margin-bottom: 40px;">Marcus's Result</h2>
                <ul style="font-size: 40px;">
                    <li>Week 1-2: Identified 8 target companies</li>
                    <li>Week 3-5: LinkedIn optimization, gathered referrals</li>
                    <li>Week 6: First exploratory call</li>
                    <li>Week 8: Three formal interviews scheduled</li>
                    <li>Week 10: Offer in hand</li>
                </ul>
                <p style="font-size: 48px; margin-top: 50px; font-weight: 600;">$95K → $185K ($90K raise)</p>
            </div>
        """)
    },
    {
        'num': 85,
        'html': create_html_template(f"""
            <div class="slide">
                <div class="quote">"I can't believe I waited so long. 30 minutes per day changed my family's life. We went from barely scraping by to comfortable—and I work LESS now."</div>
            </div>
        """)
    },
    {
        'num': 86,
        'html': create_html_template(f"""
            <div class="slide slide-left">
                <h2 style="margin-bottom: 40px;">Why This Doesn't Take Forever</h2>
                <p style="margin-bottom: 30px; font-size: 40px;">Because:</p>
                <ul>
                    <li>You're TARGETING not spray-and-pray</li>
                    <li>Hiring managers come to YOU (less chasing)</li>
                    <li>You focus on HIGH-VALUE activities only</li>
                    <li>System is repeatable (no reinventing the wheel)</li>
                </ul>
            </div>
        """)
    },
    {
        'num': 87,
        'html': create_html_template(f"""
            <div class="slide slide-left">
                <h2 style="margin-bottom: 40px;">Time Wasters To AVOID</h2>
                <p style="margin-bottom: 30px; font-size: 40px;">Don't:</p>
                <ul>
                    <li class="xmark">Apply through job portals (black hole)</li>
                    <li class="xmark">Attend generic networking events</li>
                    <li class="xmark">Rewrite resume 50 times</li>
                    <li class="xmark">Chase recruiters who ghost you</li>
                </ul>
                <p class="subhead" style="margin-top: 40px;">These waste HOURS with little return</p>
            </div>
        """)
    },
    {
        'num': 88,
        'html': create_html_template(f"""
            <div class="slide slide-left">
                <h2 style="margin-bottom: 40px;">What You DO Instead</h2>
                <p style="margin-bottom: 30px; font-size: 40px;">High-value activities ONLY:</p>
                <ul>
                    <li class="checkmark">Target specific hiring managers</li>
                    <li class="checkmark">Leverage referrals strategically</li>
                    <li class="checkmark">Optimize LinkedIn once (then maintain)</li>
                    <li class="checkmark">Focus on 5-10 ideal companies MAX</li>
                </ul>
                <p class="subhead" style="margin-top: 40px;">Result: Way more efficient</p>
            </div>
        """)
    },
    {
        'num': 89,
        'html': create_html_template(f"""
            <div class="slide slide-left">
                <h2 style="margin-bottom: 40px;">This Works Across Industries</h2>
                <ul style="font-size: 44px;">
                    <li>Sarah (SaaS): $125K → $240K</li>
                    <li>David (Pharma): $110K → $195K</li>
                    <li>Lisa (Manufacturing): $85K → $165K</li>
                    <li>James (Fintech): $150K → $320K</li>
                </ul>
            </div>
        """)
    },
    {
        'num': 90,
        'html': create_html_template(f"""
            <div class="slide">
                <h2 style="margin-bottom: 60px;">The Real Question Isn't "Do I Have Time?"</h2>
                <p class="large-text">The real question is: "Can I afford NOT to do this?"</p>
                <p class="subhead" style="margin-top: 80px;">Every month you delay = $4K-$12K in lost income</p>
            </div>
        """)
    },
    {
        'num': 91,
        'html': create_html_template(f"""
            <div class="slide">
                <h2 style="margin-bottom: 40px;">If You Could Earn $90K More Per Year...</h2>
                <div style="text-align: left; max-width: 1200px; margin: 40px auto;">
                    <p style="font-size: 48px; margin: 25px 0;">Waiting 6 months = <span style="color: {COLORS['warning']}; font-weight: 700;">$45K lost</span></p>
                    <p style="font-size: 48px; margin: 25px 0;">Waiting 1 year = <span style="color: {COLORS['warning']}; font-weight: 700;">$90K lost</span></p>
                    <p style="font-size: 48px; margin: 25px 0;">Waiting 2 years = <span style="color: {COLORS['warning']}; font-weight: 700;">$180K lost</span></p>
                </div>
                <p class="subhead" style="margin-top: 60px;">Can you afford to wait?</p>
            </div>
        """)
    },
    {
        'num': 92,
        'html': create_html_template(f"""
            <div class="slide">
                <h2 style="margin-bottom: 60px;">Right Now, Companies Are Hiring</h2>
                <p class="large-text" style="font-size: 48px;">Premium sales roles are in demand. If you wait until the "perfect time," opportunities pass you by.</p>
                <p class="subhead" style="margin-top: 80px;">There's never a perfect time. But there IS right now.</p>
            </div>
        """)
    },
    {
        'num': 93,
        'html': create_html_template(f"""
            <div class="slide">
                <h2 style="margin-bottom: 60px;">Secret #3 Recap</h2>
                <p class="large-text">You CAN do this while employed in just 30 minutes/day. It works across industries. And the cost of waiting is too high.</p>
            </div>
        """)
    },
    {
        'num': 94,
        'html': create_html_template(f"""
            <div class="slide slide-left">
                <h2 style="margin-bottom: 50px;">Let's Recap All Three Secrets</h2>
                <ul style="font-size: 42px;">
                    <li><strong>Secret #1:</strong> The Active Offer System (position strategically)</li>
                    <li><strong>Secret #2:</strong> Your skills ARE valuable (inventory and reposition)</li>
                    <li><strong>Secret #3:</strong> You can do this NOW (30 min/day while employed)</li>
                </ul>
            </div>
        """)
    },
    {
        'num': 95,
        'html': create_html_template(f"""
            <div class="slide">
                <h2 style="margin-bottom: 60px;">You Now Know What Most Salespeople Never Learn</h2>
                <p class="large-text">You know the system. You know you're qualified. You know it's doable.</p>
                <p class="subhead" style="margin-top: 80px;">So what's next?</p>
            </div>
        """)
    },

    # PHASE 5: APPOINTMENT CLOSE (Slides 96-120)
    {
        'num': 96,
        'html': create_html_template(f"""
            <div class="slide">
                <h2 style="margin-bottom: 80px;">Here's What Happens Next</h2>
                <p class="large-text">Some of you are thinking: "This sounds great... but how do I actually GET STARTED?"</p>
            </div>
        """)
    },
    {
        'num': 97,
        'html': create_html_template(f"""
            <div class="slide">
                <h2 style="margin-bottom: 60px;">Here's What I'm NOT Going To Do</h2>
                <p class="large-text">I'm not going to throw a price on the screen and tell you to "buy now"</p>
                <p class="subhead" style="margin-top: 80px;">Why? Because every person's situation is different.</p>
            </div>
        """)
    },
    {
        'num': 98,
        'html': create_html_template(f"""
            <div class="slide slide-left">
                <h2 style="margin-bottom: 40px;">Your Career Is Too Important For A Cookie-Cutter Approach</h2>
                <ul>
                    <li>Someone at $80K has different needs than someone at $200K</li>
                    <li>Your industry matters</li>
                    <li>Your timeline matters</li>
                    <li>Your specific goals matter</li>
                </ul>
                <p class="subhead" style="margin-top: 50px;">This requires a conversation, not a checkout button</p>
            </div>
        """)
    },
    {
        'num': 99,
        'html': create_html_template(f"""
            <div class="slide">
                <h2 style="margin-bottom: 80px;">Introducing: The Active Offer Program</h2>
                <p class="large-text">A 90-day intensive where I personally work with you to implement this system and land your premium offer</p>
            </div>
        """)
    },
    {
        'num': 100,
        'html': create_html_template(f"""
            <div class="slide slide-left">
                <h2 style="margin-bottom: 50px;">Here's What You Get</h2>
                <ul style="font-size: 48px;">
                    <li>1-on-1 Coaching</li>
                    <li>Strategic Resources</li>
                    <li>Implementation Support</li>
                    <li>Accountability & Community</li>
                </ul>
            </div>
        """)
    },
    {
        'num': 101,
        'html': create_html_template(f"""
            <div class="slide slide-left">
                <h2 style="margin-bottom: 40px;">Module 1: Profile Matching</h2>
                <ul>
                    <li>Reverse-engineering your ideal role</li>
                    <li>Compensation benchmarking</li>
                    <li>Target company identification</li>
                    <li>Career trajectory mapping</li>
                </ul>
            </div>
        """)
    },
    {
        'num': 102,
        'html': create_html_template(f"""
            <div class="slide slide-left">
                <h2 style="margin-bottom: 40px;">Module 2: Reverse Attraction</h2>
                <ul>
                    <li>LinkedIn profile optimization</li>
                    <li>Referral navigation strategies</li>
                    <li>Direct outreach templates</li>
                    <li>Positioning scripts</li>
                </ul>
            </div>
        """)
    },
    {
        'num': 103,
        'html': create_html_template(f"""
            <div class="slide slide-left">
                <h2 style="margin-bottom: 40px;">Module 3: Interview Mastery</h2>
                <ul>
                    <li>Interview preparation framework</li>
                    <li>Company evaluation criteria</li>
                    <li>Value positioning tactics</li>
                    <li>Creating urgency strategies</li>
                </ul>
            </div>
        """)
    },
    {
        'num': 104,
        'html': create_html_template(f"""
            <div class="slide slide-left">
                <h2 style="margin-bottom: 40px;">Module 4: Negotiating The Offer</h2>
                <ul>
                    <li>Comp structure strategies</li>
                    <li>Leveraging multiple offers</li>
                    <li>Negotiation scripts</li>
                    <li>Win-win frameworks</li>
                </ul>
            </div>
        """)
    },
    {
        'num': 105,
        'html': create_html_template(f"""
            <div class="slide slide-left">
                <h2 style="margin-bottom: 40px;">Premium Resources Included</h2>
                <ul style="font-size: 40px;">
                    <li>Resume templates</li>
                    <li>LinkedIn audit checklist</li>
                    <li>Cold email vault</li>
                    <li>Interview question database</li>
                    <li>Target account selector</li>
                    <li>Accountability log</li>
                </ul>
            </div>
        """)
    },
    {
        'num': 106,
        'html': create_html_template(f"""
            <div class="slide slide-left">
                <h2 style="margin-bottom: 40px;">PLUS: Direct Coaching With Me</h2>
                <ul>
                    <li>Weekly strategy calls</li>
                    <li>Resume and LinkedIn review</li>
                    <li>Interview prep sessions</li>
                    <li>Negotiation strategy planning</li>
                    <li>Real-time feedback and adjustments</li>
                </ul>
            </div>
        """)
    },
    {
        'num': 107,
        'html': create_html_template(f"""
            <div class="slide slide-left">
                <h2 style="margin-bottom: 40px;">What's This Worth?</h2>
                <p style="margin-bottom: 30px;">Questions to consider:</p>
                <ul>
                    <li>What's a $90K raise worth to you?</li>
                    <li>What's working from home worth?</li>
                    <li>What's getting your time back worth?</li>
                    <li>What's doing this in 90 days vs. 2 years worth?</li>
                </ul>
            </div>
        """)
    },
    {
        'num': 108,
        'html': create_html_template(f"""
            <div class="slide">
                <h2 style="margin-bottom: 40px;">Let's Do Simple Math</h2>
                <div style="text-align: left; max-width: 1200px; margin: 40px auto;">
                    <p style="font-size: 44px; margin: 20px 0;">Average raise: $90K per year</p>
                    <p style="font-size: 44px; margin: 20px 0;">Over 5 years: <span style="color: {COLORS['accent']}; font-weight: 700;">$450K</span></p>
                    <p style="font-size: 44px; margin: 20px 0;">Over 10 years: <span style="color: {COLORS['accent']}; font-weight: 700;">$900K</span></p>
                    <p style="font-size: 44px; margin: 20px 0;">Plus: Compounding career trajectory</p>
                </div>
                <p class="subhead" style="margin-top: 60px;">What would you invest to capture that?</p>
            </div>
        """)
    },
    {
        'num': 109,
        'html': create_html_template(f"""
            <div class="slide">
                <h2 style="margin-bottom: 80px;">But Like I Said...</h2>
                <p class="large-text">I'm not revealing a price. Because your situation is unique.</p>
                <p class="subhead" style="margin-top: 80px;">Instead, here's what I want to do...</p>
            </div>
        """)
    },
    {
        'num': 110,
        'html': create_html_template(f"""
            <div class="slide">
                <h2 style="margin-bottom: 80px;">I Want To Invite You To A Strategy Session</h2>
                <p class="large-text">This is a 45-minute call where we'll:</p>
            </div>
        """)
    },
    {
        'num': 111,
        'html': create_html_template(f"""
            <div class="slide slide-left">
                <h2 style="margin-bottom: 40px;">On This Call, We'll...</h2>
                <ul>
                    <li>Map out your ideal role (comp, company, lifestyle)</li>
                    <li>Identify the exact positioning gaps keeping you stuck</li>
                    <li>Show you the roadmap to your $50K-$150K raise</li>
                    <li>Determine if Active Offer is the right fit for you</li>
                </ul>
            </div>
        """)
    },
    {
        'num': 112,
        'html': create_html_template(f"""
            <div class="slide">
                <h2 style="margin-bottom: 60px;">This Is NOT A High-Pressure Sales Call</h2>
                <p class="large-text">If it's not a fit, I'll tell you. If it is, we'll talk about what it looks like to work together.</p>
                <p class="subhead" style="margin-top: 80px;">Either way, you'll leave with clarity</p>
            </div>
        """)
    },
    {
        'num': 113,
        'html': create_html_template(f"""
            <div class="slide slide-left">
                <h2 style="margin-bottom: 40px;">Who Should Book This Call?</h2>
                <p style="margin-bottom: 30px; font-size: 40px;">Good fit:</p>
                <ul style="font-size: 38px;">
                    <li>Making $80K+ in B2B sales currently</li>
                    <li>Proven track record of results</li>
                    <li>Ready to invest in your career</li>
                    <li>Willing to put in 30 min/day for 90 days</li>
                    <li>Want to double income in next 6-12 months</li>
                </ul>
            </div>
        """)
    },
    {
        'num': 114,
        'html': create_html_template(f"""
            <div class="slide slide-left">
                <h2 style="margin-bottom: 40px;">Who Shouldn't Book This Call</h2>
                <p style="margin-bottom: 30px; font-size: 40px;">Not a fit:</p>
                <ul style="font-size: 38px;">
                    <li>Looking for a magic button (no work)</li>
                    <li>Not in B2B sales</li>
                    <li>Not willing to invest in yourself</li>
                    <li>Want to "think about it for 6 months"</li>
                    <li>Making under $50K (not ready yet)</li>
                </ul>
            </div>
        """)
    },
    {
        'num': 115,
        'html': create_html_template(f"""
            <div class="slide">
                <h2 style="margin-bottom: 40px;">One Important Thing...</h2>
                <p class="large-text" style="font-size: 48px;">I only take on 10 clients per quarter</p>
                <p class="subhead" style="margin-top: 50px;">Why? Because I personally work with each person. I can't scale beyond that and deliver results.</p>
                <p style="margin-top: 60px; font-size: 44px; font-weight: 600; color: {COLORS['accent']};">Right now I have 3 spots available</p>
            </div>
        """)
    },
    {
        'num': 116,
        'html': create_html_template(f"""
            <div class="slide">
                <h2 style="margin-bottom: 60px;">Every Month You Wait...</h2>
                <p class="large-text">Is another month at your current income</p>
                <div style="text-align: left; max-width: 1000px; margin: 50px auto;">
                    <p style="font-size: 44px; margin: 20px 0;">If $90K raise is possible...</p>
                    <p style="font-size: 44px; margin: 20px 0;">Waiting 3 months = <span style="color: {COLORS['warning']}; font-weight: 700;">$22,500 lost</span></p>
                    <p style="font-size: 44px; margin: 20px 0;">Waiting 6 months = <span style="color: {COLORS['warning']}; font-weight: 700;">$45,000 lost</span></p>
                </div>
                <p class="subhead" style="margin-top: 60px;">Can you afford to wait?</p>
            </div>
        """)
    },
    {
        'num': 117,
        'html': create_html_template(f"""
            <div class="slide slide-left">
                <h2 style="margin-bottom: 40px;">Imagine 90 Days From Now...</h2>
                <ul>
                    <li>Multiple competing offers on the table</li>
                    <li>$50K-$150K increase in comp</li>
                    <li>Working from home (if you want)</li>
                    <li>Better work-life balance</li>
                    <li>Complete control over your career</li>
                </ul>
                <p class="subhead" style="margin-top: 50px;">This is possible for you</p>
            </div>
        """)
    },
    {
        'num': 118,
        'html': create_html_template(f"""
            <div class="slide">
                <h2 style="margin-bottom: 60px;">Ready To Get Started?</h2>
                <div class="cta">BOOK YOUR STRATEGY SESSION</div>
                <p class="small-text" style="margin-top: 40px;">No credit card required. Just 45 minutes to map your path to premium offers.</p>
            </div>
        """)
    },
    {
        'num': 119,
        'html': create_html_template(f"""
            <div class="slide slide-left">
                <h2 style="margin-bottom: 50px;">Here's What To Do Right Now</h2>
                <ul style="font-size: 44px;">
                    <li>Click the button below</li>
                    <li>Pick a time that works for you</li>
                    <li>Show up ready to discuss your goals</li>
                    <li>Leave with complete clarity</li>
                </ul>
                <div class="cta" style="margin-top: 60px;">BOOK YOUR STRATEGY SESSION NOW</div>
            </div>
        """)
    },
    {
        'num': 120,
        'html': create_html_template(f"""
            <div class="slide">
                <h2 style="margin-bottom: 80px;">I'll See You On The Call</h2>
                <p class="large-text">This is your time. Let's make it happen.</p>
                <div class="cta" style="margin-top: 80px;">BOOK NOW</div>
            </div>
        """)
    },
]

def generate_slides():
    """Generate all slides as PNG files"""
    output_dir = "/Users/terrancebrandon/Desktop/Active Offer/AO- Course Content/Active Offer- Course Material/.Webinar Script v.2"

    print(f"Starting slide generation...")
    print(f"Output directory: {output_dir}")

    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(viewport={'width': 1920, 'height': 1080})

        for slide_data in SLIDES:
            slide_num = slide_data['num']
            html_content = slide_data['html']

            # Set content
            page.set_content(html_content)

            # Wait for fonts and rendering
            page.wait_for_timeout(500)

            # Take screenshot
            output_path = os.path.join(output_dir, f"{slide_num}.png")
            page.screenshot(path=output_path, full_page=False)

            print(f"Generated slide {slide_num}/120")

        browser.close()

    print(f"\nAll 120 slides generated successfully!")
    print(f"Location: {output_dir}")

if __name__ == "__main__":
    generate_slides()
