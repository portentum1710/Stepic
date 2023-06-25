class Translator:
    def add(self, eng, rus):
        if 'tr' not in self.__dict__:
            self.tr = {}

        self.tr.setdefault(eng, [])
        # здесь продолжайте метод add

    def remove(self, eng):
        # здесь продолжайте метод remove

    def translate(self, eng):
        # здесь продолжайте метод translate

