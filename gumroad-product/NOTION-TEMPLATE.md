# AUTOMATEIT AUTOMATION HUB — NOTION TEMPLATE
## Your Complete Business Automation Workspace

---

## HOW TO IMPORT THIS TEMPLATE

1. Go to **notion.so** and create a free account
2. Open: `https://www.notion.so/[COPY-FROM-LINK-when-shared]`
3. Click **Duplicate** to add to your workspace
4. Rename to "[Your Business] Automation Hub"

---

## DATABASE 1: Automation Pipeline

### Properties
| Field | Type | Description |
|-------|------|-------------|
| Name | Title | Automation name |
| Status | Select | Idea / Building / Testing / Live / Paused / Archived |
| Category | Multi-select | Lead / Email / Content / Support / Scheduling / CRM / Other |
| Pain Point | Text | What problem does this solve? |
| Est. Hours Saved/Week | Number | Estimated weekly hours recovered |
| Actual Hours Saved/Week | Number | Real hours saved (after 2 weeks) |
| Tools Used | Multi-select | ChatGPT / Claude / Make / Zapier / Other |
| Prompt/Tool Link | URL | Link to the prompt or automation setup |
| Complexity | Select | Simple (5min) / Medium (30min) / Complex (2hr) |
| Date Added | Date | When you created this |
| Date Live | Date | When it went live |
| Revenue Impact | Select | Low / Medium / High |
| Notes | Text | Any important context |

### Views
- **Board** by Status (kanban)
- **Table** by Category
- **Calendar** by Date Live
- **Gallery** by Category (card view)

### Suggested Starting Automations (fill these in):
1. Lead Response Automation — Category: Lead — Pain: "Losing leads who go unanswered" — Est: 3 hrs/week
2. Email Triage — Category: Email — Pain: "Drowning in inbox" — Est: 2 hrs/week
3. Social Content Queue — Category: Content — Pain: "Can't keep up with posting" — Est: 2 hrs/week
4. Appointment Reminders — Category: Scheduling — Pain: "Clients missing appointments" — Est: 1 hr/week
5. CRM Auto-Updates — Category: CRM — Pain: "CRM is always out of date" — Est: 1 hr/week

---

## DATABASE 2: Lead Tracker

### Properties
| Field | Type | Description |
|-------|------|-------------|
| Name | Title | Lead name |
| Company | Text | Their business |
| Source | Select | Website / LinkedIn / Referral / Cold Email / Podcast / Other |
| Status | Select | New / Contacted / Qualified / Demo Scheduled / Proposal Sent / Customer / Lost |
| Score | Number | 1-10 hotness |
| Email | Email | Contact email |
| Phone | Phone | Contact phone |
| Budget | Select | <$500 / $500-1K / $1K-5K / $5K+ / Unknown |
| Timeline | Select | Immediate / 1-3 months / 3-6 months / Exploratory |
| Pain Point | Text | What they want to automate |
| Assigned To | Person | Who owns this lead |
| Last Contact | Date | Last time touched |
| Next Action | Text | What to do next |
| Next Action Date | Date | When to do it |
| Notes | Text | Call notes, context |

### Views
- **Board** by Status
- **Table** sorted by Score (highest first)
- **Calendar** by Next Action Date

---

## DATABASE 3: Content Queue

### Properties
| Field | Type | Description |
|-------|------|-------------|
| Title | Title | Content piece name |
| Platform | Multi-select | LinkedIn / Twitter / Instagram / Email / YouTube / Blog |
| Status | Select | Idea / Drafting / In Review / Scheduled / Published |
| Type | Select | Post / Thread / Newsletter / Video / Carousel |
| Week | Text | e.g., "Week of April 7" |
| Topic | Text | What it's about |
| Primary CTA | Text | What action we want |
| Publish Date | Date | When to publish |
| Hook | Text | The opening line |
| Link | URL | Link to published content |
| Performance | Select | Low / Medium / High / N/A |
| Notes | Text | What worked / what didn't |

### Views
- **Board** by Status
- **Calendar** by Publish Date
- **Gallery** by Platform

---

## DATABASE 4: Task Automations (Daily/Weekly)

### Properties
| Field | Type | Description |
|-------|------|-------------|
| Task Name | Title | What to do |
| Frequency | Select | Daily / Weekly / Monthly / As Needed |
| Trigger | Text | What makes this run |
| AI Prompt | Text | The prompt to use |
| Tool | Select | ChatGPT / Claude / Other |
| Time to Complete | Text | e.g., "5 minutes" |
| Last Run | Date | When last executed |
| Run Count | Number | How many times run |
| Effectiveness | Select | High / Medium / Low / Untested |
| Notes | Text | Results, improvements |

