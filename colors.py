COLORS_BLACK = "\033[0;30m"
COLORS_RED = "\033[0;31m"
COLORS_GREEN = "\033[0;32m"
COLORS_YELLOW = "\033[0;33m"
COLORS_BLUE = "\033[0;34m"
COLORS_MAGENTA = "\033[0;35m"
COLORS_CYAN = "\033[0;36m"
COLORS_WHITE = "\033[0;37m"
COLORS_RESET = "\033[0m"  # Reset text to default

def colors_print(color, text):
    """
    COLORS:
        BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE
    
    EXAMPLE:
        colors_print(COLORS_RED, "This is a red text")
    """

    print(color + text + COLORS_RESET)
