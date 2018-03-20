"""Super thin wrapper of Facebook API."""
import facebook


class FacebookClient:
    """Simple class to get basic information on Facebook Pages."""

    def __init__(self, access_token):
        """Initialize GraphAPI object."""
        self.graph = facebook.GraphAPI(access_token=access_token,
                                       version='2.7')

    def get_page_fan_count(self, page_id):
        """Return number of fans for the given page."""
        page = self.graph.get_object(id=page_id, fields='fan_count')
        return page['fan_count']

    def get_page_about(self, page_id):
        """Return some information about the given page."""
        page = self.graph.get_object(id=page_id, fields='about')
        return page['about']
