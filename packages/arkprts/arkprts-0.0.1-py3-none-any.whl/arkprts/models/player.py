"""Arknights API models.

Any field description prefixed with IDK means it's just a guess.
"""


from __future__ import annotations

import datetime
import typing

import pydantic


class Avatar(pydantic.BaseModel):
    """User display avatar."""

    type: typing.Literal["ASSISTANT", "ICON"]
    """Avatar type."""
    id: str
    """Avatar ID. For example a skin ID."""


class Skill(pydantic.BaseModel):
    """Skill of a character."""

    skill_id: str = pydantic.Field(alias="skillId")
    """Skill ID."""
    unlock: int
    """Whether the skill is unlocked."""
    state: int
    """Skill state."""
    specialize_level: int = pydantic.Field(alias="specializeLevel")
    """Skill mastery level."""
    complete_upgrade_time: int = pydantic.Field(alias="completeUpgradeTime")
    """IDK. Time left until skill upgrade is complete."""


class UniEquip(pydantic.BaseModel):
    """Equipped modules."""

    hide: int
    """IDK. Whether the module is publicly hidden."""
    locked: int
    """Whether module access is locked."""
    level: int
    """Module level."""


class AssistChar(pydantic.BaseModel):
    """Publicly visible operator info."""

    char_id: str = pydantic.Field(alias="charId")
    """Character ID."""
    skin_id: str = pydantic.Field(alias="skinId")
    """Equipped skin ID."""
    skills: typing.Sequence[Skill]
    """Operator skills."""
    main_skill_lvl: int = pydantic.Field(alias="mainSkillLvl")
    """Level of the equipped skill."""
    skill_index: int = pydantic.Field(alias="skillIndex")
    """Index of the equipped skill."""
    evolve_phase: int = pydantic.Field(alias="evolvePhase")
    """Elite phase."""
    favor_point: int = pydantic.Field(alias="favorPoint")
    """Raw trust points (25570 is 200% Trust)"""
    potential_rank: int = pydantic.Field(alias="potentialRank")
    """Operator potential. Starts at 0."""
    level: int
    """Operator level."""
    crisis_record: typing.Any = pydantic.Field(alias="crisisRecord")
    """IDK. selectedCrisis is used for contingency contracts elsewhere."""
    current_equip: str | None = pydantic.Field(alias="currentEquip")
    """ID of the currently equipped module."""
    equip: typing.Mapping[str, UniEquip]
    """Equipped modules. Module ID to module info."""


class PlacedMedal(pydantic.BaseModel):
    """A single medal on a board."""

    id: str
    """Medal ID."""
    pos: tuple[int, int]
    """Medal position on the board."""


class MedalBoardCustom(pydantic.BaseModel):
    """Custom medal board layout."""

    layout: typing.Sequence[PlacedMedal]
    """Medals on the board."""


class MedalBoardTemplate(pydantic.BaseModel):
    """Template medal board layout."""

    group_id: str = pydantic.Field(alias="groupId")
    """Medal board template ID."""
    medal_list: typing.Sequence[str] = pydantic.Field(alias="medalList")
    """Medal IDs on the board."""


class MedalBoard(pydantic.BaseModel):
    """Medal board info."""

    type: typing.Literal["CUSTOM"]
    """Medal board layout type."""
    custom: MedalBoardCustom | None
    """Custom medal board layout."""
    template: MedalBoardTemplate | None
    """Template medal board layout."""


class Player(pydantic.BaseModel):
    """Partial player info from search."""

    nickname: str = pydantic.Field(alias="nickName")
    """Player nickname."""
    nick_number: str = pydantic.Field(alias="nickNumber")
    """Player nickname number after #."""
    uid: str
    """Player UID."""
    friend_num_limit: int = pydantic.Field(alias="friendNumLimit")
    """How many more friend slots are open."""
    server_name: str = pydantic.Field(alias="serverName")
    """Server name. Should always be Terra."""
    level: int
    """Player level."""
    avatar_id: str = pydantic.Field(alias="avatarId")
    """IDK. Always 0."""
    avatar: Avatar
    """Selected avatar."""
    assist_char_list: typing.Sequence[AssistChar] = pydantic.Field(alias="assistCharList")
    """Assist operator list."""
    last_online_time: datetime.datetime = pydantic.Field(alias="lastOnlineTime")
    """Last online time."""
    medal_board: MedalBoard = pydantic.Field(alias="medalBoard")
    """Medal board."""
