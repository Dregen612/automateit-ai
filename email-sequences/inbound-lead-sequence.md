# 5-EMAIL FOLLOW-UP SEQUENCE FOR INBOUND LEADS
## AutomateIt · ed@automateit.ai

---

## TRIGGER
Sent when someone submits the booking form or requests the free demo.

---

## EMAIL 1: Instant Confirmation (0 hours)
**Subject:** You're on the list — here's what happens next

```
Hi {{first_name}},

Thanks for reaching out. I've got your request and I'll be in touch within the next few hours to confirm your time slot.

Before we jump on the call, I want to set expectations:

→ This isn't a pitch. I don't do slide decks.
→ I'll have a working demo ready for you — built specifically around the problem you described.
→ If it makes sense, we go live. If it doesn't, you walk away with fresh ideas and zero cost.

Your call is 15 minutes. We'll map out where you're losing the most time, and I'll show you exactly how I'd automate it.

Talk soon,
Ed
```

---

## EMAIL 2: Reminder (24 hours before call)
**Subject:** See you {{day}} — a few things to know

```
Hi {{first_name}},

Quick reminder: we're set for {{day}} at {{time}}.

To get the most out of our 15 minutes, here's what to have ready:

1. The ONE task you wish you never had to do again
2. What tools you're currently using (email, CRM, calendar, etc.)
3. Roughly how many hours/week that task takes

I'll come prepared with a working prototype — not a proposal, not a quote. An actual automation you can see running.

If something comes up and you need to reschedule, just reply here.

Ed
```

---

## EMAIL 3: Post-Call Follow-Up (2 hours after call)
**Subject:** Your demo recording + next steps

```
Hi {{first_name}},

Great speaking with you today.

As promised, here's a quick summary of what we covered:

{{custom: paste call notes here — e.g., "We looked at automating your lead follow-up process. Current state: manual, 3 hrs/week. Demo showed: AI drafting responses in under 2 minutes."}}

YOUR NEXT STEP:
If you want to move forward, reply here and I'll send an invoice. Your first automation goes live within 24 hours of payment.

If you want to think about it — totally fair. The demo I showed you is yours to keep. No pressure.

Either way, let me know if you have questions.

Ed
```

---

## EMAIL 4: Soft Follow-Up (3 days after call)
**Subject:** One thing I'd change if I were you

```
Hi {{first_name}},

Hope you're well. I was thinking about our conversation and there's one thing I wanted to share:

Most people who pass on automation think it's about the cost. It's not. It's about the uncertainty — "will this actually work for me?"

That's why I offer a working demo before you pay anything. You see it running. You decide.

The automation I showed you on the call would save you roughly {{custom: hours}} hours per week. That's {{custom: value}} in recovered time every month.

If you want to revisit, just reply. I'm happy to adjust the approach based on how your business works.

No follow-up after this one. I respect your time.

Ed
```

---

## EMAIL 5: Exit Intent / Breakup (7 days after call)
**Subject:** Fair enough — one free thing for you

```
Hi {{first_name}},

I get it — not the right time, or you're not convinced yet. That's fine.

Before I close your file, I want to leave you with something useful.

If you're doing {{custom: their pain point}} manually, here's the fastest way to get一半 the benefit with zero tools:

{{custom: insert relevant quick-win tip or simplified version of the automation discussed — e.g., "Next time a lead comes in, copy their message and paste it into ChatGPT with: 'Write a 3-sentence response that acknowledges this and asks for a call. Keep it under 50 words.' That's the core of what I'd automate for you — and it's free."}}

If you ever want to revisit automation, my door's open. The process is the same: 15-minute call, working demo, you decide.

Best of luck with everything,

Ed
```

---

## EMAIL 6: Re-engagement (30 days later — optional)
**Subject:** Still think about that automation

```
Hi {{first_name}},

Checking back in. Last time we talked, you were working on {{custom: their mentioned project/goal}}.

Has anything changed? If the time drain is still there, I'd still love to show you what's possible.

No pressure. Just wanted to stay on your radar.

Ed
```

---

## SEGMENTATION NOTES

| Lead Type | Trigger | Customization |
|-----------|---------|---------------|
| Booking form submitted | Email 1 → Email 2 | {{time_slot}} + {{day}} |
| Showed up to call | Email 3 → Email 4 → Email 5 | Use call notes |
| No-show on call | Email 1 → Email 4 (modified) | Skip Email 2 & 3 |
| Toolkit buyer | Different sequence | 30-day onboarding |
| Cold outreach lead | Different sequence | See cold outreach sequence |

---

*AutomateIt · AI Automation · automateit.ai*
