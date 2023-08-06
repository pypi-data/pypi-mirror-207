from abc import ABCMeta, abstractmethod
from datetime import datetime
from typing import Optional

from twitter_api.rate_limit.rate_limit_info import RateLimitInfo


class RateLimitChecker(metaclass=ABCMeta):
    @abstractmethod
    def check_limit_over(
        self,
        rate_limit_info: RateLimitInfo,
        now: Optional[datetime] = None,
    ) -> Optional[float]:
        """
        レートリミットオーバーかを調べ、超えている場合は必要な待ち時間[秒]を返す。
        """

        ...
