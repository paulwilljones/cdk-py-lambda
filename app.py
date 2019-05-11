#!/usr/bin/env python3

from aws_cdk import cdk

from cdk-py-lambda.cdk-py-lambda_stack import PyStack


app = cdk.App()
PyStack(app, "cdk-py-lambda-cdk-1")

app.run()
