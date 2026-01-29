from .nodes.combiner import ETSplitTextNode, ETJoinTextNode, ETSwitchTextNode
from .nodes.converter import ETATOI, ETITOA, ETFTOA
from .nodes.formatter import ETTextFormatter2Node, ETTextFormatter5Node, ETTextFormatter10Node
from .nodes.replacer import ETReplaceTextNode

NODE_CLASS_MAPPINGS = {
    "ETSplitTextNode": ETSplitTextNode,
    "ETJoinTextNode": ETJoinTextNode,
    "ETSwitchTextNode": ETSwitchTextNode,

    "ETATOI": ETATOI,
    "ETITOA": ETITOA,
    "ETFTOA": ETFTOA,

    "ETTextFormatter2Node": ETTextFormatter2Node,
    "ETTextFormatter5Node": ETTextFormatter5Node,
    "ETTextFormatter10Node": ETTextFormatter10Node,

    "ETReplaceTextNode": ETReplaceTextNode,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "ETSplitTextNode": "Split Text",
    "ETJoinTextNode": "Join Text",
    "ETSwitchTextNode": "Switch Text",

    "ETATOI": "ATOI",
    "ETITOA": "ITOA",
    "ETFTOA": "FTOA",

    "ETTextFormatter2Node": "Text Formatter (2 Arguments)",
    "ETTextFormatter5Node": "Text Formatter (5 Arguments)",
    "ETTextFormatter10Node": "Text Formatter (10 Arguments)",

    "ETReplaceTextNode": "Text Replacer",
}

__all__ = ["NODE_CLASS_MAPPINGS", "NODE_DISPLAY_NAME_MAPPINGS"]
