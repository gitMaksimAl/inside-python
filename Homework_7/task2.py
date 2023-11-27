lines = [
"def rename_files(desired_name: str, num_digits: int,",
"                 source_ext: str, target_ext: str,",
"                 name_slice: list[int]=None) -> None:",
"    folder = 'test_folder'",
"    start = end = 0",
"    if name_slice:",
"        start, end = name_slice",
"    if not target_ext.startswith('.'):",
"        target_ext = '.' + target_ext",
"    if Path(folder).is_dir():",
"        chdir(Path.cwd().joinpath(folder))",
"    i = 1",
"    for file in Path.cwd().iterdir():",
"        if file.suffix[1:] == source_ext:",
"            path = file.parent",
"            name = file.stem",
"            suff = file.suffix if not target_ext else target_ext",
"            file_name = f'{name[start: end]}{desired_name}{i:0={num_digits}}'",
"            file.replace(Path.joinpath(path, file_name).with_suffix(suff))",
"            i += 1"
]


with open('__init__.py', 'w', encoding='utf-8') as init_file:
    for line in lines:
        init_file.writelines(line + '\n')
    init_file.writelines("\n")

