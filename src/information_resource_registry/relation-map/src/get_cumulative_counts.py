import pandas as pd
import sys

input_csv = sys.argv[1]
output_csv = sys.argv[2]

df = pd.read_csv(input_csv)

root = "infores:ars"

path_count = {}
visited = {}

def count_paths(node):
    print("counting "+node)
    if node in visited:
        return path_count[node]
    visited[node] = True

    children = df[df['Consumed By']==node]['ID']
    if children.empty:
        total_paths = 1
    else:
        total_paths = 0
        for child in children:
            child_count = int(count_paths(child))
            total_paths += child_count
        
    path_count[node] = total_paths
    return(total_paths)

count_paths(root)

print(path_count)

df['path_count'] = df['ID'].map(path_count)
print(df)

df.to_csv(output_csv, index=False)
