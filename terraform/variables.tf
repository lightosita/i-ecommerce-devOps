variable "subscription_id" {
  type = string
}

variable "ssh_public_key" {
  type = string
}

variable "location" {
  type    = string
  default = "eastus"
}

variable "vm_size" {
  type    = string
  default = "Standard_D2s_v4"
}

variable "admin_user" {
  type    = string
  default = "azureuser"
}
