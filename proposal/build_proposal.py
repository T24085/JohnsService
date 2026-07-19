from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT, TA_CENTER
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import (
    BaseDocTemplate,
    Frame,
    PageTemplate,
    Paragraph,
    PageBreak,
    Spacer,
    Image,
    Table,
    TableStyle,
    KeepTogether,
)
from reportlab.lib.utils import ImageReader


ROOT = Path(__file__).resolve().parents[1]
SCREENSHOTS = ROOT / "output" / "screenshots"
PDF_PATH = ROOT / "output" / "pdf" / "johns-service-website-proposal.pdf"
PDF_PATH.parent.mkdir(parents=True, exist_ok=True)

NAVY = colors.HexColor("#07131E")
BLUE = colors.HexColor("#1455A0")
PALE_BLUE = colors.HexColor("#DDEBFA")
YELLOW = colors.HexColor("#F4C84A")
PAPER = colors.HexColor("#F4F1EA")
INK = colors.HexColor("#1B2631")
MUTED = colors.HexColor("#63707C")
RULE = colors.HexColor("#D7D3C9")
WHITE = colors.white


def styles():
    base = getSampleStyleSheet()
    return {
        "kicker": ParagraphStyle(
            "Kicker", parent=base["Normal"], fontName="Helvetica-Bold", fontSize=8,
            leading=10, textColor=YELLOW, tracking=1.2, spaceAfter=8,
        ),
        "cover_title": ParagraphStyle(
            "CoverTitle", parent=base["Title"], fontName="Helvetica-Bold", fontSize=31,
            leading=31, textColor=WHITE, alignment=TA_LEFT, spaceAfter=10,
        ),
        "cover_subtitle": ParagraphStyle(
            "CoverSubtitle", parent=base["Normal"], fontName="Helvetica", fontSize=12,
            leading=17, textColor=PALE_BLUE, spaceAfter=15,
        ),
        "h1": ParagraphStyle(
            "H1", parent=base["Heading1"], fontName="Helvetica-Bold", fontSize=24,
            leading=26, textColor=NAVY, spaceAfter=8,
        ),
        "h2": ParagraphStyle(
            "H2", parent=base["Heading2"], fontName="Helvetica-Bold", fontSize=13,
            leading=16, textColor=NAVY, spaceBefore=5, spaceAfter=5,
        ),
        "body": ParagraphStyle(
            "Body", parent=base["BodyText"], fontName="Helvetica", fontSize=9.8,
            leading=14, textColor=INK, spaceAfter=7,
        ),
        "small": ParagraphStyle(
            "Small", parent=base["BodyText"], fontName="Helvetica", fontSize=8,
            leading=11, textColor=MUTED,
        ),
        "small_white": ParagraphStyle(
            "SmallWhite", parent=base["BodyText"], fontName="Helvetica", fontSize=8.4,
            leading=11.5, textColor=PALE_BLUE,
        ),
        "caption": ParagraphStyle(
            "Caption", parent=base["BodyText"], fontName="Helvetica-Bold", fontSize=8.3,
            leading=11, textColor=NAVY, spaceBefore=5,
        ),
        "price": ParagraphStyle(
            "Price", parent=base["BodyText"], fontName="Helvetica-Bold", fontSize=21,
            leading=24, textColor=NAVY,
        ),
        "price_label": ParagraphStyle(
            "PriceLabel", parent=base["BodyText"], fontName="Helvetica-Bold", fontSize=9,
            leading=12, textColor=BLUE,
        ),
        "center_small": ParagraphStyle(
            "CenterSmall", parent=base["BodyText"], fontName="Helvetica", fontSize=8.4,
            leading=11, textColor=MUTED, alignment=TA_CENTER,
        ),
    }


S = styles()


def screenshot(name, max_width, max_height):
    path = SCREENSHOTS / name
    iw, ih = ImageReader(str(path)).getSize()
    scale = min(max_width / iw, max_height / ih)
    image = Image(str(path), width=iw * scale, height=ih * scale)
    image.hAlign = "CENTER"
    return image


def rule(width=7.2 * inch, color=RULE):
    table = Table([[""]], colWidths=[width], rowHeights=[1])
    table.setStyle(TableStyle([("BACKGROUND", (0, 0), (-1, -1), color)]))
    return table


