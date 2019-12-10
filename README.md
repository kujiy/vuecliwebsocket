# 開発環境

* Ubuntu16.04
* python3.5.2
* Vue CLI 3.2.2
* Node 10.11.0
* yarn 1.12.3

# 環境構築

python仮想環境作成

```bash
python3 -m venv env
source ./env/bin/activate
```

## サーバ

```bash
git clone https://github.com/dbgso/vuecliwebsocket.git
cd vuecliwebsocket
# サーバ起動
pip install -r requirements.txt
python app.py
```

## フロント

npmの場合

```bash
cd frontend
npm install
npm run serve
```

```bash
cd frontend
yarn
yarn serve
```

* frontendサーバが8080ポートで起動
    - http://localhost:8080/
* backendサーバが8081で起動する
    - http://localhost:8081/websocket
