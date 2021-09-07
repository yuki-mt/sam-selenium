# sam-selenium

## Run locally
```
docker-compose up -d
docker exec -it selenium-app bash
python app.py
```

## Build
```
sh/build_package.sh
sh/download_chrome.sh
sam build
```

## Deploy

```bash
# for the first time
sam deploy --guided
# from the second time
sam deploy
```

## Logs
```bash
sam logs -n <function_name> --stack-name sam-selenium --tail
```

## Cleanup

```bash
aws cloudformation delete-stack --stack-name sam-selenium
```
