import json
import azure.functions as func
import logging

app = func.FunctionApp(http_auth_level=func.AuthLevel.FUNCTION)

@app.route(route="http_trigger1")
def http_trigger1(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    ldl = req.params.get('LDL')
    hdl = req.params.get('HDL')

    if ldl is None or hdl is None:
        return func.HttpResponse(
            json.dumps({"error": "Please provide both LDL and HDL"}),
            status_code=400,
            mimetype="application/json"
        )
    try:
        ldl_value = float(ldl)
        hdl_value = float(hdl)
    except (TypeError, ValueError): 
        return func.HttpResponse(
            json.dumps({"error": "LDL and HDL must be numbers."}),
            status_code=400,
            mimetype="application/json"
        )

    status = "normal" if (ldl_value < 100 and hdl_value >= 60) else "abnormal"
    category = "Normal (LDL<100/HDL≥60)" if status == "normal" else "Elevated (simplified)"

    payload = {
        "LDL": ldl_value,
        "HDL": hdl_value,
        "status": status,
        "category": category,
    }

    return func.HttpResponse(json.dumps({"payload": payload}),mimetype="application/json")