# Multi-Domain Support Triage Agent

## Overview

This project implements a terminal-based support triage agent that processes support tickets across multiple ecosystems:

* HackerRank
* Claude
* Visa

The agent:

* Classifies issue types
* Identifies product areas
* Determines whether a case should be responded to or escalated
* Generates safe and grounded responses

The project was developed as part of the HackerRank Orchestrate May 2026 Challenge.

---

## Features

* Multi-domain support ticket handling
* Rule-based issue classification
* Escalation detection for sensitive requests
* Safe response generation
* CSV input/output processing
* Terminal-based execution
* Lightweight implementation with minimal dependencies

---

## Approach

### 1. Text Normalization

Support tickets may contain:

* line breaks
* inconsistent formatting
* noisy text

A cleaning step standardizes input text before processing.

---

### 2. Classification

Issues are categorized into:

* billing
* account_access
* bug
* fraud
* faq

Keyword-based matching is used for deterministic classification.

---

### 3. Decision Logic

The triage engine determines whether to:

* respond safely
* escalate to human support

Examples of escalation:

* fraud reports
* refund/payment disputes
* account access requests
* unethical requests
* technical blockers

---

### 4. Response Generation

* Escalated tickets are routed to human support
* Low-risk queries receive safe guidance responses

---

## Project Structure

```text id="onxevx"
main.py               -> Core triage engine
support_tickets.csv   -> Input dataset
output.csv            -> Generated predictions
log.txt               -> Execution logs
README.md             -> Project documentation
```

---

## How to Run

```bash id="jlwm31"
python3 main.py
```

---

## Example Capabilities

* Detect fraud-related requests
* Handle billing/payment complaints
* Route technical issues
* Prevent unsafe or unsupported actions
* Generate consistent support responses

---

## Design Choices

* Rule-based system for deterministic behavior
* Safety-first escalation strategy
* Lightweight architecture
* Avoids unsupported claims and hallucinations

---

## Future Improvements

* Semantic search using embeddings
* Retrieval-Augmented Generation (RAG)
* Confidence scoring
* Support knowledge base integration
* LLM-assisted summarization

---

## Technologies Used

* Python 3
* Git & GitHub
* CSV Processing
* Rule-Based NLP Logic

---

## Author

Veera Prasad
