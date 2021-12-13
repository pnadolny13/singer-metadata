
terraform_up:
	cd src && python3 -m venv venv && source venv/bin/activate && pip install -r api/requirements.txt && cp -r ./venv/lib/python3.9/site-packages/ ../infra/.temp && cp -r api/* ../infra/.temp
	cd infra && terraform apply

terraform_down:
	cd infra && terraform destroy

local_up:
	cd src/api/ && uvicorn main:app --reload