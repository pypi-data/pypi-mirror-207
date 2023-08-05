def help_aria(d: dict) -> dict[str, str]:
    """Filter `k`, `v` from `d` based on keys prefixed with `aria_`. Based on this result, rename the key.
    This enables a shortcut for gathering all aria-* attributes found in the dict `d` and parse them properly
    before inserting them into html tags.

    Examples:
        >>> res = help_aria(d={"aria_hidden":"true"})
        >>> res['aria-hidden'] == "true"
        True

    Args:
        d (dict): Values from a template tag.

    Returns:
        dict[str, str]: dict to be used for a html tag's aria-* attributes.
    """  # noqa: E501
    return {
        k.replace("_", "-"): v for k, v in d.items() if k.startswith("aria_")
    }


def help_key(key: str, d: dict, remove_prefix: bool = False) -> dict[str, str]:
    """Filter `k`, `v` from `d` based on keys prefixed with `key`. Based on this result, rename the key,
    if `remove_prefix` is marked `True`. This enables a shortcut for gathering all attributes that should
    be applied to the element's neighbouring tags, e.g. parent, post, pre.

    Examples:
        >>> parent_res = help_key(key="parent", d={"non-a-parent": "test", "parent_css":"flex items-center", "parent_title": "I should be centered"})
        >>> "parent_css" in parent_res
        True
        >>> "parent_title" in parent_res
        True
        >>> "non-a-parent" in parent_res
        False
        >>> pre_res = help_key(key="pre", d={"pre_class":"sr-only", "post_class":"whatever"})
        >>> "pre_class" in pre_res
        True

    Args:
        d (dict): Values from a template tag.

    Returns:
        dict[str, str]: dict to be used for an html tag's parent element's attributes.
    """  # noqa: E501
    if remove_prefix:
        return {
            k.removeprefix(f"{key}_"): v
            for k, v in d.items()
            if k.startswith(f"{key}_")
        }
    return {k: v for k, v in d.items() if k.startswith(f"{key}_")}


def help_hx(d: dict) -> dict[str, str]:
    """Filter `k`, `v` from `d` based on keys prefixed with `hx_`. Based on this result, rename the key.
    This enables a shortcut for gathering all hx-* attributes found in the dict `d` and parse them properly
    before inserting them into html tags.

    Examples:
        >>> res = help_hx(d={"hx_get":"https://test.html",  "hx_target":"body"})
        >>> res['hx-get'] == "https://test.html"
        True
        >>> res['hx-target'] == "body"
        True

    Args:
        d (dict): Values from a template tag.

    Returns:
        dict[str, str]: dict to be used for an inclusion tag's variables.
    """  # noqa: E501
    return {
        k.replace("_", "-"): v for k, v in d.items() if k.startswith("hx_")
    }


def help_data(d: dict) -> dict[str, str]:
    """Filter `k`, `v` from `d` based on keys prefixed with `data_`. Based on this result, rename the key.
    This enables a shortcut for gathering all data-* attributes found in the dict `d` and parse them properly
    before inserting them into html tags.

    Examples:
        >>> res = help_data(d={"data_site_good":"https://test.html"})
        >>> res['data-site-good'] == "https://test.html"
        True

    Args:
        d (dict): Values from a template tag.

    Returns:
        dict[str, str]: dict to be used for an inclusion tag's variables.
    """  # noqa: E501
    return {
        k.replace("_", "-"): v for k, v in d.items() if k.startswith("data_")
    }


def help_btn(d: dict) -> dict[str, str]:
    """Filter `k`, `v` from `d` based on keys prefixed with `btn_`. Based on this result, rename the key
    by removing the prefix. Useful for template tags `{% ... %}` returning a `<button>` html tag.

    Examples:
        >>> res = help_btn(d={"btn_name":"i-am-button", "btn_id": "btn-1"})
        >>> res["name"] == "i-am-button"
        True
        >>> res["id"] == "btn-1"
        True

    Args:
        d (dict): Values from a template tag.

    Returns:
        dict[str, str]: dict to be used for an inclusion tag's variables.
    """  # noqa: E501
    return {
        k.removeprefix("btn_"): v for k, v in d.items() if k.startswith("btn_")
    }
