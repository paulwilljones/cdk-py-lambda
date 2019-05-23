#!/usr/bin/env python3

from aws_cdk import aws_lambda as lambda_, cdk


class PyStack(cdk.Stack):

    def __init__(self, app: cdk.App, id: str, **kwargs) -> None:
        super().__init__(app, id)

        with open('lambda_handler.py', encoding="utf8") as fp:
            handler_code = fp.read()

            lambdaFn = lambda_.Function(
                self,
                "InlineLambda",
                code=lambda_.InlineCode(handler_code),
                handler="index.main",
                timeout=300,
                runtime=lambda_.Runtime.PYTHON37
            )

app = cdk.App()
PyStack(app, "cdk-py-lambda-cdk")
app.run()
