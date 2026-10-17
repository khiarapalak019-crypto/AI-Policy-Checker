
# AI Policy Compliance Checker
# Module: AI Policy and Usages

def check_compliance(activity):
    violations = []
    review_items = []

    # Rule 1: Protect sensitive information
    if activity["sensitive_data"] and not activity["approved_tool"]:
        violations.append(
            "Sensitive data used in an unapproved AI tool."
        )
    elif activity["sensitive_data"]:
        review_items.append(
            "Confirm that sensitive data use is authorised."
        )

    # Rule 2: Check tool approval
    if not activity["approved_tool"]:
        violations.append(
            "AI tool is not approved by the organisation."
        )

    # Rule 3: Verify AI-generated information
    if not activity["output_verified"]:
        review_items.append(
            "AI-generated output has not been verified."
        )

    # Rule 4: Follow disclosure requirements
    if activity["disclosure_required"] and not activity["disclosed"]:
        violations.append(
            "Required AI disclosure is missing."
        )

    # Determine the result
    if violations:
        status = "NON-COMPLIANT"
    elif review_items:
        status = "MANUAL REVIEW REQUIRED"
    else:
        status = "COMPLIANT"

    return status, violations, review_items


def main():
    # Fictional test cases; no real personal data is used.
    test_cases = [
        {
            "name": "Public article summary",
            "sensitive_data": False,
            "approved_tool": True,
            "output_verified": True,
            "disclosure_required": False,
            "disclosed": False
        },
        {
            "name": "Confidential report upload",
            "sensitive_data": True,
            "approved_tool": False,
            "output_verified": False,
            "disclosure_required": False,
            "disclosed": False
        },
        {
            "name": "Unverified AI report",
            "sensitive_data": False,
            "approved_tool": True,
            "output_verified": False,
            "disclosure_required": False,
            "disclosed": False
        },
        {
            "name": "Undisclosed AI presentation",
            "sensitive_data": False,
            "approved_tool": True,
            "output_verified": True,
            "disclosure_required": True,
            "disclosed": False
        }
    ]

    print("=" * 60)
    print("       AI POLICY COMPLIANCE CHECKER")
    print("=" * 60)

    for activity in test_cases:
        status, violations, review_items = check_compliance(activity)

        print(f"\nActivity: {activity['name']}")
        print(f"Status: {status}")

        for item in violations:
            print(f"  Violation: {item}")

        for item in review_items:
            print(f"  Review: {item}")

        if not violations and not review_items:
            print("  All defined policy checks passed.")

    print("\n" + "=" * 60)
    print("Compliance checking completed.")


if __name__ == "__main__":
    main()

           
