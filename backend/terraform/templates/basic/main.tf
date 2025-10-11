terraform {
  required_providers {
    null = {
        source = "hashicorp/null"
        version = "~> 3.0"
    }
  }
}

provider "null" {}

resource "null_resource" "dummy_env" {
  triggers = {
    env_id = var.env_id
  }

  provisioner "local-exec" {
    command = "echo 'Provisioning environment ${self.triggers.env_id}'"
  }

  provisioner "local-exec" {
    when = destroy
    command = "echo 'Destroying environment ${self.triggers.env_id}'"
  }
}