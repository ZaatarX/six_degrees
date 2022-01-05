class Content:
    """
    Common base class for all articles/pages
    """

    def __init__(self, topic, url, title, body):
        self.topic = topic
        self.url = url
        self.title = title
        self.body = body

    def print(self):
        """
        Flexible printing function controls output
        """
        print(f'New article found for topic: {self.topic}')
        print(f'URL: {self.url}')
        print(f'TITLE: {self.title}')
        print(f'BODY:\n{self.body}')
