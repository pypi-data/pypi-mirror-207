from typing import Literal, TypedDict

GOLD = "gold"
SILVER = "silver"
BRONZE = "bronze"

COMPETITIONS = "competitions"
DATASETS = "datasets"
NOTEBOOKS = "notebooks"
DISCUSSION = "discussion"

CategoriesType = Literal["competitions", "datasets", "notebooks", "disucssion"]


class MedalsDict(TypedDict):
    gold: int
    silver: int
    bronze: int


class SummaryDict(TypedDict):
    tier: str
    tier_image: str
    medals: MedalsDict
    highest_rank: int
