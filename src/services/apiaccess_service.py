from typing import List, Optional
from domain.models.apiaccess import Apiaccess
from domain.models.iapiaccess_repository import IApiaccessRepository


class ApiaccessService:
    def __init__(self, apiaccess_repository: IApiaccessRepository):
        self.apiaccess_repository = apiaccess_repository
    
    # def add_apiaccess(self, developer_id: int, api_type: str, api_key: str, sdk_link: str, request_date, status: str) -> Apiaccess:
    #     apiaccess = Apiaccess(id=None, developer_id=developer_id, api_type=api_type, api_key=api_key, sdk_link=sdk_link, request_date=request_date, status=status)
    #     return self.apiaccess_repository.add(apiaccess)
    
    def add_apiaccess(self, developer_id: int, admin_id: int, api_type: str, api_key: str, sdk_link: str, request_date, status: str) -> Apiaccess:
        apiaccess = Apiaccess(
            id=None,
            developer_id=developer_id,
            admin_id=admin_id,
            api_type=api_type,
            api_key=api_key,
            sdk_link=sdk_link,
            request_date=request_date,
            status=status
        )
        return self.apiaccess_repository.add(apiaccess)
    
    def get_apiaccess_by_id(self, apiaccess_id: int) -> Optional[Apiaccess]:
        return self.apiaccess_repository.get_by_id(apiaccess_id)
    
    def list_apiaccess(self) -> List[Apiaccess]:
        return self.apiaccess_repository.list()
    
    # def update_apiaccess(self, apiaccess_id: int, developer_id: int, api_type: str, api_key: str, sdk_link: str, request_date, status: str) -> Apiaccess:
    #     apiaccess = Apiaccess(id=apiaccess_id, developer_id=developer_id, api_type=api_type, api_key=api_key, sdk_link=sdk_link, request_date=request_date, status=status)
    #     return self.apiaccess_repository.update(apiaccess)
    
    def update_apiaccess(self, apiaccess_id: int, developer_id: int, admin_id: int, api_type: str, api_key: str, sdk_link: str, request_date, status: str) -> Apiaccess:
        apiaccess = Apiaccess(
            id=apiaccess_id,
            developer_id=developer_id,
            admin_id=admin_id,
            api_type=api_type,
            api_key=api_key,
            sdk_link=sdk_link,
            request_date=request_date,
            status=status
        )
        return self.apiaccess_repository.update(apiaccess)
    
    def delete_apiaccess(self, apiaccess_id: int) -> None:
        self.apiaccess_repository.delete(apiaccess_id)
