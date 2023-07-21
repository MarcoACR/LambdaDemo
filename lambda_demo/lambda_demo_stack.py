from constructs import Construct
from aws_cdk import (
    Duration,
    Stack,
    aws_iam as iam,
    aws_sqs as sqs,
    aws_lambda as _lambda,
    aws_lambda_event_sources as _aws_lambda_event_sources,
)


class LambdaDemoStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Making our SQS Queue
        queue = sqs.Queue(
            self, "LambdaDemoQueue",
            visibility_timeout=Duration.seconds(300),
        )

        # Make our Lambda Functions
        sqs_lambda = _lambda.Function(self, 'SQSLambdaTrigger',
                                      handler='lambda_handler.handler',
                                      runtime=_lambda.Runtime.PYTHON_3_10,
                                      code=_lambda.Code.from_asset( "lambda")
                                      )
        # Make Our SQS + Lambda Event Source
        sqs_event_source = _aws_lambda_event_sources.SqsEventSource(queue)

        # Add SQS event source to the lambda function
        sqs_lambda.add_event_source(sqs_event_source)