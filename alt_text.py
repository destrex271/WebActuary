from markup_content import MarkupContent
from directory_create_module import create_dir


class AltText:

    def __init__(self, url):
        mk = MarkupContent(url=url)
        self.final_list = []
        self.content = mk.get_markup_content()
        self.folder_name = "alt_text"
        create_dir(self.folder_name)

    def alt_check(self):
        tag_list = self.content.findAll("img")
        i = 1
        for tag in tag_list:
            if not tag.has_attr('alt'):
                self.final_list.append(f"{i} : {str(tag)}")
                i += 1
        st = ""
        for item in self.final_list:
            st += item + "\n"
        self.write_to_file(st.encode('utf-8'))

    def write_to_file(self, content):
        with open(f"{self.folder_name}/alt_text.txt", "wb") as file:
            file.write(content)
            file.close()

