output "db_name" {
  value = azurerm_postgresql_flexible_server_database.main.name
  sensitive = true
}

output "db_user" {
  value = azurerm_postgresql_flexible_server.main.administrator_login
  sensitive = true
}

output "db_pass" {
  value = azurerm_postgresql_flexible_server.main.administrator_password
  sensitive = true
}

output "db_host" {
  value = azurerm_postgresql_flexible_server.main.fqdn
  sensitive = true
}