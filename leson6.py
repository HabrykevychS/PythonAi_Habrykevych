




    import warnings

    warnings.simplefilter("ignore", SyntaxWarning)
    warnings.simplefilter("always", ImportWarning)

    warnings.warn("Warning, no code here", SyntaxWarning)

    try:
        warnings.warn("Warning, module not import", ImportWarning)
    except Exception:
        print("Warning")