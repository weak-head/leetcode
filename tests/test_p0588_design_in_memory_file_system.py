from leetcode.p0588_design_in_memory_file_system import FileSystem


def test_ls():
    fs = FileSystem()
    assert fs.ls("/") == []

    fs._root.dirs["a"] = FileSystem.Dir()
    fs._root.dirs["a"].dirs["d1"] = FileSystem.Dir()
    fs._root.dirs["a"].files["f1"] = "v1"
    fs._root.dirs["a"].files["f2"] = "v2"
    assert fs.ls("/a") == ["d1", "f1", "f2"]

    d = FileSystem.Dir()
    d.dirs["a"] = FileSystem.Dir()
    d.dirs["b"] = FileSystem.Dir()
    d.dirs["e"] = FileSystem.Dir()
    d.files["b"] = "b"
    d.files["c"] = "c"
    fs._root.dirs["a"].dirs["d1"].dirs["dir"] = d
    assert fs.ls("/a/d1/dir") == ["a", "b", "b", "c", "e"]


def test_mkdir():
    fs = FileSystem()
    fs.mkdir("/a/b/c/d/e")
    assert "a" in fs._root.dirs
    assert "b" in fs._root.dirs["a"].dirs
    assert "c" in fs._root.dirs["a"].dirs["b"].dirs
    assert "d" in fs._root.dirs["a"].dirs["b"].dirs["c"].dirs
    assert "e" in fs._root.dirs["a"].dirs["b"].dirs["c"].dirs["d"].dirs


def test_addContent():
    fs = FileSystem()
    fs.mkdir("/a/b/c")

    fs.addContentToFile("/a/b/c/f", "1")
    assert fs._root.dirs["a"].dirs["b"].dirs["c"].files["f"] == "1"

    fs.addContentToFile("/a/b/c/f", "2")
    assert fs._root.dirs["a"].dirs["b"].dirs["c"].files["f"] == "12"


def test_readContent():
    fs = FileSystem()
    fs.mkdir("/a/b/c")

    fs.addContentToFile("/a/b/c/f", "1")
    assert fs.readContentFromFile("/a/b/c/f") == "1"

    fs.addContentToFile("/a/b/c/f", "2")
    assert fs.readContentFromFile("/a/b/c/f") == "12"
