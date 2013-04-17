from interfaces import ICustomTitled


class CustomTitled(object):
   "Mix-in class for custom titling"
   
   def Title(self):
      "return a custom title"
      return ICustomTitled(self)

   def setTitle(self, title):
      "silently fail on attempts to change the title"
      return
