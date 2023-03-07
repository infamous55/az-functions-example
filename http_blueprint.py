import azure.functions as func
import logging
import pyjokes
import json

blueprint = func.Blueprint()

# For HTTP triggered functions, specify the route.
@blueprint.function_name(name="HttpTriggerExample")
@blueprint.route(route="jokes", methods=["GET"])
def get_joke(req: func.HttpRequest) -> func.HttpResponse:
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

@blueprint.function_name(name="BlobInputExample")
@blueprint.route(route="settings", methods=["GET"])
@blueprint.blob_input(arg_name="input", path="files/settings.json", connection="AzureWebJobsStorage")
def get_settings(req: func.HttpRequest, input: bytes) -> func.HttpResponse:
    logging.info("Python Blob input function processed a request.")
    
    settings = json.loads(input)
    return func.HttpResponse(
        body=json.dumps({"settings": settings}),
        mimetype="application/json",
        status_code=200
    )