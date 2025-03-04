
<h2>Telegram-cli</h2>

This project uses python telegram bot api. by using command-line you can share files/documents and messages directly to your telegram bot group or can be used to import to your python code


<h6> Installation </h6>

To install cli go inside telebot_cli tool just run this command 
```bash
 pip install .
```

To install cli for exprement or for further modification use
```bash
 pip install -e .
```

<h6> Setup </h6>


```bash
 telebot-cli setting --set-token "telegram-bot-token"
```

```bash
telebot-cli setting --set-chatid "user-chat-id"`
```


<h6> Usage </h6>

Run cli-tool at current directory where file located

```bash
 telebot-cli sendfile -f "file-name"
```


#Usage in github actions

1) 📦 Cloning telebot-cli<br/>

```yml
      - name: 📦 Cloning telebot-cli
        run: git clone https://github.com/Mahesh-R-Mesta/telebot_cli.git
```
2) 📦 Installing telebot-cli<br/>

```yml
      - name: 📦 Installing telebot-cli
        run: |
          cd telebot_cli
          pip install .
          cd ..
          rm -r telebot_cli
```
3) Send file through telegram bot<br/>

```yml
      - name: Send file through telegram bot
        env:
          TELEGRAM_TOKEN: ${{ secrets.TELEGRAM_TOKEN }}
          TELEGRAM_CHAT_ID: ${{secrets.TELEGRAM_CHAT_ID}}
        run: |
          cd build/app/outputs/flutter-apk/
          telebot-cli setting --set-token "$TELEGRAM_TOKEN"
          telebot-cli setting --set-chatid "$TELEGRAM_CHAT_ID"
          telebot-cli sendfile -f "app-release.apk"
```
