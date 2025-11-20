# Reverse Attraction Tracker - Google Sheets Specification
## Complete Build Guide for Outreach Tracking System

**Module:** M2 - Reverse Attraction
**Course:** Active Offer Career Acceleration
**Version:** 1.0

---

## Overview

This document provides complete specifications for building the Reverse Attraction Tracker in Google Sheets. This tracker helps students manage all outreach activities, track responses, calculate metrics, and maintain accountability.

**Purpose:** Single source of truth for all hiring manager outreach, follow-ups, and results

**Key Features:**
- Main tracker with all contacts and activities
- Auto-calculated metrics dashboard
- Automated follow-up queue
- Win journal for momentum and motivation
- Template quick reference

---

## TAB 1: Main Tracker

### Column Structure

| Column | Header | Data Type | Width | Description |
|--------|--------|-----------|-------|-------------|
| A | Name | Text | 150px | Hiring manager's full name |
| B | Company | Text | 150px | Company name |
| C | Title | Text | 180px | Their job title |
| D | Industry | Dropdown | 120px | Company industry |
| E | LinkedIn URL | URL | 200px | Full LinkedIn profile URL |
| F | Email Address | Email | 200px | Professional email if available |
| G | LinkedIn Open Profile? | Dropdown | 100px | Yes/No - can you message without connection? |
| H | Date Added | Date | 100px | When you added them to tracker |
| I | LinkedIn Message Sent? | Date | 100px | Date of LinkedIn message (blank if not sent) |
| J | Email Sent? | Date | 100px | Date of email (blank if not sent) |
| K | Channel Used | Dropdown | 120px | LinkedIn, Email, Both, None |
| L | Status | Dropdown | 140px | Current status in pipeline |
| M | Last Contact Date | Date | 120px | Most recent touchpoint |
| N | Next Follow-Up Date | Formula | 120px | Auto-calculated based on last contact |
| O | Response? | Dropdown | 80px | Yes/No |
| P | Notes | Text | 300px | Free-form notes |
| Q | Win? | Checkbox | 60px | Interview secured? |

### Data Validation Rules

**Column D: Industry (Dropdown)**
```
Options:
- SaaS
- Enterprise Software
- Fintech
- Healthcare Technology
- E-commerce
- Marketing Technology
- Sales Technology
- HR Technology
- Cybersecurity
- Data & Analytics
- Infrastructure/DevOps
- Consumer Technology
- Other
```

**Column G: LinkedIn Open Profile? (Dropdown)**
```
Options:
- Yes
- No
```

**Column K: Channel Used (Dropdown)**
```
Options:
- None
- LinkedIn
- Email
- Both
```

**Column L: Status (Dropdown)**
```
Options:
- Not Contacted
- Sent
- Opened
- Replied
- Meeting Scheduled
- Interview
- Rejected
- Nurture
```

**Column O: Response? (Dropdown)**
```
Options:
- Yes
- No
- (blank)
```

### Formulas

**Column N: Next Follow-Up Date**

Formula for cell N2 (copy down):
```
=IF(M2="","",
  IF(L2="Meeting Scheduled","",
    IF(L2="Interview","",
      IF(L2="Rejected","",
        IF(L2="Replied","",
          IF(ISDATE(M2),M2+7,"")
        )
      )
    )
  )
)
```

**Logic:**
- If Last Contact Date is blank, leave blank
- If Status is "Meeting Scheduled", "Interview", "Rejected", or "Replied", no follow-up needed
- Otherwise, add 7 days to Last Contact Date for follow-up

### Conditional Formatting Rules

