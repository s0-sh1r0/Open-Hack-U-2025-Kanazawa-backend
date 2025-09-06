@ -1,31 +0,0 @@
# Open-Hack-U-2025-Kanazawa-backend

## Gitルール ##
- 作業は必ず **課題単位** のブランチで行う
- `main` への直接 push は禁止（保護ブランチ）
- 作業前に `git pull --rebase` で最新化

## Git ブランチ命名規則
- **種別**  
- `feature/` : 新機能追加
- `fix/` : 修正
- `docs/` : ドキュメント関連

- **ルール**  
- 小文字とハイフン（`-`）で単語を区切る  
- 内容は簡潔に（1〜3語程度）  
- 日本語は使用せず英語で統一  

---

## インフラ環境のルール

### Dockerの実行方法
- ドキュメント`how-to-docker-compose.md`をリポジトリ内に配置しておくので参照しながら行うこと

### 開発時の注意
- 最初から必要最低限のパッケージなどはインストールしてあるが，自身が新たにインストールしたものは必ず**成功したコマンド**をメモしておくこと
- もし忘れてしまった際には`history`コマンドを打つことで履歴が確認できる
- `history`はすべてのコマンド履歴を表示するため，非常に効率が悪いことを念頭において作業すること
- コンテナを停止するだけではコマンド履歴は消えないが，コンテナを削除すると履歴もすべて消えるので注意すること
## 質問 (2025-09-06 05:04:07)
Djangoの環境構築をしたい

### 回答
Djangoの環境を構築するための手順を以下に示します。これにはPythonのインストールからDjangoのセットアップまで含まれています。

### 1. Pythonのインストール
DjangoはPythonで書かれているため、まずPythonをインストールします。

- **Windows**
  1. [Pythonの公式サイト](https://www.python.org/)にアクセスします。
  2. "Downloads"セクションからWindows版の最新のPythonをダウンロードします。
  3. インストーラを実行し、「Add Python to PATH」オプションにチェックを入れ、「Install Now」を選択します。

- **macOS**
  1. Homebrewがインストールされていない場合は、[Homebrewの公式サイト](https://brew.sh/index_ja)を参考にするか、ターミナルで次のコマンドを実行してインストールします。
     ```bash
     /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
     ```
  2. ターミナルを開いて次のコマンドを実行します。
     ```bash
     brew install python
     ```

- **Linux**
  1. ディストリビューションに応じて次のコマンドを実行します。
     - Ubuntu/Debian:
       ```bash
       sudo apt update
       sudo apt install python3 python3-pip
       ```
     - CentOS/RHEL:
       ```bash
       sudo yum install python3 python3-pip
       ```

### 2. 仮想環境の作成
プロジェクトごとに依存関係を管理するために、仮想環境を作成します。

1. ターミナルまたはコマンドプロンプトを開きます。
2. 任意のディレクトリに移動します（例：デスクトップ）。
3. 次のコマンドを実行して仮想環境を作成します。
   ```bash
   python -m venv myenv
   ```
   `myenv`は仮想環境の名前です。好きな名前に変更できます。

4. 仮想環境をアクティブにします。
   - **Windows**:
     ```bash
     myenv\Scripts\activate
     ```
   - **macOS/Linux**:
     ```bash
     source myenv/bin/activate
     ```

### 3. Djangoのインストール
仮想環境がアクティブな状態でDjangoをインストールします。

1. 次のコマンドを実行します。
   ```bash
   pip install django
   ```

### 4. Djangoプロジェクトの作成
Djangoをインストールしたら、プロジェクトを作成します。

1. 次のコマンドを実行します（`myproject`はプロジェクト名です）。
   ```bash
   django-admin startproject myproject
   ```

### 5. サーバーの起動
プロジェクトディレクトリに移動し、開発サーバーを起動します。

1. プロジェクトディレクトリに移動します。
   ```bash
   cd myproject
   ```
   
2. サーバーを起動します。
   ```bash
   python manage.py runserver
   ```

3. ブラウザを開き、`http://127.0.0.1:8000/`にアクセスします。Djangoのウェルカムページが表示されれば成功です。

### 6. 必要に応じてアプリケーションの作成
Djangoプロジェクト内にアプリケーションを追加したい場合は、次のコマンドを実行します（`myapp`はアプリケーション名です）。

```bash
python manage.py startapp myapp
```

### 以上がDjangoの基本的な環境構築手順です。必要に応じて、設定ファイルやアプリケーションの構成を調整してください。

---

