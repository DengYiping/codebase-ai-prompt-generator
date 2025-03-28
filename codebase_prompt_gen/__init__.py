"""
Codebase AI Prompt Generator.

A tool to scan Git repositories and generate comprehensive prompts for AI models.
"""

from codebase_prompt_gen.core import generate_prompt

__version__ = "0.1.2"
version_info = tuple(int(part) for part in __version__.split("."))

__all__ = ["__version__", "generate_prompt", "version_info"]
