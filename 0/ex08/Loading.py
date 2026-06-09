import os

def ft_tqdm(lst: range) -> None:
    """ This function recreates the tqdm function behaviour """
    try:
        terminal_width = os.get_terminal_size().columns
    except OSError:
        terminal_width = 80
    terminal_width = max(terminal_width, 40)
    total = len(lst)
    for i,item in enumerate(lst, start=1):
        1