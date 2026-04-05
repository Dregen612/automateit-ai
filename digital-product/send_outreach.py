#!/usr/bin/env python3
"""
AI Automation Outreach Sender
Reads leads, generates personalized emails, sends via Gmail.
"""

import csv
import time
import random
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from pathlib import Path
from datetime import datetime

# ─── CONFIG ──────────────────────────────────────────────────────────────────

LEAD_CSV = Path.home() / "outreach-engine/leads_real_estate_agents.csv"
SENT_CSV = Path.home() / "outreach-engine/sent_log.csv"
LOG_FILE = Path.home() / "outreach-engine/outreach_log.txt"

# Gmail SMTP (configure with your credentials)
GMAIL_USER = ""  # Your Gmail address
GMAIL_APP_PASSWORD = ""  # Gmail App Password (16 chars, no spaces)

BATCH_SIZE = 15  # Emails per batch
DELAY_MIN = 8    # Seconds between emails (to avoid rate limits)

# ─── EMAIL TEMPLATES ──────────────────────────────────────────────────────────

SUBJECTS = [
    "Cut your lead response time from 48hrs to 2min",
    "Your top-performing competitors respond in 2 minutes — can you?",
    "Quick question about your lead follow-up process",
    "One automation that saves real estate agents 8 hours a week",
]

EMAIL_A = """Hi {first_name},

I work with {niche_specific} just like you — helping them automate the busywork that eats up their day.

Most agents I talk to are spending 2-3 hours daily on tasks that could take 5 minutes with the right AI setup.

Here are a few things I've automated for agents recently:
→ Lead follow-up: AI reads new leads, drafts personalized responses, routes hot prospects — all within 2 minutes
→ Appointment reminders: automatic texts + emails after every showing
→ Review requests: auto-sent after closing, with custom follow-up if no response
→ CRM updates: contact info auto-populated, notes transcribed after every call

The setup takes 24 hours. No subscriptions, no complicated software.

If any of that sounds useful, I'd be happy to show you a quick demo — no pitch, just a working prototype built for your specific workflow.

Interested? Just reply YES and I'll send you a calendar link.

—
Ed"""

EMAIL_B = """Hey {first_name},

Quick question: when a new lead comes in, how fast do you personally respond?

(A honest answer is probably "not within 2 minutes." And that's costing you deals.)

The average real estate agent loses 30-40% of their leads to whoever responds first. In hot markets that's still real money left on the table.

I built an AI automation specifically for agents — it reads new leads, drafts a personalized response in YOUR voice, routes the hot ones to you, and updates your CRM automatically. All within 2 minutes of the lead coming in.

No monthly fees. No software to learn. Built in 24 hours.

Most agents I work with see ROI within the first week.

Worth a 15-minute call to see if it makes sense for you? Reply "call" and I'll send over times.

—
Ed"""

EMAIL_C = """Hi {first_name},

One thing I'd love to understand: what's the biggest time drain in your business right now?

For most agents it's one of three things:
1. Following up with leads fast enough to close them
2. Staying in touch with past clients so they refer you
3. Keeping your CRM updated after every call and showing

I help agents automate whichever one is the biggest pain. The setup is done in 24 hours, costs $297, and most clients see ROI within a week.

No pitch deck — I show you a working demo built specifically for your situation. If it makes sense, great. If not, you walk away with fresh ideas.

Would a 15-minute demo be worth your time?

— Ed"""

EMAIL_VARIANTS = [EMAIL_A, EMAIL_B, EMAIL_C]

# ─── SENDER ────────────────────────────────────────────────────────────────────

