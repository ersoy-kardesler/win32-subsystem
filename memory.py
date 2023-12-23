class Memory:
    def __init__(self, size):
        self.memory_image = [0] * size

    def get_memory_item(self, address):
        return self.memory_image[address]

    def set_memory_item(self, address, value):
        if value < 0x00 and value > 0xff:
            return 1
        else:
            self.memory_image[address] = value
            return 0
