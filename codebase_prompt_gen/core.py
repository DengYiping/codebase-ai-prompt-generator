"""Core functionality for the Codebase AI Prompt Generator."""

import os
import fnmatch
from pathlib import Path


def generate_file_tree(root_dir, exclude_patterns=None, include_patterns=None):
    """Generate a file tree structure for a given directory.
    
    Args:
        root_dir: The root directory to scan
        exclude_patterns: List of glob patterns to exclude
        include_patterns: List of glob patterns to include
        
    Returns:
        Tuple of (file_tree, files_content) where file_tree is a list of 
        formatted strings and files_content is a list of dictionaries with 
        path and content keys
    """
    if exclude_patterns is None:
        exclude_patterns = [".git", "__pycache__", "*.pyc", "node_modules", ".DS_Store"]
    
    file_tree = []
    files_content = []
    
    # Get all files and directories
    all_files = []
    for dirpath, dirnames, filenames in os.walk(root_dir):
        # Skip excluded directories
        dirnames[:] = [d for d in dirnames if not any(fnmatch.fnmatch(d, pattern) for pattern in exclude_patterns)]
        
        # Process files
        rel_path = os.path.relpath(dirpath, root_dir)
        if rel_path == '.':
            rel_path = ''
        
        # Add directory to tree
        if rel_path:
            file_tree.append(f"📁 {rel_path}/")
        
        # Add files to tree
        for filename in sorted(filenames):
            # Skip excluded files
            if any(fnmatch.fnmatch(filename, pattern) for pattern in exclude_patterns):
                continue
                
            # Apply include patterns if specified
            if include_patterns and not any(fnmatch.fnmatch(filename, pattern) for pattern in include_patterns):
                continue
                
            file_path = os.path.join(rel_path, filename) if rel_path else filename
            file_tree.append(f"📄 {file_path}")
            all_files.append(file_path)
    
    # Get content of all files
    for file_path in all_files:
        abs_path = os.path.join(root_dir, file_path)
        try:
            with open(abs_path, 'r', encoding='utf-8', errors='replace') as f:
                content = f.read()
                files_content.append({
                    "path": file_path,
                    "content": content
                })
        except Exception as e:
            files_content.append({
                "path": file_path,
                "content": f"[Error reading file: {str(e)}]"
            })
    
    return file_tree, files_content


def generate_prompt(repo_path, exclude_patterns=None, include_patterns=None, output_file=None):
    """Generate a prompt for AI models containing the file tree and file contents.
    
    Args:
        repo_path: Path to the Git repository
        exclude_patterns: List of glob patterns to exclude
        include_patterns: List of glob patterns to include
        output_file: Optional file path to write the prompt to
        
    Returns:
        The generated prompt as a string
    """
    repo_path = os.path.abspath(repo_path)
    repo_name = os.path.basename(repo_path)
    
    file_tree, files_content = generate_file_tree(repo_path, exclude_patterns, include_patterns)
    
    # Build the prompt
    prompt = f"# Repository: {repo_name}\n\n"
    
    # Add file tree
    prompt += "## File Tree Structure\n\n"
    prompt += "\n".join(file_tree)
    prompt += "\n\n"
    
    # Add file contents
    prompt += "## File Contents\n\n"
    for file_info in files_content:
        prompt += f"### {file_info['path']}\n\n"
        prompt += "```\n"
        prompt += file_info['content']
        prompt += "\n```\n\n"
    
    # Write to file or print
    if output_file:
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(prompt)
        print(f"Prompt written to {output_file}")
    
    return prompt 