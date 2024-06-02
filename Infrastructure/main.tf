locals {
  naming-location = lower(replace(var.location, " ", ""))
}

resource "azurerm_resource_group" "main" {
  name     = "rg-ecommerce-prod-${local.naming-location}"
  location = var.location
}

module "postgres_db" {
  source = "./modules/postgress_db"
  resource-group = azurerm_resource_group.main.name
  location = var.location
}

module "web_app" {
  depends_on = [ module.postgres_db ]
  source = "./modules/webapp"
  resource-group = azurerm_resource_group.main.name
  location = var.location
  db_name = module.postgres_db.db_name
  db_user = module.postgres_db.db_user
  db_pass = module.postgres_db.db_pass
  db_host = module.postgres_db.db_host
  db_port = 5432
}