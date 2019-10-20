from abc import ABCMeta, abstractmethod
from FactoryPattern.SocialNetworkExample.section import PersonalSection
from FactoryPattern.SocialNetworkExample.section import PatentSection
from FactoryPattern.SocialNetworkExample.section import AlbumSection
from FactoryPattern.SocialNetworkExample.section import PublicationSection

class Profile(metaclass=ABCMeta):
    def __init__(self):
        self.sections = []
        self.createProfile()

    @abstractmethod
    def createProfile(self):
        pass

    def getSections(self):
        return self.sections

    def addSections(self, section):
        self.sections.append(section)


class linkedin(Profile):
    def createProfile(self):
        self.addSections(PersonalSection)
        self.addSections(PatentSection)
        self.addSections(PublicationSection)

class facebook(Profile):
    def createProfile(self):
        self.addSections(PersonalSection)
        self.addSections(AlbumSection)