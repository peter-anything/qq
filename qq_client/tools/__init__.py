class Tool(object):
    @staticmethod
    def get_qss_from_file(file_path):
        with open(file_path) as f:
            lines = f.readlines()
            return ''.join(filter(None, map(lambda line: ''.join(line.strip().split()), lines)))