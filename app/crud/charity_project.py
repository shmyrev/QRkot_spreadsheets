from typing import Dict, List
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.base import CRUDBase
from app.models.charity_project import CharityProject


class CRUDCharityProject(CRUDBase):

    async def get_charity_project_by_name(
        self,
        charity_project_name: str,
        session: AsyncSession
    ):
        charity_project = await session.scalar(
            select(self.model).where(
                self.model.name == charity_project_name
            )
        )
        return charity_project

    async def get_projects_by_completion_rate(
        self,
        session: AsyncSession,
    ) -> List[Dict[str, str]]:
        projects = await session.execute(
            select(CharityProject).where(
                CharityProject.fully_invested)
        )
        projects_list = []
        projects = projects.scalars().all()
        for project in projects:
            projects_list.append({
                'Название проекта': project.name,
                'Время сбора': str(project.close_date - project.create_date),
                'Описание': project.description
            })
        projects_list = sorted(projects_list, key=lambda k: k['Время сбора'])
        return projects_list


charity_project_crud = CRUDCharityProject(CharityProject)
