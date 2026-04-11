# """
# This is HtmlParser's API interface.
# You should not implement it, or speculate about its implementation
# """
#class HtmlParser(object):
#    def getUrls(self, url):
#        """
#        :type url: str
#        :rtype List[str]
#        """

class Solution:
    """
    DROPBOX:
    explore:
        - get urls from calling HtmlParser.getUrls(startUrl)
        - have a list of urls and return only those that match the same
        hostname as startUrl
        - we consider trailing /s as different urls

     brainstorm:
        - preprocess starting url by tokenising url split on /
        - hash tokens[2] to original urls when get urls back
        - if we see a tokenised that matches starting but doesn't equal
        string it's different  
    """
    def crawl(self, startUrl: str, htmlParser: 'HtmlParser') -> List[str]:
        def get_hostname(url):
            return url.split("/")[2]

        start_hostname = get_hostname(startUrl)
        visited = set()

        def dfs(url, htmlParser):
            visited.add(url)

            for next_url in htmlParser.getUrls(url):
                if (get_hostname(next_url) == start_hostname and 
                next_url not in visited):
                    dfs(next_url, htmlParser)

        dfs(startUrl, htmlParser)

        return visited
