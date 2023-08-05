from bs4 import BeautifulSoup, Tag

from .filter_attrs import help_aria, help_key


def wrap_svg(
    html_markup: str, css: str | None = None, **kwargs
) -> BeautifulSoup:
    """Supplement html fragment of `<svg>` icon with css classes and attributes, include parent/sibling `<span>`s when parameters dictate.

    The following kwargs: `pre_`, `post_`, and `parent_` args are respected.

    So `pre_text` + `pre_class` will add:

    ```html
     <!-- pre_ implies before the icon, with special rule for pre_text -->
    <span class='the-value-of-pre_class'>the-value-of-pre_text</span><svg></svg>
    ```

    `post_text` + `post_class` will add:

    ```html
    <!-- post_ implies after the icon, with special rule for post_text -->
    <svg></svg><span class='the-value-of-post_class'>the-value-of-post_text</span>
    ```

    `parent_class`  + `parent_title` will add:

    ```html
     <!-- parent_ implies a wrapper over the icon,
     'parent_text' will not have same effect.
     -->
    <span class='the-value-of-parent_class' title='the-value-of-parent_title'><svg></svg></span>
    ```

    Examples:
        >>> markup = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="currentColor" class="w-5 h-5"><path d="M6.28 5.22a.75.75 0 00-1.06 1.06L8.94 10l-3.72 3.72a.75.75 0 101.06 1.06L10 11.06l3.72 3.72a.75.75 0 101.06-1.06L11.06 10l3.72-3.72a.75.75 0 00-1.06-1.06L10 8.94 6.28 5.22z" /></svg>'
        >>> res = wrap_svg(html_markup=markup, pre_text="Close menu", pre_class="sr-only", aria_hidden="true")
        >>> len(res.contents) == 2
        True
        >>> res.contents[0]
        <span class="sr-only">Close menu</span>
        >>> res.contents[1].attrs == {'xmlns': 'http://www.w3.org/2000/svg', 'viewbox': '0 0 20 20', 'fill': 'currentColor', 'class': ['w-5', 'h-5'], 'aria-hidden': 'true'}
        True

    Args:
        html_markup (str): The template that contains the `<svg>` tag converted into its html string format.
        css (str, optional): Previously defined CSS to add to the `<svg>` icon. Defaults to None.

    Returns:
        SafeString: Small HTML fragment visually representing an svg icon.
    """  # noqa: E501

    soup = BeautifulSoup(html_markup, "html.parser")
    icon = soup("svg")[0]
    if css:
        icon["class"] = css
    if aria_attrs := help_aria(kwargs):
        for k, v in aria_attrs.items():
            icon[k] = v

    # sibling of icon svg tag (left of icon), special rule for pre_text
    if pre_text := kwargs.pop("pre_text", None):
        pre_span = soup.new_tag("span")
        pre_span.string = pre_text
        if pre_attrs := help_key("pre", kwargs, remove_prefix=True):
            for k, v in pre_attrs.items():
                pre_span[k] = v
        icon.insert_before(pre_span)

    # sibling of icon svg tag (right of icon), special rule for post_text
    if post_text := kwargs.pop("post_text", None):
        post_span = soup.new_tag("span")
        post_span.string = post_text
        if post_attrs := help_key("post", kwargs, remove_prefix=True):
            for k, v in post_attrs.items():
                post_span[k] = v
        icon.insert_after(post_span)

    # no rule for text, assumes that parent will simply contain the icon
    if parent_attrs := help_key("parent", kwargs, remove_prefix=True):
        parent_span = soup.new_tag("span")
        for k, v in parent_attrs.items():
            parent_span[k] = v
        icon.wrap(parent_span)
    return soup
