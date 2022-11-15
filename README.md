# devops_challenge

### Pre-requisites

1. Install [Terraform](https://www.terraform.io/) version `1.1.4` and
   [Terragrunt](https://github.com/gruntwork-io/terragrunt) version `v0.36.0` or newer.
1. Update the `bucket` parameter in the root `terragrunt.hcl`. We use S3 [as a Terraform
   backend](https://www.terraform.io/docs/backends/types/s3.html) to store your
   Terraform state, and S3 bucket names must be globally unique.
1. Configure your AWS credentials using one of the supported [authentication
   mechanisms](https://www.terraform.io/docs/providers/aws/#authentication).
1. Fill in your AWS Account ID's in `prod/account.hcl` and `non-prod/account.hcl`.

### Deploying all resources in a environment.

1. `cd` into the module's folder (e.g. `cd non-prod/us-east-1/qa/`).
1. Run `terragrunt plan-all` to see all the changes you're about to apply.
1. If the plan looks good, run `terragrunt apply-all`.


### Build application locally

To build the application locally, you need the docker installed and `docker-compose up` inside the app folder
