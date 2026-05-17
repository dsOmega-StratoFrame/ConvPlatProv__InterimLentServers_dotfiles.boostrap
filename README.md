<!-- mtoc-start -->

* [InterimLentServers%Foreign_dotfiles.bootstrap](#interimlentserversforeign_dotfilesbootstrap)
  * [VLESS/NixOS Deployment](#vlessnixos-deployment)
  * [Usage](#usage)
  * [Variables](#variables)
  * [References](#references)

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
   * `vault_bootstrap_server_ip` - VPS public IP
   * `vault_bootstrap_vps_root_password` - Initial root password

3. Set host variables:
   You can gather all variables and their usage in roles. Pay attention to
   `defaults` - these serve as a variable declarations and are usually
   important to fill in host variables.

   Already configured hosts:
   * [MelisStoke](./group_vars/MelisStoke/vars.yml)

   1. Also note that it's recommended to check `bootstrap_reality_domain` by
      running [RealiTLScanner](./bin/RealiTLScanner) (submodule of this repo).
      
      Follow instructions in it's README. It's basically just:
      ```bash
      cd ./bin/RealiTLScanner
      docker build -t realitlscanner .
      docker run --rm realitlscanner -addr <serverIpOrHost>
      ```

      For example:
      ```bash
      docker run --rm realitlscanner -addr MelisStoke
      ```

      Will output a bunch of ipp addresses and hosts. Select a legal and most popular host in your country to mask your vless connection [Source][@/Nnagibator228Nixosanywherexray]|[Zotero][z@/Nnagibator228Nixosanywherexray].

4. Run:

   ```bash
   make run-vless
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


## References
[@/Nnagibator228Nixosanywherexray]: <https://github.com/nnagibator228/nixos-anywhere-xray/tree/e896926f18c988e11610f9a6760b598ff47b60ae#preparations> 'Nnagibator228/Nixos-Anywhere-Xray'
[z@/Nnagibator228Nixosanywherexray]: <zotero://select/items/@/Nnagibator228Nixosanywherexray> 'Select in Zotero: Nnagibator228/Nixos-Anywhere-Xray'
