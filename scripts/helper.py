import requests



resp = requests.get("https://docs.aws.amazon.com/apigateway/latest/developerguide/toc-contents.json")
data = resp.json()


def walk(nodes, out):
    for n in nodes:
        if 'href' in n:
            out.append({"title": n['title'], "href": n['href']})
        if 'contents' in n:
            walk(n['contents'],out)
        
    return out


pages = walk(data['contents'],[])

WANTED = [
    "welcome.html",
    "api-gateway-basic-concept.html",
    "http-api-vs-rest.html",
    "set-up-lambda-integrations.html",
    "set-up-lambda-proxy-integrations.html",
    "set-up-lambda-custom-integrations.html",
    "set-up-lambda-integration-async.html",
    "handle-errors-in-lambda-integration.html",
    "apigateway-use-lambda-authorizer.html",
    "configure-api-gateway-lambda-authorization.html",
    "http-api-develop-integrations-lambda.html",
    "http-api-troubleshooting-lambda.html",
    "apigateway-control-access-to-api.html",
    "apigateway-resource-policies.html",
    "permissions.html",
    "api-gateway-request-throttling.html",
    "api-gateway-caching.html",
    "how-to-cors.html",
    "api-gateway-api-integration-types.html",
]

selected = [p for p in pages if p["href"] in WANTED]
print(len(selected))   # should be ~19