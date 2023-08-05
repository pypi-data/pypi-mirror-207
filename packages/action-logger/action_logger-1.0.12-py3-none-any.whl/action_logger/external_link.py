import dash_bootstrap_components as dbc
import base64


class External_Link(dbc.DropdownMenuItem):
    def __init__(self, href, **kwargs):
        self.real_href = href
        self.show_link = '/external_link/' + kwargs['children'] + '/' + base64.urlsafe_b64encode(href.encode()).decode()
        if 'href' in kwargs:
            del kwargs['href']
        super().__init__(href=self.show_link, **kwargs)
