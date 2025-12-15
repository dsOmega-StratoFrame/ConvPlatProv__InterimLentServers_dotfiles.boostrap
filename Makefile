ifneq (,$(wildcard ./.env.dev))
    include .env.dev
    export
endif

run:
	ANSIBLE_CONFIG=${ANSIBLE_CONFIG} ./bin/dot-bootstrap

# TODO: Move to snakemake and add optional param for host.
vault-edit-creamsoda .vault_pass.py ./group_vars/creamsoda/vault:
	ANSIBLE_CONFIG=ansible.cfg ansible-vault edit --vault-password-file ./.vault_pass.py ./group_vars/creamsoda/vault

install requirements.yml:
	ansible-galaxy install -r requirements.yml

# TODO: Move to snakemake and add optional param for host.
facts:
	ANSIBLE_CONFIG=ansible.cfg ansible localhost -m ansible.builtin.setup

config:
	ansible-config dump
