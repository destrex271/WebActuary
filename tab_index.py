from markup_content import MarkupContent
from directory_create_module import create_dir


class TabIndex:

    def __init__(self, url):
        mk = MarkupContent(url=url)
        self.final_list = []
        self.folder_name = "tab_index"
        create_dir(self.folder_name)
        self.content = mk.get_markup_content()

    def tab_index_check(self):

        tags = ['button', 'a', 'input']
        for tg in tags:
            cora = False
            if tg == 'a':
                cora = True
            tag_list = self.content.find_all(tg)
            for tag in tag_list:
                if not tag.has_attr('tabindex'):
                    if cora and not tag.has_attr('href'):
                            continue
                    self.final_list.append(str(tag))
        st = ""
        for item in self.final_list:
            st += item + "\n"
        self.write_to_file(st.encode("utf-8"))

    def write_to_file(self, content):
        with open(f"{self.folder_name}/tab_index.txt", "wb") as file:
            file.write(content)
            file.close()

