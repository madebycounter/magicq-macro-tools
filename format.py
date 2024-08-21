class Hex:
    @staticmethod
    def format(n, fill=4):
        return "{:x}".format(n).zfill(fill)

    @staticmethod
    def parse(s):
        return int(s, 16)


class String:
    @staticmethod
    def format(s):
        return '"%s"' % s

    @staticmethod
    def parse(s):
        return s.strip('"')
