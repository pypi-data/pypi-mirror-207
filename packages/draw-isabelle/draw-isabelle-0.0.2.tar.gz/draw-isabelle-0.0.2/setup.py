from setuptools import find_packages, setup

with open("README.md", "r", encoding="utf-8") as f:
    readme = f.read()

required = [
    "binarytree~=6.5.1",
]

# pylint: disable=use-dict-literal
setup_args = dict(
    name="draw-isabelle",
    version="0.0.2",
    packages=find_packages(),
    author="Søren Winkel Holm",
    author_email="swholm@protonmail.com",
    url="https://github.com/sorenmulli/draw-isabelle",
    download_url="https://pypi.org/project/draw-isabelle",
    install_requires=required,
    description="Viz Isabelle ⟨l, a, r⟩ graphs",
    long_description_content_type="text/markdown",
    long_description=readme,
    license="MIT",
    entry_points={
        "console_scripts": [
            "draw-isabelle = draw_isabelle.__main__:run_from_cli",
        ]
    },
)

if __name__ == "__main__":
    setup(**setup_args)
