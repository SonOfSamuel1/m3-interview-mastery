#!/usr/bin/env python3
"""
Generate Self-Assessment Worksheet PDF
"""

from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT

def create_self_assessment_pdf():
    """Create the Self-Assessment Worksheet PDF"""
    output_path = "/Users/terrancebrandon/Desktop/Active Offer/AO- Course Content/Active Offer- Course Material/External Assets/Self-Assessment-Worksheet.pdf"

    # Create PDF
    doc = SimpleDocTemplate(output_path, pagesize=letter,
                            rightMargin=0.75*inch, leftMargin=0.75*inch,
                            topMargin=0.75*inch, bottomMargin=0.75*inch)

    # Container for PDF elements
    story = []

    # Styles
    styles = getSampleStyleSheet()

    # Custom styles
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=20,
        textColor=colors.HexColor('#1a1a1a'),
        spaceAfter=12,
        alignment=TA_CENTER,
        fontName='Helvetica-Bold'
    )

    subtitle_style = ParagraphStyle(
        'CustomSubtitle',
        parent=styles['Normal'],
        fontSize=11,
        textColor=colors.HexColor('#555555'),
        spaceAfter=20,
        alignment=TA_CENTER,
        fontName='Helvetica-Oblique'
    )

    section_heading_style = ParagraphStyle(
        'SectionHeading',
        parent=styles['Heading2'],
        fontSize=14,
        textColor=colors.HexColor('#1a1a1a'),
        spaceAfter=10,
        spaceBefore=15,
        fontName='Helvetica-Bold'
    )

    question_style = ParagraphStyle(
        'Question',
        parent=styles['Normal'],
        fontSize=11,
        textColor=colors.HexColor('#1a1a1a'),
        spaceAfter=6,
        fontName='Helvetica-Bold',
        leftIndent=0.2*inch
    )

    answer_style = ParagraphStyle(
        'Answer',
        parent=styles['Normal'],
        fontSize=10,
        textColor=colors.HexColor('#333333'),
        spaceAfter=4,
        leftIndent=0.4*inch,
        fontName='Helvetica'
    )

    # Title and Introduction
    story.append(Paragraph("SELF-ASSESSMENT WORKSHEET", title_style))
    story.append(Paragraph("M1: Profile Matching | Active Offer Career Program", subtitle_style))
    story.append(Spacer(1, 0.2*inch))

    intro_text = """This self-assessment will help you identify your optimal company profile match based on your current
    situation, goals, and constraints. Answer each question honestly—there are no "right" answers, only honest self-reflection
    that will guide you to the company types where you're most likely to succeed and be satisfied."""
    story.append(Paragraph(intro_text, styles['Normal']))
    story.append(Spacer(1, 0.3*inch))

    # Question 1
    story.append(Paragraph("QUESTION 1: SaaS Sales Experience", section_heading_style))
    story.append(Paragraph("How many years of SaaS sales experience do you have?", question_style))
    story.append(Paragraph("☐ 0-1 years (Career switcher or new to SaaS) = 1 point", answer_style))
    story.append(Paragraph("☐ 1-3 years (Building foundational skills) = 2 points", answer_style))
    story.append(Paragraph("☐ 3-7 years (Experienced mid-career professional) = 3 points", answer_style))
    story.append(Paragraph("☐ 7+ years (Senior/veteran sales professional) = 4 points", answer_style))
    story.append(Paragraph("Your Score: _____", answer_style))
    story.append(Spacer(1, 0.2*inch))

    # Question 2
    story.append(Paragraph("QUESTION 2: Financial Obligations", section_heading_style))
    story.append(Paragraph("What is your current financial situation?", question_style))
    story.append(Paragraph("☐ Significant obligations (mortgage, dependents, debt) requiring stable income = 1 point", answer_style))
    story.append(Paragraph("☐ Moderate obligations (rent, some savings, manageable expenses) = 2 points", answer_style))
    story.append(Paragraph("☐ Minimal obligations (low expenses, single, no major financial commitments) = 3 points", answer_style))
    story.append(Paragraph("☐ Financially independent (significant savings, no obligations) = 4 points", answer_style))
    story.append(Paragraph("Your Score: _____", answer_style))
    story.append(Spacer(1, 0.2*inch))

    # Question 3
    story.append(Paragraph("QUESTION 3: Financial Runway", section_heading_style))
    story.append(Paragraph("How many months of expenses do you have saved?", question_style))
    story.append(Paragraph("☐ Less than 3 months (immediate income needs) = 1 point", answer_style))
    story.append(Paragraph("☐ 3-6 months (some cushion) = 2 points", answer_style))
    story.append(Paragraph("☐ 6-12 months (comfortable cushion) = 3 points", answer_style))
    story.append(Paragraph("☐ 12-18+ months (significant financial runway) = 4 points", answer_style))
    story.append(Paragraph("Your Score: _____", answer_style))
    story.append(Spacer(1, 0.2*inch))

    # Question 4
    story.append(Paragraph("QUESTION 4: Primary Career Goal", section_heading_style))
    story.append(Paragraph("What is your top priority right now?", question_style))
    story.append(Paragraph("☐ Maximize current cash earnings and income stability = 1 point", answer_style))
    story.append(Paragraph("☐ Build enterprise sales skills and resume credibility = 2 points", answer_style))
    story.append(Paragraph("☐ Balance current income with equity upside potential = 3 points", answer_style))
    story.append(Paragraph("☐ Pursue maximum equity upside and wealth creation = 4 points", answer_style))
    story.append(Paragraph("Your Score: _____", answer_style))
    story.append(Spacer(1, 0.2*inch))

    # Question 5
    story.append(Paragraph("QUESTION 5: Work Environment Preference", section_heading_style))
    story.append(Paragraph("Which work environment helps you perform best?", question_style))
    story.append(Paragraph("☐ Highly structured (clear processes, training, mentorship, defined roles) = 1 point", answer_style))
    story.append(Paragraph("☐ Moderately structured (some process, growing organization) = 2 points", answer_style))
    story.append(Paragraph("☐ Flexible/evolving (adapting processes, self-direction required) = 3 points", answer_style))
    story.append(Paragraph("☐ High autonomy (ambiguity, wearing multiple hats, defining your own role) = 4 points", answer_style))
    story.append(Paragraph("Your Score: _____", answer_style))
    story.append(Spacer(1, 0.2*inch))

    # Question 6
    story.append(Paragraph("QUESTION 6: Learning Style", section_heading_style))
    story.append(Paragraph("How do you learn and develop skills most effectively?", question_style))
    story.append(Paragraph("☐ Structured training programs and proven methodologies = 1 point", answer_style))
    story.append(Paragraph("☐ Combination of training and hands-on experience = 2 points", answer_style))
    story.append(Paragraph("☐ Hands-on experience with some mentorship = 3 points", answer_style))
    story.append(Paragraph("☐ Trial-and-error, rapid iteration, figuring it out myself = 4 points", answer_style))
    story.append(Paragraph("Your Score: _____", answer_style))
    story.append(Spacer(1, 0.2*inch))

    # Question 7
    story.append(Paragraph("QUESTION 7: Risk Tolerance", section_heading_style))
    story.append(Paragraph("How comfortable are you with career and income uncertainty?", question_style))
    story.append(Paragraph("☐ Very low tolerance (need predictable income, avoid uncertainty) = 1 point", answer_style))
    story.append(Paragraph("☐ Low-moderate tolerance (some risk acceptable with safeguards) = 2 points", answer_style))
    story.append(Paragraph("☐ Moderate-high tolerance (can handle uncertainty for upside) = 3 points", answer_style))
    story.append(Paragraph("☐ High tolerance (embrace risk for potential big outcomes) = 4 points", answer_style))
    story.append(Paragraph("Your Score: _____", answer_style))
    story.append(Spacer(1, 0.2*inch))

    # Question 8
    story.append(Paragraph("QUESTION 8: Work-Life Balance Priority", section_heading_style))
    story.append(Paragraph("How important is work-life balance to you right now?", question_style))
    story.append(Paragraph("☐ Critical (family, health, personal commitments require boundaries) = 1 point", answer_style))
    story.append(Paragraph("☐ Important (prefer 40-50 hour weeks, reasonable travel) = 2 points", answer_style))
    story.append(Paragraph("☐ Somewhat important (willing to work 50-60 hours for growth) = 3 points", answer_style))
    story.append(Paragraph("☐ Not a priority (willing to work 60-70+ hours for career advancement) = 4 points", answer_style))
    story.append(Paragraph("Your Score: _____", answer_style))

    # Add page break for scoring section
    story.append(PageBreak())

    # Scoring Section
    story.append(Paragraph("SCORING YOUR ASSESSMENT", title_style))
    story.append(Spacer(1, 0.2*inch))

    story.append(Paragraph("Add up your total points from all 8 questions:", styles['Normal']))
    story.append(Spacer(1, 0.1*inch))
    story.append(Paragraph("TOTAL SCORE: _____ / 32", question_style))
    story.append(Spacer(1, 0.3*inch))

    # Score interpretation
    story.append(Paragraph("INTERPRETING YOUR SCORE", section_heading_style))

    interpretation_data = [
        ['Score Range', 'Recommended Profile', 'Why This Match'],
        ['8-14 points', 'ENTERPRISE LEADERS', 'You prioritize income stability, structured environment, work-life balance, '
                                             'and predictable earnings. Enterprise Leaders offer the lowest risk, highest cash '
                                             'compensation, comprehensive training, and work-life balance you need.'],
        ['15-21 points', 'GROWTH CHAMPIONS', 'You have some experience, moderate financial cushion, and want to balance '
                                            'current income with equity upside. Growth Champions offer competitive cash '
                                            'compensation with meaningful equity potential and faster career progression.'],
        ['22-28 points', 'GROWTH CHAMPIONS\n(Aggressive)', 'You have experience, financial runway, high risk tolerance, and strong '
                                                          'equity focus. You can target earlier-stage Growth Champions (Series B/C) '
                                                          'with higher equity grants for maximum upside while maintaining reasonable income.'],
        ['29-32 points', 'VENTURE-BACKED\nSTARTUPS', 'You have significant financial runway, high risk tolerance, thrive in '
                                                     'ambiguity, and prioritize learning velocity and equity upside over cash. '
                                                     'You\'re well-suited for Venture-Backed Startups, but remember 70-80% fail—only '
                                                     'pursue if you can afford the risk.']
    ]

    # Create table
    table = Table(interpretation_data, colWidths=[1.2*inch, 1.5*inch, 4*inch])
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#366092')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 10),
        ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 1), (-1, -1), 9),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('TOPPADDING', (0, 1), (-1, -1), 8),
        ('BOTTOMPADDING', (0, 1), (-1, -1), 8),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor('#f5f5f5')])
    ]))

    story.append(table)
    story.append(Spacer(1, 0.3*inch))

    # Next Steps
    story.append(Paragraph("NEXT STEPS", section_heading_style))

    next_steps = """Based on your recommended profile match, proceed to the company list examples in the module
    that align with your profile. Use the Target Company List Template (Excel) to build your personalized list
    of 20-30 target companies. Then use the Company Evaluation Scorecard to systematically evaluate and compare
    your top candidates before beginning your targeted outreach strategy."""

    story.append(Paragraph(next_steps, styles['Normal']))
    story.append(Spacer(1, 0.2*inch))

    important_note = """<b>Important Note:</b> This assessment is a guide, not a rule. Your situation is unique,
    and you may choose to target a different profile based on specific opportunities, personal circumstances, or
    strategic career considerations. Use this as a starting point for informed decision-making."""

    story.append(Paragraph(important_note, styles['Normal']))

    # Build PDF
    doc.build(story)
    print(f"✓ Saved Self-Assessment Worksheet: {output_path}")

def main():
    print("=" * 60)
    print("Generating Self-Assessment Worksheet PDF")
    print("=" * 60)
    print()

    create_self_assessment_pdf()

    print()
    print("✓ Self-Assessment Worksheet generated successfully!")

if __name__ == "__main__":
    main()
