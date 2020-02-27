# Industry Crawler: Hints!

Get `SIC` form `url`:

```python
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
        return SIC(
            title="SIC",
            children=divisions
        )
```

Get `MajorGroup` from `url`: 

```python
    @staticmethod
    def from_url(url):
        response = requests.get(url)
        html = BeautifulSoup(response.text, 'html.parser')
        return MajorGroup(
            title=[elm.text for elm in html.find_all("h2") if elm.text.lower().startswith("major group")][0],
            children=[
                Group(
                    title=group.text,
                    children=[
                        Single(
                            title=f"{inner.parent.text}{inner.attrs.get('title', '')}"
                            if len(inner.parent.text) < 5
                            else inner.parent.text,
                            children=[]
                        )
                        for inner in html.find_all("a")
                        if inner.attrs.get("href", "").startswith("sic_manual")
                        and inner.parent.text.startswith(group.text.split(":")[0].split(" ")[-1])
                    ]
                )
                for group in html.find_all("strong") if group.text.lower().startswith("industry group")
            ]
        )
```
