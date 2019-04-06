from git import Repo

repo = Repo(".")
tree = repo.head.commit.tree

for item in tree.traverse():
    # Filter out the tree items
    if item.type != 'tree':
        print(item.data_stream.read())