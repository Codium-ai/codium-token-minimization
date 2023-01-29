def tabify_code(
        string: str,
        tab_spaces=4,
        remove_newlines=True,
        remove_trailing_spaces=True) -> str:
    """
    replace spaces with tabs at the beginning of each line
    """
    outlines = []
    lines = string.splitlines()
    for line in lines:

        # Remove any white spaces at the end of the string
        if remove_trailing_spaces:
            line = line.rstrip()

        # scan the line until we encounter a non-whitespace character
        indent = pos = 0
        while pos < len(line) and line[pos] in [' ', '\t']:
            if line[pos] == ' ':
                indent += 1
            elif line[pos] == '\t':
                indent += tab_spaces
            else:
                break
            pos = pos + 1

        # cut the spaces and tabs from the beginning of the line
        line = line[pos:]

        # enter only tabs
        num_of_tabs_in_line = (indent // tab_spaces)
        leftover = indent - num_of_tabs_in_line * tab_spaces
        if leftover > 0:
            line = (' ' * leftover) + line
        for i in range(0, num_of_tabs_in_line):
            line = '\t' + line
        outlines.append(line)
    out = "\n".join(outlines)

    if remove_newlines:
        out = out.replace("\n\n", "\n")

    return out


def tabify_code2(
        string: str,
        remove_newlines=True,
        remove_trailing_spaces=True) -> str:
    """
    replace spaces with tabs all along the code
    """

    string.replace("    ", "\t")

    # Remove any white spaces at the end of the string
    if remove_trailing_spaces:
        string.replace(" \n", "\n")

    if remove_newlines:
        string = string.replace("\n\n", "\n")

    return string
