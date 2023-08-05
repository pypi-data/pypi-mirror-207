import json
import requests
from urllib.parse import urlparse

from .utils.config import K12Config
from .utils.mqtt_client import K12MqttClient
from .utils.attachment import Attachment

from .utils.log import setup_logger

class CommandHandler:
    def __init__(self):
        self.commands = {}

    def register_command(self, command, func):
        self.commands[command] = func

    def handle_command(self, command, *args, **kwargs):
        if command in self.commands:
            return self.commands[command](*args, **kwargs)
        else:
            return None

class MsgType:
    Text = "Text"
    Image = "Image"
    Audio = "audio"
    Document = "Document"
    Sticker = "Sticker"


class ChatMessage:
    def __init__(self, data):
        self.mode = data.get("Mode", "")
        self.msg_id = data.get("MsgID", "")
        self.room_id = data.get("RoomID", "")
        self.msg_type = data.get("MsgType", "")
        self.msg_body = data.get("MsgBody", "")
        self.send_user_id = data.get("SendUserID", "")
        self.send_user_name = data.get("SendUserName", "")
        self.send_user_image = data.get("SendUserImage", "")
        self.timestamp = data.get("Timestamp", 0)

    def __str__(self):
        return f"ChatMessage(Mode={self.mode}, MsgID={self.msg_id}, RoomID={self.room_id}, MsgType={self.msg_type}, MsgBody={self.msg_body}, SendUserID={self.send_user_id}, SendUserName={self.send_user_name}, SendUserImage={self.send_user_image}, Timestamp={self.timestamp})"


