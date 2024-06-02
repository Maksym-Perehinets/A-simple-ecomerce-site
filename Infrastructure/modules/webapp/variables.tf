variable "location" {
  default = "West Europe"
}

variable "resource-group" {
  description = "name of resource group"
  type        = string
}

# ENV variables for db

variable "db_name" {
  type = string
  sensitive = true
}

variable "db_user" {
  type = string
  sensitive = true
}

variable "db_pass" {
  type = string
  sensitive = true
}

variable "db_host" {
  type = string
  sensitive = true
}

variable "db_port" {
  type = string
  sensitive = true
}