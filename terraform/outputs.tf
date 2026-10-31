output "public_ip" {
  value = azurerm_public_ip.pip.ip_address
}

output "ssh_command" {
  value = "ssh -i ~/.ssh/nexvion_key ${var.admin_user}@${azurerm_public_ip.pip.ip_address}"
}