class BOT:
    # K12 class 的實現
    def __init__(self, config_file='config/k12.yaml') -> None:
        self.logger = setup_logger('chatbot')

        self.header = {
            'Referer': f'https://k12.54ucl.com/RoomSelection'}

        self.client_msg_history = {}

        self.config = K12Config(config_file)
        # 載入設定
        # 這邊是存取資料庫的部分
        bot = self.config.get('bot', {})
        # 防止重複
        self.duplicate = []
        self.logger.info('K12 database config loaded')
        # 這邊是存取網站的部分
        website = self.config.get('website', {})
        self.host = website['host']
        self.GetMsg = website['GetMsg']
        self.GetMsgHistory = website['GetMsgHistory']
        self.GetContent = website['GetContent']
        self.GetTicketID = website['GetTicketID']
        self.SendMeg = website['SendMeg']
        self.GetRoomInfo = website['GetRoomInfo']
        self.GetRoomName = website['GetRoomName']
        self.ImageSave = website['ImageSave']
        self.DocumentSave = website['DocumentSave']
        self.logger.info('K12 website config loaded')
        # 這邊是存取mqtt的部分
        k12mqtt = self.config.get('mqtt', {})
        self.logger.info('K12 mqtt config loaded')
        # 建立mqtt client
        self.client = K12MqttClient(k12mqtt, client_id=str("mqttjs_daa97e1a"), transport=k12mqtt['transport'])
        # 初始化msg
        self.chat_msg = ChatMessage({})
    
    def run(self):
        self.client.run(self.default_on_connect, self.default_on_message)
        self.logger.info('K12 mqtt client start', exc_info=True)

    def get_last_msg_id(self):
        payload = {"RoomID": "02"}
        data = requests.post(f"{self.host}{self.GetMsg}",
                             headers=self.header, json=payload).json()
        return {
            'MsgList': [data['List'][-1]],
            'Timestamp': data['Timestamp']
        }

    def get_last_msg_content(self):
        data = requests.post(f"{self.host}{self.GetContent}",
                             headers=self.header, json=self.get_last_msg_id()).json()
        data = json.loads(data['MsgBodyList'][0])
        self.logger.info(f"Last Message Content: {data}")
        return data['MsgBody']
    
    def get_ticket(self):
        return requests.post(f"{self.host}{self.GetTicketID}", headers=self.header).json()

    def set_chat_bot_info(self, SendUserID, SendUserName, SendUserImage):
        self.SendUserID = SendUserID
        self.SendUserName = SendUserName
        self.SendUserImage = SendUserImage

    def image_saver(self, roomid, url):
        attachment = Attachment(url)
        attachment_data = attachment.get_attachment()
        files = {"Image": attachment_data}
        data = requests.post(f"{self.host}{self.ImageSave}",
                             headers={
                                 'Referer': f'{self.host}/Chat/{roomid}'
                             },files=files).json()
        #ErrorCode
        if data.get('ErrorCode', 0) == 0:
            return data.get('FileName', '')
        else:
            raise Exception(f"Image Save Error: {data.get('ErrorCode', '')}")
        
    def document_saver(self, roomid, url):
        attachment = Attachment(url)
        attachment_data = attachment.get_attachment()
        files = {"Document": attachment_data}
        data = requests.post(f"{self.host}{self.DocumentSave}",
                             headers={
                                 'Referer': f'{self.host}/Chat/{roomid}'
                             },files=files).json()
        #ErrorCode
        if data.get('ErrorCode', 0) == 0:
            return {
                "FileName":data.get('FileName', ''),
                "FileSize":len(attachment_data[1]),
                "RawName":attachment_data[0]
            }
        else:
            raise Exception(f"Image Save Error: {data.get('ErrorCode', '')}")

    def send_msg(self, roomid, text, msg_type=MsgType.Text):
        tit = self.get_ticket()['Timestamp']
        payload = {
            "RoomID": f"{roomid}",
            "SendUserID": self.SendUserID,
            "SendUserName": self.SendUserName,
            "SendUserImage": self.SendUserImage,
            "id": f"{roomid}-{tit}",
            "MsgType": msg_type,
            "MsgBody": text,
            "Timestamp": tit
        }
        if msg_type == MsgType.Image:
            # 如果是圖片
            msg_body = self.image_saver(roomid, text)
            payload["MsgBody"] = msg_body
        elif msg_type == MsgType.Document:
            # 文字
            msg_body = self.document_saver(roomid, text)
            payload["MsgBody"] = msg_body
        else:
            # 如果是文字
            payload["MsgBody"] = text
        data = requests.post(f"{self.host}{self.SendMeg}",
                             headers={
                                 'Referer': f'{self.host}/chat/{roomid}'
                             }, json=payload).json()
        self.logger.info(f"傳出訊息：{data}")
    
    def send_text(self, roomid, text):
        self.send_msg(roomid, text, MsgType.Text)

    def send_image(self, roomid, image_path):
        self.send_msg(roomid, image_path, MsgType.Image)
    
    def send_document(self, roomid, doc_path):
        self.send_msg(roomid, doc_path, MsgType.Document)

    def get_room_info(self, id):
        data = requests.post(f"{self.host}{self.GetRoomName}",
                             headers=self.header, json={'RoomidList': [id]}).json()
        return data
    @classmethod
    def on_connect(cls, func=None):
        if func:
            cls._default_on_connect = func
        return func

    def _default_on_connect(self, client, userdata, flags, rc):
        # Default on_connect behavior
        pass

    def default_on_connect(self, client, userdata, flags, rc):
        self._default_on_connect(client, userdata, flags, rc)

    def default_on_message(self, client, userdata, msg):
        self.logger.debug(f"Message received: {msg.payload.decode()}")
        data = json.loads(msg.payload.decode())
        self.process_message(data)
    
    def process_message(self, data):
        _this_msg = ChatMessage(data)
        # 防止重複
        if _this_msg.msg_id not in self.duplicate:
            # 先清空重複訊息的 list，避免 list 過大
            self.duplicate.clear()
            # 然後把這個訊息的 msg_id 加入重複訊息的 list，這樣就不會重複處理
            self.duplicate.append(_this_msg.msg_id)
            self.display_log(data)
            self.chat_msg = _this_msg
            # 當處理完訊息後，呼叫 on_processed_message
            self._on_processed_message(self.chat_msg)
    
    @classmethod
    def on_processed_message(cls, func=None):
        if func:
            cls._on_processed_message = func
        return func

    def _on_processed_message(self, chat_msg):
        pass

    def display_log(self, data):
        # display_log 的實現
        self.logger.debug(f"""
            message: {data['MsgBody']}
            from: {data['SendUserName']}
            at: {data['Timestamp']}
            id: {data['SendUserID']}
            room: {data['RoomID']}
            type: {data['MsgType']}
            msgid: {data['MsgID']}
            """)


    
        