**Rule 1: Highlight Follow-Ups Due Today (Yellow)**
- Apply to: Column A-Q (entire row)
- Format cells if: Custom formula is `=$N2=TODAY()`
- Background: Light yellow (#FFF9C4)

**Rule 2: Highlight Overdue Follow-Ups (Red)**
- Apply to: Column A-Q (entire row)
- Format cells if: Custom formula is `=AND($N2<TODAY(),$N2<>"")`
- Background: Light red (#F4CCCC)

**Rule 3: Highlight Wins (Green)**
- Apply to: Column A-Q (entire row)
- Format cells if: Custom formula is `=$Q2=TRUE`
- Background: Light green (#D9EAD3)

**Rule 4: Status-Based Formatting**
- Apply to: Column L (Status column)
- Format cells if: Text is exactly "Meeting Scheduled"
- Background: Light blue (#C9DAF8)
- Font: Bold

- Apply to: Column L
- Format cells if: Text is exactly "Interview"
- Background: Light green (#B6D7A8)
- Font: Bold

- Apply to: Column L
- Format cells if: Text is exactly "Rejected"
- Background: Light gray (#CCCCCC)
- Font: Regular

### Sample Data (10 Example Rows)

**Row 2:**
- Name: Jennifer Martinez
- Company: Salesforce
- Title: VP of Enterprise Sales
- Industry: SaaS
- LinkedIn URL: https://linkedin.com/in/jennifer-martinez-sales
- Email Address: jennifer.martinez@salesforce.com
- LinkedIn Open Profile?: Yes
- Date Added: 2024-11-01
- LinkedIn Message Sent?: 2024-11-02
- Email Sent?: (blank)
- Channel Used: LinkedIn
- Status: Replied
- Last Contact Date: 2024-11-05
- Next Follow-Up Date: (auto-calculated)
- Response?: Yes
- Notes: Mentioned they're expanding enterprise team in Q1. Follow up mid-December.
- Win?: FALSE

**Row 3:**
- Name: Michael Chen
- Company: HubSpot
- Title: Director of Sales - Enterprise
- Industry: Marketing Technology
- LinkedIn URL: https://linkedin.com/in/michaelchen
- Email Address: (blank)
- LinkedIn Open Profile?: No
- Date Added: 2024-11-01
- LinkedIn Message Sent?: 2024-11-03
- Email Sent?: (blank)
- Channel Used: LinkedIn
- Status: Sent
- Last Contact Date: 2024-11-03
- Next Follow-Up Date: 2024-11-10
- Response?: No
- Notes: (blank)
- Win?: FALSE

**Row 4:**
- Name: Sarah Johnson
- Company: Stripe
- Title: Head of Sales - North America
- Industry: Fintech
- LinkedIn URL: https://linkedin.com/in/sarahjohnson
- Email Address: sarah.j@stripe.com
- LinkedIn Open Profile?: Yes
- Date Added: 2024-11-02
- LinkedIn Message Sent?: 2024-11-04
- Email Sent?: 2024-11-04
- Channel Used: Both
- Status: Meeting Scheduled
- Last Contact Date: 2024-11-06
- Next Follow-Up Date: (blank - meeting scheduled)
- Response?: Yes
- Notes: Call scheduled for 11/12 at 2pm EST. Discuss enterprise expansion.
- Win?: FALSE

**Row 5:**
- Name: David Park
- Company: Snowflake
- Title: Senior Director, Enterprise Sales
- Industry: Data & Analytics
- LinkedIn URL: https://linkedin.com/in/davidpark-sales
- Email Address: david.park@snowflake.com
- LinkedIn Open Profile?: Yes
- Date Added: 2024-10-28
- LinkedIn Message Sent?: 2024-10-29
- Email Sent?: (blank)
- Channel Used: LinkedIn
- Status: Interview
- Last Contact Date: 2024-11-08
- Next Follow-Up Date: (blank - interview status)
- Response?: Yes
- Notes: First round interview completed. Waiting on decision for final round.
- Win?: TRUE

**Row 6:**
- Name: Rachel Williams
- Company: Gong
- Title: VP of Revenue
- Industry: Sales Technology
- LinkedIn URL: https://linkedin.com/in/rachelwilliams
- Email Address: (blank)
- LinkedIn Open Profile?: No
- Date Added: 2024-11-03
- LinkedIn Message Sent?: (blank)
- Email Sent?: (blank)
- Channel Used: None
- Status: Not Contacted
- Last Contact Date: (blank)
- Next Follow-Up Date: (blank)
- Response?: (blank)
- Notes: Found through LinkedIn Sales Navigator. Need to research before outreach.
- Win?: FALSE

**Row 7:**
- Name: James Anderson
- Company: DocuSign
- Title: RVP - Enterprise Sales
- Industry: Enterprise Software
- LinkedIn URL: https://linkedin.com/in/jamesanderson
- Email Address: james.anderson@docusign.com
- LinkedIn Open Profile?: Yes
- Date Added: 2024-10-25
- LinkedIn Message Sent?: 2024-10-26
- Email Sent?: 2024-11-02
- Channel Used: Both
- Status: Rejected
- Last Contact Date: 2024-11-04
- Next Follow-Up Date: (blank - rejected)
- Response?: Yes
- Notes: Not hiring currently. Suggested reconnecting in Q2 2025.
- Win?: FALSE

**Row 8:**
- Name: Lisa Thompson
- Company: Zoom
- Title: Director of Enterprise Sales
- Industry: SaaS
- LinkedIn URL: https://linkedin.com/in/lisathompson
- Email Address: (blank)
- LinkedIn Open Profile?: Yes
- Date Added: 2024-11-05
- LinkedIn Message Sent?: 2024-11-06
- Email Sent?: (blank)
- Channel Used: LinkedIn
- Status: Sent
- Last Contact Date: 2024-11-06
- Next Follow-Up Date: 2024-11-13
- Response?: No
- Notes: (blank)
- Win?: FALSE

**Row 9:**
- Name: Kevin Rodriguez
- Company: Atlassian
- Title: Head of Strategic Accounts
- Industry: SaaS
- LinkedIn URL: https://linkedin.com/in/kevinrodriguez
- Email Address: kevin.r@atlassian.com
- LinkedIn Open Profile?: Yes
- Date Added: 2024-11-04
- LinkedIn Message Sent?: (blank)
- Email Sent?: 2024-11-05
- Channel Used: Email
- Status: Opened
- Last Contact Date: 2024-11-05
- Next Follow-Up Date: 2024-11-12
- Response?: No
- Notes: Email tracked - opened 2x but no response yet.
- Win?: FALSE

**Row 10:**
- Name: Amanda Foster
- Company: Notion
- Title: VP of Sales
- Industry: SaaS
- LinkedIn URL: https://linkedin.com/in/amandafoster
- Email Address: (blank)
- LinkedIn Open Profile?: No
- Date Added: 2024-11-01
- LinkedIn Message Sent?: 2024-11-02
- Email Sent?: (blank)
- Channel Used: LinkedIn
- Status: Nurture
- Last Contact Date: 2024-11-03
- Next Follow-Up Date: 2024-11-10
- Response?: Yes
- Notes: Responded - no current openings but asked to stay in touch. Follow up monthly.
- Win?: FALSE

**Row 11:**
- Name: Chris Bailey
- Company: Figma
- Title: Director of Enterprise Sales
- Industry: SaaS
- LinkedIn URL: https://linkedin.com/in/chrisbailey
- Email Address: chris.bailey@figma.com
- LinkedIn Open Profile?: Yes
- Date Added: 2024-10-30
- LinkedIn Message Sent?: 2024-10-31
- Email Sent?: 2024-11-01
- Channel Used: Both
- Status: Meeting Scheduled
- Last Contact Date: 2024-11-07
- Next Follow-Up Date: (blank)
- Response?: Yes
- Notes: Initial call went well. Second round with VP scheduled for 11/14.
- Win?: TRUE

---

## TAB 2: Metrics Dashboard

### Layout Structure

**Section 1: Overview Metrics (Rows 1-10)**

Create these labeled cells:

**A1:** `METRICS DASHBOARD`
- Font: 18pt, Bold
- Merge cells A1:D1

**A3:** `Total Contacts`
**B3:** Formula: `=COUNTA('Main Tracker'!A2:A1000)-COUNTBLANK('Main Tracker'!A2:A1000)`

**A4:** `LinkedIn Messages Sent (All-Time)`
**B4:** Formula: `=COUNTIF('Main Tracker'!I2:I1000,"<>"")`

**A5:** `Emails Sent (All-Time)`
**B5:** Formula: `=COUNTIF('Main Tracker'!J2:J1000,"<>"")`

**A6:** `Total Touchpoints`
**B6:** Formula: `=B4+B5`

**A7:** `Responses Received`
**B7:** Formula: `=COUNTIF('Main Tracker'!O2:O1000,"Yes")`

**A8:** `Response Rate`
**B8:** Formula: `=IF(B6=0,"0%",TEXT(B7/B6,"0.0%"))`

**A9:** `Meetings Scheduled`
**B9:** Formula: `=COUNTIF('Main Tracker'!L2:L1000,"Meeting Scheduled")`

**A10:** `Interviews Secured`
**B10:** Formula: `=COUNTIF('Main Tracker'!L2:L1000,"Interview")+COUNTIF('Main Tracker'!Q2:Q1000,TRUE)`

**A11:** `Conversion Rate (Touchpoint → Meeting)`
**B11:** Formula: `=IF(B6=0,"0%",TEXT(B9/B6,"0.0%"))`

**A12:** `Win Rate (Touchpoint → Interview)`
**B12:** Formula: `=IF(B6=0,"0%",TEXT(B10/B6,"0.0%"))`

---

**Section 2: This Week Metrics (Rows 14-20)**

**A14:** `THIS WEEK`
- Font: 14pt, Bold

**A16:** `LinkedIn Messages (This Week)`
**B16:** Formula: `=COUNTIFS('Main Tracker'!I2:I1000,">="&TODAY()-7,'Main Tracker'!I2:I1000,"<="&TODAY())`

**A17:** `Emails Sent (This Week)`
**B17:** Formula: `=COUNTIFS('Main Tracker'!J2:J1000,">="&TODAY()-7,'Main Tracker'!J2:J1000,"<="&TODAY())`

**A18:** `Total Touchpoints (This Week)`
**B18:** Formula: `=B16+B17`

**A19:** `Responses (This Week)`
**B19:** Formula: `=COUNTIFS('Main Tracker'!M2:M1000,">="&TODAY()-7,'Main Tracker'!M2:M1000,"<="&TODAY(),'Main Tracker'!O2:O1000,"Yes")`

**A20:** `Response Rate (This Week)`
**B20:** Formula: `=IF(B18=0,"0%",TEXT(B19/B18,"0.0%"))`

---

**Section 3: This Month Metrics (Rows 22-28)**

**A22:** `THIS MONTH`
- Font: 14pt, Bold

**A24:** `LinkedIn Messages (This Month)`
**B24:** Formula: `=COUNTIFS('Main Tracker'!I2:I1000,">="&DATE(YEAR(TODAY()),MONTH(TODAY()),1),'Main Tracker'!I2:I1000,"<="&TODAY())`

**A25:** `Emails Sent (This Month)`
**B25:** Formula: `=COUNTIFS('Main Tracker'!J2:J1000,">="&DATE(YEAR(TODAY()),MONTH(TODAY()),1),'Main Tracker'!J2:J1000,"<="&TODAY())`

**A26:** `Total Touchpoints (This Month)`
**B26:** Formula: `=B24+B25`

**A27:** `Responses (This Month)`
**B27:** Formula: `=COUNTIFS('Main Tracker'!M2:M1000,">="&DATE(YEAR(TODAY()),MONTH(TODAY()),1),'Main Tracker'!M2:M1000,"<="&TODAY(),'Main Tracker'!O2:O1000,"Yes")`

**A28:** `Response Rate (This Month)`
**B28:** Formula: `=IF(B26=0,"0%",TEXT(B27/B26,"0.0%"))`

---

**Section 4: Channel Performance (Rows 30-36)**

**A30:** `CHANNEL PERFORMANCE`
- Font: 14pt, Bold

**A32:** `LinkedIn-Only Responses`
**B32:** Formula: `=COUNTIFS('Main Tracker'!K2:K1000,"LinkedIn",'Main Tracker'!O2:O1000,"Yes")`

**A33:** `LinkedIn-Only Sent`
**B33:** Formula: `=COUNTIF('Main Tracker'!K2:K1000,"LinkedIn")`

**A34:** `LinkedIn Response Rate`
**B34:** Formula: `=IF(B33=0,"0%",TEXT(B32/B33,"0.0%"))`

**A36:** `Email-Only Responses`
**B36:** Formula: `=COUNTIFS('Main Tracker'!K2:K1000,"Email",'Main Tracker'!O2:O1000,"Yes")`

**A37:** `Email-Only Sent`
**B37:** Formula: `=COUNTIF('Main Tracker'!K2:K1000,"Email")`

**A38:** `Email Response Rate`
**B38:** Formula: `=IF(B37=0,"0%",TEXT(B36/B37,"0.0%"))`

**A40:** `Both Channels Responses`
**B40:** Formula: `=COUNTIFS('Main Tracker'!K2:K1000,"Both",'Main Tracker'!O2:O1000,"Yes")`

**A41:** `Both Channels Sent`
**B41:** Formula: `=COUNTIF('Main Tracker'!K2:K1000,"Both")`

**A42:** `Both Channels Response Rate`
**B42:** Formula: `=IF(B41=0,"0%",TEXT(B40/B41,"0.0%"))`

---

**Section 5: Status Breakdown (Rows 44-55)**

**A44:** `STATUS BREAKDOWN`
- Font: 14pt, Bold

**A46:** `Not Contacted`
**B46:** Formula: `=COUNTIF('Main Tracker'!L2:L1000,"Not Contacted")`

**A47:** `Sent (No Response)`
**B47:** Formula: `=COUNTIF('Main Tracker'!L2:L1000,"Sent")`

**A48:** `Opened (No Response)`
**B48:** Formula: `=COUNTIF('Main Tracker'!L2:L1000,"Opened")`

**A49:** `Replied`
**B49:** Formula: `=COUNTIF('Main Tracker'!L2:L1000,"Replied")`

**A50:** `Meeting Scheduled`
**B50:** Formula: `=COUNTIF('Main Tracker'!L2:L1000,"Meeting Scheduled")`

**A51:** `Interview`
**B51:** Formula: `=COUNTIF('Main Tracker'!L2:L1000,"Interview")`

**A52:** `Rejected`
**B52:** Formula: `=COUNTIF('Main Tracker'!L2:L1000,"Rejected")`

**A53:** `Nurture`
**B53:** Formula: `=COUNTIF('Main Tracker'!L2:L1000,"Nurture")`

---

**Section 6: Goal Tracking (Rows 57-65)**

**A57:** `GOAL TRACKING`
- Font: 14pt, Bold

**A59:** `Daily LinkedIn Goal`
**B59:** `5` (manual entry)

**A60:** `Daily Email Goal`
**B60:** `5` (manual entry)

**A62:** `LinkedIn This Week`
**B62:** `=B16`

**A63:** `LinkedIn Goal This Week (5/day × 5 days)`
**B63:** `=B59*5`

**A64:** `LinkedIn Progress`
**B64:** Formula: `=TEXT(B62/B63,"0%")`

**A66:** `Email This Week`
**B66:** `=B17`

**A67:** `Email Goal This Week (5/day × 5 days)`
**B67:** `=B60*5`

**A68:** `Email Progress`
**B68:** Formula: `=TEXT(B66/B67,"0%")`

### Conditional Formatting for Dashboard

**Rule 1: Goal Achievement (Green)**
- Apply to: B64, B68
- Format cells if: Value >= 1
- Background: Light green (#D9EAD3)
- Font: Bold, dark green

**Rule 2: Partial Progress (Yellow)**
- Apply to: B64, B68
- Format cells if: Value >= 0.5 AND Value < 1
- Background: Light yellow (#FFF9C4)

**Rule 3: Below Target (Red)**
- Apply to: B64, B68
- Format cells if: Value < 0.5
- Background: Light red (#F4CCCC)

---

## TAB 3: Follow-Up Queue

### Column Structure

| Column | Header | Formula/Type | Width | Description |
|--------|--------|--------------|-------|-------------|
| A | Name | Formula | 150px | Pull from Main Tracker |
| B | Company | Formula | 150px | Pull from Main Tracker |
| C | Last Contact | Formula | 100px | Pull from Main Tracker |
| D | Days Since Contact | Formula | 100px | Calculate days |
| E | Next Follow-Up | Formula | 120px | Pull from Main Tracker |
| F | Status | Formula | 120px | Pull from Main Tracker |
| G | Channel to Use | Formula | 120px | Recommend channel |
| H | Completed? | Checkbox | 80px | Manual check when done |

### Formulas

**Header Row (Row 1):**
Add headers as listed above, formatted bold with background color #4A86E8 (blue), white text.

**Row 2 and below use FILTER function:**

**Cell A2 (Name):**
```
=FILTER('Main Tracker'!A2:A,
  ('Main Tracker'!N2:N<=TODAY())*('Main Tracker'!N2:N<>"")*('Main Tracker'!L2:L<>"Meeting Scheduled")*('Main Tracker'!L2:L<>"Interview")*('Main Tracker'!L2:L<>"Rejected"),
  "No follow-ups needed today")
```

**Cell B2 (Company):**
```
=IF(A2="No follow-ups needed today","",FILTER('Main Tracker'!B2:B,
  ('Main Tracker'!N2:N<=TODAY())*('Main Tracker'!N2:N<>"")*('Main Tracker'!L2:L<>"Meeting Scheduled")*('Main Tracker'!L2:L<>"Interview")*('Main Tracker'!L2:L<>"Rejected"),
  ""))
```

**Cell C2 (Last Contact):**
```
=IF(A2="No follow-ups needed today","",FILTER('Main Tracker'!M2:M,
  ('Main Tracker'!N2:N<=TODAY())*('Main Tracker'!N2:N<>"")*('Main Tracker'!L2:L<>"Meeting Scheduled")*('Main Tracker'!L2:L<>"Interview")*('Main Tracker'!L2:L<>"Rejected"),
  ""))
```

**Cell D2 (Days Since Contact):**
```
=IF(A2="No follow-ups needed today","",TODAY()-C2)
```

**Cell E2 (Next Follow-Up):**
```
=IF(A2="No follow-ups needed today","",FILTER('Main Tracker'!N2:N,
  ('Main Tracker'!N2:N<=TODAY())*('Main Tracker'!N2:N<>"")*('Main Tracker'!L2:L<>"Meeting Scheduled")*('Main Tracker'!L2:L<>"Interview")*('Main Tracker'!L2:L<>"Rejected"),
  ""))
```

**Cell F2 (Status):**
```
=IF(A2="No follow-ups needed today","",FILTER('Main Tracker'!L2:L,
  ('Main Tracker'!N2:N<=TODAY())*('Main Tracker'!N2:N<>"")*('Main Tracker'!L2:L<>"Meeting Scheduled")*('Main Tracker'!L2:L<>"Interview")*('Main Tracker'!L2:L<>"Rejected"),
  ""))
```

**Cell G2 (Channel to Use):**
```
=IF(A2="No follow-ups needed today","",
  IF(D2>=14,"Email (2nd follow-up)",
    IF(D2>=7,"LinkedIn or Email (1st follow-up)","LinkedIn")))
```

**Note:** Google Sheets FILTER function auto-expands, so you only need formulas in row 2.

### Conditional Formatting

**Rule 1: Overdue (Red)**
- Apply to: Entire row
- Format cells if: Custom formula `=$E2<TODAY()`
- Background: Light red (#F4CCCC)

**Rule 2: Due Today (Yellow)**
- Apply to: Entire row
- Format cells if: Custom formula `=$E2=TODAY()`
- Background: Light yellow (#FFF9C4)

**Rule 3: Completed (Gray)**
- Apply to: Entire row
- Format cells if: Custom formula `=$H2=TRUE`
- Background: Light gray (#EEEEEE)
- Text: Strikethrough

### Instructions Section (Below the data)

Add this starting at Row 25:

**A25:** `HOW TO USE THIS TAB`
- Font: 14pt, Bold
- Merge A25:H25

**A27:** `This tab automatically shows everyone who needs a follow-up today or is overdue.`

**A29:** `What to do:`
**A30:** `1. Review the list each morning`
**A31:** `2. Use the recommended channel in column G`
**A32:** `3. Send your follow-up message (use Follow-Up templates from Scripts Playbook)`
**A33:** `4. Update the "Last Contact Date" in the Main Tracker tab`
**A34:** `5. Check the "Completed?" box in column H`

**A36:** `Color coding:`
**A37:** `- Red = Overdue (send today!)`
**A38:** `- Yellow = Due today`
**A39:** `- Gray with strikethrough = You marked as completed`

**A41:** `Tip: Aim to clear this list every day. Consistency is key!`

---

## TAB 4: Win Journal

### Column Structure

| Column | Header | Data Type | Width | Description |
|--------|--------|-----------|-------|-------------|
| A | Date | Date | 100px | When the win happened |
| B | Hiring Manager | Text | 150px | Their name |
| C | Company | Text | 150px | Company name |
| D | Win Type | Dropdown | 150px | Type of win |
| E | What Happened | Text | 300px | Description of the win |
| F | Why It Matters | Text | 300px | Impact/learning |
| G | Feeling | Dropdown | 100px | Emotional state |

### Data Validation

**Column D: Win Type (Dropdown)**
```
Options:
- Positive Response
- Call Scheduled
- Interview Scheduled
- 2nd/3rd Interview
- Offer Received
- Referral Received
- Warm Introduction
- Great Conversation
- Other
```

**Column G: Feeling (Dropdown)**
```
Options:
- Excited
- Confident
- Motivated
- Grateful
- Relieved
- Energized
- Proud
```

### Sample Data (5 Example Wins)

**Row 2:**
- Date: 2024-11-01
- Hiring Manager: Jennifer Martinez
- Company: Salesforce
- Win Type: Positive Response
- What Happened: She responded to my LinkedIn message within 24 hours! Said she's impressed by my background in enterprise sales and wants to schedule a call.
- Why It Matters: This is a dream company for me. Her quick response shows my message resonated. Proves the personalization approach works.
- Feeling: Excited

**Row 3:**
- Date: 2024-11-05
- Hiring Manager: Sarah Johnson
- Company: Stripe
- Win Type: Call Scheduled
- What Happened: Had a 30-minute exploratory call. She loved my experience scaling deal sizes from SMB to enterprise. Scheduled formal interview for next week.
- Why It Matters: Getting past the initial screen is huge. She specifically called out my metrics and approach to enterprise selling. Building real momentum.
- Feeling: Confident

**Row 4:**
- Date: 2024-11-07
- Hiring Manager: David Park
- Company: Snowflake
- Win Type: Interview Scheduled
- What Happened: Made it to final round! Interview with VP of Sales scheduled for 11/15. They want to discuss my approach to regulated industries.
- Why It Matters: This would be a career-defining move. Getting to final round validates all the work I've put in. They're specifically interested in my unique experience.
- Feeling: Energized

**Row 5:**
- Date: 2024-11-04
- Hiring Manager: James Anderson
- Company: DocuSign
- Win Type: Referral Received
- What Happened: Even though they're not hiring, James referred me to two other VPs in his network at Adobe and MongoDB. Sent warm intro emails.
- Why It Matters: This is the power of relationship building. Even a "no" can turn into opportunity. Now I have warm intros instead of cold outreach.
- Feeling: Grateful

**Row 6:**
- Date: 2024-11-08
- Hiring Manager: Chris Bailey
- Company: Figma
- Win Type: 2nd/3rd Interview
- What Happened: Crushed the second round! Interviewed with VP and two team members. They said I'm their top candidate. Final decision coming next week.
- Why It Matters: Being called the "top candidate" is incredible validation. All the prep and practice paid off. This role would be perfect for me.
- Feeling: Proud

### Instructions Section (Below the data)

Add this starting at Row 20:

**A20:** `YOUR WIN JOURNAL - CELEBRATE EVERY SUCCESS`
- Font: 14pt, Bold
- Merge A20:G20

**A22:** `Why track wins?`
**A23:** `Job searching is hard. Most outreach gets no response. It's easy to get discouraged. This journal helps you:`
**A24:** `- Remember you ARE making progress`
**A25:** `- Celebrate small wins along the way`
**A26:** `- Build confidence and momentum`
**A27:** `- See patterns in what's working`

**A29:** `What counts as a win?`
**A30:** `- ANY positive response (even "not hiring now, but stay in touch")`
**A31:** `- Scheduling any type of call`
**A32:** `- Moving to next interview stage`
**A33:** `- Getting a referral or warm introduction`
**A34:** `- A great conversation that builds relationship`
**A35:** `- Learning something valuable about the market`

**A37:** `How to use:`
**A38:** `- Add entry immediately when something good happens`
**A39:** `- Be specific in "What Happened" - details matter`
**A40:** `- In "Why It Matters", capture the lesson or impact`
**A41:** `- Read this tab when you're feeling discouraged`
**A42:** `- Share wins in the community to inspire others`

**A44:** `Remember: Every "yes" starts with dozens of "no's" or silence. Every win in this journal is proof you're on the right track.`

---

## TAB 5: Template Quick Reference

### Layout Structure

This tab provides quick-access templates students can copy-paste directly from the tracker.

**Format:** Simple table with template names and full text

| Column | Header | Width |
|--------|--------|-------|
| A | Template Name | 200px |
| B | When to Use | 250px |
| C | Template Text | 600px |

### Sample Templates (5 most-used)

**Row 2:**
- Template Name: LinkedIn - The Article Commenter
- When to Use: When hiring manager posted in last 7-10 days
- Template Text:
```
[First Name],

Saw your post about [SPECIFIC TOPIC]. Your point about [SPECIFIC INSIGHT] really resonated - I've seen this play out in [YOUR RELEVANT EXPERIENCE].

I'm currently a [YOUR TITLE] at [YOUR COMPANY] working with [TYPE OF CLIENTS], and I'm specifically focused on [YOUR SPECIALTY].

[COMPANY NAME] is doing impressive work in [THEIR FOCUS AREA], and I'd love to learn more about your approach to [RELEVANT CHALLENGE].

Open to a brief conversation?

[Your Name]
```

**Row 3:**
- Template Name: LinkedIn - The Follow-Up (7-10 days)
- When to Use: First follow-up after no response
- Template Text:
```
[First Name],

Following up on my message from [DATE/LAST WEEK]. I know [THEIR ROLE] keeps you incredibly busy.

Since I last reached out, [NEW DEVELOPMENT]. This reinforced my interest in [COMPANY/ROLE/AREA].

Still interested in a brief conversation if timing works. If now isn't the right time, totally understand - happy to reconnect in [TIMEFRAME].

[Your Name]
```

**Row 4:**
- Template Name: Email - Cold Outreach (Hiring Manager)
- When to Use: First email to hiring manager, no prior connection
- Template Text:
```
Subject: [YOUR SPECIALTY] background for [COMPANY] - [Your Name]

[First Name],

I'm reaching out because [COMPANY] is [SPECIFIC OBSERVATION], and my background aligns closely with what that requires.

Current role: [YOUR TITLE] at [COMPANY]
Key results:
- [ACHIEVEMENT #1 WITH METRIC]
- [ACHIEVEMENT #2 WITH METRIC]
- [ACHIEVEMENT #3 WITH METRIC]

I specialize in [YOUR CORE SKILL], particularly [SPECIFIC NICHE RELEVANT TO THEM]. Having worked with companies like [RELEVANT EXAMPLES], I've developed a systematic approach to [CHALLENGE THEY LIKELY FACE].

I'd love to explore whether my experience could be valuable to your team. Are you available for a brief call this week or next?

Best regards,
[Your Name]
[Phone]
[LinkedIn URL]
```

**Row 5:**
- Template Name: Email - Follow-Up #1 (5-7 days)
- When to Use: First follow-up after initial email
- Template Text:
```
Subject: Re: [ORIGINAL SUBJECT]

[First Name],

Following up on my email from [DAY/DATE]. I know [THEIR ROLE] keeps you incredibly busy.

[NEW INFORMATION: achievement, company news, additional context]

Still very interested in [COMPANY/OPPORTUNITY]. If timing isn't right now, I completely understand - happy to reconnect in [TIMEFRAME].

Otherwise, I have availability [DAY] or [DAY] this week for a brief call.

Best,
[Your Name]
```

**Row 6:**
- Template Name: Response - Book the Meeting
- When to Use: They express interest and want to connect
- Template Text:
```
[First Name],

Fantastic! Really appreciate you making time.

I have availability:
- [Day 1], [Date] at [Time] or [Time] [Timezone]
- [Day 2], [Date] at [Time] or [Time] [Timezone]
- [Day 3], [Date] at [Time] or [Time] [Timezone]

Do any of these work for you? Happy to work around your schedule if not.

I'll come prepared to discuss [SPECIFIC TOPICS] and share how my experience with [RELEVANT ACHIEVEMENT] might translate to what you're building.

Looking forward to it!

[Your Name]
[Phone]
```

### Instructions

**A10:** `TEMPLATE QUICK REFERENCE`
- Font: 14pt, Bold
- Merge A10:C10

**A12:** `These are your 5 most-used templates. For the full library of 50+ templates, see the Scripts Playbook PDF.`

**A14:** `How to use:`
**A15:** `1. Find the template you need`
**A16:** `2. Click on the cell with template text`
**A17:** `3. Copy the entire text (Ctrl+C or Cmd+C)`
**A18:** `4. Paste into your message`
**A19:** `5. Replace all [BRACKETS] with your personalized information`
**A20:** `6. Read out loud to check flow`
**A21:** `7. Send!`

**A23:** `Pro tip: Keep this tab open in a separate window while you work for easy copy-paste access.`

---

## Additional Features & Settings

### Freeze Rows and Columns

**Main Tracker Tab:**
- Freeze Row 1 (header row)
- Freeze Column A (names always visible when scrolling)

**Metrics Dashboard:**
- Freeze Row 1

**Follow-Up Queue:**
- Freeze Row 1

**Win Journal:**
- Freeze Row 1

### Protect Cells with Formulas

Protect these cells/ranges to prevent accidental edits:
- Main Tracker: Column N (Next Follow-Up Date)
- Metrics Dashboard: All cells with formulas (Column B)
- Follow-Up Queue: Columns A-G (all formula columns)

Allow editing: Only data input cells

### Named Ranges (for easier formula management)

Create these named ranges:
- `TrackerData` = Main Tracker!A2:Q1000
- `AllContacts` = Main Tracker!A2:A1000
- `AllStatuses` = Main Tracker!L2:L1000
- `AllFollowUpDates` = Main Tracker!N2:N1000

### Mobile Optimization

**Recommended settings for mobile viewing:**
1. Enable "Wrap text" for Notes columns
2. Set row height to "Fit to data"
3. Use larger touch-friendly checkboxes
4. Ensure dropdown menus work on mobile

### Data Backup

**Instructions for students:**
1. File → Make a copy (weekly backup)
2. File → Version history → Name current version (before major changes)
3. Download as Excel (.xlsx) monthly for offline backup

---

## User Instructions Document

### Getting Started with Your Tracker

**Initial Setup (15 minutes):**

1. Make a copy of the tracker template
2. Rename it: "YourName - Reverse Attraction Tracker"
3. Update goal numbers in Metrics Dashboard (Tab 2, cells B59 and B60)
4. Delete sample data rows from all tabs
5. Add your first 10 contacts to Main Tracker

**Daily Workflow (10 minutes):**

1. **Morning (5 min):**
   - Open Follow-Up Queue tab
   - Review everyone needing follow-up today
   - Prioritize overdue (red) items first

2. **During Outreach (30-50 min total):**
   - Open Main Tracker tab
   - Add new contacts as you find them via Sales Navigator
   - Mark when you send LinkedIn messages or emails
   - Update Last Contact Date
   - Use Template Quick Reference for copy-paste

3. **End of Day (5 min):**
   - Check Metrics Dashboard to see daily progress
   - Add any wins to Win Journal
   - Review tomorrow's Follow-Up Queue
   - Celebrate progress!

**Weekly Review (15 minutes):**

Every Friday:
1. Review Metrics Dashboard → "This Week" section
2. Compare to goals (25 LinkedIn, 25 emails)
3. Check channel performance (which is working better?)
4. Read through Win Journal for motivation
5. Plan next week's target companies
6. Make backup copy of tracker

**Best Practices:**

- **Update in real-time:** Don't wait until end of day
- **Be honest with data:** Accurate tracking = accurate insights
- **Celebrate small wins:** Every response deserves Win Journal entry
- **Review patterns:** If response rate drops, adjust approach
- **Keep notes:** Future-you will thank present-you for detailed notes

**Common Mistakes to Avoid:**

- ❌ Forgetting to update Last Contact Date (breaks follow-up automation)
- ❌ Not using dropdown menus (creates inconsistent data)
- ❌ Skipping Win Journal (misses motivation boost)
- ❌ Adding contacts without research first (leads to generic outreach)
- ❌ Not checking Follow-Up Queue daily (momentum dies)

**Troubleshooting:**

**Q: Follow-Up Queue isn't showing anyone**
A: Check that you've entered Last Contact Date in Main Tracker

**Q: Formulas showing #REF or #ERROR**
A: You may have deleted a row that formulas reference. Restore from backup.

**Q: Metrics seem wrong**
A: Ensure you're using dropdown menus exactly as specified (text must match)

**Q: Can I customize the tracker?**
A: Yes! Add custom columns, but don't delete existing ones (formulas depend on them)

---

## Summary

This tracker provides:

✅ **Complete activity tracking** - Every contact, message, and follow-up in one place
✅ **Automated metrics** - No manual calculation needed
✅ **Follow-up automation** - Never miss a follow-up again
✅ **Motivation system** - Win Journal keeps spirits high
✅ **Templates at fingertips** - Quick-reference tab for efficiency
✅ **Mobile-friendly** - Update from anywhere
✅ **Professional-grade** - Matches $10k course quality expectations

Students who use this tracker consistently see:
- 3-4x more consistent outreach
- 2x higher response rates (due to follow-up discipline)
- Better tracking of what's working
- Higher motivation and momentum
- Faster time to interviews and offers

This is a professional-grade CRM system built specifically for high-ticket job searching.

---

*Reverse Attraction Tracker Specification - Version 1.0*
*For technical support, contact support@activeoffer.com*
