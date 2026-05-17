ifneq (,$(wildcard ./.env.dev))
    include .env.dev
    export
endif

run:
	ANSIBLE_CONFIG=${ANSIBLE_CONFIG} ./bin/dot-bootstrap

run-vless:
	ANSIBLE_CONFIG=${ANSIBLE_CONFIG} ./bin/dot-bootstrap vless

vault-init-melis-stoke .vault_pass.py ./group_vars/MelisStoke/vault:
	ANSIBLE_CONFIG=ansible.cfg ansible-vault encrypt --encrypt-vault-id default --vault-password-file ./.vault_pass.py ./group_vars/MelisStoke/vault

# TODO: Move to snakemake and add optional param for host.
vault-edit-melis-stoke .vault_pass.py ./group_vars/MelisStoke/vault:
	ANSIBLE_CONFIG=ansible.cfg ansible-vault edit --vault-password-file ./.vault_pass.py ./group_vars/MelisStoke/vault

install requirements.yml:
	ansible-galaxy install -r requirements.yml

# TODO: Move to snakemake and add optional param for host.
facts:
	ANSIBLE_CONFIG=ansible.cfg ansible localhost -m ansible.builtin.setup

test:
	ANSIBLE_CONFIG=ansible.cfg ansible-playbook ./test.yml -v

config:
	ansible-config dump
