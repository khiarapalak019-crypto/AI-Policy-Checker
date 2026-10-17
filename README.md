# AI Policy Compliance Checker

A small Python program that checks fictional AI-use activities against a set of basic organisational policy rules. It reports policy violations and items that need manual review.

## Requirements

- Python 3.6 or later
- No third-party packages

## Policy checks

For each activity, the checker evaluates whether:

1. Sensitive data was used in an approved AI tool. Use of sensitive data in an unapproved tool is a violation; otherwise, sensitive data use is flagged for authorisation review.
2. The AI tool is approved by the organisation. An unapproved tool is a violation.
3. AI-generated output has been verified. Unverified output requires manual review.
4. Required AI disclosure was made. Missing required disclosure is a violation.

## Results

Each activity receives one status:

- **COMPLIANT** — no violations or review items were found.
- **MANUAL REVIEW REQUIRED** — no violations were found, but at least one item needs review.
- **NON-COMPLIANT** — one or more violations were found.

The program also prints the individual violations and review items. A violation takes precedence in the overall status, even if review items are present.

## Included examples

The `main()` function checks four fictional activities: a public article summary, a confidential report upload, an unverified AI report, and an undisclosed AI presentation. The examples contain no real personal data.

## Limitations

This is a demonstration with a fixed set of rules and example activities. It does not read external data, determine whether information is sensitive, or replace a formal policy or human review. Update `test_cases` in `main.py` to try other activities, using the same fields:

- `name`
- `sensitive_data`
- `approved_tool`
- `output_verified`
- `disclosure_required`
- `disclosed`
