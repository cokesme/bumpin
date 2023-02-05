# AWS Notes
The AWS journey and javascript...

AWS Well-Architected Framework Doc: https://docs.aws.amazon.com/pdfs/wellarchitected/latest/framework/wellarchitected-framework.pdf
## CloudTrail
Turned this shit on to see what's up

## Cognito
Doesn't seem to show up in RAM for some reason as a resource?

### Creating a CloudFormation template
After minutes of waiting for the AWS perms to propogate I go from 
```
C:\Users\test\Documents\awfl\resources>aws serverlessrepo create-cloud-formation-template --application-id arn:aws:cognito-idp:us-east-1:000000000000:userpool/us-east-1_000000000

An error occurred (AccessDeniedException) when calling the CreateCloudFormationTemplate operation: User: arn:aws:iam::000000000000:user/comcma-dev is not authorized to perform: serverlessrepo:CreateCloudFormationTemplate on resource: arn:aws:cognito-idp:us-east-1:000000000000:userpool/us-east-1_000000000

C:\Users\test\Documents\awfl\resources>aws serverlessrepo create-cloud-formation-template --application-id arn:aws:cognito-idp:us-east-1:000000000000:userpool/us-east-1_000000000

An error occurred (NotFoundException) when calling the CreateCloudFormationTemplate operation: Application with id arn:aws:cognito-idp:us-east-1:000000000000:userpool/us-east-1_000000000 could not be found.
```