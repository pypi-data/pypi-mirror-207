# 12

# **NKUST UCL K12 ChatBot**

## **簡介**

NKUST UCL K12 ChatBot 是一個基於 K12 API 的 ChatBot，它能夠自動發送文字訊息、圖片、文件，接收到來自聊天室的訊息，支援消息歷史查詢。

## **安裝**

使用 pip 安裝：

```bash
pip install nkust-ucl-k12-bot

```

## **用法**

### **初始化 K12 Bot**

```python
from nkust_ucl_k12_bot import K1
custom_k12 = K12(config_file='config/k12.yaml')
custom_k12.set_chat_bot_info(
    SendUserID="my_id",
    SendUserName="ChatGPT_ucl",
    SendUserImage="https://upload.wikimedia.org/wikipedia/commons/thumb/0/04/ChatGPT_logo.svg/512px-ChatGPT_logo.svg.png"
)

```

### **發送文字訊息**

```python
custom_k12.send_text(roomid="12345", text="你好！")

```

### **發送圖片**

```python
# image_path可以是網址或是本地路徑
custom_k12.send_image(roomid="12345", image_path="/path/to/image.png")

```

### **發送文件**

```
# doc_path可以是網址或是本地路徑
custom_k12.send_document(roomid="12345", doc_path="/path/to/document.pdf")

```

### **接收訊息**

註冊 **`on_processed_message`** 處理方法以接收來自聊天室的訊息：

```

@K12.on_processed_message
def my_custom_on_processed_message(self, chat_msg):
    # ... 自定義的 on_processed 行為 ...
    # ChatMsg 為訊息物件

```

### **自定義 on_connect 行為**

```

@K12.on_connect
def my_custom_on_connect(self, client, userdata, flags, rc):
    # ... 自定義的 on_connect 行為 ...
    # self.client.mqttSubscribe為訂閱的主題
    client.subscribe(self.client.mqttSubscribe)
    print("開始訂閱")

```

## **如何貢獻**

1. Fork 專案
2. 創建新的分支 (**`git checkout -b feature/fooBar`**)
3. 提交你的修改 (**`git commit -am 'Add some fooBar'`**)
4. 推送到分支 (**`git push origin feature/fooBar`**)
5. 創建一個新的 Merge Request

## **License**

**[MIT](https://choosealicense.com/licenses/mit/)**