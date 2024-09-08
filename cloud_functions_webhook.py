import functions_framework


@functions_framework.http
def hello_http(request):
    request_json = request.get_json(silent=True)
    request_args = request.args

    print(request_json)
    print(request_args)

    return "200"