def bullet(text):
    return Paragraph(f"<font color='#1455A0'><b>+</b></font>&nbsp;&nbsp;{text}", S["body"])


def section_title(number, title, subtitle):
    return [
        Paragraph(number, S["kicker"]),
        Paragraph(title, S["h1"]),
        Paragraph(subtitle, S["body"]),
        Spacer(1, 5),
        rule(),
        Spacer(1, 15),
    ]


def page_background(canvas, doc, first=False):
    canvas.saveState()
    if first:
        canvas.setFillColor(NAVY)
        canvas.rect(0, 0, letter[0], letter[1], fill=1, stroke=0)
        canvas.setFillColor(YELLOW)
        canvas.rect(0.65 * inch, 0.44 * inch, 0.42 * inch, 0.06 * inch, fill=1, stroke=0)
        canvas.setFillColor(PALE_BLUE)
        canvas.setFont("Helvetica", 7.5)
        canvas.drawRightString(letter[0] - 0.65 * inch, 0.46 * inch, "JOHN'S SERVICE | ABILENE, KS")
    else:
        canvas.setFillColor(PAPER)
        canvas.rect(0, 0, letter[0], letter[1], fill=1, stroke=0)
        canvas.setStrokeColor(RULE)
        canvas.setLineWidth(0.6)
        canvas.line(0.65 * inch, letter[1] - 0.45 * inch, letter[0] - 0.65 * inch, letter[1] - 0.45 * inch)
        canvas.setFillColor(BLUE)
        canvas.setFont("Helvetica-Bold", 7.5)
        canvas.drawString(0.65 * inch, letter[1] - 0.32 * inch, "JOHN'S SERVICE WEBSITE PROPOSAL")
        canvas.setFillColor(MUTED)
        canvas.setFont("Helvetica", 7.5)
        canvas.drawRightString(letter[0] - 0.65 * inch, 0.35 * inch, f"{doc.page - 1:02d}")
        canvas.line(0.65 * inch, 0.49 * inch, letter[0] - 0.65 * inch, 0.49 * inch)
    canvas.restoreState()


