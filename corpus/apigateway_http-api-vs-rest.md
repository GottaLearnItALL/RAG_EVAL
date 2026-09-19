

# Choose between REST APIs and HTTP APIs
<a name="http-api-vs-rest"></a>

REST APIs and HTTP APIs are both RESTful API products. REST APIs support more features than HTTP APIs, while HTTP APIs are designed with minimal features so that they can be offered at a lower price. Choose REST APIs if you need features such as API keys, per-client throttling, request validation, AWS WAF integration, or private API endpoints. Choose HTTP APIs if you don't need the features included with REST APIs.

The following sections summarize core features that are available in REST APIs and HTTP APIs. When necessary, additional links are provided to navigate between the REST API and HTTP API sections of the API Gateway Developer Guide.

## Endpoint type
<a name="http-api-vs-rest.differences.endpoint-type"></a>

The endpoint type refers to the endpoint that API Gateway creates for your API. For more information, see [API endpoint types for REST APIs in API Gateway](api-gateway-api-endpoint-types.md). 


| Endpoint types | REST API | HTTP API | 
| --- | --- | --- | 
| [Edge-optimized](api-gateway-api-endpoint-types.md#api-gateway-api-endpoint-types-edge-optimized) | ![](https://docs.aws.amazon.com/apigateway/latest/developerguide/images/success_icon.png) Yes | ![](https://docs.aws.amazon.com/apigateway/latest/developerguide/images/negative_icon.png) No | 
| [Regional](api-gateway-api-endpoint-types.md#api-gateway-api-endpoint-types-regional) | ![](https://docs.aws.amazon.com/apigateway/latest/developerguide/images/success_icon.png) Yes | ![](https://docs.aws.amazon.com/apigateway/latest/developerguide/images/success_icon.png) Yes | 
| [Private](api-gateway-api-endpoint-types.md#api-gateway-api-endpoint-types-private) | ![](https://docs.aws.amazon.com/apigateway/latest/developerguide/images/success_icon.png) Yes | ![](https://docs.aws.amazon.com/apigateway/latest/developerguide/images/negative_icon.png) No | 

## Security
<a name="http-api-vs-rest.differences.security"></a>

API Gateway provides a number of ways to protect your API from certain threats, like malicious actors or spikes in traffic. To learn more, see [Protect your REST APIs in API Gateway](rest-api-protect.md) and [Protect your HTTP APIs in API Gateway](http-api-protect.md).


| Security features | REST API | HTTP API | 
| --- | --- | --- | 
| [Mutual TLS authentication](rest-api-mutual-tls.md) | ![](https://docs.aws.amazon.com/apigateway/latest/developerguide/images/success_icon.png) [Yes](rest-api-mutual-tls.md) | ![](https://docs.aws.amazon.com/apigateway/latest/developerguide/images/success_icon.png) [Yes](http-api-mutual-tls.md) | 
| [Certificates for backend authentication](getting-started-client-side-ssl-authentication.md) | ![](https://docs.aws.amazon.com/apigateway/latest/developerguide/images/success_icon.png) Yes | ![](https://docs.aws.amazon.com/apigateway/latest/developerguide/images/negative_icon.png) No | 
| [AWS WAF](apigateway-control-access-aws-waf.md) | ![](https://docs.aws.amazon.com/apigateway/latest/developerguide/images/success_icon.png) Yes | ![](https://docs.aws.amazon.com/apigateway/latest/developerguide/images/negative_icon.png) No | 

## Authorization
<a name="http-api-vs-rest.differences.authorization"></a>

API Gateway supports multiple mechanisms for controlling and managing access to your API. For more information, see [Control and manage access to REST APIs in API Gateway](apigateway-control-access-to-api.md) and [Control and manage access to HTTP APIs in API Gateway](http-api-access-control.md).


| Authorization options | REST API | HTTP API | 
| --- | --- | --- | 
| [IAM](permissions.md) | ![](https://docs.aws.amazon.com/apigateway/latest/developerguide/images/success_icon.png) [Yes](permissions.md) | ![](https://docs.aws.amazon.com/apigateway/latest/developerguide/images/success_icon.png) [Yes](http-api-access-control-iam.md) | 
| [Resource policies](apigateway-resource-policies.md) | ![](https://docs.aws.amazon.com/apigateway/latest/developerguide/images/success_icon.png) Yes | ![](https://docs.aws.amazon.com/apigateway/latest/developerguide/images/negative_icon.png) No<br /> | 
| [Amazon Cognito](apigateway-integrate-with-cognito.md) | ![](https://docs.aws.amazon.com/apigateway/latest/developerguide/images/success_icon.png) Yes | ![](https://docs.aws.amazon.com/apigateway/latest/developerguide/images/success_icon.png) Yes 1 | 
| [Custom authorization with an AWS Lambda function](apigateway-use-lambda-authorizer.md) | ![](https://docs.aws.amazon.com/apigateway/latest/developerguide/images/success_icon.png) [Yes](apigateway-use-lambda-authorizer.md) | ![](https://docs.aws.amazon.com/apigateway/latest/developerguide/images/success_icon.png) [Yes](http-api-lambda-authorizer.md) | 
| [JSON Web Token (JWT)](http-api-jwt-authorizer.md) 2 | ![](https://docs.aws.amazon.com/apigateway/latest/developerguide/images/negative_icon.png) No | ![](https://docs.aws.amazon.com/apigateway/latest/developerguide/images/success_icon.png) Yes | 

1 You can use Amazon Cognito with a [JWT authorizer](http-api-jwt-authorizer.md).

2 You can use a [Lambda authorizer](apigateway-use-lambda-authorizer.md) to validate JWTs for REST APIs.

## API management
<a name="http-api-vs-rest.differences.management"></a>

Choose REST APIs if you need API management capabilities such as API keys and per-client rate limiting. For more information, see [Distribute your REST APIs to clients in API Gateway](rest-api-distribute.md), [Custom domain name for public REST APIs in API Gateway](how-to-custom-domains.md), and [Custom domain names for HTTP APIs in API Gateway](http-api-custom-domain-names.md).


| Features | REST API | HTTP API | 
| --- | --- | --- | 
| [Custom domains](how-to-custom-domains.md) | ![](https://docs.aws.amazon.com/apigateway/latest/developerguide/images/success_icon.png) [Yes](how-to-custom-domains.md) | ![](https://docs.aws.amazon.com/apigateway/latest/developerguide/images/success_icon.png) [Yes](http-api-custom-domain-names.md) | 
| [API keys](api-gateway-api-usage-plans.md) | ![](https://docs.aws.amazon.com/apigateway/latest/developerguide/images/success_icon.png) Yes | ![](https://docs.aws.amazon.com/apigateway/latest/developerguide/images/negative_icon.png) No | 
| [Per-client rate limiting](api-gateway-request-throttling.md) | ![](https://docs.aws.amazon.com/apigateway/latest/developerguide/images/success_icon.png) Yes | ![](https://docs.aws.amazon.com/apigateway/latest/developerguide/images/negative_icon.png) No | 
| [Per-client usage throttling](api-gateway-api-usage-plans.md) | ![](https://docs.aws.amazon.com/apigateway/latest/developerguide/images/success_icon.png) Yes | ![](https://docs.aws.amazon.com/apigateway/latest/developerguide/images/negative_icon.png) No | 
| [Developer portal](apigateway-portals.md) | ![](https://docs.aws.amazon.com/apigateway/latest/developerguide/images/success_icon.png) Yes | ![](https://docs.aws.amazon.com/apigateway/latest/developerguide/images/negative_icon.png) No | 

## Development
<a name="http-api-vs-rest.differences.development"></a>

As you're developing your API Gateway API, you decide on a number of characteristics of your API. These characteristics depend on the use case of your API. For more information see [Develop REST APIs in API Gateway](rest-api-develop.md) and [Develop HTTP APIs in API Gateway](http-api-develop.md).


| Features | REST API | HTTP API | 
| --- | --- | --- | 
| [CORS configuration](how-to-cors.md) | ![](https://docs.aws.amazon.com/apigateway/latest/developerguide/images/success_icon.png) [Yes](how-to-cors.md) | ![](https://docs.aws.amazon.com/apigateway/latest/developerguide/images/success_icon.png) [Yes](http-api-cors.md) | 
| [Test invocations](how-to-test-method.md) | ![](https://docs.aws.amazon.com/apigateway/latest/developerguide/images/success_icon.png) Yes | ![](https://docs.aws.amazon.com/apigateway/latest/developerguide/images/negative_icon.png) No | 
| [Caching](api-gateway-caching.md) | ![](https://docs.aws.amazon.com/apigateway/latest/developerguide/images/success_icon.png) Yes | ![](https://docs.aws.amazon.com/apigateway/latest/developerguide/images/negative_icon.png) No | 
| [User-controlled deployments](how-to-deploy-api.md) | ![](https://docs.aws.amazon.com/apigateway/latest/developerguide/images/success_icon.png) [Yes](how-to-deploy-api.md) | ![](https://docs.aws.amazon.com/apigateway/latest/developerguide/images/success_icon.png) [Yes](http-api-stages.md) | 
| [Automatic deployments](http-api-stages.md) | ![](https://docs.aws.amazon.com/apigateway/latest/developerguide/images/negative_icon.png) No | ![](https://docs.aws.amazon.com/apigateway/latest/developerguide/images/success_icon.png) Yes | 
| [Custom gateway responses](api-gateway-gatewayResponse-definition.md) | ![](https://docs.aws.amazon.com/apigateway/latest/developerguide/images/success_icon.png) Yes | ![](https://docs.aws.amazon.com/apigateway/latest/developerguide/images/negative_icon.png) No | 
| [Canary release deployments](canary-release.md) | ![](https://docs.aws.amazon.com/apigateway/latest/developerguide/images/success_icon.png) Yes | ![](https://docs.aws.amazon.com/apigateway/latest/developerguide/images/negative_icon.png) No | 
| [Request validation](api-gateway-method-request-validation.md) | ![](https://docs.aws.amazon.com/apigateway/latest/developerguide/images/success_icon.png) Yes | ![](https://docs.aws.amazon.com/apigateway/latest/developerguide/images/negative_icon.png) No | 
| [Request parameter transformation](rest-api-data-transformations.md) | ![](https://docs.aws.amazon.com/apigateway/latest/developerguide/images/success_icon.png) [Yes](rest-api-data-transformations.md) | ![](https://docs.aws.amazon.com/apigateway/latest/developerguide/images/success_icon.png) [Yes](http-api-parameter-mapping.md) | 
| [Request body transformation](rest-api-data-transformations.md) | ![](https://docs.aws.amazon.com/apigateway/latest/developerguide/images/success_icon.png) Yes | ![](https://docs.aws.amazon.com/apigateway/latest/developerguide/images/negative_icon.png) No | 

## Monitoring
<a name="http-api-vs-rest.differences.monitoring"></a>

API Gateway supports several options to log API requests and monitor your APIs. For more information, see [Monitor REST APIs in API Gateway](rest-api-monitor.md) and [Monitor HTTP APIs in API Gateway](http-api-monitor.md).


| Feature | REST API | HTTP API | 
| --- | --- | --- | 
| [Amazon CloudWatch metrics](monitoring-cloudwatch.md) | ![](https://docs.aws.amazon.com/apigateway/latest/developerguide/images/success_icon.png) [Yes](monitoring-cloudwatch.md) | ![](https://docs.aws.amazon.com/apigateway/latest/developerguide/images/success_icon.png) [Yes](http-api-metrics.md) | 
| [Access logs to CloudWatch Logs](set-up-logging.md) | ![](https://docs.aws.amazon.com/apigateway/latest/developerguide/images/success_icon.png) [Yes](set-up-logging.md) | ![](https://docs.aws.amazon.com/apigateway/latest/developerguide/images/success_icon.png) [Yes](http-api-logging.md) | 
| [Access logs to Amazon Data Firehose](apigateway-logging-to-kinesis.md) | ![](https://docs.aws.amazon.com/apigateway/latest/developerguide/images/success_icon.png) Yes | ![](https://docs.aws.amazon.com/apigateway/latest/developerguide/images/negative_icon.png) No | 
| [Execution logs](rest-api-execution-logging.md) | ![](https://docs.aws.amazon.com/apigateway/latest/developerguide/images/success_icon.png) Yes | ![](https://docs.aws.amazon.com/apigateway/latest/developerguide/images/negative_icon.png) No | 
| [AWS X-Ray tracing](apigateway-xray.md) | ![](https://docs.aws.amazon.com/apigateway/latest/developerguide/images/success_icon.png) Yes | ![](https://docs.aws.amazon.com/apigateway/latest/developerguide/images/negative_icon.png) No | 

## Integrations
<a name="http-api-vs-rest.differences.integrations"></a>

Integrations connect your API Gateway API to backend resources. For more information, see [Integrations for REST APIs in API Gateway](how-to-integration-settings.md) and [Create integrations for HTTP APIs in API Gateway](http-api-develop-integrations.md).


| Feature | REST API | HTTP API | 
| --- | --- | --- | 
| [Public HTTP endpoints](setup-http-integrations.md) | ![](https://docs.aws.amazon.com/apigateway/latest/developerguide/images/success_icon.png) [Yes](setup-http-integrations.md) | ![](https://docs.aws.amazon.com/apigateway/latest/developerguide/images/success_icon.png) [Yes](http-api-develop-integrations-http.md) | 
| [AWS services](api-gateway-api-integration-types.md) | ![](https://docs.aws.amazon.com/apigateway/latest/developerguide/images/success_icon.png) [Yes](api-gateway-api-integration-types.md) | ![](https://docs.aws.amazon.com/apigateway/latest/developerguide/images/success_icon.png) [Yes](http-api-develop-integrations-aws-services.md) | 
| [AWS Lambda functions](set-up-lambda-integrations.md) | ![](https://docs.aws.amazon.com/apigateway/latest/developerguide/images/success_icon.png) [Yes](set-up-lambda-integrations.md) | ![](https://docs.aws.amazon.com/apigateway/latest/developerguide/images/success_icon.png) [Yes](http-api-develop-integrations-lambda.md) | 
| [Private integrations with Network Load Balancers](set-up-private-integration.md) | ![](https://docs.aws.amazon.com/apigateway/latest/developerguide/images/success_icon.png) [Yes](set-up-private-integration.md) | ![](https://docs.aws.amazon.com/apigateway/latest/developerguide/images/success_icon.png) [Yes](http-api-develop-integrations-private.md) | 
| [Private integrations with Application Load Balancers](http-api-develop-integrations-private.md) | ![](https://docs.aws.amazon.com/apigateway/latest/developerguide/images/success_icon.png) [Yes](set-up-private-integration.md) | ![](https://docs.aws.amazon.com/apigateway/latest/developerguide/images/success_icon.png) Yes | 
| [Private integrations with AWS Cloud Map](http-api-develop-integrations-private.md) | ![](https://docs.aws.amazon.com/apigateway/latest/developerguide/images/negative_icon.png) No<br /> | ![](https://docs.aws.amazon.com/apigateway/latest/developerguide/images/success_icon.png) Yes | 
| [Mock integrations](how-to-mock-integration.md) | ![](https://docs.aws.amazon.com/apigateway/latest/developerguide/images/success_icon.png) Yes | ![](https://docs.aws.amazon.com/apigateway/latest/developerguide/images/negative_icon.png) No | 
| [Response streaming](response-transfer-mode.md) | ![](https://docs.aws.amazon.com/apigateway/latest/developerguide/images/success_icon.png) Yes | ![](https://docs.aws.amazon.com/apigateway/latest/developerguide/images/negative_icon.png) No | 