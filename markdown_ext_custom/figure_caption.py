import xml.etree.ElementTree as etree

from markdown import Extension
from markdown.treeprocessors import Treeprocessor


class FigureCaptionProcessor(Treeprocessor):
    def run(self, root):
        for parent in root.iter():
            for i, child in enumerate(list(parent)):
                # Find standalone img tags (wrapped in <p>)
                if child.tag == "p" and len(child) == 1 and child[0].tag == "img":
                    img = child[0]
                    alt_text = img.get("alt", "")

                    if alt_text:  # Only create figure if there's alt text
                        # Create figure element
                        figure = etree.Element("figure")

                        # Create link to open image in new window
                        link = etree.SubElement(figure, "a")
                        link.set("href", img.get("src", ""))
                        link.set("target", "_blank")
                        link.set("rel", "noopener")

                        # Move img into link
                        img_copy = etree.SubElement(link, "img")
                        img_copy.set("src", img.get("src", ""))
                        img_copy.set("alt", alt_text)
                        if img.get("title"):
                            img_copy.set("title", img.get("title"))

                        # Add figcaption
                        figcaption = etree.SubElement(figure, "figcaption")
                        figcaption.text = alt_text

                        # Replace <p><img></p> with <figure>
                        parent[i] = figure

        return root


class FigureCaptionExtension(Extension):
    def extendMarkdown(self, md):
        md.treeprocessors.register(FigureCaptionProcessor(md), "figure_caption", 15)


def makeExtension(**kwargs):
    return FigureCaptionExtension(**kwargs)
