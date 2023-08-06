from encrypta.config.base import BaseConfig


class BadArgError(Exception):
    pass

def cutKey(fn):
    '''
        Decorator to ensure the key is cut to the correct length for the target array
    '''    
    def wrapper(*args, **kwargs):
        if len(args) == 2:
            tgt = args[0]
            key = args[1]
            if not(type(tgt) == bytearray or type(tgt) == str):
                raise BadArgError('tgt argument must be a string or a bytearray object')
            if type(key) != str:
                raise BadArgError('key argument must be a string object')
            lt = len(tgt)
            lk = len(key)
            if lt < lk:
                key = key[:lt]
            elif lt > lk:
                (q, r) = divmod(lt, lk)
                key = (key * q) + key[:r]
            newArgs = (tgt, key)
            return fn(*newArgs, **kwargs)
    return wrapper

@cutKey
def _encrypt(tgt, key: str) -> bytearray:
    '''
    tgt: could be a bytearray or a string
    '''    
    tgt = tgt if type(tgt) == bytearray else tgt.encode()
    key = key.encode()
    out = bytearray(len(tgt))
    for n, (x, y) in enumerate(zip(tgt, key)):
        out[n] = x ^ y
    return out

@cutKey
def _decrypt(tgt, key: str) -> str:
    '''
    tgt: could be a bytearray or a string
    '''       
    tgt = tgt if type(tgt) == bytearray else tgt.encode()
    key = key.encode()
    out = ''
    for x, y in zip(tgt, key):
        out += chr(x ^ y)
    return out

def encrypt(tgt: str, key: str) -> bytearray:
    '''
    Double encrypt the tgt string, first with the provided key argument and then again with the 
    encrypto version as key
    '''
    return _encrypt(_encrypt(tgt, key), BaseConfig.VERSION)

def decrypt(tgt: bytearray, key: str) -> str:
    '''
    Double decrypt the tgt bytearray, first with the encrypto version as key and then again with the
    provided key argument
    '''
    return _decrypt(_decrypt(tgt, BaseConfig.VERSION), key)