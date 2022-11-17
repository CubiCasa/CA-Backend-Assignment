import enum


class UserTypes(enum.Enum):
    Student = 1
    Volunteer = 2


class Genders(enum.Enum):
    Male = 1
    Female = 2


class TranslationText:
    MathIsRequired = 'Math is required'
    PhysicsIsRequired = 'Physics is required'
    ChemistryIsRequired = 'Chemistry is required'
    BiologyIsRequired = 'Biology is required'
    LiteratureIsRequired = 'Literature is required'
    HistoryIsRequired = 'Literature is required'
    GeographyIsRequired = 'Geography is required'
    PhylosophyIsRequired = 'Phylosophy is required'
    ArtIsRequired = 'Art is required'
    ForeignIsRequired = 'Foreign is required'
    JobIsRequired = 'Job is required'
    UserNotFound = 'User not found'
    PerformanceNotFound = 'Performance not found'
    PleaseInputAtLeastOnePerformanceBeforeYouUpdateYourJob = 'Please input at least one performance before you update your job'


class Pagination:
    DefaultLimit = 20
    DefaultPage = 1
