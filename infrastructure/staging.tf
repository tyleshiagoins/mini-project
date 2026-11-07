resource "render_web_service" "staging" {
  name              = "task-tracker"
  plan              = "free"
  region            = "oregon"
  health_check_path = "/"

  env_vars = {
    APP_ENV = {
      value = var.app_environment
    }
  }

  root_directory = "task-tracker/"

  runtime_source = {
    native_runtime = {
      repo_url      = "https://github.com/tyleshiagoins/mini-project"
      branch        = "main"
      runtime       = "python"
      build_command = "bash build_staging.sh"
      auto_deploy   = false
    }
  }

  start_command = "gunicorn app:app --bind 0.0.0.0:$PORT"

  lifecycle {
    ignore_changes = [
    maintenance_mode,
    custom_domains
    ]
  }
}

variable "app_environment" {
  description = "Environment for the application"
  type        = string
  default     = "staging"
}