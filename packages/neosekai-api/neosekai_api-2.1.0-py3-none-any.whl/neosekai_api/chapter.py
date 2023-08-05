from neosekai_api.novel import Novel
import requests
from bs4 import BeautifulSoup
from neosekai_api.helper import heavy_translate


class NovelChapter:
    '''
    NovelChapter object

    :params _url : The Mangadex Chapter URL
    '''

    def __init__(self, _url: str) -> None:
        self.url = _url
        self.__response_object = requests.get(self.url, timeout=10)

    def chapter_details(self, name_only=False):
        """
        returns chapter details : 

        - chapter volume
        - chapter name
        - url
        - chapter release date

        In the given order in JSON format
        - If option name_only is set to True, the function will only return the name of the chapter
        - This makes the program much faster as it has to go through a bunch of processes in order to get the other details 
        """
        if not name_only:
            novel_url_ = self.url.split('neosekaitranslations.com/novel/')[-1]
            novel_name = novel_url_[:novel_url_.index('/')]
            novel_url = f"https://www.neosekaitranslations.com/novel/{novel_name}/"
            novel = Novel(novel_url)
            index_page = novel.get_index_page()
            for i in index_page:
                if index_page[i]['url'] == self.url:
                    return index_page[i]
        else:
            soup = BeautifulSoup(self.__response_object.content, 'lxml')
            heading = soup.find('li', attrs={'class': ['active']})
            return heading.text.strip()

    def get_chapter_content(self, fancy=True):
        """
        returns main chapter content in JSON format

        JSON format:
        ```json
            {
                "1" : {
                    "type" : '...', "content" : '...'
                }
            }
        ```
        - each key will be a paragraphs
        - ```type```  can have a value of ```text``` for textual content
        - ```type``` can have a value of ```img``` if the content is an image. link to the image will be provided in ```content```

        """
        soup = BeautifulSoup(self.__response_object.text, 'lxml')
        div = soup.find('div', attrs={'class': 'text-left'})
        paras = div.find_all('p')
        content = {}
        n = 1
        for i in paras:
            if i.span != None:
                content[str(n)] = {'type': 'text',
                                   'content': i.span.text.strip() if fancy else heavy_translate(i.span.text.strip())}
                n += 1
            elif i.img != None:
                content[str(n)] = {'type': 'img', 'content': i.img['src']}
                n += 1
            else:
                continue
        return content


print(NovelChapter('https://www.neosekaitranslations.com/novel/transfer-student/chapter-114/').chapter_details(name_only=True))