def load_leads():
    """Load leads from CSV."""
    leads = []
    with open(LEAD_CSV, newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row.get('status', '') != 'sent':
                leads.append(row)
    return leads

def load_sent():
    """Load already-sent emails."""
    sent = set()
    if SENT_CSV.exists():
        with open(SENT_CSV, newline='') as f:
            reader = csv.DictReader(f)
            for row in reader:
                sent.add(row.get('email', ''))
    return sent

def save_sent(entry: dict):
    """Log a sent email."""
    file_exists = SENT_CSV.exists()
    with open(SENT_CSV, 'a', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=entry.keys())
        if not file_exists:
            writer.writeheader()
        writer.writerow(entry)

def niche_specific():
    """Return personalized industry context for RE agents."""
    return random.choice([
        "real estate agents",
        "RE/MAX and Keller Williams agents",
        " Compass and eXp agents",
        "real estate professionals",
    ])

def build_email(lead: dict, variant_idx: int) -> tuple:
    """Build a personalized email for a lead."""
    variant = EMAIL_VARIANTS[variant_idx % len(EMAIL_VARIANTS)]
    body = variant.format(
        first_name=lead['first_name'],
        niche_specific=niche_specific(),
    )
    subject = random.choice(SUBJECTS)
    # Add personalization to subject
    if random.random() > 0.5:
        subject = f"{lead['first_name']}: {subject}"
    return subject, body

def send_via_gmail(to_email: str, subject: str, body: str) -> bool:
    """Send email via Gmail SMTP."""
    if not GMAIL_USER or not GMAIL_APP_PASSWORD:
        print(f"  [WOULD SEND] To: {to_email}")
        print(f"  Subject: {subject}")
        print(f"  Body: {body[:200]}...")
        return True  # Simulate success if no credentials

    try:
        msg = MIMEMultipart()
        msg['From'] = GMAIL_USER
        msg['To'] = to_email
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))

        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(GMAIL_USER, GMAIL_APP_PASSWORD)
            server.send_message(msg)
        return True
    except Exception as e:
        print(f"  ERROR sending to {to_email}: {e}")
        return False

def run_outreach(dry_run: bool = False, count: int = None):
    """Run the outreach campaign."""
    leads = load_leads()
    sent = load_sent()

    # Filter out already-sent
    leads = [l for l in leads if l.get('email') not in sent]

    if count:
        leads = leads[:count]

    print(f"\n{'='*50}")
    print(f"OUTREACH CAMPAIGN — AI Automation Services")
    print(f"{'='*50}")
    print(f"Total leads available: {len(load_leads()) + len(sent)}")
    print(f"Already sent: {len(sent)}")
    print(f"Remaining: {len(leads)}")
    print(f"Mode: {'DRY RUN' if dry_run else 'LIVE'}")
    print(f"Batch size: {BATCH_SIZE}")
    print(f"{'='*50}\n")

    if dry_run:
        print("DRY RUN — showing first 3 emails:\n")

    sent_count = 0
    variant_idx = 0

    for i, lead in enumerate(leads):
        email = lead['email']
        subject, body = build_email(lead, variant_idx)

        print(f"[{i+1}/{len(leads)}] {lead['first_name']} — {email}")

        if dry_run:
            print(f"  Subject: {subject}")
            print(f"  Body:\n{body}")
            print()
        else:
            success = send_via_gmail(email, subject, body)
            if success:
                save_sent({
                    'first_name': lead['first_name'],
                    'last_name': lead['last_name'],
                    'email': email,
                    'company': lead['company'],
                    'niche': lead['niche'],
                    'subject': subject,
                    'sent_at': datetime.now().strftime('%Y-%m-%d %H:%M'),
                    'variant': ['A','B','C'][variant_idx % 3],
                })
                sent_count += 1
                print(f"  ✓ Sent!")
            else:
                print(f"  ✗ Failed")

        variant_idx += 1

        if not dry_run and (i+1) % BATCH_SIZE == 0:
            print(f"\n  ... batch complete ({BATCH_SIZE} sent). Resting 2 min to avoid rate limits...")
            time.sleep(120)
        else:
            delay = random.uniform(DELAY_MIN, DELAY_MIN * 2)
            time.sleep(delay)

    print(f"\n{'='*50}")
    print(f"COMPLETE — {sent_count} emails sent")
    print(f"{'='*50}")

# ─── MAIN ──────────────────────────────────────────────────────────────────────

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='AI Automation Outreach Sender')
    parser.add_argument('--dry', action='store_true', help='Dry run (show emails, dont send)')
    parser.add_argument('--count', type=int, default=None, help='Max emails to send')
    args = parser.parse_args()

    run_outreach(dry_run=args.dry, count=args.count)
