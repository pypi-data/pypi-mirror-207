from dollar.dollarobject import DollarObject


class DollarObjectImpl(DollarObject):

    def __init__(self, content, path, output_path, target_path):
        super().__init__(path, output_path, target_path)

        self.content = content.split("\n")
        self.header_end = 0
        self.header = None
        self.unparsed_header = {}
        self.raw_formats = []
        self.input_formats = []
        self.output = ""

    def get_id(self):
        if self.header is None:
            return self.unparsed_header["id"]
        return self.header["id"]

    def get_type(self):
        if self.header is None:
            return self.unparsed_header["type"]
        return self.header["type"]

    def get_content(self) -> str:
        return "\n".join(self.content)

    def get_header(self):
        return self.header

    def set_header(self, header):
        self.header = header

    def get_header_end(self):
        return self.header_end

    def set_header_end(self, header_end):
        self.header_end = header_end

    def get_unparsed_header(self):
        return self.unparsed_header

    def set_unparsed_header(self, unparsed_header: str):
        self.unparsed_header = unparsed_header

    def get_content_without_header(self):
        return "\n".join(self.content[self.header_end + 1:])

    def set_content_without_header(self, content_body: str):
        content_body_split = content_body.split("\n")
        self.content = self.content[:self.header_end + 1] + content_body_split

    def get_output(self) -> str:
        return self.output

    def set_output(self, output: str):
        self.output = output

    def get_path(self):
        return self.path

    def get_output_path(self):
        return self.output_path

    def get_target_path(self):
        return self.target_path

    def get_raw_formats(self):
        return self.raw_formats

    def set_raw_formats(self, raw_formats):
        self.raw_formats = raw_formats

    def get_input_formats(self):
        return self.input_formats

    def set_input_formats(self, input_formats):
        self.input_formats = input_formats

    def equals(self, dollar_object):
        if not super().equals(dollar_object):
            return False
        if self.content == None:
            if dollar_object.content == None:
                return True
            return False
        if dollar_object.content == None or len(self.content) != len(dollar_object.content):
            return False
        for i in range(0, len(self.content)):
            self_line = self.content[i]
            do_line = dollar_object.content[i]
            if self_line != do_line:
                return False
        return True
