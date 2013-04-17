from plone.app.content.interfaces import INameFromTitle
from zope.interface.declarations import implementer
from interfaces import ICustomTitle

class INameFromCustomTitle(INameFromTitle):
    def title():
        """Return a custom title from ICustomTitle"""


@implementer(INameFromCustomTitle)
class NameFromCustomTitle(object):

    def __init__(self, context):
        self.context = context

    @property
    def title(self):
        return ICustomTitle(self.context)
