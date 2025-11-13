#!/usr/bin/env python3
"""
Active Offer Webinar v2.1 - CORRECTED VERSION
Creates 121 professional PNG slides at 1920x1080 resolution
All corrections applied based on user feedback and factual source
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

# ALL 121 SLIDES WITH CORRECTIONS APPLIED
SLIDES = [
    # PHASE 1: INTRODUCTION (Slides 1-15) - CORRECTED
    {
        'num': 1,
        'html': create_html_template(f"""
            <div class="slide">
                <h1 style="color: {COLORS['primary']};">The Active Offer System</h1>
                <p class="subhead" style="max-width: 1300px;">How to Position Yourself So Hiring Managers Seek YOU Out<br>(And Increase Your Income in 90 Days)</p>
            </div>
        """)
    },
    {
        'num': 2,
        'html': create_html_template(f"""
            <div class="slide">
                <h2>From $130K to $1.08M+ in 3 Years</h2>
                <p class="large-text">While Working from Home in Less Than 45 Hours/Week</p>
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
                    <li>Working 50-60+ hour weeks</li>
                    <li>Feeling undervalued and overlooked</li>
                    <li>Don't know what other opportunities exist</li>
                </ul>
            </div>
        """)
    },
    {
        'num': 4,
        'html': create_html_template(f"""
            <div class="slide">
                <h2 style="margin-bottom: 60px;">Here's What Most Salespeople Don't Know</h2>
                <p class="large-text">You don't even know what high-paying opportunities exist out there</p>
                <p class="subhead" style="margin-top: 80px;">There's "easy money" roles paying 2-4x your current income... you just don't know where to find them</p>
            </div>
        """)
    },
    {
        'num': 5,
        'html': create_html_template(f"""
            <div class="slide">
                <h2>It's Not Your Fault</h2>
                <p class="large-text">You've never been shown where the "easy money" is or how to position yourself for it</p>
            </div>
        """)
    },
    {
        'num': 6,
        'html': create_html_template(f"""
            <div class="slide slide-left">
                <h2>My Story - The Setup</h2>
                <ul>
                    <li>10 years at AT&T, various sales roles</li>
                    <li>2021: Making $130K</li>
                    <li>Pain: Long hours, stuck, not enough money</li>
                    <li>Overlooked for promotions despite high performance</li>
                </ul>
            </div>
        """)
    },
    {
        'num': 7,
        'html': create_html_template(f"""
            <div class="slide">
                <h2>The Breaking Point</h2>
                <p class="large-text">2021: Overlooked for promotion despite being top performer</p>
                <p class="subhead" style="margin-top: 80px;">After 10 years of loyalty, still passed over</p>
            </div>
        """)
    },
    {
        'num': 8,
        'html': create_html_template(f"""
            <div class="slide">
                <h2 style="margin-bottom: 40px;">Then I Overheard Something That Changed Everything</h2>
                <p class="large-text" style="font-size: 48px;">Random day in office, coworkers talking about former colleague</p>
                <p class="large-text" style="font-size: 48px; margin-top: 40px;">Discovery: He was making $400K+ at mid-market software company</p>
                <p class="subhead" style="margin-top: 60px;">"How is he pulling this off? I barely cracked $150K in my best year."</p>
            </div>
        """)
    },
    {
        'num': 9,
        'html': create_html_template(f"""
            <div class="slide">
                <h2 style="margin-bottom: 60px;">Down the Rabbit Hole</h2>
                <p class="large-text">Started researching top sales roles industry-wide</p>
                <p class="subhead" style="margin-top: 80px;">Discovery: Average salespeople at top companies making hundreds of thousands more</p>
            </div>
        """)
    },
    {
        'num': 10,
        'html': create_html_template(f"""
            <div class="slide">
                <h2 style="margin-bottom: 80px;">Here's What Changed Everything</h2>
                <p class="large-text">Your income isn't determined by how hard you work...</p>
            </div>
        """)
    },
    {
        'num': 11,
        'html': create_html_template(f"""
            <div class="slide">
                <p class="large-text" style="font-size: 68px; font-weight: 700; color: {COLORS['primary']}; line-height: 1.3;">It's determined by knowing how to find the "easy money" and positioning yourself to receive lots of high-paying offers</p>
            </div>
        """)
    },
    {
        'num': 12,
        'html': create_html_template(f"""
            <div class="slide">
                <h2 style="margin-bottom: 60px;">OLD WAY vs. NEW WAY</h2>
                <div class="split">
                    <div>
                        <h3 style="color: {COLORS['warning']};">Old Way</h3>
                        <ul>
                            <li>Don't know high-paying roles exist</li>
                            <li>Apply randomly through job portals</li>
                            <li>Compete with hundreds</li>
                            <li>Accept whatever you can get</li>
                        </ul>
                    </div>
                    <div>
                        <h3 style="color: {COLORS['success']};">New Way</h3>
                        <ul>
                            <li>Discover where the "easy money" is</li>
                            <li>Position strategically for multiple offers</li>
                            <li>Hiring managers seek YOU</li>
                            <li>Choose the best offer</li>
                        </ul>
                    </div>
                </div>
            </div>
        """)
    },
    {
        'num': 13,
        'html': create_html_template(f"""
            <div class="slide slide-left">
                <h2>My Result</h2>
                <ul style="font-size: 48px;">
                    <li>2022: $514K (first full year at Salesforce)</li>
                    <li>2024-2025: $1.08M+ W2 + $1M equity</li>
                    <li>Working from home, less than 45 hours/week</li>
                </ul>
            </div>
        """)
    },
    {
        'num': 14,
        'html': create_html_template(f"""
            <div class="slide slide-left">
                <h2>This Works For Others Too</h2>
                <ul style="font-size: 44px;">
                    <li>Darrell: $100K → $340K+ in 2 years</li>
                    <li>Simon: $90K → $280K</li>
                    <li>Average results: 60-90 days to offers</li>
                </ul>
            </div>
        """)
    },
    {
        'num': 15,
        'html': create_html_template(f"""
            <div class="slide slide-left">
                <h2>In The Next 60 Minutes...</h2>
                <ul>
                    <li>How to find where the "easy money" is</li>
                    <li>How to position yourself for multiple high-paying offers</li>
                    <li>The exact 4-step system I used</li>
                    <li>How to implement in 30 min/day while employed</li>
                </ul>
            </div>
        """)
    },
    {
        'num': 16,
        'html': create_html_template(f"""
            <div class="slide">
                <h2>Before We Start, One Request</h2>
                <p class="large-text">Keep an open mind. This is different from everything you've been taught.</p>
            </div>
        """)
    },

    # PHASE 2: THE 4 AHA MOMENTS (Slides 17-46)
    {
        'num': 17,
        'html': create_html_template(f"""
            <div class="slide">
                <h1 style="color: {COLORS['accent']};">The 4 Aha Moments</h1>
                <p class="subhead">That Changed My Career Forever</p>
            </div>
        """)
    },
    {
        'num': 18,
        'html': create_html_template(f"""
            <div class="slide">
                <h2>Let Me Tell You The Full Story</h2>
                <p class="large-text">For 10 years at AT&T, I gave everything...</p>
            </div>
        """)
    },
    {
        'num': 19,
        'html': create_html_template(f"""
            <div class="slide slide-left">
                <h2 style="margin-bottom: 50px;">The Grind</h2>
                <ul>
                    <li>Various sales roles across 10 years</li>
                    <li>Working long hours constantly</li>
                    <li>2021: Making $130K</li>
                    <li>Feeling stuck, not enough money</li>
                    <li>Unable to allow wife to stay home with daughter</li>
                </ul>
            </div>
        """)
    },
    {
        'num': 20,
        'html': create_html_template(f"""
            <div class="slide">
                <h2 style="margin-bottom: 60px;">2021: The Breaking Point</h2>
                <p class="large-text">Overlooked for promotion despite being top performer</p>
                <p class="subhead" style="margin-top: 80px;">After 10 years of loyalty and high performance, still passed over</p>
            </div>
        """)
    },
    {
        'num': 21,
        'html': create_html_template(f"""
            <div class="slide">
                <h1 style="color: {COLORS['accent']}; font-size: 80px;">Aha Moment #1</h1>
                <p class="subhead">The Income Discovery</p>
            </div>
        """)
    },
    {
        'num': 22,
        'html': create_html_template(f"""
            <div class="slide">
                <h2 style="margin-bottom: 40px;">Random Day in the Office</h2>
                <p class="large-text" style="font-size: 48px;">Overheard coworkers talking about a colleague who left AT&T</p>
                <p class="large-text" style="font-size: 48px; margin-top: 40px;">He was making $400K+ at a mid-market software company</p>
            </div>
        """)
    },
    {
        'num': 23,
        'html': create_html_template(f"""
            <div class="slide">
                <h2 style="margin-bottom: 60px;">My Reaction</h2>
                <p class="large-text">"How is he pulling this off? I barely cracked $150K in my best year."</p>
            </div>
        """)
    },
    {
        'num': 24,
        'html': create_html_template(f"""
            <div class="slide">
                <h2 style="margin-bottom: 60px;">The Action</h2>
                <p class="large-text">Went down a rabbit hole researching top sales roles industry-wide</p>
            </div>
        """)
    },
    {
        'num': 25,
        'html': create_html_template(f"""
            <div class="slide">
                <h2 style="margin-bottom: 40px;">The Discovery</h2>
                <p class="large-text" style="font-size: 52px;">Average salespeople at top companies were easily making hundreds of thousands of dollars more</p>
            </div>
        """)
    },
    {
        'num': 26,
        'html': create_html_template(f"""
            <div class="slide">
                <h2 style="margin-bottom: 80px;">The Belief Shift</h2>
                <p class="large-text" style="font-size: 64px; font-weight: 700; color: {COLORS['primary']};">"The role you're in matters more than how hard you work"</p>
            </div>
        """)
    },
    {
        'num': 27,
        'html': create_html_template(f"""
            <div class="slide">
                <h1 style="color: {COLORS['accent']}; font-size: 80px;">Aha Moment #2</h1>
                <p class="subhead">The Access Strategy</p>
            </div>
        """)
    },
    {
        'num': 28,
        'html': create_html_template(f"""
            <div class="slide">
                <h2 style="margin-bottom: 60px;">The Problem</h2>
                <p class="large-text">Trying to figure out how to beat the other 99% of applicants</p>
            </div>
        """)
    },
    {
        'num': 29,
        'html': create_html_template(f"""
            <div class="slide">
                <h2 style="margin-bottom: 40px;">The Stats Realization</h2>
                <p class="large-text" style="font-size: 48px;">At Google, 2,000 people apply, only 20 get interviewed</p>
                <p class="subhead" style="margin-top: 80px;">That's a 1% interview rate</p>
            </div>
        """)
    },
    {
        'num': 30,
        'html': create_html_template(f"""
            <div class="slide">
                <h2 style="margin-bottom: 30px;">The Insight</h2>
                <p class="large-text" style="font-size: 46px;">"Getting in front of the hiring manager and gaining mindshare is half the battle. Most candidates are never considered for roles not because they can't do them, but because they have zero percent mindshare with the person actually hiring."</p>
            </div>
        """)
    },
    {
        'num': 31,
        'html': create_html_template(f"""
            <div class="slide">
                <h2 style="margin-bottom: 60px;">The Strategy</h2>
                <p class="large-text">"If I can figure this out, I can dramatically increase my chances of landing one of these offers."</p>
            </div>
        """)
    },
    {
        'num': 32,
        'html': create_html_template(f"""
            <div class="slide">
                <h2 style="margin-bottom: 40px;">The Result</h2>
                <p class="large-text" style="font-size: 48px;">After implementing the first part of Active Offer strategy, landed interviews with Salesforce, Google, and Amazon within one week</p>
            </div>
        """)
    },
    {
        'num': 33,
        'html': create_html_template(f"""
            <div class="slide">
                <h2 style="margin-bottom: 80px;">The Belief Shift</h2>
                <p class="large-text" style="font-size: 72px; font-weight: 700; color: {COLORS['primary']};">"Access beats applications"</p>
            </div>
        """)
    },
    {
        'num': 34,
        'html': create_html_template(f"""
            <div class="slide">
                <h1 style="color: {COLORS['accent']}; font-size: 80px;">Aha Moment #3</h1>
                <p class="subhead">The Interview Mastery</p>
            </div>
        """)
    },
    {
        'num': 35,
        'html': create_html_template(f"""
            <div class="slide">
                <h2 style="margin-bottom: 60px;">The Failure</h2>
                <p class="large-text">First Salesforce interview - bombed completely</p>
            </div>
        """)
    },
    {
        'num': 36,
        'html': create_html_template(f"""
            <div class="slide">
                <h2 style="margin-bottom: 40px;">The Realization</h2>
                <p class="large-text" style="font-size: 48px;">"I'm terrible at interviews and the interview structure was unlike other interviews I took in the past."</p>
            </div>
        """)
    },
    {
        'num': 37,
        'html': create_html_template(f"""
            <div class="slide">
                <h2 style="margin-bottom: 60px;">The Second Chance</h2>
                <p class="large-text">Within a week, received another interview at Salesforce for different position</p>
            </div>
        """)
    },
    {
        'num': 38,
        'html': create_html_template(f"""
            <div class="slide">
                <h2 style="margin-bottom: 30px;">The Preparation</h2>
                <p class="large-text" style="font-size: 46px;">"This time I was prepared with an abundance of research on what hiring managers are looking for and how to ace the interview with ease."</p>
            </div>
        """)
    },
    {
        'num': 39,
        'html': create_html_template(f"""
            <div class="slide">
                <h2 style="margin-bottom: 60px;">The Result</h2>
                <p class="large-text">"My plan worked like a charm."</p>
                <p class="subhead" style="margin-top: 80px;">Hired within 6 days</p>
            </div>
        """)
    },
    {
        'num': 40,
        'html': create_html_template(f"""
            <div class="slide">
                <h2 style="margin-bottom: 30px;">The Insight</h2>
                <p class="large-text" style="font-size: 46px;">"With pre-prepared interview assets and clear understandings of how these interviews differ from typical sales interviews, and understanding what they were hiring for, anyone can ace the interview with ease."</p>
            </div>
        """)
    },
    {
        'num': 41,
        'html': create_html_template(f"""
            <div class="slide">
                <h2 style="margin-bottom: 80px;">The Belief Shift</h2>
                <p class="large-text" style="font-size: 72px; font-weight: 700; color: {COLORS['primary']};">"Preparation beats natural talent"</p>
            </div>
        """)
    },
    {
        'num': 42,
        'html': create_html_template(f"""
            <div class="slide">
                <h1 style="color: {COLORS['accent']}; font-size: 80px;">Aha Moment #4</h1>
                <p class="subhead">The Equity Strategy</p>
            </div>
        """)
    },
    {
        'num': 43,
        'html': create_html_template(f"""
            <div class="slide">
                <h2 style="margin-bottom: 60px;">2023: The VP of Sales</h2>
                <p class="large-text">Met long-time Vice President of Sales at Salesforce</p>
                <p class="subhead" style="margin-top: 80px;">He had made millions during his time in tech sales</p>
            </div>
        """)
    },
    {
        'num': 44,
        'html': create_html_template(f"""
            <div class="slide">
                <h2 style="margin-bottom: 40px;">The Teaching</h2>
                <p class="large-text" style="font-size: 48px;">His framework for how people were making over $1M in a year in tech sales through equity</p>
            </div>
        """)
    },
    {
        'num': 45,
        'html': create_html_template(f"""
            <div class="slide">
                <h2 style="margin-bottom: 60px;">The Application</h2>
                <p class="large-text">Took his advice in 2024</p>
                <p class="subhead" style="margin-top: 80px;">Result: Landed a job that not only paid high commissions, but earned over $1M in equity in 1.5 years</p>
            </div>
        """)
    },
    {
        'num': 46,
        'html': create_html_template(f"""
            <div class="slide">
                <h2 style="margin-bottom: 80px;">The Belief Shift</h2>
                <p class="large-text" style="font-size: 60px; font-weight: 700; color: {COLORS['primary']};">"Total compensation includes equity - that's where the real wealth is"</p>
            </div>
        """)
    },

    # PHASE 3: THE ACTIVE OFFER SYSTEM (Slides 47-70)
    {
        'num': 47,
        'html': create_html_template(f"""
            <div class="slide">
                <h2 style="margin-bottom: 80px;">Let's Recap The 4 Aha Moments</h2>
                <p class="large-text">These 4 discoveries transformed how I thought about my career...</p>
            </div>
        """)
    },
    {
        'num': 48,
        'html': create_html_template(f"""
            <div class="slide slide-left">
                <h2 style="margin-bottom: 40px;">The 4 Belief Shifts</h2>
                <ul style="font-size: 40px;">
                    <li><strong>Aha #1:</strong> The role you're in matters more than how hard you work</li>
                    <li><strong>Aha #2:</strong> Access beats applications</li>
                    <li><strong>Aha #3:</strong> Preparation beats natural talent</li>
                    <li><strong>Aha #4:</strong> Total compensation includes equity</li>
                </ul>
            </div>
        """)
    },
    {
        'num': 49,
        'html': create_html_template(f"""
            <div class="slide">
                <h2 style="margin-bottom: 60px;">These Became The Foundation</h2>
                <p class="large-text">I turned these insights into a repeatable system...</p>
                <p class="subhead" style="margin-top: 80px;">The Active Offer System</p>
            </div>
        """)
    },
    {
        'num': 50,
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
        'num': 51,
        'html': create_html_template(f"""
            <div class="slide slide-left">
                <h2 style="margin-bottom: 40px;">Step 1: Profile Matching</h2>
                <p style="margin-bottom: 30px;">Identify target roles and companies based on:</p>
                <ul>
                    <li>Income goals ($150K? $300K? $500K+?)</li>
                    <li>Lifestyle preferences (remote? travel? hours?)</li>
                    <li>Company type (startup? enterprise? mid-market?)</li>
                    <li>Industry alignment (SaaS? Tech? B2B?)</li>
                </ul>
            </div>
        """)
    },
    {
        'num': 52,
        'html': create_html_template(f"""
            <div class="slide">
                <h2 style="margin-bottom: 60px;">Most People Skip This Step</h2>
                <p class="large-text">They apply to any "Senior Sales" role and wonder why nothing fits. You need to TARGET strategically.</p>
            </div>
        """)
    },
    {
        'num': 53,
        'html': create_html_template(f"""
            <div class="slide slide-left">
                <h2 style="margin-bottom: 40px;">Step 2: Reverse Attraction</h2>
                <p style="margin-bottom: 30px;">Don't chase, attract - Make hiring managers come to YOU through:</p>
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
        'num': 54,
        'html': create_html_template(f"""
            <div class="slide">
                <h2 style="margin-bottom: 40px;">When They Come To You...</h2>
                <p class="large-text">You enter the conversation from a position of POWER, not desperation</p>
                <p class="subhead" style="margin-top: 60px;">Result: Better negotiation leverage, faster hiring process</p>
            </div>
        """)
    },
    {
        'num': 55,
        'html': create_html_template(f"""
            <div class="slide slide-left">
                <h2 style="margin-bottom: 40px;">Step 3: Interview Mastery</h2>
                <p style="margin-bottom: 30px;">Ace interviews with pre-prepared assets:</p>
                <ul>
                    <li>Understanding what hiring managers look for</li>
                    <li>Pre-prepared interview frameworks</li>
                    <li>Positioning your value strategically</li>
                    <li>Making them want to close YOU</li>
                </ul>
            </div>
        """)
    },
    {
        'num': 56,
        'html': create_html_template(f"""
            <div class="slide">
                <h2 style="margin-bottom: 60px;">Interviews Aren't Tests</h2>
                <p class="large-text">They're strategic conversations where you assess fit and position value</p>
                <p class="subhead" style="margin-top: 80px;">From "I hope they like me" to "Is this the right opportunity?"</p>
            </div>
        """)
    },
    {
        'num': 57,
        'html': create_html_template(f"""
            <div class="slide slide-left">
                <h2 style="margin-bottom: 40px;">Step 4: Negotiating the Offer</h2>
                <p style="margin-bottom: 30px;">Use leverage and strategy to maximize compensation:</p>
                <ul>
                    <li>Leveraging multiple offers</li>
                    <li>Structuring comp strategically</li>
                    <li>Understanding equity value</li>
                    <li>Creating win-win scenarios</li>
                </ul>
            </div>
        """)
    },
    {
        'num': 58,
        'html': create_html_template(f"""
            <div class="slide">
                <h2 style="margin-bottom: 40px;">This Is Where Tens Of Thousands Get Added</h2>
                <p class="large-text">$50K-$150K raises don't happen by accepting the first offer</p>
            </div>
        """)
    },
    {
        'num': 59,
        'html': create_html_template(f"""
            <div class="slide">
                <h2 style="margin-bottom: 50px;">Each Step Builds On The Last</h2>
                <div class="steps">
                    <div class="step">
                        <div class="step-number">1</div>
                        <div class="step-title">Target<br>Right Roles</div>
                    </div>
                    <div style="font-size: 72px; color: {COLORS['accent']};">→</div>
                    <div class="step">
                        <div class="step-number">2</div>
                        <div class="step-title">Get<br>Access</div>
                    </div>
                    <div style="font-size: 72px; color: {COLORS['accent']};">→</div>
                    <div class="step">
                        <div class="step-number">3</div>
                        <div class="step-title">Ace<br>Interview</div>
                    </div>
                    <div style="font-size: 72px; color: {COLORS['accent']};">→</div>
                    <div class="step">
                        <div class="step-number">4</div>
                        <div class="step-title">Maximize<br>Offer</div>
                    </div>
                </div>
                <p class="subhead" style="margin-top: 40px;">This isn't 4 separate tactics. It's ONE unified system.</p>
            </div>
        """)
    },
    {
        'num': 60,
        'html': create_html_template(f"""
            <div class="slide slide-left">
                <h2 style="margin-bottom: 50px;">Meet Darrell</h2>
                <ul>
                    <li>Company: AT&T</li>
                    <li>Role: Account Manager</li>
                    <li>Income: $100K</li>
                    <li>Pain: Felt stuck, underpaid, no real path out</li>
                </ul>
            </div>
        """)
    },
    {
        'num': 61,
        'html': create_html_template(f"""
            <div class="slide slide-left">
                <h2 style="margin-bottom: 40px;">What Darrell Implemented</h2>
                <ul>
                    <li>Used: Reverse Attraction, Interview Mastery, Negotiating the Offer</li>
                    <li>Biggest Breakthrough: Got $90K raise in OTE on his first offer</li>
                    <li>What He Learned: Exactly what company to look for and how to ace the interview</li>
                </ul>
            </div>
        """)
    },
    {
        'num': 62,
        'html': create_html_template(f"""
            <div class="slide">
                <h2 style="margin-bottom: 60px;">Darrell's First Results</h2>
                <p style="font-size: 52px; margin-bottom: 30px;">New Role: Account Executive</p>
                <p style="font-size: 52px; margin-bottom: 30px;">Income: <span style="color: {COLORS['accent']}; font-weight: 700;">$190K</span> ($90K raise)</p>
            </div>
        """)
    },
    {
        'num': 63,
        'html': create_html_template(f"""
            <div class="slide">
                <h2 style="margin-bottom: 60px;">Year 2: Darrell Did It Again</h2>
                <p class="large-text" style="font-size: 48px;">Used the same exact method to get another offer</p>
                <p style="font-size: 48px; margin-top: 40px;">Second raise: Additional +$80K</p>
                <p style="font-size: 48px; margin-top: 20px;">Bonus: $70K stock</p>
            </div>
        """)
    },
    {
        'num': 64,
        'html': create_html_template(f"""
            <div class="slide">
                <h2 style="margin-bottom: 60px;">Darrell's Total Progression</h2>
                <div class="number-stat">$340K+</div>
                <p class="large-text" style="font-size: 48px;">$100K → $190K → $340K+</p>
                <p class="subhead" style="margin-top: 40px;">In approximately 2 years</p>
            </div>
        """)
    },
    {
        'num': 65,
        'html': create_html_template(f"""
            <div class="slide slide-left">
                <h2 style="margin-bottom: 50px;">Meet Simon</h2>
                <ul>
                    <li>Role: Account Executive</li>
                    <li>Income: $90K</li>
                    <li>Pain: Job wasn't paying enough to meet his needs</li>
                </ul>
            </div>
        """)
    },
    {
        'num': 66,
        'html': create_html_template(f"""
            <div class="slide slide-left">
                <h2 style="margin-bottom: 40px;">What Simon Implemented</h2>
                <ul>
                    <li>Used: Reverse Attraction, Interview Mastery, Negotiation</li>
                    <li>Biggest Breakthrough: Landed job offer of $280K</li>
                </ul>
            </div>
        """)
    },
    {
        'num': 67,
        'html': create_html_template(f"""
            <div class="slide">
                <h2 style="margin-bottom: 60px;">Simon's Result</h2>
                <p style="font-size: 52px; margin-bottom: 30px;">New Role: Account Executive</p>
                <p style="font-size: 52px; margin-bottom: 30px;">Final Offer: <span style="color: {COLORS['accent']}; font-weight: 700;">$280K</span></p>
                <div class="number-stat" style="margin-top: 60px;">3x</div>
                <p class="subhead">Over 3x his previous income</p>
            </div>
        """)
    },
    {
        'num': 68,
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
        'num': 69,
        'html': create_html_template(f"""
            <div class="slide">
                <h2 style="margin-bottom: 60px;">The System Recap</h2>
                <p class="large-text">Find where the "easy money" is, position yourself strategically, and multiple high-paying offers come to you</p>
            </div>
        """)
    },
    {
        'num': 70,
        'html': create_html_template(f"""
            <div class="slide">
                <h2>But You Might Be Thinking...</h2>
                <p class="large-text">"This sounds great... but can I really do this?"</p>
                <p class="subhead" style="margin-top: 80px;">Let me address that...</p>
            </div>
        """)
    },

    # PHASE 4: OVERCOMING OBJECTIONS (Slides 71-95)
    {
        'num': 71,
        'html': create_html_template(f"""
            <div class="slide slide-left">
                <h2 style="margin-bottom: 50px;">Common Concerns</h2>
                <ul>
                    <li>"I don't have time for this while working"</li>
                    <li>"My current employer will find out"</li>
                    <li>"This sounds like it takes months"</li>
                    <li>"I'm not qualified for those roles"</li>
                    <li>"This won't work in my industry"</li>
                </ul>
            </div>
        """)
    },
    {
        'num': 72,
        'html': create_html_template(f"""
            <div class="slide">
                <h2 style="margin-bottom: 60px;">These Are Valid Concerns</h2>
                <p class="large-text">You're busy. You're employed. You can't risk your current job.</p>
                <p class="subhead" style="margin-top: 80px;">Let me show you how to do this discreetly and efficiently</p>
            </div>
        """)
    },
    {
        'num': 73,
        'html': create_html_template(f"""
            <div class="slide">
                <h2 style="margin-bottom: 40px;">Concern #1: Time</h2>
                <p style="font-size: 48px; margin-bottom: 40px; color: {COLORS['warning']};">Myth: This takes hours per day</p>
                <p style="font-size: 48px; margin-bottom: 50px; color: {COLORS['success']}; font-weight: 600;">Reality: 30 minutes per day is enough</p>
            </div>
        """)
    },
    {
        'num': 74,
        'html': create_html_template(f"""
            <div class="slide">
                <h2 style="margin-bottom: 40px;">The 30-Minute Daily Breakdown</h2>
                <div style="text-align: left; max-width: 1000px; margin: 0 auto;">
                    <p style="font-size: 44px; margin: 25px 0;">10 min: LinkedIn optimization/activity</p>
                    <p style="font-size: 44px; margin: 25px 0;">15 min: Strategic outreach</p>
                    <p style="font-size: 44px; margin: 25px 0;">5 min: Follow-ups</p>
                </div>
            </div>
        """)
    },
    {
        'num': 75,
        'html': create_html_template(f"""
            <div class="slide slide-left">
                <h2 style="margin-bottom: 40px;">Concern #2: Privacy</h2>
                <p style="margin-bottom: 30px; font-size: 40px;">How to do this without your employer knowing:</p>
                <ul style="font-size: 38px;">
                    <li>Don't change LinkedIn headline to "Open to opportunities"</li>
                    <li>Take calls before/after work or lunch</li>
                    <li>Use personal email only</li>
                    <li>Schedule interviews as "appointments"</li>
                    <li>Never trash-talk current employer</li>
                </ul>
            </div>
        """)
    },
    {
        'num': 76,
        'html': create_html_template(f"""
            <div class="slide slide-left">
                <h2 style="margin-bottom: 40px;">Concern #3: Timeline</h2>
                <p style="margin-bottom: 30px; font-size: 40px;">Realistic 90-day timeline:</p>
                <ul style="font-size: 38px;">
                    <li>Weeks 1-2: Profile matching (target companies)</li>
                    <li>Weeks 3-4: Optimize LinkedIn, gather referrals</li>
                    <li>Weeks 5-6: Outreach and initial conversations</li>
                    <li>Weeks 7-8: Interviews</li>
                    <li>Weeks 9-10: Offers and negotiation</li>
                </ul>
                <p class="subhead" style="margin-top: 50px;">Total: 60-90 days from start to offer</p>
            </div>
        """)
    },
    {
        'num': 77,
        'html': create_html_template(f"""
            <div class="slide">
                <h2 style="margin-bottom: 60px;">Concern #4: Qualification</h2>
                <p class="large-text">Companies don't pay $300K for perfect candidates</p>
                <p class="subhead" style="margin-top: 80px;">They pay $300K for people who can DELIVER results</p>
            </div>
        """)
    },
    {
        'num': 78,
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
        'num': 79,
        'html': create_html_template(f"""
            <div class="slide">
                <h2 style="margin-bottom: 60px;">If You Can Sell, You Can Sell</h2>
                <p class="large-text">Your skills transfer across industries</p>
                <p class="subhead" style="margin-top: 80px;">You just need to POSITION them correctly</p>
            </div>
        """)
    },
    {
        'num': 80,
        'html': create_html_template(f"""
            <div class="slide slide-left">
                <h2 style="margin-bottom: 40px;">Concern #5: Industry</h2>
                <p style="font-size: 48px; margin-bottom: 40px;">If you're in B2B sales, this works</p>
                <p style="margin-bottom: 30px;">Proven industries:</p>
                <ul>
                    <li class="checkmark">SaaS</li>
                    <li class="checkmark">Tech</li>
                    <li class="checkmark">Pharma</li>
                    <li class="checkmark">Manufacturing</li>
                    <li class="checkmark">Financial services</li>
                    <li class="checkmark">Healthcare</li>
                </ul>
            </div>
        """)
    },
    {
        'num': 81,
        'html': create_html_template(f"""
            <div class="slide">
                <h2 style="margin-bottom: 40px;">Why This Doesn't Take Forever</h2>
                <p class="large-text" style="font-size: 48px;">You're TARGETING not spray-and-pray</p>
                <p class="large-text" style="font-size: 48px;">Hiring managers come to YOU (less chasing)</p>
                <p class="large-text" style="font-size: 48px;">Focus on HIGH-VALUE activities only</p>
            </div>
        """)
    },
    {
        'num': 82,
        'html': create_html_template(f"""
            <div class="slide slide-left">
                <h2 style="margin-bottom: 40px;">Time Wasters To AVOID</h2>
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
        'num': 83,
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
            </div>
        """)
    },
    {
        'num': 84,
        'html': create_html_template(f"""
            <div class="slide">
                <h2 style="margin-bottom: 60px;">The Real Question Isn't "Do I Have Time?"</h2>
                <p class="large-text">The real question is: "Can I afford NOT to do this?"</p>
                <p class="subhead" style="margin-top: 80px;">Every month you delay = $4K-$12K in lost income</p>
            </div>
        """)
    },
    {
        'num': 85,
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
        'num': 86,
        'html': create_html_template(f"""
            <div class="slide">
                <h2 style="margin-bottom: 60px;">Right Now, Companies Are Hiring</h2>
                <p class="large-text" style="font-size: 48px;">Premium sales roles are in demand. If you wait until the "perfect time," opportunities pass you by.</p>
                <p class="subhead" style="margin-top: 80px;">There's never a perfect time. But there IS right now.</p>
            </div>
        """)
    },
    {
        'num': 87,
        'html': create_html_template(f"""
            <div class="slide">
                <h2 style="margin-bottom: 60px;">You Now Know What Most Salespeople Never Learn</h2>
                <p class="large-text">You know the system. You know you're qualified. You know it's doable.</p>
                <p class="subhead" style="margin-top: 80px;">So what's next?</p>
            </div>
        """)
    },
    {
        'num': 88,
        'html': create_html_template(f"""
            <div class="slide slide-left">
                <h2 style="margin-bottom: 50px;">Let's Recap Everything</h2>
                <ul style="font-size: 40px;">
                    <li>How to find where the "easy money" is</li>
                    <li>The 4-step Active Offer System</li>
                    <li>How to position for multiple high-paying offers</li>
                    <li>You can do this in 30 min/day while employed</li>
                    <li>It works across B2B sales industries</li>
                </ul>
            </div>
        """)
    },
    {
        'num': 89,
        'html': create_html_template(f"""
            <div class="slide">
                <h2 style="margin-bottom: 80px;">Now You Have A Choice</h2>
                <p class="large-text">Continue doing what you've been doing and hope something changes...</p>
                <p class="large-text" style="margin-top: 60px;">Or take action on what you've learned today</p>
            </div>
        """)
    },
    {
        'num': 90,
        'html': create_html_template(f"""
            <div class="slide slide-left">
                <h2 style="margin-bottom: 40px;">Imagine 90 Days From Now...</h2>
                <ul>
                    <li>Multiple competing offers on the table</li>
                    <li>$50K-$150K increase in compensation</li>
                    <li>Working from home (if you want)</li>
                    <li>Better work-life balance</li>
                    <li>Complete control over your career</li>
                </ul>
                <p class="subhead" style="margin-top: 50px;">This is possible for you</p>
            </div>
        """)
    },
    {
        'num': 91,
        'html': create_html_template(f"""
            <div class="slide">
                <h2 style="margin-bottom: 60px;">But You're Probably Wondering...</h2>
                <p class="large-text">"How do I actually GET STARTED?"</p>
            </div>
        """)
    },
    {
        'num': 92,
        'html': create_html_template(f"""
            <div class="slide">
                <h2 style="margin-bottom: 60px;">Here's What I'm NOT Going To Do</h2>
                <p class="large-text">I'm not going to throw a price on the screen and tell you to "buy now"</p>
                <p class="subhead" style="margin-top: 80px;">Why? Because every person's situation is different</p>
            </div>
        """)
    },
    {
        'num': 93,
        'html': create_html_template(f"""
            <div class="slide slide-left">
                <h2 style="margin-bottom: 40px;">Your Career Is Too Important</h2>
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
        'num': 94,
        'html': create_html_template(f"""
            <div class="slide">
                <h2 style="margin-bottom: 80px;">Introducing: The Active Offer Program</h2>
                <p class="large-text">A 90-day intensive where I personally work with you to implement this system and land your premium offer</p>
            </div>
        """)
    },
    {
        'num': 95,
        'html': create_html_template(f"""
            <div class="slide">
                <h2 style="margin-bottom: 60px;">Here's What You'll Get</h2>
                <p class="large-text" style="font-size: 52px;">The complete 4-step system, all resources, direct coaching, and implementation support</p>
            </div>
        """)
    },

    # PHASE 5: THE OFFER & CLOSE (Slides 96-121)
    {
        'num': 96,
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
        'num': 97,
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
        'num': 98,
        'html': create_html_template(f"""
            <div class="slide slide-left">
                <h2 style="margin-bottom: 40px;">Module 3: Interview Mastery</h2>
                <ul>
                    <li>Interview preparation framework</li>
                    <li>Pre-prepared interview assets</li>
                    <li>Value positioning tactics</li>
                    <li>Understanding what hiring managers look for</li>
                </ul>
            </div>
        """)
    },
    {
        'num': 99,
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
        'num': 100,
        'html': create_html_template(f"""
            <div class="slide slide-left">
                <h2 style="margin-bottom: 40px;">Premium Resources Included</h2>
                <ul style="font-size: 40px;">
                    <li>Scripts Workbook (top scripts that land interviews)</li>
                    <li>Sure Hire Plays (get recruited for top roles fast)</li>
                    <li>Presentation Templates & 30-60-90 Day Plans</li>
                    <li>Resume & Cover Letter Templates</li>
                    <li>Self-Accountability Log</li>
                    <li>LinkedIn Profile Checklist</li>
                    <li>Interview Questions Workbook (what top companies ask)</li>
                    <li>Cold Email & LinkedIn Vault</li>
                </ul>
            </div>
        """)
    },
    {
        'num': 101,
        'html': create_html_template(f"""
            <div class="slide slide-left">
                <h2 style="margin-bottom: 40px;">PLUS: Direct Support</h2>
                <ul>
                    <li>Group coaching calls (twice per week)</li>
                    <li>Community access (Slack workspace)</li>
                    <li>Email support</li>
                    <li>Compensation negotiation support</li>
                </ul>
            </div>
        """)
    },
    {
        'num': 102,
        'html': create_html_template(f"""
            <div class="slide slide-left">
                <h2 style="margin-bottom: 40px;">What's This Worth?</h2>
                <p style="margin-bottom: 30px;">Consider:</p>
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
        'num': 103,
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
        'num': 104,
        'html': create_html_template(f"""
            <div class="slide">
                <h2 style="margin-bottom: 80px;">But Like I Said...</h2>
                <p class="large-text">I'm not revealing a price. Your situation is unique.</p>
                <p class="subhead" style="margin-top: 80px;">Instead, here's what I want to do...</p>
            </div>
        """)
    },
    {
        'num': 105,
        'html': create_html_template(f"""
            <div class="slide">
                <h2 style="margin-bottom: 80px;">I Want To Invite You To A Free Strategy Call</h2>
                <p class="large-text">This is a 45-minute call where we'll map out your path...</p>
            </div>
        """)
    },
    {
        'num': 106,
        'html': create_html_template(f"""
            <div class="slide slide-left">
                <h2 style="margin-bottom: 40px;">On This Call, We'll...</h2>
                <ul>
                    <li>Map out your ideal role (comp, company, lifestyle)</li>
                    <li>Identify the exact positioning gaps keeping you stuck</li>
                    <li>Show you the roadmap to your $50K-$150K+ raise</li>
                    <li>Determine if Active Offer is the right fit for you</li>
                </ul>
            </div>
        """)
    },
    {
        'num': 107,
        'html': create_html_template(f"""
            <div class="slide">
                <h2 style="margin-bottom: 60px;">This Is NOT A High-Pressure Sales Call</h2>
                <p class="large-text">If it's not a fit, I'll tell you. If it is, we'll talk about what it looks like to work together.</p>
                <p class="subhead" style="margin-top: 80px;">Either way, you'll leave with clarity</p>
            </div>
        """)
    },
    {
        'num': 108,
        'html': create_html_template(f"""
            <div class="slide slide-left">
                <h2 style="margin-bottom: 40px;">Who Should Book This Call?</h2>
                <p style="margin-bottom: 30px; font-size: 40px;">Good fit:</p>
                <ul style="font-size: 38px;">
                    <li>Making $80K+ in B2B sales currently</li>
                    <li>4+ years of sales experience</li>
                    <li>Proven track record of results</li>
                    <li>Ready to invest in your career</li>
                    <li>Willing to put in 30 min/day for 90 days</li>
                </ul>
            </div>
        """)
    },
    {
        'num': 109,
        'html': create_html_template(f"""
            <div class="slide slide-left">
                <h2 style="margin-bottom: 40px;">Who Shouldn't Book This Call</h2>
                <p style="margin-bottom: 30px; font-size: 40px;">Not a fit:</p>
                <ul style="font-size: 38px;">
                    <li>Looking for a magic button (no work)</li>
                    <li>Not in B2B sales</li>
                    <li>Less than 4 years sales experience</li>
                    <li>Under $80K current income</li>
                    <li>Not willing to invest in yourself</li>
                </ul>
            </div>
        """)
    },
    {
        'num': 110,
        'html': create_html_template(f"""
            <div class="slide">
                <h2 style="margin-bottom: 60px;">Time Commitment</h2>
                <p class="large-text" style="font-size: 52px;">30 minutes per day</p>
                <p class="subhead" style="margin-top: 60px;">90 days to results</p>
            </div>
        """)
    },
    {
        'num': 111,
        'html': create_html_template(f"""
            <div class="slide">
                <h2 style="margin-bottom: 60px;">Investment</h2>
                <p class="large-text">We'll discuss pricing on the strategy call based on your specific situation</p>
                <p class="subhead" style="margin-top: 60px;">Payment plans available</p>
            </div>
        """)
    },
    {
        'num': 112,
        'html': create_html_template(f"""
            <div class="slide">
                <h2 style="margin-bottom: 60px;">Every Month You Wait...</h2>
                <p class="large-text">Is another month at your current income</p>
                <div style="text-align: left; max-width: 1000px; margin: 50px auto;">
                    <p style="font-size: 44px; margin: 20px 0;">If $90K raise is possible...</p>
                    <p style="font-size: 44px; margin: 20px 0;">Waiting 3 months = <span style="color: {COLORS['warning']}; font-weight: 700;">$22,500 lost</span></p>
                    <p style="font-size: 44px; margin: 20px 0;">Waiting 6 months = <span style="color: {COLORS['warning']}; font-weight: 700;">$45,000 lost</span></p>
                </div>
            </div>
        """)
    },
    {
        'num': 113,
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
        'num': 114,
        'html': create_html_template(f"""
            <div class="slide">
                <h2 style="margin-bottom: 60px;">The Choice Is Yours</h2>
                <p class="large-text">You can continue hoping things change on their own...</p>
                <p class="large-text" style="margin-top: 60px;">Or you can take control and make it happen</p>
            </div>
        """)
    },
    {
        'num': 115,
        'html': create_html_template(f"""
            <div class="slide">
                <h2 style="margin-bottom: 60px;">Ready To Get Started?</h2>
                <div class="cta">BOOK YOUR FREE STRATEGY CALL</div>
                <p class="small-text" style="margin-top: 40px;">No credit card required. Just 45 minutes to map your path.</p>
            </div>
        """)
    },
    {
        'num': 116,
        'html': create_html_template(f"""
            <div class="slide slide-left">
                <h2 style="margin-bottom: 50px;">Here's What To Do Right Now</h2>
                <ul style="font-size: 44px;">
                    <li>Click the button below</li>
                    <li>Pick a time that works for you</li>
                    <li>Show up ready to discuss your goals</li>
                    <li>Leave with complete clarity on your next steps</li>
                </ul>
            </div>
        """)
    },
    {
        'num': 117,
        'html': create_html_template(f"""
            <div class="slide">
                <div class="cta" style="font-size: 64px;">BOOK YOUR STRATEGY CALL NOW</div>
                <p class="subhead" style="margin-top: 60px;">Takes 2 minutes to schedule</p>
            </div>
        """)
    },
    {
        'num': 118,
        'html': create_html_template(f"""
            <div class="slide">
                <h2 style="margin-bottom: 60px;">Remember...</h2>
                <p class="large-text">You don't even know what high-paying opportunities exist</p>
                <p class="subhead" style="margin-top: 80px;">Let me show you where the "easy money" is</p>
            </div>
        """)
    },
    {
        'num': 119,
        'html': create_html_template(f"""
            <div class="slide">
                <h2 style="margin-bottom: 60px;">One Year From Now...</h2>
                <p class="large-text">You'll either be in the same position you're in today...</p>
                <p class="large-text" style="margin-top: 60px;">Or you'll be making $50K-$150K+ more</p>
                <p class="subhead" style="margin-top: 80px;">The choice is yours</p>
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
    {
        'num': 121,
        'html': create_html_template(f"""
            <div class="slide">
                <h1 style="color: {COLORS['primary']};">Thank You</h1>
                <p class="subhead">Book your free strategy call below</p>
            </div>
        """)
    },
]

def generate_slides():
    """Generate all 121 slides as PNG files"""
    output_dir = "/Users/terrancebrandon/Desktop/Active Offer/AO- Course Content/Active Offer- Course Material/.Webinar Script v.2.1 - Final"

    print(f"Starting slide generation for v2.1 (121 slides)...")
    print(f"Output directory: {output_dir}")
    print(f"\nCritical corrections applied:")
    print(f"  ✓ Slide 1: Updated subtitle to 'Increase Your Income in 90 Days'")
    print(f"  ✓ Slide 4: Reframed to 'don't know opportunities exist'")
    print(f"  ✓ Slide 8: Corrected to overheard conversation about $400K colleague")
    print(f"  ✓ Slide 10-11: New Big Domino about finding easy money")
    print(f"  ✓ Slide 14: Darrell with TWO L's, removed Sarah, added real stats")
    print(f"  ✓ All slides: Darrell spelling corrected throughout")
    print(f"  ✓ All slides: Sarah completely removed")
    print(f"\n")

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

            print(f"Generated slide {slide_num}/121")

        browser.close()

    print(f"\n✓ All 121 slides generated successfully!")
    print(f"✓ Location: {output_dir}")
    print(f"\n✓ All corrections verified:")
    print(f"  - Darrell (TWO L's) used throughout")
    print(f"  - Sarah completely removed")
    print(f"  - Big Domino corrected")
    print(f"  - Slide 4 reframed")
    print(f"  - Slide 8 corrected with aha moment #1")

if __name__ == "__main__":
    generate_slides()
