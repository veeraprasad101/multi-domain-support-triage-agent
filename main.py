import csv

# -----------------------------
# TEXT CLEANING (CRITICAL)
# -----------------------------
def clean_text(issue):
    issue = str(issue).lower()

    # Remove line breaks
    issue = issue.replace("\n", " ").replace("\r", " ")

    # Fix broken words like "i ncrease"
    issue = issue.replace("i ncrease", "increase")

    # Normalize spaces
    issue = " ".join(issue.split())

    return issue


# -----------------------------
# CLASSIFICATION
# -----------------------------
def classify(issue):
    issue = clean_text(issue)

    if any(x in issue for x in ["refund", "payment", "charge", "money"]):
        return "billing"

    elif any(x in issue for x in ["access", "login", "account", "permission", "remove", "employee"]):
        return "account_access"

    elif any(x in issue for x in ["error", "not working", "failing", "issue"]):
        return "bug"

    elif any(x in issue for x in ["fraud", "stolen", "identity", "unauthorized"]):
        return "fraud"

    else:
        return "faq"


# -----------------------------
# DECISION ENGINE
# -----------------------------
def decide_action(issue):
    issue = clean_text(issue)

    # 🚨 High-risk (always escalate)
    if any(x in issue for x in ["fraud", "stolen", "identity", "unauthorized"]):
        return "escalate"

    # ❌ Invalid / unethical (score manipulation)
    if ("score" in issue and any(x in issue for x in ["increase", "review", "unfair", "grade"])):
        return "escalate"

    # 🔒 Account / admin actions
    if any(x in issue for x in ["access", "login", "account", "remove", "employee"]):
        return "escalate"

    # 💰 Billing
    if any(x in issue for x in ["refund", "payment", "charge", "money"]):
        return "escalate"

    # ❌ Dangerous request
    if "delete all files" in issue:
        return "escalate"

    # 🐞 Technical issues
    if any(x in issue for x in ["error", "not working", "failing", "issue"]):
        return "escalate"

    # 🤷 Weak / unclear input
    if len(issue.strip()) < 15:
        return "escalate"

    return "respond"


# -----------------------------
# RESPONSE GENERATION
# -----------------------------
def generate_response(action, product, request_type):
    if action == "escalate":
        return f"This issue has been escalated to {product} support for further assistance."

    return f"For {request_type} related queries in {product}, please refer to the official help center."


# -----------------------------
# MAIN PROCESSING
# -----------------------------
output = []

with open("log.txt", "w") as log:
    with open("support_tickets.csv", "r") as f:
        reader = csv.DictReader(f)

        for i, row in enumerate(reader):
            issue = row.get("Issue", "")
            product = row.get("Company", "General")

            # Handle missing product
            if not product or product == "None":
                product = "General"

            request_type = classify(issue)
            action = decide_action(issue)
            response = generate_response(action, product, request_type)

            # Logging (important for submission)
            log.write(f"{i} | {product} | {request_type} | {action} | {issue[:60]}\n")

            output.append({
                "ticket_id": i,
                "request_type": request_type,
                "product": product,
                "action": action,
                "response": response
            })


# -----------------------------
# WRITE OUTPUT
# -----------------------------
with open("output.csv", "w") as f:
    writer = csv.DictWriter(f, fieldnames=[
        "ticket_id", "request_type", "product", "action", "response"
    ])
    writer.writeheader()
    writer.writerows(output)


print("Done! Check output.csv and log.txt")