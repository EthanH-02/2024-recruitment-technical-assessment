from dataclasses import dataclass

@dataclass
class File:
    id: int
    name: str
    categories: list[str]
    parent: int
    size: int


"""
Task 1
"""
def leafFiles(files: list[File]) -> list[str]:
    parent_set = set([file.parent for file in files])
    files_set = set([file.id for file in files])
    leaf_set = files_set - parent_set
    return [file.name for file in files if file.id in leaf_set]


"""
Task 2
"""
def kLargestCategories(files: list[File], k: int) -> list[str]:
    category_dict = {}
    for file in files:
        for category in file.categories:
            category_dict[category] = category_dict.get(category, 0) + 1
    category_dict = {category: value for category, value in sorted(category_dict.items(), key=lambda item: item[1])}
    return list(category_dict.keys())[:-4:-1]


"""
Task 3
"""
def recurSearchSize(file, child_files_dict) -> int:
    if file.id not in child_files_dict:
        return file.size

    total_sum = 0
    for file in child_files_dict[file.id]:
        total_sum += recurSearchSize(file, child_files_dict)
    return total_sum


def largestFileSize(files: list[File]) -> int:
    child_files = {}

    for file in files:
        child_files.setdefault(file.parent, []).append(file)

    max_size = []
    for file in files:
        max_size.append(recurSearchSize(file, child_files))
    return max(max_size)


if __name__ == '__main__':
    testFiles = [
        File(1, "Document.txt", ["Documents"], 3, 1024),
        File(2, "Image.jpg", ["Media", "Photos"], 34, 2048),
        File(3, "Folder", ["Folder"], -1, 0),
        File(5, "Spreadsheet.xlsx", ["Documents", "Excel"], 3, 4096),
        File(8, "Backup.zip", ["Backup"], 233, 8192),
        File(13, "Presentation.pptx", ["Documents", "Presentation"], 3, 3072),
        File(21, "Video.mp4", ["Media", "Videos"], 34, 6144),
        File(34, "Folder2", ["Folder"], 3, 0),
        File(55, "Code.py", ["Programming"], -1, 1536),
        File(89, "Audio.mp3", ["Media", "Audio"], 34, 2560),
        File(144, "Spreadsheet2.xlsx", ["Documents", "Excel"], 3, 2048),
        File(233, "Folder3", ["Folder"], -1, 4096),
    ]

    assert sorted(leafFiles(testFiles)) == [
        "Audio.mp3",
        "Backup.zip",
        "Code.py",
        "Document.txt",
        "Image.jpg",
        "Presentation.pptx",
        "Spreadsheet.xlsx",
        "Spreadsheet2.xlsx",
        "Video.mp4"
    ]

    assert kLargestCategories(testFiles, 3) == [
        "Documents", "Folder", "Media"
    ]

    assert largestFileSize(testFiles) == 20992
