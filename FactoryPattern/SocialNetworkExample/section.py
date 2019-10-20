from abc import ABCMeta, abstractmethod


class Section(metaclass=ABCMeta):
    """
    Abstract Base class for all sections
    """
    @abstractmethod
    def describe(self):
        """
        Abstract method insures all Sections describe themselves
        :return:
        """
        pass


class PersonalSection(Section):
    def describe(self):
        print("Personal Section")


class AlbumSection(Section):
    def describe(self):
        print("Album Section")


class PatentSection(Section):
    def describe(self):
        print("Patent Section")


class PublicationSection(Section):
    def describe(self):
        print("Publication Section")

