# boto3-sample

## 手順

### pyenvのインストール

```
brew install pyenv
```

### bash_profileの編集
pyenvのパスを通すためにbash_profileを編集します。
```
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bash_profile
echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bash_profile
echo 'eval "$(pyenv init -)"' >> ~/.bash_profile
```

bash_profileの保存を適用します
```
source ~/.bash_profile
```

### pyenvでpythonをインストール
```
pyenv install 3.7.4
pyenv install 2.7.10
```

現在選択しているバージョンの確認
```
pyenv versions
```

バージョンを切り替え
```
pyenv global 3.7.4
```

切り替えたあと、公式コマンドpythonでバージョン確認を行う
```
python --version
```
「Python 3.7.4」になっていることを確認


### boto3のconf「credentials」作成

```
mkdir ~/.aws
sudo vi ~/.aws/credentials
```

```
[default]
aws_access_key_id = YOUR_ACCESS_KEY
aws_secret_access_key = YOUR_SECRET_KEY
```
「YOUR_ACCESS_KEY」と「YOUR_SECRET_KEY」については、https://console.aws.amazon.com/iam/home 画面からユーザを作成し、アクセスキーとシークレットキーを設定してください。

### boto3のconf「config」作成
```
sudo vi ~/.aws/config
```

```
[default]
region=ap-northeast-1
```

### pip インストール
```
brew install pipenv
```

### boto3 インストール
```
pip install boto3
pip install boto3==1.0.0
pip install --upgrade boto3
```

## 確認

```
python src/quick_start.py 
```
s3のバケット一覧が表示されて入ればOKです！
