import re

# Task 1: Email Extraction Enhancement

text = "Emails: user1@domain.com, user2@exclude.com, user3@domain.com"

# emails = re.findall(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b", text) -- Original expression
emails = re.findall(r"\b[A-Za-z0-9._%+-]+@(?!exclude)[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b", text) # -- Adapted expression

print("Matches with adapted expression:", emails)