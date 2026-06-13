import traceback

from app.utils.retry import retry_execute


def safe_execute(
    agent_name,
    func,
    *args
):

    try:

        result = retry_execute(
            func,
            *args
        )

        return {
            "success": True,
            "result": result,
            "error": None
        }

    except Exception as e:

        print(
            f"\n[{agent_name}] FAILED"
        )

        traceback.print_exc()

        return {
            "success": False,
            "result": None,
            "error": str(e)
        }