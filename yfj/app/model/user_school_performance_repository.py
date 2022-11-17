"""It contains UserRepository class."""
from sqlalchemy import func

from .models import User, UserSchoolPerformance
from .repository import Repository
from ..base.constants import UserTypes


class UserSchoolPerformanceRepository(Repository):
    """It Contains specific method related to de User
    model to do operation in the database.
    """

    def __init__(self):
        Repository.__init__(self, UserSchoolPerformance)

    def get_by_id(self, id: str) -> UserSchoolPerformance:
        return self.session.query(UserSchoolPerformance).filter_by(id=id).filter_by(deleted_at=None).first()

    def get_by_user_id(self, id: str) -> UserSchoolPerformance:
        return self.session.query(UserSchoolPerformance).filter_by(user_id=id).filter_by(deleted_at=None).all()

    def get_sum_by_user(self, id) -> [UserSchoolPerformance]:
        return self.session.query(UserSchoolPerformance.user_id, func.avg(UserSchoolPerformance.math).label('math'),
                                  func.avg(UserSchoolPerformance.physics).label('physics'),
                                  func.avg(UserSchoolPerformance.chemistry).label('chemistry'),
                                  func.avg(UserSchoolPerformance.biology).label('biology'),
                                  func.avg(UserSchoolPerformance.literature).label('literature'),
                                  func.avg(UserSchoolPerformance.history).label('history'),
                                  func.avg(UserSchoolPerformance.geography).label('geography'),
                                  func.avg(UserSchoolPerformance.phylosophy).label('phylosophy'),
                                  func.avg(UserSchoolPerformance.art).label('art'),
                                  func.avg(UserSchoolPerformance.foreign_language).label('foreign_language')).join(
            User).filter_by(id=id).group_by(
            UserSchoolPerformance.user_id).all()

    def get_list_sum(self):
        return self.session.query(UserSchoolPerformance.user_id, func.avg(UserSchoolPerformance.math).label('math'),
                                  func.avg(UserSchoolPerformance.physics).label('physics'),
                                  func.avg(UserSchoolPerformance.chemistry).label('chemistry'),
                                  func.avg(UserSchoolPerformance.biology).label('biology'),
                                  func.avg(UserSchoolPerformance.literature).label('literature'),
                                  func.avg(UserSchoolPerformance.history).label('history'),
                                  func.avg(UserSchoolPerformance.geography).label('geography'),
                                  func.avg(UserSchoolPerformance.phylosophy).label('phylosophy'),
                                  func.avg(UserSchoolPerformance.art).label('art'),
                                  func.avg(UserSchoolPerformance.foreign_language).label('foreign_language')).join(
            User).filter(
            User.user_type.in_((UserTypes.Volunteer,))).filter(User.jobs.isnot(None)).group_by(
            UserSchoolPerformance.user_id).all()

    def is_invalid(self, user: User) -> list:
        return []
