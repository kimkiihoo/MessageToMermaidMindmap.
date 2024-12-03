# MessageToMermaidMindmap.
The Message to Mermaid Mindmap Converter is a Python script that transforms structured messages from text files into Mermaid mindmap diagrams. This tool is particularly useful for visualizing hierarchical data and relationships in Visual Studio Code (VSCode) using the Mermaid extension.
Prepare Your Data Files

Create one or more text files (e.g., data.txt, data2.txt) in the same directory as the script.

Format each line in the files as:
<Parent><include><Child>
Example:

data.txt
<A><include><B>
<A><include><C>
<B><include><D>

bash
python mindmap_generator.py
View the Output

The script generates a mindmap.md file inside a mermaid directory.
Open mindmap.md in VSCode to visualize the mindmap.
