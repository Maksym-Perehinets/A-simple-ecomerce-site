locals {
  naming-location = lower(replace(var.location, " ", ""))
}

resource "azurerm_service_plan" "main" {
  name                = "serviceplan-ecommerce-prod-${local.naming-location}"
  resource_group_name = var.resource-group
  location            = var.location
  os_type             = "Linux"
  sku_name            = "B1"
}

resource "azurerm_linux_web_app" "mian" {
  name                = "webapp-website-prod-${local.naming-location}"
  resource_group_name = var.resource-group
  location            = var.location
  service_plan_id     = azurerm_service_plan.main.id

  site_config {
    cors {
      allowed_origins = ["*"]
    }
    application_stack {
      python_version = "3.11"
    }
  }
  app_settings = {
    "DATABASE_NAME" = var.db_name
    "DATABASE_USER" = var.db_user
    "DATABASE_PASS" = var.db_pass
    "DATABASE_HOST" = var.db_host
    "DATABASE_PORT" = var.db_port
  }
}