from xmlrpc.client import DateTime
from user import User
from page import Page
class Comic:
    def __init__(self, name, owner):
        self.__name = name
        self.__owner = owner
        self.__pages = []
        self.__likes = 0
        self.__like_enabled = False
        self.__comment_enabled = False
        self.__visible = False
    def setName(self, name):
        self.__name = name
    def getName(self):
        return self.__name
    def setOwner(self, owner):
        self.__owner = owner
    def getOwner(self):
        return self.__owner.getName()
    def setPublished(self):
        #set by date and time current
        self.__published = DateTime.now()
    def getPublished(self):
        return self.__published
    def addPage(self, page):
        self.__pages.append(page)
    def getPages(self):
        return self.__pages
    def getLikes(self):
        return self.__likes
    def addLike(self):
        self.__likes += 1
    def removeLike(self):
        self.__likes -= 1
    def likeEnable(self):
        self.__like_enabled = True
    def likeDisable(self):
        self.__like_enabled = False
    def isLikeEnabled(self):
        return self.__like_enabled
    def commentEnable(self):
        self.__comment_enabled = True
    def commentDisable(self):
        self.__comment_enabled = False
    def isCommentEnabled(self):
        return self.__comment_enabled
    def setVisible(self):
        self.__visible = True
    def setInvisible(self):
        self.__visible = False
    def isVisible(self):
        return self.__visible
    def create(self, ):
        self.likeEnable()
        self.commentEnable()
        self.setVisible()
        self.setPublished()