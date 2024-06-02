locals {
  naming-location = lower(replace(var.location, " ", ""))
}

resource "random_password" "password" {
  length           = 16
  special          = true
  override_special = "!#$%&*()-_=+[]{}<>:?"
}


resource "azurerm_postgresql_flexible_server" "main" {
  name                   = "postgresserver-ecommerce-prod-${local.naming-location}"
  resource_group_name    = var.resource-group
  location               = var.location
  version                = "16"
  administrator_login    = "webapp"
  administrator_password = random_password.password.result
  storage_mb             = 32768
  sku_name               = "B_Standard_B1ms"
}

resource "azurerm_postgresql_flexible_server_database" "main" {
  name      = "postgressdb-ecommerce-prod-${local.naming-location}"
  server_id = azurerm_postgresql_flexible_server.main.id
  collation = "en_US.utf8"
  charset   = "utf8"
}