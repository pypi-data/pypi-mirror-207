# © Copyright Databand.ai, an IBM Company 2022

from typing import Optional
from uuid import UUID

import attr

from airflow_monitor.shared.base_monitor_config import BaseMonitorConfig


@attr.s
class BaseServerConfig:
    source_name: str = attr.ib()
    source_type: str = attr.ib()
    tracking_source_uid: UUID = attr.ib()

    sync_interval: int = attr.ib(default=10)  # Sync interval in seconds
    is_sync_enabled: bool = attr.ib(default=True)
    fetcher_type = attr.ib(default=None)  # type: str

    log_level = attr.ib(default=None)  # type: str

    @classmethod
    def create(
        cls, server_config: dict, monitor_config: Optional[BaseMonitorConfig] = None
    ):
        raise NotImplementedError()

    @property
    def identifier(self):
        return self.tracking_source_uid
