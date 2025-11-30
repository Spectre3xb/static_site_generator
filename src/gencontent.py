import os
from markdown_blocks import markdown_to_html_node


def generate_page(from_path, template_path, dest_path):
    print(f" * {from_path} {template_path} -> {dest_path}")
    from_file = open(from_path, "r")
    markdown_content = from_file.read()
    from_file.close()

    template_file = open(template_path, "r")
    template = template_file.read()
    template_file.close()

    node = markdown_to_html_node(markdown_content)
    html = node.to_html()

    title = extract_title(markdown_content)
    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", html)

    dest_dir_path = os.path.dirname(dest_path)
    if dest_dir_path != "":
        os.makedirs(dest_dir_path, exist_ok=True)
    to_file = open(dest_path, "w")
    to_file.write(template)

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
       """
       Recursively generates HTML pages for all markdown files in a directory.
       Maintains the same directory structure in the destination.
       """
       # Check if the content directory exists
       if not os.path.exists(dir_path_content):
           raise ValueError(f"Content directory '{dir_path_content}' does not exist")
       # List all items in the content directory
       items = os.listdir(dir_path_content)

       for item in items:
           src_path = os.path.join(dir_path_content, item)

           if os.path.isfile(src_path):
               # If it's a markdown file, generate the HTML page
               if item.endswith(".md"):
                   # Convert .md to .html for destination filename
                   dest_filename = item.replace(".md", ".html")
                   dest_path = os.path.join(dest_dir_path, dest_filename)

                   # Generate the page
                   generate_page(src_path, template_path, dest_path)
           else:
                # It's a directory, recursively process it
               new_dest_dir = os.path.join(dest_dir_path, item)
               generate_pages_recursive(src_path, template_path, new_dest_dir)


def extract_title(md):
    lines = md.split("\n")
    for line in lines:
        if line.startswith("# "):
            return line[2:]
    raise ValueError("no title found")
