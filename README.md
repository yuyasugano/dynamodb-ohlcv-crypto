## ccxt DynamoDB architecture with AWS SAM

This example show how to set up DynamoDB time-series data for storing high frequent crypto currency ohlcv data by using ccxt with `AWS SAM`. 

## sam version

Ensure your `sam` version is as follows (some modifications would be required if you run other `sam` versions):
```sh
$ pip install aws-sam-cli
$ sam --version
SAM CLI, version 0.48.0
```
To install `aws-sam-cli`, visit https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html

## Setup steps

From `dynamodb-sam` folder:
1. Prepare S3 bucket to upload a deploy file and generate a compiled version of the template `compiled.yml`. You need to manually create an S3 bucket or use an existing one to store files.
2. Compile `template.yml` and generate a compiled version of the template `compiled.yml` with `sam package`command
3. Submit the compiled template to CloudFormation and deploy your serverless application with `sam deploy`command as follows
```sh
cd dynamodb-sam/
sam package --template-file template.yml --s3-bucket <Your S3 bucket> --output-template-file compiled.yml
sam deploy --template-file compiled.yml --stack-name <Your stack name> --capabilities CAPABILITY_IAM --parameter-overrides TablePrefix=<Your prefix>
```
 
From `crypto-sam` folder:
1. Prepare S3 bucket to upload a deploy file and generate a compiled version of the template `compiled.yml`. You need to manually create an S3 bucket or use an existing one to store files.
2. Compile `template.yml` and generate a compiled version of the template `compiled.yml` with `sam package`command
3. Submit the compiled template to CloudFormation and deploy your serverless application with `sam deploy`command as follows
```sh
cd crypto-sam/
pip install ccxt -t ./
sam package --template-file template.yml --s3-bucket <Your S3 bucket> --output-template-file compiled.yml
sam deploy --template-file compiled.yml --stack-name <Your stack name> --capabilities CAPABILITY_IAM --parameter-overrides TablePrefix=<Your prefix> Exchange=<ccxt exchange> Pair=<pair name>
```

## License

This code is licensed under the MIT License.
