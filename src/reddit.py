import praw

class API(object):
    # initialize reddit client
    def __init__(self):
        self.r = praw.Reddit(user_agent='listentothis blog bot by enkarta')
        
    # get new posts from a subreddit
    def getNewPosts(self, subreddit = 'listentothis', limit = 100, after = None):
        if(after):
            posts = self.r.get_subreddit(subreddit).get_new(limit=limit, after=after)
        else:
            posts = self.r.get_subreddit(subreddit).get_new(limit=limit)
        
        return [post for post in posts]