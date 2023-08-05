import sqlite3


class SQLiteHandler:
    def __init__(self, db_name):
        self.db_name = db_name

    def _connect(self):
        return sqlite3.connect(self.db_name)

    def subscribe(self, user_id):
        conn = self._connect()
        c = conn.cursor()
        c.execute("CREATE TABLE IF NOT EXISTS users (tgID text)")
        c.execute("SELECT tgID FROM users WHERE tgID=?", (user_id,))
        msg = '重複'
        if not c.fetchone():
            c.execute("INSERT INTO users (tgID) VALUES (?)", (user_id,))
            conn.commit()
            msg = '成功'
        conn.close()
        return f"您的TG ID:{user_id} {msg} 訂閱小雞訊息！"

    def get_subscribed_users(self):
        conn = self._connect()
        c = conn.cursor()
        c.execute("SELECT tgID FROM users")
        subscribed_users = [row[0] for row in c.fetchall()]
        conn.close()
        return subscribed_users

    def add_chat_message(self, message):
        conn = self._connect()
        c = conn.cursor()
        table_check = "SELECT name FROM sqlite_master WHERE type='table' AND name='chat';"
        if not c.execute(table_check).fetchone():
            c.execute('''CREATE TABLE chat
                         (MsgID text, RoomID text, MsgType text, MsgBody text,
                         SendUserID text, SendUserName text, SendUserImage text,
                         Timestamp integer)''')
            print("Chat table created.")
        c.execute("SELECT * FROM chat WHERE MsgID=?", (message['MsgID'],))
        if not c.fetchone():
            c.execute("INSERT INTO chat VALUES (?,?,?,?,?,?,?,?)", (
                str(message['MsgID']),
                str(message['RoomID']),
                str(message['MsgType']),
                str(message['MsgBody']),
                str(message['SendUserID']),
                str(message['SendUserName']),
                str(message['SendUserImage']).strip(
                ) if message['SendUserImage'] else str(None),
                message['Timestamp']
            ))
            conn.commit()
            #print("Chat message added.")
            conn.close()
            return True
        else:
            conn.close()
            return False

    def get_chat_messages(self, msg_type="Text"):
        conn = self._connect()
        c = conn.cursor()
        c.execute(
            "SELECT MsgID, MsgBody, SendUserName FROM chat WHERE MsgType=?", (msg_type,))
        messages = c.fetchall()
        conn.close()
        return messages

    def add_user_info(self, tgID, SendUserID, SendUserName, SendUserImage):
        conn = self._connect()
        c = conn.cursor()
        c.execute(
            "CREATE TABLE IF NOT EXISTS k12Users (tgID text, SendUserID text, SendUserName text, SendUserImage text)")
        c.execute("SELECT tgID FROM k12Users WHERE tgID=?", (tgID,))
        user = c.fetchone()

        if user:
            print("User already exists")
            return False
        else:
            c.execute("INSERT INTO k12Users (tgID, SendUserID, SendUserName, SendUserImage) VALUES (?, ?, ?, ?)",
                      (tgID, SendUserID, SendUserName, SendUserImage))
            conn.commit()
            print("User added successfully")
            return True

    def get_user_info(self, tgID):
        conn = self._connect()
        c = conn.cursor()
        c.execute("SELECT * FROM k12Users WHERE tgID=?", (tgID,))
        user_info = c.fetchone()
        conn.close()
        if user_info:
            return user_info
        else:
            return None

    def clear_k12_users_table(self):
        conn = self._connect()
        c = conn.cursor()
        c.execute("DROP TABLE IF EXISTS k12Users")
        conn.commit()
        conn.close()
        print("k12Users 表已被清除。")
