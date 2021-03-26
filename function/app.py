import boto3
from time import time


def lambda_handler(event, context):
    print('EVENT', event)
    print('CONTEXT', context)
    cloudfront_id = event['CodePipeline.job']['data']['actionConfiguration']['configuration']['UserParameters']
    cloudfront_client = boto3.client('cloudfront')
    code_pipeline = boto3.client('codepipeline')
    code_pipeline_job = event['CodePipeline.job']['id']
    print('CLOUDFRONT_ID', cloudfront_id)
    response = cloudfront_client.create_invalidation(
        DistributionId=cloudfront_id,
        InvalidationBatch={
            'Paths': {
                'Quantity': 1,
                'Items': [
                    '/*',
                ]
            },
            'CallerReference': str(time()).replace(".", "")
        }
    )
    http_cloudfront_result = response['ResponseMetadata']['HTTPStatusCode']
    print('HTTP_CLOUDFRONT_RESULT', http_cloudfront_result)
    success_result = True if http_cloudfront_result == 200 or http_cloudfront_result == 201 else False
    print('SUCCESS', success_result)
    if success_result:
        return code_pipeline.put_job_success_result(jobId=code_pipeline_job)
    else:
        return code_pipeline.put_job_failure_result(jobId=code_pipeline_job, failureDetails='error in pipeline')