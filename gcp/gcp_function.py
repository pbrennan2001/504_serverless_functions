import json
import functions_framework

@functions_framework.http
def hello_http(request):
    """HTTP Cloud Function.
    Expects JSON with 'LDL' and 'HDL' (or query params as fallback).
    Returns a JSON classification of cholesterol levels.
    """
    # Prefer JSON body; fall back to query parameters for convenience
    data = request.get_json(silent=True) or {}
    args = request.args or {}

    ldl = data.get("LDL", args.get("LDL"))
    hdl = data.get("HDL", args.get("HDL"))

    # Presence check
    if ldl is None or hdl is None:
        return (
            json.dumps({"error": "Both 'LDL' and 'HDL' are required."}),
            400,
            {"Content-Type": "application/json"},
        )

    # Type/convert check
    try:
        ldl_val = float(ldl)
        hdl_val = float(hdl)
    except (TypeError, ValueError):
        return (
            json.dumps({"error": "'LDL' and 'HDL' must be numbers."}),
            400,
            {"Content-Type": "application/json"},
        )

    status = "normal" if (ldl_val < 100 and hdl_val >= 60) else "abnormal"
    category = "Normal (LDL<100/HDL≥60)" if status == "normal" else "Elevated (simplified)"

    payload = {
        "LDL": ldl_val,
        "HDL": hdl_val,
        "status": status,
        "category": category,
    }

    return json.dumps(payload), 200, {"Content-Type": "application/json"}

