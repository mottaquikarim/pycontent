envvars:
	touch .env envvars

clean:
	find . -name __pycache__ -prune -exec rm -fr {} \;
	rm -fr dist/ build/ *.egg-info

docker-clean:
	docker-compose down

require-env:
ifndef env
	$(error env arg is required for this target)
endif

build-app: envvars
	docker-compose build pycontent

build-config: envvars
ifdef env
	docker-compose run pycontent ansible-playbook -i scripts/inventories/${env} scripts/infrastructure.yml
else
	docker-compose run pycontent ansible-playbook scripts/infrastructure.yml
endif

run-app: require-env build-app build-config
	docker-compose run pycontent python -m run

prep-sync: require-env build-app build-config
	docker-compose run pycontent docker/pycontent/prep_sync.sh

encrypt:
	docker-compose run pycontent ansible-vault encrypt scripts/group_vars/all/vault scripts/inventories/*/group_vars/all/vault

decrypt:
	docker-compose run pycontent ansible-vault decrypt scripts/group_vars/all/vault scripts/inventories/*/group_vars/all/vault
