#!/bin/bash
rm -rf ../meal-recommend-app-dist
pip install -r ./requirements.txt -t ../meal-recommend-app-dist
rsync -av ./* ../meal-recommend-app-dist/ --exclude '*.csv'
cd ../meal-recommend-app-dist/
rm -rf boto3 botocore
zip -r meal-recommend-app.zip .  -x "*.dist-info*" -x "*__pycache__*" -x "*.egg-info*"
aws s3 cp meal-recommend-app.zip s3://meal-recommend-app --profile oe-assume
aws lambda update-function-code --function-name meal-recommend-app --s3-bucket meal-recommend-app --s3-key meal-recommend-app.zip --profile oe-assume
