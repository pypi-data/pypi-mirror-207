from typing import Any, Dict, Iterator, List, Optional
from urllib.parse import urlparse, urlunparse
from docutils import nodes
from sphinx.transforms.post_transforms import SphinxPostTransform
from sphinx.util.nodes import NodeMatcher
from .utils import traverse_or_findall



class ShortenLinkTransform(SphinxPostTransform):
    """
    Shorten link when they are coming from github or gitlab and add an extra class to the tag
    for further styling.
    Before::
        <a class="reference external" href="https://github.com/2i2c-org/infrastructure/issues/1329">
            https://github.com/2i2c-org/infrastructure/issues/1329
        </a>
    After::
        <a class="reference external github" href="https://github.com/2i2c-org/infrastructure/issues/1329">
            2i2c-org/infrastructure#1329
        </a>
    """  # noqa

    default_priority = 400
    formats = ("html",)
    supported_platform = {"github.com": "github", "gitlab.com": "gitlab"}
    platform = None

    def run(self, **kwargs):
        matcher = NodeMatcher(nodes.reference)
        # TODO: just use "findall" once docutils min version >=0.18.1
        for node in traverse_or_findall(self.document, matcher):
            uri = node.attributes.get("refuri")
            text = next(iter(node.children), None)
            # only act if the uri and text are the same
            # if not the user has already customized the display of the link
            if uri is not None and text is not None and text == uri:
                uri = urlparse(uri)
                # only do something if the platform is identified
                self.platform = self.supported_platform.get(uri.netloc)
                if self.platform is not None:
                    node.attributes["classes"].append(self.platform)
                    node.children[0] = nodes.Text(self.parse_url(uri))

    def parse_url(self, uri):
        """
        parse the content of the url with respect to the selected platform
        """
        path = uri.path

        if path == "":
            # plain url passed, return platform only
            return self.platform

        # if the path is not empty it contains a leading "/", which we don't want to
        # include in the parsed content
        path = path.lstrip("/")

        # check the platform name and read the information accordingly
        # as "<organisation>/<repository>#<element number>"
        # or "<group>/<subgroup 1>/…/<subgroup N>/<repository>#<element number>"
        if self.platform == "github":
            # split the url content
            parts = path.split("/")

            if parts[0] == "orgs" and "/projects" in path:
                # We have a projects board link
                # ref: `orgs/{org}/projects/{project-id}`
                text = f"{parts[1]}/projects#{parts[3]}"
            else:
                # We have an issues, PRs, or repository link
                if len(parts) > 0:
                    text = parts[0]  # organisation
                if len(parts) > 1:
                    text += f"/{parts[1]}"  # repository
                if len(parts) > 2:
                    if parts[2] in ["issues", "pull", "discussions"]:
                        text += f"#{parts[-1]}"  # element number

        elif self.platform == "gitlab":
            # cp. https://docs.gitlab.com/ee/user/markdown.html#gitlab-specific-references
            if "/-/" in path and any(
                map(uri.path.__contains__, ["issues", "merge_requests"])
            ):
                group_and_subgroups, parts, *_ = path.split("/-/")
                parts = parts.split("/")
                url_type, element_number, *_ = parts
                if url_type == "issues":
                    text = f"{group_and_subgroups}#{element_number}"
                elif url_type == "merge_requests":
                    text = f"{group_and_subgroups}!{element_number}"
            else:
                # display the whole uri (after "gitlab.com/") including parameters
                # for example "<group>/<subgroup1>/<subgroup2>/<repository>"
                text = uri._replace(netloc="", scheme="")  # remove platform
                text = urlunparse(text)[1:]  # combine to string and strip leading "/"

        return text


class WrapTableAndMathInAContainerTransform(SphinxPostTransform):
    """A Sphinx post-transform that wraps `table` and `div.math` in a container `div`.

    This makes it possible to handle these overflowing the content-width, which is
    necessary in a responsive theme.
    """

    formats = ("html",)
    default_priority = 500

    def run(self, **kwargs: Any) -> None:
        """Perform the post-transform on `self.document`."""
        get_nodes = (
            self.document.findall  # docutils 0.18+
            if hasattr(self.document, "findall")
            else self.document.traverse  # docutils <= 0.17.x
        )
        for node in list(get_nodes(nodes.table)):
            new_node = nodes.container(classes=["table-wrapper"])
            new_node.update_all_atts(node)
            node.parent.replace(node, new_node)
            new_node.append(node)

        for node in list(get_nodes(nodes.math_block)):
            new_node = nodes.container(classes=["math-wrapper"])
            new_node.update_all_atts(node)
            node.parent.replace(node, new_node)
            new_node.append(node)
