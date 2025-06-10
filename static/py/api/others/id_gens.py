import random, time

def generator(select_func, size: int):
    CHARSET = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-_"
    while True:
        time.sleep(0.05)
        id_var = ''.join(random.choice(CHARSET) for _ in range(size))
        if not select_func(id_var):
            return id_var
