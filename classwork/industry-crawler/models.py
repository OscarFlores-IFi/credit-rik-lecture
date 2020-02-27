import logging

import json
import requests

from bs4 import BeautifulSoup


logger = logging.getLogger(__name__)


class AbstractIndustry(object):

    def __init__(self, title, children):
        logger.info("Creating industry ({title})".format(title=title))
        self.title = title
        self.children = children

    @property
    def level(self):
        raise NotImplementedError

    def add_child(self, child):
        self.children.append(child)

    def to_dict(self):
        return {
            "title": self.title,
            "children": [
                child.to_dict() for child in self.children
            ]
        }

    @staticmethod
    def from_dict(**kwargs):
        raise NotImplementedError

    def jsonify(self):
        return json.dumps(self.to_dict())


class Division(AbstractIndustry):
    level = "SIC Division"

    @staticmethod
    def from_dict(**kwargs):
        return Division(
            title=kwargs["title"],
            children=[
                MajorGroup.from_dict(**k)
                for k in kwargs.get("children", [])
            ]
        )


class MajorGroup(AbstractIndustry):
    level = "SIC Major Group"

    @staticmethod
    def from_dict(**kwargs):
        return MajorGroup(
            title=kwargs["title"],
            children=[
                Group.from_dict(**k)
                for k in kwargs.get("children", [])
            ]
        )

    @staticmethod
    def from_url(url):
        response = requests.get(url)
        html = BeautifulSoup(response.text, "html.parser")
        return MajorGroup(
            title=[elm.text for elm in html.find_all("h2") if elm.text.lower().startswith("major group")][0],
            children=[
                Group(
                    title=group.text,
                    children=[
                        Single(
                            title=inner.parent.text,
                            children=[]
                        )
                        for inner in html.find_all("a")
                        if inner.attrs.get("href").startswith("sic_manual.display")
                        and inner.parent.text.startswith(group.text.split(":")[0].split(" ")[-1])
                    ]
                )
                for group in html.find_all("strong") if group.text.lower().startswith("industry group")
            ]
        )


class Group(AbstractIndustry):
    level = "SIC Industry Group"

    @staticmethod
    def from_dict(**kwargs):
        return Group(
            title=kwargs["title"],
            children=[
                Single.from_dict(**k)
                for k in kwargs.get("children", [])
            ]
        )


class Single(AbstractIndustry):
    level = "SIC Industry"

    @staticmethod
    def from_dict(**kwargs):
        return Single(
            title=kwargs["title"],
            children=[]
        )


class SIC(AbstractIndustry):
    level = "Standard Industry Classification"

    @staticmethod
    def from_dict(**kwargs):
        return SIC(
            title=kwargs["title"],
            children=[
                Division.from_dict(**k)
                for k in kwargs.get("children", [])
            ]
        )

    @staticmethod
    def load(filename):
        with open(filename, "r") as file:
            data = json.loads(file.read())
        return SIC.from_dict(**data)

    def save(self, filename):
        with open(filename, "w") as file:
            data = self.jsonify()
            file.write(data)

    @staticmethod
    def from_url(url):
        response = requests.get(url)
        html = BeautifulSoup(response.text, 'html.parser')
        divisions = []
        for element in html.find_all("a"):
            href = element.attrs.get("href", "")
            title = element.attrs.get("title", "")
            if not href.startswith("sic_manual"):
                continue
            elif href.endswith("division"):
                divisions.append(Division(title=title, children=[]))
            elif href.endswith("group"):
                major_group_url = url.replace("sic_manual.html", href)
                divisions[-1].add_child(MajorGroup.from_url(major_group_url))
        return SIC(title="SIC", children=divisions)

