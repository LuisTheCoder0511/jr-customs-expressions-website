import random, string


class CodeGenerator:
    def __init__(self, ids):
        self.codes = set()
        self.codes.update(ids)
        print(f"IDs: {self.codes}")
        self.size = 12

    def __generate__(self):
        code = ""
        index = 0
        chars = string.ascii_letters + string.digits
        while index < self.size:
            code += "".join(random.choice(chars))
            index += 1
        if self.__validate__(code):
            return code
        return self.__generate__()

    def __validate__(self, code: str):
        binary = bytes(code, "ascii")
        if self.codes.__contains__(binary) or not code.isalnum() or len(code) < self.size:
            return False
        self.codes.add(binary)
        return True
