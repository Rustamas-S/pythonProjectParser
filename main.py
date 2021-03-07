import re
class Employee:
class DataParser:
    def __init__(self, path, parsed_fields):
        self.path = path
        self.instructions_list = []
        for parsed_key, regex_expression in parsed_fields.items():
            self.instructions_list.append((parsed_key, regex_expression))
            #print(self.instructions_list)
    def parse_file(self):
        file_content = self.read_file()
        results = []
        for line in file_content:
            line_data = dict()
            for field, regex in self.instructions_list:
                match = re.search(regex, line) and re.search(regex, line)[0] or ''
                line_data[field] = match
            results.append(line_data)
        return results
    def read_file(self):
        file_content_list = []
        with open(self.path) as file_data:
            for line in file_data:
                file_content_list.append(line)
        return file_content_list
parser = DataParser(
    "C:\\users\\miros\\tekst.txt",
    {
        "email": r'[\w\.-]+@[\w\.-]+',
        "telephone": r'[\d|\-]{2,23}'
    }
)
print(parser.read_file())
print(parser.parse_file())