<!-- mtoc-start -->

* [InterimLentServers%Foreign_dotfiles.bootstrap](#interimlentserversforeign_dotfilesbootstrap)
  * [VLESS/NixOS Deployment](#vlessnixos-deployment)
  * [Usage](#usage)
  * [Variables](#variables)

<!-- mtoc-end -->
# InterimLentServers%Foreign_dotfiles.bootstrap

Ansible role to configure external VPS servers.

## VLESS/NixOS Deployment

Deploys VLESS (Xray) on a VPS using NixOS via nixos-anywhere.

## Usage

1. Edit `hosts.ini` to add MelisStoke with its IP:
   ```
   [melisstoke]
   MelisStoke ansible_host=<VPS_IP>
   ```

2. Populate vault:
   ```sh
   ansible-vault edit group_vars/melisstoke/vault
   ```
   Required variables:
   - `vault_bootstrap_server_ip` - VPS public IP
   - `vault_bootstrap_vps_root_password` - Initial root password

3. Run:
   ```sh
   ansible-playbook deploy_vless.yml -e bootstrap_server_ip=X -e bootstrap_vps_root_password=Y
   ```

## Variables

| Variable | Default | Description |
|---|---|---|
| `bootstrap_server_ip` | `""` | VPS public IP (required) |
| `bootstrap_vps_root_password` | `""` | Initial root SSH password (required) |
| `bootstrap_ssh_private_key_file` | `"~/.ssh/id_rsa"` | SSH private key path |
| `bootstrap_disk_device` | `"/dev/sda"` | Target disk device |
| `bootstrap_clients_count` | `2` | Number of VLESS client configs |
| `bootstrap_reality_domain` | `"www.microsoft.com"` | REALITY masking domain |
| `bootstrap_enable_nodeexporter` | `false` | Enable Prometheus node exporter |

