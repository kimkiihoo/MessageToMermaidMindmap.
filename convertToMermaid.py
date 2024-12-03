import os
from collections import defaultdict

def parse_line(line):

    try:
        parts = line.strip().split('><')
        if len(parts) != 3:
            return None, None, None
        parent = parts[0].replace('<', '').strip()
        relation = parts[1].replace('>', '').strip()
        child = parts[2].replace('>', '').strip()
        return parent, relation, child
    except Exception as e:
        print(f"Error parsing line: {line}. Error: {e}")
        return None, None, None

def read_data_files(file_paths):
 
    tree = defaultdict(list)
    all_children = set()
    for file_path in file_paths:
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                for line in f:
                    parent, relation, child = parse_line(line)
                    if relation == "include":
                        tree[parent].append(child)
                        all_children.add(child)
        except FileNotFoundError:
            print(f"File not found: {file_path}")
        except Exception as e:
            print(f"Error reading file {file_path}: {e}")
    return tree, all_children

def find_roots(tree, all_children):
    roots = []
    for parent in tree:
        if parent not in all_children:
            roots.append(parent)
    return roots

def traverse_tree(tree, node, depth, lines):
    indent = '  ' * depth
    node_escaped = node.replace('"', '\\"').replace('\\', '\\\\')
    lines.append(f"{indent}{node_escaped}")
    for child in tree.get(node, []):
        traverse_tree(tree, child, depth + 1, lines)

def generate_mermaid_mindmap(tree, roots):
    mermaid = ["mindmap"]
    for root in roots:
        traverse_tree(tree, root, 1, mermaid)
    return "\n".join(mermaid)

def save_markdown(content, output_dir, filename="mindmap.md"):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    output_path = os.path.join(output_dir, filename)
    try:
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write("```mermaid\n")
            f.write(content)
            f.write("\n```")
        print(f"Mermaid Markdown file saved to: {output_path}")
    except Exception as e:
        print(f"Error saving file {output_path}: {e}")

def main():
  
    script_dir = os.path.dirname(os.path.abspath(__file__))
    

    data_files = [os.path.join(script_dir, "data.txt"),
                 os.path.join(script_dir, "data2.txt")]
    

    tree, all_children = read_data_files(data_files)
    

    roots = find_roots(tree, all_children)
    if not roots:
        print("no root in the file")
        return
    
  
    mermaid_content = generate_mermaid_mindmap(tree, roots)

    output_directory = os.path.join(script_dir, "mermaid")
    

    save_markdown(mermaid_content, output_directory, "mindmap.md")

if __name__ == "__main__":
    main()
