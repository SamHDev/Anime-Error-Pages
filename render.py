import base64
import dataclasses

from jinja2 import Environment, Template, FileSystemLoader

env = Environment(loader=FileSystemLoader("./", encoding="utf-8"))
template = env.get_template("./template.html.jinja")


@dataclasses.dataclass
class Impl:
    code: int
    title: str
    img: str


impls = [
    Impl(code=403, title="Forbidden", img="./img/Forbidden.png"),
    Impl(code=404, title="Not Found", img="./img/NotFound.png"),
    Impl(code=418, title="I'm a Tea Pot", img="./img/ImATeaPot.png"),
    Impl(code=503, title="Service Unavailable", img="./img/ServiceUnavailable.png")
]

with open("./style.css", "r", encoding="utf8") as f:
    style_data = f.read()


for impl in impls:
    with open(impl.img, "rb") as f:
        img_bytes = f.read()
    img_base64 = base64.standard_b64encode(img_bytes)
    img_src = b"data:image/png;base64, " + img_base64

    rendered = template.render(
        code=impl.code,
        title=impl.title,
        styles=style_data,
        img=img_src.decode("utf8"),
        bullet="•"
    )

    with open(f"./rendered/{impl.code}.html", "w") as f:
        f.write(rendered)
