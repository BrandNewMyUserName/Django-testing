Install script before running program
pip install "json"


Installing docker Loki and Promtail
https://grafana.com/docs/loki/latest/setup/install/docker/#install-with-docker-on-windows

cd "<local-path>"
wget https://raw.githubusercontent.com/grafana/loki/v3.4.1/cmd/loki/loki-local-config.yaml -O loki-config.yaml
wget https://raw.githubusercontent.com/grafana/loki/v3.4.1/clients/cmd/promtail/promtail-docker-config.yaml -O promtail-config.yaml

docker run --name loki -v /c/Users/User/VS-CODE-APPS/VS-PYTHON_APPS/djanog-testing/loki:/mnt/config -p 3100:3100 grafana/loki:3.4.1 --config.file=/mnt/config/loki-config.yaml
docker run -v /c/Users/User/VS-CODE-APPS/VS-PYTHON_APPS/djanog-testing/loki:/mnt/config -v /c/Users/User/VS-CODE-APPS/VS-PYTHON_APPS/djanog-testing/logs:/var/log --link loki grafana/promtail:3.4.1 --config.file=/mnt/config/promtail-config.yaml