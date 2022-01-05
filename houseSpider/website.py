class Website:
    """
    Contains information about website structure
    Stores information on how to collect the data
    """

    def __init__(self, name, url, searchUrl, resultUrl, resultListing,      absoluteUrl, titleTag, bodyTag):
        self.name = name
        self.url = url
        self.titleTag = titleTag
        self.bodyTag = bodyTag
        self.searchUrl = searchUrl
        self.resultUrl = resultUrl
        self.resultListing = resultListing
        self.absoluteUrl = absoluteUrl
