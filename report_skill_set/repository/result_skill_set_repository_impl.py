from report_skill_set.entity.report_skill_set import ResultReportSkillSet
from report_skill_set.repository.report_skill_set_repository import ResultReportSkillSetRepository


class ResultReportSkillSetRepositoryImpl(ResultReportSkillSetRepository):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance

    def getResultReportSkillSetById(self, id):
        return ResultReportSkillSet.objects.get(id=id)

    def create(self, report):
        ResultReportSkillSet.objects.create(report=report)
