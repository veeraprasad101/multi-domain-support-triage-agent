# Multi-Domain Support Triage Agent

## Overview

This project implements a terminal-based support triage agent that processes support tickets across multiple domains (HackerRank, Claude, Visa).

The agent:

* Classifies the issue type
* Determines product area
* Decides whether to respond or escalate
* Generates safe responses

---

## Approach

### 1. Text Normalization

Input tickets may contain noisy formatting (line breaks, split words).
A cleaning function standardizes text for reliable processing.

### 2. Classification

Issues are categorized into:

* billing
* account_access
* bug
* fraud
* faq

### 3. Decision Logic

A rule-based system determines action:

* High-risk issues (fraud, billing, access) → escalated
* Invalid/unethical requests → escalated
* Technical issues → escalated
* Simple queries → responded

### 4. Response Generation

* Escalated → routed to human support
* Respond → directed to official help documentation

---

## Files

* main.py → core triage logic
* output.csv → generated predictions
* log.txt → processing logs

---

## How to Run

```bash
python3 main.py
```

---

## Design Choices

* Rule-based system ensures deterministic behavior
* Avoids hallucinations from LLMs
* Safety-first escalation strategy
* Lightweight (no external dependencies)

---

## Future Improvements

* Add semantic search using embeddings
* Improve response grounding using support corpus
* Add confidence scoring

---