def build():
    frame = Frame(0.65 * inch, 0.65 * inch, 7.2 * inch, 9.9 * inch, id="normal")
    doc = BaseDocTemplate(
        str(PDF_PATH), pagesize=letter, leftMargin=0.65 * inch, rightMargin=0.65 * inch,
        topMargin=0.65 * inch, bottomMargin=0.65 * inch, title="John's Service Website Proposal",
        author="Local Abilene Web Developer",
    )
    doc.addPageTemplates([
        PageTemplate(id="all", frames=frame, onPage=lambda c, d: page_background(c, d, c.getPageNumber() == 1)),
    ])

    story = []

    # Cover
    story.append(Spacer(1, 0.28 * inch))
    story.append(Paragraph("WEBSITE PROPOSAL", S["kicker"]))
    story.append(Paragraph("A better roadside<br/><font color='#F4C84A'>first impression.</font>", S["cover_title"]))
    story.append(Paragraph("A focused, mobile-first website concept for John's Service - built around fast calls, capable equipment, and local trust in Abilene.", S["cover_subtitle"]))
    story.append(screenshot("01-hero.png", 7.2 * inch, 4.55 * inch))
    story.append(Spacer(1, 0.12 * inch))
    story.append(Table([
        [Paragraph("PREPARED FOR", S["kicker"]), Paragraph("INVESTMENT", S["kicker"]), Paragraph("LOCATION", S["kicker"])],
        [Paragraph("John's Service", S["small_white"]), Paragraph("$500 one-time build", S["small_white"]), Paragraph("Abilene, Kansas", S["small_white"])],
    ], colWidths=[2.4 * inch, 2.4 * inch, 2.4 * inch], style=TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 0),
        ("RIGHTPADDING", (0, 0), (-1, -1), 10),
        ("TOPPADDING", (0, 0), (-1, -1), 0),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 2),
    ])))
    story.append(PageBreak())

    # Overview and pricing
    story.extend(section_title("01 / THE OPPORTUNITY", "Turn a missed call into a clear next step.", "When someone needs a tow, recovery, or roadside help, the website should make the decision simple: see capability, trust the team, and call now."))
    overview = Table([
        [Paragraph("THE OUTREACH ANGLE", S["price_label"]), Paragraph("THE SITE DIRECTION", S["price_label"])],
        [Paragraph("Your current web presence appeared unavailable when checked. This concept gives John's Service a working, professional home base that can be shared from Facebook, Google, and every truck in the fleet.", S["body"]), Paragraph("A confident blue-and-yellow system, strong equipment photography, clear service categories, and a persistent click-to-call path for phones and desktops.", S["body"])],
    ], colWidths=[3.48 * inch, 3.48 * inch])
    overview.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), colors.white),
        ("BOX", (0, 0), (-1, -1), 0.8, RULE),
        ("INNERGRID", (0, 0), (-1, -1), 0.5, RULE),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 13),
        ("RIGHTPADDING", (0, 0), (-1, -1), 13),
        ("TOPPADDING", (0, 0), (-1, -1), 12),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 10),
    ]))
    story.append(overview)
    story.append(Spacer(1, 18))
    story.append(Paragraph("WHAT IS INCLUDED", S["h2"]))
    included = [
        "Custom responsive one-page website with mobile navigation and call-first layout.",
        "Service sections for light-duty towing, heavy-duty recovery, roadside help, lockouts, and auto repair.",
        "Fleet and equipment gallery using the provided John's Service photography.",
        "Google map location section for 425 N Buckeye Ave, Abilene, KS 67410.",
        "Contact area with phone CTA, Facebook link, and request-a-call form layout.",
        "Motion details across sections so the page feels active without getting in the way of urgent calls.",
    ]
    for item in included:
        story.append(bullet(item))
    story.append(Spacer(1, 5))
    pricing = Table([
        [Paragraph("WEBSITE BUILD", S["price_label"]), Paragraph("CONTINUED SUPPORT", S["price_label"]), Paragraph("WHAT HAPPENS NEXT", S["price_label"])],
        [Paragraph("$500", S["price"]), Paragraph("$85/month", S["price"]), Paragraph("Approve the concept, confirm launch details, and connect the final domain and inbox.", S["body"])],
        [Paragraph("One-time project fee for the site build and launch-ready front end.", S["small"]), Paragraph("Optional monthly maintenance for continued support, small content updates, and keeping the site cared for after launch.", S["small"]), Paragraph("Third-party domain, hosting, booking, or payment services can be added separately if needed.", S["small"])],
    ], colWidths=[2.32 * inch, 2.32 * inch, 2.32 * inch])
    pricing.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), PALE_BLUE),
        ("BOX", (0, 0), (-1, -1), 0.8, BLUE),
        ("INNERGRID", (0, 0), (-1, -1), 0.5, colors.white),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 12),
        ("RIGHTPADDING", (0, 0), (-1, -1), 12),
        ("TOPPADDING", (0, 0), (-1, -1), 11),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 10),
    ]))
    story.append(pricing)
    story.append(PageBreak())

    # Hero screenshot
    story.extend(section_title("02 / FIRST IMPRESSION", "A clear call when the road stops.", "The opening screen puts John's Service, the phone number, and the full range of capability in front of a customer immediately."))
    story.append(screenshot("01-hero.png", 7.2 * inch, 5.5 * inch))
    story.append(Paragraph("HERO / The first screen establishes trust quickly with a direct headline, click-to-call CTA, and real fleet photography.", S["caption"]))
    story.append(Spacer(1, 12))
    story.append(Paragraph("Designed to work as the link behind a Facebook post, a Google Business profile, or the phone number printed on the trucks.", S["body"]))
    story.append(PageBreak())

    # Services + fleet
    story.extend(section_title("03 / CAPABILITY", "Make the hard jobs easy to understand.", "Customers can scan the services, see the equipment behind the promise, and recognize that one number covers both everyday roadside calls and serious recovery work."))
    service_fleet = Table([
        [screenshot("02-services.png", 3.38 * inch, 3.05 * inch), screenshot("03-fleet.png", 3.38 * inch, 3.05 * inch)],
        [Paragraph("SERVICES / A structured service index for towing, recovery, lockouts, roadside support, and auto repair.", S["caption"]), Paragraph("FLEET / Real trucks and equipment give the site local proof instead of generic stock imagery.", S["caption"])],
    ], colWidths=[3.52 * inch, 3.52 * inch])
    service_fleet.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 0),
        ("RIGHTPADDING", (0, 0), (-1, -1), 10),
        ("TOPPADDING", (0, 0), (-1, -1), 0),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 12),
    ]))
    story.append(service_fleet)
    story.append(Spacer(1, 4))
    story.append(Paragraph("The visual language is intentionally sturdy and local: navy for confidence, yellow for the action moment, and blue equipment photography that makes the work feel tangible.", S["body"]))
    story.append(PageBreak())

    # Location + contact
    story.extend(section_title("04 / CONVERSION", "Put the next move within reach.", "A location map helps local customers orient themselves, while the final contact section makes the urgent action unmistakable on every screen size."))
    location_contact = Table([
        [screenshot("04-location.png", 3.38 * inch, 3.05 * inch), screenshot("05-contact.png", 3.38 * inch, 3.05 * inch)],
        [Paragraph("LOCATION / Google map context for 425 N Buckeye Ave, Abilene, KS 67410.", S["caption"]), Paragraph("CONTACT / Large phone CTA plus a simple request-a-call path for customers who are not ready to dial.", S["caption"])],
    ], colWidths=[3.52 * inch, 3.52 * inch])
    location_contact.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 0),
        ("RIGHTPADDING", (0, 0), (-1, -1), 10),
        ("TOPPADDING", (0, 0), (-1, -1), 0),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 12),
    ]))
    story.append(location_contact)
    story.append(Spacer(1, 8))
    story.append(rule())
    story.append(Spacer(1, 13))
    story.append(Paragraph("THE RESULT", S["kicker"]))
    story.append(Paragraph("A simple digital front door for a team that already does the difficult part: showing up and getting people moving again.", S["h2"]))
    story.append(PageBreak())

    # Next steps and message
    story.extend(section_title("05 / NEXT STEP", "Ready to send from Facebook.", "This is written to feel like a local introduction, not a mass sales pitch. Attach this packet and let the work speak for itself."))
    message = Table([[Paragraph(
        "Hey guys - I'm a local Abilene web developer and I came across John's Service. I noticed your current website does not seem to be working, so I put together a new website concept using your trucks, services, and Abilene location.<br/><br/>I would be happy to build it for $500. If you want continued help after launch, I also offer optional maintenance and support for $85/month.<br/><br/>I put together a short proposal with screenshots so you can see what I had in mind. No pressure at all - I just thought a stronger website could make it easier for people who need towing or recovery to call you quickly. Would you like me to send it over?",
        S["body"],
    )]], colWidths=[7.0 * inch])
    message.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), colors.white),
        ("BOX", (0, 0), (-1, -1), 1, BLUE),
        ("LEFTPADDING", (0, 0), (-1, -1), 18),
        ("RIGHTPADDING", (0, 0), (-1, -1), 18),
        ("TOPPADDING", (0, 0), (-1, -1), 17),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 10),
    ]))
    story.append(message)
    story.append(Spacer(1, 17))
    story.append(Paragraph("THE SIMPLE CLOSE", S["kicker"]))
    close = Table([
        [Paragraph("1", S["price"]), Paragraph("Confirm the $500 site build and any details that need changing.", S["body"])],
        [Paragraph("2", S["price"]), Paragraph("Approve the final photos, phone number, service wording, and form destination.", S["body"])],
        [Paragraph("3", S["price"]), Paragraph("Launch the site and decide whether the optional $85/month support plan is useful after handoff.", S["body"])],
    ], colWidths=[0.45 * inch, 6.55 * inch])
    close.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LINEBELOW", (0, 0), (-1, -2), 0.5, RULE),
        ("LEFTPADDING", (0, 0), (-1, -1), 0),
        ("RIGHTPADDING", (0, 0), (-1, -1), 12),
        ("TOPPADDING", (0, 0), (-1, -1), 7),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 7),
    ]))
    story.append(close)
    story.append(Spacer(1, 17))
    story.append(Paragraph("Prepared July 19, 2026 | John's Service | Abilene, Kansas", S["small"]))

    doc.build(story)


if __name__ == "__main__":
    build()
    print(PDF_PATH)
