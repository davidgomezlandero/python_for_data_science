import os


def ft_tqdm(lst: range) -> None:
    """ This function recreates the tqdm function behaviour """
    try:
        terminal_width = os.get_terminal_size().columns
    except OSError:
        terminal_width = 80
    terminal_width = max(terminal_width, 40)
    total = len(lst)
    for i, item in enumerate(lst, start=1):
        p = i / total
        prefix = f"{int(p * 100):3}%|["
        suffix = f"]| {i}/{total}"
        bar_length = terminal_width - len(prefix) \
            - len(suffix) - len("  [00:01<00:00, 191.61it/s]")

        filled = int(p * bar_length)

        if filled > 0:
            bar = "=" * (filled - 1) + ">" + " " * (bar_length - filled)
        else:
            bar = " " * bar_length
        print(f"\r{prefix}{bar}{suffix}", end="", flush=True)
        yield item
