"""
Pelican plugin to transform Markdown footnotes into Tufte-style sidenotes.

Transforms:
    <sup id="fnref:X"><a class="footnote-ref" href="#fn:X">X</a></sup>
    ...
    <div class="footnote"><ol><li id="fn:X">Content</li></ol></div>

Into:
    <span class="sidenote-wrapper">
      <label for="sn-X" class="sidenote-number"></label>
      <input type="checkbox" id="sn-X" class="sidenote-toggle"/>
      <span class="sidenote">Content</span>
    </span>
"""

from bs4 import BeautifulSoup
from pelican import signals


def transform_footnotes_to_sidenotes(content):
    """Transform standard Markdown footnotes to Tufte-style sidenotes."""
    if not content._content:
        return

    soup = BeautifulSoup(content._content, "html.parser")

    # Find the footnote definitions section
    footnote_div = soup.find("div", class_="footnote")
    if not footnote_div:
        return

    # Build mapping of footnote ID -> content
    footnote_map = {}
    footnote_list = footnote_div.find("ol")
    if footnote_list:
        for li in footnote_list.find_all("li", id=True):
            fn_id = li.get("id")
            if fn_id and fn_id.startswith("fn:"):
                key = fn_id[3:]  # Strip "fn:" prefix

                # Clone content and remove backref link
                content_parts = []
                for child in li.children:
                    if child.name == "p":
                        # Process paragraph, removing backref
                        p_content = []
                        for p_child in child.children:
                            if hasattr(p_child, "get"):
                                classes = p_child.get("class", [])
                                if "footnote-backref" in classes:
                                    continue
                            p_content.append(str(p_child))
                        content_parts.append("".join(p_content).strip())
                    elif hasattr(child, "get"):
                        classes = child.get("class", [])
                        if "footnote-backref" in classes:
                            continue
                        content_parts.append(str(child))
                    else:
                        content_parts.append(str(child))

                footnote_map[key] = " ".join(content_parts).strip()

    # Find and replace each footnote reference with sidenote markup
    for sup in soup.find_all("sup", id=True):
        sup_id = sup.get("id")
        if not sup_id or not sup_id.startswith("fnref:"):
            continue

        key = sup_id[6:]  # Strip "fnref:" prefix
        if key not in footnote_map:
            continue

        sidenote_id = f"sn-{key}"

        # Create sidenote wrapper structure
        wrapper = soup.new_tag(
            "span", attrs={"class": "sidenote-wrapper", "id": sup_id}
        )

        # Label (shows superscript number, clickable for mobile toggle)
        label = soup.new_tag(
            "label", attrs={"for": sidenote_id, "class": "sidenote-number"}
        )

        # Hidden checkbox for mobile toggle
        checkbox = soup.new_tag(
            "input",
            attrs={"type": "checkbox", "id": sidenote_id, "class": "sidenote-toggle"},
        )

        # The sidenote content
        sidenote_span = soup.new_tag("span", attrs={"class": "sidenote"})
        sidenote_content = BeautifulSoup(footnote_map[key], "html.parser")
        for child in list(sidenote_content.children):
            sidenote_span.append(child)

        # Assemble wrapper
        wrapper.append(label)
        wrapper.append(checkbox)
        wrapper.append(sidenote_span)

        # Replace original <sup> element
        sup.replace_with(wrapper)

    # Hide original footnote section on desktop (CSS will handle visibility)
    footnote_div["class"] = footnote_div.get("class", []) + ["sidenote-hidden-desktop"]

    # Update content
    content._content = str(soup)


def process_articles(generator):
    """Process all articles after generation."""
    if hasattr(generator, "articles"):
        for article in generator.articles:
            transform_footnotes_to_sidenotes(article)
    if hasattr(generator, "drafts"):
        for draft in generator.drafts:
            transform_footnotes_to_sidenotes(draft)


def process_pages(generator):
    """Process all pages after generation."""
    if hasattr(generator, "pages"):
        for page in generator.pages:
            transform_footnotes_to_sidenotes(page)


def register():
    """Register the plugin with Pelican."""
    signals.article_generator_finalized.connect(process_articles)
    signals.page_generator_finalized.connect(process_pages)
