def printNice(text: str):
    """Returns a formatted string, to be outputted to the console with print()."""

    dedented = textwrap.dedent(text).strip()
    wrapper = textwrap.TextWrapper(initial_indent=" "*8, subsequent_indent=" "*4)
    formatted = "\n" + wrapper.fill(text=dedented)
    formatted += "\n"
    print(formatted)
    # for char in formatted: 
    #     print(char, end='') 
    #     sys.stdout.flush() 
    #     time.sleep(0.07) 