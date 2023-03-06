import azure.functions as func
import logging
import pyjokes
import json

blueprint = func.Blueprint()

# For HTTP triggered functions, specify the route.
@blueprint.function_name(name="HttpTriggerExample")
@blueprint.route(route="jokes", methods=["GET"])
def test_function(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    category = req.params.get("category") or "neutral"
    if category not in ["neutral", "chuck", "all"]:
        response_body = json.dumps({
            "message": "Category must be 'neutral', 'chuck', or 'all'."
        })
        return func.HttpResponse(
            body=response_body,
            mimetype="application/json",
            status_code=400
        )

    joke = pyjokes.get_joke(language="en", category=category)
    return func.HttpResponse(
        body=json.dumps({"joke": joke}),
        mimetype="application/json",
        status_code=200
    )