def human_review(state):

    print("\n===== HUMAN REVIEW =====")

    summaries = state.get(
    "summaries",
    []
)

    for summary in summaries:

        print(
            f"\nTitle: {summary['title']}"
        )

        print(
            summary["summary"][:300]
        )

    choice = input(
        "\nApprove summaries? (y/n): "
    )

    if choice.lower() == "y":

        return {
            "review_status": "approved"
        }

    return {
        "review_status": "rejected"
    }