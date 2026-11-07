terraform {
  required_version = ">= 1.17.0"

  required_providers {
    render = {
      source  = "render-oss/render"
      version = "~> 1.0"
    }
  }
  cloud {
  organization = "dcccd_assignments"

  workspaces {
    name = "mini-project-staging"
  }
  }
}
