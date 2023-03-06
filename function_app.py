import azure.functions as func
from http_blueprint import blueprint as http_blueprint

app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)
app.register_blueprint(http_blueprint)