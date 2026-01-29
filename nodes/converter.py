class ETATOI:
    """
    A node that converts a string to an integer.
    """

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "text": ("STRING", {"default": "", "multiline": False}),
            },
        }

    RETURN_TYPES = ("INT",)
    RETURN_NAMES = ("integer",)

    CATEGORY = "exectails/Strings"
    FUNCTION = "process"

    def process(self, text: str) -> tuple:
        return (int(text),)


class ETITOA:
    """
    A node that converts an integer to a string.
    """

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "integer": ("INT", {"default": 0, "min": -2000000000, "max": 2000000000}),
            },
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("text",)

    CATEGORY = "exectails/Strings"
    FUNCTION = "process"

    def process(self, integer: int) -> tuple:
        return (str(integer),)

class ETFTOA:
    """
    A node that converts a float to a string.
    """

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "value": ("FLOAT", {"default": 0.0, "min": -2000000000, "max": 2000000000}),
                "decimals": ("INT", {"default": 3, "min": 0, "max": 8}),
            },
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("text",)

    CATEGORY = "exectails/Strings"
    FUNCTION = "process"

    def process(self, value: float, decimals: int) -> tuple:
        return ("{:.{}f}".format(value,decimals),)
