"""Non correlated useful functions.
"""
# path
import pathlib
import git


def manual_root(file: str, num_parent: int = 1) -> pathlib.Path:
    """Manually gets the root absolute path of the project.

    Parameters
    ----------
    file : str
        The passed file path with __file__.
    num_parent : int, optional
        Number of parents between relative position and the root, by default 1.

    Returns
    -------
    pathlib.Path
        The root absolute path.

    Raises
    ------
    ValueError
        Raise an error if num_parent is not valid.
    """
    try:
        root = pathlib.Path(file).resolve().parents[num_parent - 1]
    except IndexError as exc:
        raise IndexError("num_parent value not valid") from exc
    return root


def git_root() -> pathlib.Path:
    """Automatically gets root absolute path of the project if using git.

    Returns
    -------
    pathlib.WindowsPath
        The root absolute path.
    """
    return pathlib.Path(
        git.Repo('.', search_parent_directories=True).working_tree_dir
    )


def main() -> None:
    """Runs if utils.py is run as standalone script.
    """
    print(manual_root(__name__))
    print(git_root())


if __name__ == "__main__":
    main()
