def ft_tqdm(lst: range) -> None:
    total_elems = len(lst)
    for elem in lst:
        progress = int((elem + 1) / total_elems * 50)
        print(f"{progress * 2}%|[{'=' * progress}>{' ' * (50 - progress)}]| {elem + 1}/{total_elems}", end="\r")
        yield elem