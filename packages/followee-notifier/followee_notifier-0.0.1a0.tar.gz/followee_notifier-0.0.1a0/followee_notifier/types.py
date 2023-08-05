from typing import Any, Literal


STANDARD_FOLLOWER_FIELDS = ["id", "name", "url", "display_name", "avatar", "description"]
Follower = dict[str, Any]
StandardFollower = dict[Literal['id', 'name', 'url', 'display_name', 'avatar', 'description', 'extensions'], str]
FollowerIncrements = dict[Literal['old', 'new', 'add', 'del'], list[StandardFollower]]
