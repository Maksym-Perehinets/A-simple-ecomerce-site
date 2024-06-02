terraform {
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "~>3.94.0 "
    }
    random = {
      source  = "hashicorp/random"
      version = "~>3.6.0"
    }
  }
  backend "azurerm" {
    resource_group_name  = "e-commerce-rg"
    storage_account_name = "terraformbackendasd32t45"
    container_name       = "terraform-state"
    key                  = "prod.tfstate"
  }
}

provider "azurerm" {
  features {}
}