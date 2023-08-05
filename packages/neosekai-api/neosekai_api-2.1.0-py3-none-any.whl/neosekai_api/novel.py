import requests
from bs4 import BeautifulSoup
from neosekai_api.helper import heavy_translate

class Novel:
    """
    Novel Object
    """

    def __init__(self, url):
        self.url = url
        self._response_object = requests.get(self.url, timeout=10)

    def get_novel_tags(self):
        '''
        returns novel tags as ```dict```
        '''
        soup = BeautifulSoup(self._response_object.content, 'lxml')

        # finding title
        title = soup.find('title').text.split(' - NeoSekai')[0]

        # finding rating
        rating = soup.find('span', attrs={'id': 'averagerate'}).parent.text + \
            'out of ' + soup.find('span', attrs={'id': 'countrate'}).text

        # finding everything else
        novel_tags = {'title': title, 'rating': rating}
        post_content_divs = soup.find_all(
            'div', attrs={'class': 'post-content_item'})

        for i in post_content_divs:
            if post_content_divs.index(i) == 0:
                continue
            else:
                x = i.children
                for i in x:
                    if i.name == 'div':
                        if i['class'] == ['summary-heading']:
                            j = i.find_next(
                                'div', attrs={'class': 'summary-content'})
                            key = str(i.text).strip()
                            value = str(j.text).strip()

                            if key == 'Rank':
                                key = 'rank'
                            elif key == 'Alternative':
                                key = 'alternative_titles'
                                value = value.split(', ')
                            elif key == 'Author(s)':
                                key = 'authors'
                                value = value.split(', ')
                            elif key == 'Genre(s)':
                                key = 'genre'
                                value = value.split(', ')
                            elif key == 'Tag(s)':
                                key = 'tags'
                                value = value.split(', ')
                            elif key == 'Release':
                                key = 'release'
                            elif key == 'Status':
                                key = 'status'
                            else:
                                continue

                            novel_tags[key] = value

        return novel_tags

    def get_synopsis(self, fancy=True):
        """
        returns the synopsis text

        fancy : if False, replaces all fancy punctuation marks with regular ones.
        """
        soup = BeautifulSoup(self._response_object.content, 'lxml')
        synopsis = soup.find('div', attrs={
            'class': ['summary__content', 'show-more']}).text

        if fancy:
            return synopsis
        else:
            return heavy_translate(synopsis)

    def get_index_page(self):
        """
        returns the chapter list in JSON format

        JSON : 
        ```json
            {
                "1" : {
                    "volume" : '...',
                    "chapter_name" : '...',
                    "url" : '...',
                    "release_date" : '...'
                },

                "2" : {'...'}
            }
        
        ```
        - if novel is not categorised into volumes, volume will be an empty string
        """
        content_dict = {}
        url = 'https://www.neosekaitranslations.com/wp-admin/admin-ajax.php'
        soup_ = BeautifulSoup(self._response_object.content, 'lxml')
        data_id = soup_.find(
            'div', attrs={'id': ['manga-chapters-holder']})['data-id']
        data = {'action': 'manga_get_chapters', 'manga': data_id}
        soup_2 = BeautifulSoup(requests.post(url, data).content, 'lxml')
        li_with_children = list(soup_2.find_all('li', attrs={'class' : ['parent', 'has-child']}))

        if li_with_children:
            vol_list = []

            for i in soup_2.find_all('a', attrs={'class' : ['has-child']}):
                vol_num = i.text.strip().split()[1]
                vol_list.append(int(vol_num))

            if max(vol_list) != vol_list[0]:
                pass
            else:
                li_with_children.reverse()
            n = 1
            for index,i in enumerate(li_with_children):
                lines = list(i.find_all('li', attrs={'class' : ['wp-manga-chapter']}))
                lines.reverse()
                for j in lines:
                    link = j.a['href']
                    name = j.a.text.strip()
                    date = j.span.text.strip()
                    mini_dict = {'volume' : str(index + 1), 'chapter_name' : name, 'url' : link, 'release_date' : date}
                    content_dict[str(n)] = mini_dict
                    n += 1
        else:
            lines = list(soup_2.find_all('li', attrs={'class' : ['wp-manga-chapter']}))
            lines.reverse()
            n = 1
            for j in lines:
                    link = j.a['href']
                    name = j.a.text.strip()
                    date = j.span.text.strip()
                    mini_dict = {'volume' : "", 'chapter_name' : heavy_translate(name), 'url' : link, 'release_date' : date}
                    content_dict[str(n)] = mini_dict
                    n += 1
        
        return content_dict