### Suggested Daily Tasks:
1. Morning Inbox Triage — Frequency: Daily — Time: 2 min — Prompt: [See Email section]
2. Lead Response Drafting — Frequency: As Needed — Time: 1 min/lead — Trigger: New lead arrives
3. Social Post Generation — Frequency: Weekly — Time: 10 min — Prompt: [See Content section]
4. Meeting Notes → CRM — Frequency: As Needed — Time: 2 min/call — Trigger: After every call

### Suggested Weekly Tasks:
1. Pipeline Review — Day: Monday — Time: 15 min
2. Content Queue Planning — Day: Sunday — Time: 10 min
3. Inbox Zero Check — Day: Friday — Time: 20 min
4. CRM Data Clean — Day: 1st of month — Time: 30 min

---

## DATABASE 5: Metrics Dashboard

### Properties
| Field | Type | Description |
|-------|------|-------------|
| Week Of | Title | e.g., "Week of April 7" |
| Leads Generated | Number | New leads this week |
| Demo Calls Booked | Number | Calls scheduled |
| Demos Completed | Number | Calls that happened |
| Customers Closed | Number | New paying customers |
| Revenue | Number | $ brought in |
| Hours Saved (Actual) | Number | Real hours saved this week |
| Top Automation | Text | What saved the most time |
| Top Lead Source | Text | Where best leads came from |
| Notes | Text | Anything worth remembering |

### Views
- **Table** with totals row
- **Timeline** by Week Of

---

## WIDGET SETUP: Dashboard Home Page

Set this as your homepage. Create a new page with these blocks:

```
[HEADER: Your Business Automation Hub]

[QUICK STATS — 3 columns:]
- Hours Saved This Week: [LINK to Metrics DB this week]
- Active Automations: [LINK to Automation Pipeline — Live count]
- Leads This Week: [LINK to Lead Tracker — this week's count]

[WEEKLY FOCUS — Text block:]
This week, focus on:
1. [ automation name ]
2. [ automation name ]
3. [ automation name ]

[UPCOMING — Calendar or list view:]
- [Next 3 tasks from Task Automations DB]

[RECENT LEADS — Table view:]
[Lead Tracker DB — last 5 entries]

[CONTENT QUEUE — Board view:]
[Content Queue DB — this week's content]
```

---

## AUTOMATION SCRIPTS

### Script 1: Morning Inbox Triage (ChatGPT)
```
Every morning, paste into ChatGPT:

"Triage my inbox. Categorize each email:
🔴 URGENT — respond today
📅 TODAY — handle today  
📆 THIS WEEK — respond when you can
📬 ARCHIVE — no action needed

For each email: [Subject] — Action: [what, if any]

Top 3 priorities: [list with why]
Scams to flag: [list if any]

---

[PASTE EMAILS]"
```

### Script 2: Lead Response (ChatGPT)
```
When a new lead arrives:

"You are a sales assistant for [YOUR BUSINESS]. New lead:
- Name: [NAME]
- Source: [WHERE]
- Interest: [WHAT THEY WANT]

Write 3 email options — [YOUR VOICE: professional, warm, direct]. Under 100 words each. Option A / B / C."
```

### Script 3: Social Content Sprint (ChatGPT)
```
Weekly content generation:

"I'm a [YOUR ROLE]. Topic this week: [TOPIC].
Generate 7 posts — one for each day.
LinkedIn: 150-300 words, ends with a question.
Twitter: under 280 chars, hook + value + question.

Format:
DAY 1 - LinkedIn: Hook | Post
DAY 1 - Twitter: Hook | Post"
```

---

## USAGE GUIDE

### Week 1: Set Up (30 min)
1. Duplicate this template
2. Fill in your business info
3. Add your first 3 automations to the pipeline
4. Set up the 3 daily tasks
5. Run Morning Triage for the first time

### Week 2: Run (30 min/day)
1. Run Morning Triage every day
2. Add leads as they come in
3. Generate your first week's content
4. Track hours saved

### Week 3: Optimize (30 min/day)
1. Review what's working
2. Adjust prompts based on results
3. Add your 4th and 5th automation
4. Start the cold outreach sequence

### Week 4: Scale (30 min/day)
1. Your system is running
2. Focus on what generates revenue
3. Automate the rest

---

*Automation Hub Template · AutomateIt · automateit.ai*
