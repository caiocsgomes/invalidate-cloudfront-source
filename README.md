# lambda-invalidate-cloudfront-source

This repository contains a lambda function that invalidates the source of a cloudfront distribuition from code pipeline.

I have a static personal page (caiogomes.me) and it is stored in a S3 bucket. Every time I do a deploy I want the source from the cloudfront to be refreshed
so the last version instantaneously available at the domain, and not the cached one.

The lambda function was developed using python 3.8.

## Observations on AWS configuration

- Give the lambda the CloudFrontFullAccess IAM role so that it can change the cloudfront distribution and the 
AWSCodePipelineFullAccess IAM role so that it can finish the job execution. If you can find less permissive roles
that do the same, that's better, I didn't.

- Pass the cloudfront id on the UserParameters field from the CodePipeline event. There's a test event inside the
events folder.
