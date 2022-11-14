# Set common variables for the environment. This is automatically pulled in in the root terragrunt.hcl configuration to
# feed forward to the child modules.
locals {
  environment = "dev"
  tags = {
  environment = "dev"
  }
  min_size = 1
  max_size = 1
}
