#!/usr/bin/env python3

import aws_cdk as cdk

from lambda_demo.lambda_demo_stack import LambdaDemoStack


app = cdk.App()
LambdaDemoStack(app, "lambda-demo")

app.synth()
