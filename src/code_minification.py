import python_minifier


def minify_code(code: str,
                combine_imports=True,
                remove_pass=True,
                remove_annotations=True,
                rename_locals=False,
                hoist_literals=False,
                rename_globals=False,
                convert_posargs_to_args=False) -> str:
    try:
        code_minified = python_minifier.minify(code,
                                               rename_locals=rename_locals,
                                               rename_globals=rename_globals,
                                               hoist_literals=hoist_literals,
                                               remove_annotations=remove_annotations,
                                               remove_pass=remove_pass,
                                               combine_imports=combine_imports,
                                               convert_posargs_to_args=convert_posargs_to_args)
    except:
        print("Failed to minify code")
        return code
    return code_minified
