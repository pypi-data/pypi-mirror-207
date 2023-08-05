from bs4 import BeautifulSoup
from markdownify import markdownify as md

from html2info.types.kaggle import (
    BRONZE,
    COMPETITIONS,
    DATASETS,
    DISCUSSION,
    GOLD,
    NOTEBOOKS,
    SILVER,
    CategoriesType,
    MedalsDict,
    SummaryDict,
)


class Person:
    def __init__(self, url: str, raw_html: str) -> None:
        self.soup = BeautifulSoup(raw_html, "html.parser")

        self.url = url.strip().rstrip("/").lower()
        self.name = None
        self.title = None
        self.location = None
        self.profile_photo_link = None
        self.social_network_links = None
        self.personal_website_link = None
        self.num_followers = None
        self.competitions_summary = None
        self.datasets_summary = None
        self.notebooks_summary = None
        self.discussion_summary = None
        self.bio = None

    def parse(self):
        self.profile_photo_link = self.soup.find("img", {"alt": "image-url"})["src"]
        self.name = self.soup.find("span", {"class": "profile__head-display-name"}).text

        self.title = self.soup.find("p", {"class": "profile__user-occupation"})["title"]

        self.location = self.soup.find("p", {"class": "profile__user-location"}).text

        social_links = self.soup.find_all("li", {"class": "profile__social-link"})
        self.social_network_links = [link.find("a")["href"] for link in social_links]

        personal_website_href = self.soup.find("a", {"class": "profile__social-link--url"})

        if personal_website_href is not None:
            self.personal_website_link = personal_website_href["href"]
        else:
            self.personal_website_link = None

        followers_div = self.soup.find("div", {"class": "profile__user-followers-item"})
        followers_header = followers_div.find("span", {"class": "profile__user-followers-header"})
        followers_header.extract()
        self.num_followers = int(followers_div.text.strip())

        self.parse_competitions()
        self.parse_datasets()
        self.parse_notebooks()
        self.parse_discussion()
        self.parse_bio()

    @staticmethod
    def get_num_medals(html: BeautifulSoup, medal: str) -> int:
        medals_div = html.find("div", {"class": f"achievement-summary__medal--{medal}"})
        return int(medals_div.find_all("p")[1].text)

    def get_tier(self, category: CategoriesType) -> str:
        # Find all the span elements with the specified class
        spans = self.soup.find_all("span", class_="achievement-summary__title achievement-summary__title--link")

        # Iterate over the found spans and look for the one containing 'competitions'
        for span in spans:
            if category in span.text:
                tier = span.find("span").text
                break
        return tier

    def get_summary_block(self, category: CategoriesType) -> BeautifulSoup:
        return self.soup.find(
            "div", {"class": f"achievement-summary__wrapper achievement-summary__wrapper--{category}"}
        )

    def get_block_summary(self, category: CategoriesType) -> SummaryDict:
        datasets_block = self.get_summary_block(category)
        tier = self.get_tier(category)

        tier_image = self.soup.find("img", {"alt": tier})["src"]

        medals: MedalsDict = {
            "gold": self.get_num_medals(datasets_block, GOLD),
            "silver": self.get_num_medals(datasets_block, SILVER),
            "bronze": self.get_num_medals(datasets_block, BRONZE),
        }

        achievement_summary_block = datasets_block.find("div", {"class": "achievement-summary__rank-box--highest"})
        if achievement_summary_block is None:
            highest_rank = -1
        else:
            highest_rank = int(
                achievement_summary_block.find("div", {"class": f"achievement-summary__rank-text--{tier}"}).text
            )

        return {
            "tier": tier,
            "tier_image": tier_image,
            "medals": medals,
            "highest_rank": highest_rank,
        }

    def parse_competitions(self):
        self.competitions_summary = self.get_block_summary(COMPETITIONS)

    def parse_datasets(self):
        self.datasets_summary = self.get_block_summary(DATASETS)

    def parse_notebooks(self):
        self.notebooks_summary = self.get_block_summary(NOTEBOOKS)

    def parse_discussion(self):
        self.discussion_summary = self.get_block_summary(DISCUSSION)

    def parse_bio(self):
        bio_html = self.soup.find("div", {"class": "profile__home__bio-text"})
        self.bio = md(str(bio_html))

    def to_dict(self):
        exclude_keys = {"soup"}
        return {key: value for key, value in self.__dict__.items() if key not in exclude_keys}
