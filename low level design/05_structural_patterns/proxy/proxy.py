"""Proxy Pattern: Implementing Caching and Protection Proxies."""

from abc import ABC, abstractmethod
import time
from typing import Dict


# 1. Subject Interface
class VideoDownloader(ABC):
    @abstractmethod
    def download_video(self, video_id: str) -> str:
        pass


# 2. Real Subject (Expensive network/storage call)
class RealYouTubeDownloader(VideoDownloader):
    def download_video(self, video_id: str) -> str:
        print(f"[RealYouTubeDownloader] Downloading {video_id} over HTTPS (simulating network latency)...")
        time.sleep(0.05)  # simulate latency
        return f"BinaryPayload_for_{video_id}"


# 3. Caching & Protection Proxy
class SecureCachingVideoProxy(VideoDownloader):
    def __init__(self, real_downloader: RealYouTubeDownloader, user_role: str) -> None:
        self._real_downloader = real_downloader
        self._user_role = user_role
        self._cache: Dict[str, str] = {}

    def download_video(self, video_id: str) -> str:
        # Protection Proxy check: Only PREMIUM or ADMIN can download
        if self._user_role not in ("PREMIUM", "ADMIN"):
            raise PermissionError(f"User role '{self._user_role}' is not authorized to download HD videos.")

        # Caching Proxy check: Return immediately if present
        if video_id in self._cache:
            print(f"[CachingProxy] Cache HIT for '{video_id}'! Serving instant response.")
            return self._cache[video_id]

        print(f"[CachingProxy] Cache MISS for '{video_id}'. Delegating to real service.")
        result = self._real_downloader.download_video(video_id)
        self._cache[video_id] = result
        return result


if __name__ == "__main__":
    real_service = RealYouTubeDownloader()

    # 1. Protection check: Free user blocked
    free_proxy = SecureCachingVideoProxy(real_service, user_role="FREE")
    try:
        free_proxy.download_video("vid_algorithms_101")
    except PermissionError as e:
        print(f"Protection Proxy check: {e}")

    # 2. Premium user: First call is cache miss, second call is instant cache hit
    premium_proxy = SecureCachingVideoProxy(real_service, user_role="PREMIUM")
    v1 = premium_proxy.download_video("vid_system_design")
    v2 = premium_proxy.download_video("vid_system_design")  # Cache hit!
