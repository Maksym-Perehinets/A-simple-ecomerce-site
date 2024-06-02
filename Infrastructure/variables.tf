variable "location" {
  default = "East US"
}

variable "django_secret_key" {
  sensitive = true
}
