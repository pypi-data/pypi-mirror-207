from __future__ import annotations

import base64
import io
import json

import pandas as pd
import requests

from ghs.config import settings


class GHS:
    def __init__(
        self,
        repository: str,
        access_token: str | None = None,
    ) -> None:
        self.repository = repository
        if access_token is None and not settings.access_token:
            raise ValueError("access_token is required")
        self._session = self._get_session(access_token or settings.access_token)

    def create(self, path: str, df: pd.DataFrame) -> None:
        payload = {
            "message": "Create",
            "content": base64.b64encode(
                df.reset_index(drop=True).to_csv(index=False).encode()
            ).decode(),
        }
        r = self._session.put(
            f"https://api.github.com/repos/{self.repository}/contents/{path}",
            data=json.dumps(payload),
        )
        try:
            r.raise_for_status()
        except requests.HTTPError as e:
            if e.response.status_code == 422:
                raise FileExistsError(
                    f"File {path} already exists in repository {self.repository}"
                )
            raise

    def get(self, path: str) -> pd.DataFrame:
        r = self._session.get(
            f"https://api.github.com/repos/{self.repository}/contents/{path}"
        )
        r.raise_for_status()
        rv = r.json()
        csv = base64.b64decode(rv["content"])
        return pd.read_csv(io.BytesIO(csv))

    def update(self, path: str, df: pd.DataFrame, upsert: bool = True) -> None:
        try:
            sha = self.get_sha(path)
        except FileNotFoundError:
            if upsert:
                self.create(path, df)
                return
            raise
        payload = {
            "message": "Update",
            "sha": sha,
            "content": base64.b64encode(
                df.reset_index(drop=True).to_csv(index=False).encode()
            ).decode(),
        }
        r = self._session.put(
            f"https://api.github.com/repos/{self.repository}/contents/{path}",
            data=json.dumps(payload),
        )
        try:
            r.raise_for_status()
        except requests.HTTPError as e:
            if e.response.status_code == 422:
                raise FileNotFoundError(
                    f"File {path} does not exist in repository {self.repository}"
                )
            raise

    def delete(self, path: str) -> None:
        sha = self.get_sha(path)
        r = self._session.delete(
            f"https://api.github.com/repos/{self.repository}/contents/{path}",
            data=json.dumps({"message": "Delete", "sha": sha}),
        )
        try:
            r.raise_for_status()
        except requests.HTTPError as e:
            if e.response.status_code == 404:
                raise FileNotFoundError(
                    f"File {path} does not exist in repository {self.repository}"
                )
            raise

    def objects(self) -> list[str]:
        r = self._session.get(
            f"https://api.github.com/repos/{self.repository}/contents"
        )
        r.raise_for_status()
        return [item["name"] for item in r.json()]

    def get_sha(self, path: str) -> str:
        r = self._session.get(
            f"https://api.github.com/repos/{self.repository}/contents/{path}"
        )
        try:
            r.raise_for_status()
        except requests.HTTPError as e:
            if e.response.status_code == 404:
                raise FileNotFoundError(
                    f"File {path} does not exist in repository {self.repository}"
                )
            raise
        rv = r.json()
        return rv["sha"]

    @staticmethod
    def _get_session(access_token: str) -> requests.Session:
        sess = requests.Session()
        sess.headers = {
            "Accept": "application/vnd.github+json",
            "Authorization": f"Bearer {access_token}",
            "X-GitHub-Api-Version": "2022-11-28",
        }
        return sess
