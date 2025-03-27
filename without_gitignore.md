# Repository: codebase-ai-prompt-generator

## File Tree Structure

📄 .gitignore
📄 LICENSE
📄 README.md
📄 cli_test_output.md
📄 pyproject.toml
📄 test_output.md
📄 with_gitignore.md
📁 codebase_prompt_gen/
📄 codebase_prompt_gen/__init__.py
📄 codebase_prompt_gen/core.py
📁 codebase_prompt_gen/cli/
📄 codebase_prompt_gen/cli/__init__.py
📄 codebase_prompt_gen/cli/main.py
📁 codebase_ai_prompt_generator.egg-info/
📄 codebase_ai_prompt_generator.egg-info/PKG-INFO
📄 codebase_ai_prompt_generator.egg-info/SOURCES.txt
📄 codebase_ai_prompt_generator.egg-info/dependency_links.txt
📄 codebase_ai_prompt_generator.egg-info/entry_points.txt
📄 codebase_ai_prompt_generator.egg-info/top_level.txt

## File Contents

### .gitignore

```
# Python-generated files
__pycache__/
*.py[oc]
build/
dist/
wheels/
*.egg-info

# Virtual environments
.venv
venv/
ENV/

# Testing and output files
test_output.md
cli_test_output.md

# IDEs and editors
.vscode/
.idea/
*.swp
*~
.DS_Store

```

### LICENSE

```
MIT License

Copyright (c) 2023 

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE. 
```

### README.md

```
# Codebase AI Prompt Generator

A tool to scan a Git repository and generate a comprehensive prompt for AI models, including file tree structure, file paths, and content.

## Features

- Creates a hierarchical file tree representation of a repository
- Includes file contents formatted for AI prompts
- Customizable file inclusion/exclusion via patterns
- Option to save output to a file or print to console
- Automatically respects local and global .gitignore files
- Installable CLI tool

## Installation

```bash
# From PyPI (recommended)
pip install codebase-ai-prompt-generator

# From source
git clone https://github.com/yourusername/codebase-ai-prompt-generator.git
cd codebase-ai-prompt-generator
pip install -e .
```

## Usage

After installation, you can use the `codebase-prompt` command directly from your terminal:

```bash
# Basic usage (scans current directory)
codebase-prompt

# Scan a specific repository
codebase-prompt /path/to/repository

# Exclude specific file patterns
codebase-prompt --exclude "*.log" "*.tmp" ".env"

# Include only specific file patterns
codebase-prompt --include "*.py" "*.js" "*.html"

# Write output to a file
codebase-prompt --output prompt.md

# Show version information
codebase-prompt --version

# Ignore .gitignore files (both local and global)
codebase-prompt --no-gitignore

# Combine options
codebase-prompt /path/to/repository --exclude "node_modules" "*.pyc" --include "*.py" "*.js" --output prompt.md
```

## .gitignore Support

By default, the tool respects both:
- The repository's local `.gitignore` file
- The user's global gitignore file (found via `git config --global --get core.excludesfile`)

Files matching any pattern in these files will be excluded from the output. To disable this feature, use the `--no-gitignore` flag.

## Example Output

The generated prompt will have the following structure:

```
# Repository: repo-name

## File Tree Structure

📁 src/
📄 src/main.py
📄 src/utils.py
📁 tests/
📄 tests/test_main.py
📄 README.md

## File Contents

### src/main.py

```python
def main():
    print("Hello World")
```

### src/utils.py

```python
def helper():
    return "Helper function"
```

...
```

## Use Cases

- Generate prompts for AI code assistants to understand your entire codebase
- Create documentation snapshots of your repository
- Share codebase context with AI models for better assistance
- Provide comprehensive context to LLMs for code-related questions

## Development

To set up the development environment:

```bash
# Clone the repository
git clone https://github.com/yourusername/codebase-ai-prompt-generator.git
cd codebase-ai-prompt-generator

# Create and activate a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install in development mode
pip install -e .
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

```

### cli_test_output.md

```
# Repository: codebase-ai-prompt-generator

## File Tree Structure

📄 .gitignore
📄 .python-version
📄 LICENSE
📄 pyproject.toml
📁 .git/
📄 .git/FETCH_HEAD
📄 .git/HEAD
📄 .git/config
📄 .git/description
📁 .git/objects/
📁 .git/objects/pack/
📁 .git/objects/info/
📁 .git/info/
📄 .git/info/exclude
📁 .git/hooks/
📄 .git/hooks/applypatch-msg.sample
📄 .git/hooks/commit-msg.sample
📄 .git/hooks/fsmonitor-watchman.sample
📄 .git/hooks/post-update.sample
📄 .git/hooks/pre-applypatch.sample
📄 .git/hooks/pre-commit.sample
📄 .git/hooks/pre-merge-commit.sample
📄 .git/hooks/pre-push.sample
📄 .git/hooks/pre-rebase.sample
📄 .git/hooks/pre-receive.sample
📄 .git/hooks/prepare-commit-msg.sample
📄 .git/hooks/push-to-checkout.sample
📄 .git/hooks/sendemail-validate.sample
📄 .git/hooks/update.sample
📁 .git/refs/
📁 .git/refs/heads/
📁 .git/refs/tags/
📁 codebase_prompt_gen/
📄 codebase_prompt_gen/__init__.py
📄 codebase_prompt_gen/core.py
📁 codebase_prompt_gen/__pycache__/
📄 codebase_prompt_gen/__pycache__/__init__.cpython-313.pyc
📄 codebase_prompt_gen/__pycache__/core.cpython-313.pyc
📁 codebase_prompt_gen/cli/
📄 codebase_prompt_gen/cli/__init__.py
📄 codebase_prompt_gen/cli/main.py
📁 codebase_prompt_gen/cli/__pycache__/
📄 codebase_prompt_gen/cli/__pycache__/__init__.cpython-313.pyc
📄 codebase_prompt_gen/cli/__pycache__/main.cpython-313.pyc
📁 codebase_ai_prompt_generator.egg-info/
📄 codebase_ai_prompt_generator.egg-info/PKG-INFO
📄 codebase_ai_prompt_generator.egg-info/SOURCES.txt
📄 codebase_ai_prompt_generator.egg-info/dependency_links.txt
📄 codebase_ai_prompt_generator.egg-info/entry_points.txt
📄 codebase_ai_prompt_generator.egg-info/top_level.txt

## File Contents

### .gitignore

```
# Python-generated files
__pycache__/
*.py[oc]
build/
dist/
wheels/
*.egg-info

# Virtual environments
.venv

```

### .python-version

```
3.10

```

### LICENSE

```
MIT License

Copyright (c) 2023 

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE. 
```

### pyproject.toml

```
[build-system]
requires = ["setuptools>=61.0", "wheel"]
build-backend = "setuptools.build_meta"

[project]
name = "codebase-ai-prompt-generator"
version = "0.1.0"
description = "Generate AI prompts from Git repositories with file tree structures and content"
readme = "README.md"
requires-python = ">=3.8"
license = {text = "MIT"}
keywords = ["ai", "prompt", "git", "code", "repository"]
authors = [
    {name = "Your Name", email = "your.email@example.com"}
]
classifiers = [
    "Development Status :: 3 - Alpha",
    "Intended Audience :: Developers",
    "Topic :: Software Development :: Libraries :: Python Modules",
    "License :: OSI Approved :: MIT License",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.8",
    "Programming Language :: Python :: 3.9",
    "Programming Language :: Python :: 3.10",
    "Programming Language :: Python :: 3.11",
]

[project.urls]
"Homepage" = "https://github.com/yourusername/codebase-ai-prompt-generator"
"Bug Tracker" = "https://github.com/yourusername/codebase-ai-prompt-generator/issues"

[project.scripts]
codebase-prompt = "codebase_prompt_gen.cli.main:main"

[tool.setuptools]
packages = ["codebase_prompt_gen", "codebase_prompt_gen.cli"]

```

### .git/FETCH_HEAD

```

```

### .git/HEAD

```
ref: refs/heads/master

```

### .git/config

```
[core]
	repositoryformatversion = 0
	filemode = true
	bare = false
	logallrefupdates = true
	ignorecase = true
	precomposeunicode = true

```

### .git/description

```
Unnamed repository; edit this file 'description' to name the repository.

```

### .git/info/exclude

```
# git ls-files --others --exclude-from=.git/info/exclude
# Lines that start with '#' are comments.
# For a project mostly in C, the following would be a good set of
# exclude patterns (uncomment them if you want to use them):
# *.[oa]
# *~

```

### .git/hooks/applypatch-msg.sample

```
#!/bin/sh
#
# An example hook script to check the commit log message taken by
# applypatch from an e-mail message.
#
# The hook should exit with non-zero status after issuing an
# appropriate message if it wants to stop the commit.  The hook is
# allowed to edit the commit message file.
#
# To enable this hook, rename this file to "applypatch-msg".

. git-sh-setup
commitmsg="$(git rev-parse --git-path hooks/commit-msg)"
test -x "$commitmsg" && exec "$commitmsg" ${1+"$@"}
:

```

### .git/hooks/commit-msg.sample

```
#!/bin/sh
#
# An example hook script to check the commit log message.
# Called by "git commit" with one argument, the name of the file
# that has the commit message.  The hook should exit with non-zero
# status after issuing an appropriate message if it wants to stop the
# commit.  The hook is allowed to edit the commit message file.
#
# To enable this hook, rename this file to "commit-msg".

# Uncomment the below to add a Signed-off-by line to the message.
# Doing this in a hook is a bad idea in general, but the prepare-commit-msg
# hook is more suited to it.
#
# SOB=$(git var GIT_AUTHOR_IDENT | sed -n 's/^\(.*>\).*$/Signed-off-by: \1/p')
# grep -qs "^$SOB" "$1" || echo "$SOB" >> "$1"

# This example catches duplicate Signed-off-by lines.

test "" = "$(grep '^Signed-off-by: ' "$1" |
	 sort | uniq -c | sed -e '/^[ 	]*1[ 	]/d')" || {
	echo >&2 Duplicate Signed-off-by lines.
	exit 1
}

```

### .git/hooks/fsmonitor-watchman.sample

```
#!/usr/bin/perl

use strict;
use warnings;
use IPC::Open2;

# An example hook script to integrate Watchman
# (https://facebook.github.io/watchman/) with git to speed up detecting
# new and modified files.
#
# The hook is passed a version (currently 2) and last update token
# formatted as a string and outputs to stdout a new update token and
# all files that have been modified since the update token. Paths must
# be relative to the root of the working tree and separated by a single NUL.
#
# To enable this hook, rename this file to "query-watchman" and set
# 'git config core.fsmonitor .git/hooks/query-watchman'
#
my ($version, $last_update_token) = @ARGV;

# Uncomment for debugging
# print STDERR "$0 $version $last_update_token\n";

# Check the hook interface version
if ($version ne 2) {
	die "Unsupported query-fsmonitor hook version '$version'.\n" .
	    "Falling back to scanning...\n";
}

my $git_work_tree = get_working_dir();

my $retry = 1;

my $json_pkg;
eval {
	require JSON::XS;
	$json_pkg = "JSON::XS";
	1;
} or do {
	require JSON::PP;
	$json_pkg = "JSON::PP";
};

launch_watchman();

sub launch_watchman {
	my $o = watchman_query();
	if (is_work_tree_watched($o)) {
		output_result($o->{clock}, @{$o->{files}});
	}
}

sub output_result {
	my ($clockid, @files) = @_;

	# Uncomment for debugging watchman output
	# open (my $fh, ">", ".git/watchman-output.out");
	# binmode $fh, ":utf8";
	# print $fh "$clockid\n@files\n";
	# close $fh;

	binmode STDOUT, ":utf8";
	print $clockid;
	print "\0";
	local $, = "\0";
	print @files;
}

sub watchman_clock {
	my $response = qx/watchman clock "$git_work_tree"/;
	die "Failed to get clock id on '$git_work_tree'.\n" .
		"Falling back to scanning...\n" if $? != 0;

	return $json_pkg->new->utf8->decode($response);
}

sub watchman_query {
	my $pid = open2(\*CHLD_OUT, \*CHLD_IN, 'watchman -j --no-pretty')
	or die "open2() failed: $!\n" .
	"Falling back to scanning...\n";

	# In the query expression below we're asking for names of files that
	# changed since $last_update_token but not from the .git folder.
	#
	# To accomplish this, we're using the "since" generator to use the
	# recency index to select candidate nodes and "fields" to limit the
	# output to file names only. Then we're using the "expression" term to
	# further constrain the results.
	my $last_update_line = "";
	if (substr($last_update_token, 0, 1) eq "c") {
		$last_update_token = "\"$last_update_token\"";
		$last_update_line = qq[\n"since": $last_update_token,];
	}
	my $query = <<"	END";
		["query", "$git_work_tree", {$last_update_line
			"fields": ["name"],
			"expression": ["not", ["dirname", ".git"]]
		}]
	END

	# Uncomment for debugging the watchman query
	# open (my $fh, ">", ".git/watchman-query.json");
	# print $fh $query;
	# close $fh;

	print CHLD_IN $query;
	close CHLD_IN;
	my $response = do {local $/; <CHLD_OUT>};

	# Uncomment for debugging the watch response
	# open ($fh, ">", ".git/watchman-response.json");
	# print $fh $response;
	# close $fh;

	die "Watchman: command returned no output.\n" .
	"Falling back to scanning...\n" if $response eq "";
	die "Watchman: command returned invalid output: $response\n" .
	"Falling back to scanning...\n" unless $response =~ /^\{/;

	return $json_pkg->new->utf8->decode($response);
}

sub is_work_tree_watched {
	my ($output) = @_;
	my $error = $output->{error};
	if ($retry > 0 and $error and $error =~ m/unable to resolve root .* directory (.*) is not watched/) {
		$retry--;
		my $response = qx/watchman watch "$git_work_tree"/;
		die "Failed to make watchman watch '$git_work_tree'.\n" .
		    "Falling back to scanning...\n" if $? != 0;
		$output = $json_pkg->new->utf8->decode($response);
		$error = $output->{error};
		die "Watchman: $error.\n" .
		"Falling back to scanning...\n" if $error;

		# Uncomment for debugging watchman output
		# open (my $fh, ">", ".git/watchman-output.out");
		# close $fh;

		# Watchman will always return all files on the first query so
		# return the fast "everything is dirty" flag to git and do the
		# Watchman query just to get it over with now so we won't pay
		# the cost in git to look up each individual file.
		my $o = watchman_clock();
		$error = $output->{error};

		die "Watchman: $error.\n" .
		"Falling back to scanning...\n" if $error;

		output_result($o->{clock}, ("/"));
		$last_update_token = $o->{clock};

		eval { launch_watchman() };
		return 0;
	}

	die "Watchman: $error.\n" .
	"Falling back to scanning...\n" if $error;

	return 1;
}

sub get_working_dir {
	my $working_dir;
	if ($^O =~ 'msys' || $^O =~ 'cygwin') {
		$working_dir = Win32::GetCwd();
		$working_dir =~ tr/\\/\//;
	} else {
		require Cwd;
		$working_dir = Cwd::cwd();
	}

	return $working_dir;
}

```

### .git/hooks/post-update.sample

```
#!/bin/sh
#
# An example hook script to prepare a packed repository for use over
# dumb transports.
#
# To enable this hook, rename this file to "post-update".

exec git update-server-info

```

### .git/hooks/pre-applypatch.sample

```
#!/bin/sh
#
# An example hook script to verify what is about to be committed
# by applypatch from an e-mail message.
#
# The hook should exit with non-zero status after issuing an
# appropriate message if it wants to stop the commit.
#
# To enable this hook, rename this file to "pre-applypatch".

. git-sh-setup
precommit="$(git rev-parse --git-path hooks/pre-commit)"
test -x "$precommit" && exec "$precommit" ${1+"$@"}
:

```

### .git/hooks/pre-commit.sample

```
#!/bin/sh
#
# An example hook script to verify what is about to be committed.
# Called by "git commit" with no arguments.  The hook should
# exit with non-zero status after issuing an appropriate message if
# it wants to stop the commit.
#
# To enable this hook, rename this file to "pre-commit".

if git rev-parse --verify HEAD >/dev/null 2>&1
then
	against=HEAD
else
	# Initial commit: diff against an empty tree object
	against=$(git hash-object -t tree /dev/null)
fi

# If you want to allow non-ASCII filenames set this variable to true.
allownonascii=$(git config --type=bool hooks.allownonascii)

# Redirect output to stderr.
exec 1>&2

# Cross platform projects tend to avoid non-ASCII filenames; prevent
# them from being added to the repository. We exploit the fact that the
# printable range starts at the space character and ends with tilde.
if [ "$allownonascii" != "true" ] &&
	# Note that the use of brackets around a tr range is ok here, (it's
	# even required, for portability to Solaris 10's /usr/bin/tr), since
	# the square bracket bytes happen to fall in the designated range.
	test $(git diff-index --cached --name-only --diff-filter=A -z $against |
	  LC_ALL=C tr -d '[ -~]\0' | wc -c) != 0
then
	cat <<\EOF
Error: Attempt to add a non-ASCII file name.

This can cause problems if you want to work with people on other platforms.

To be portable it is advisable to rename the file.

If you know what you are doing you can disable this check using:

  git config hooks.allownonascii true
EOF
	exit 1
fi

# If there are whitespace errors, print the offending file names and fail.
exec git diff-index --check --cached $against --

```

### .git/hooks/pre-merge-commit.sample

```
#!/bin/sh
#
# An example hook script to verify what is about to be committed.
# Called by "git merge" with no arguments.  The hook should
# exit with non-zero status after issuing an appropriate message to
# stderr if it wants to stop the merge commit.
#
# To enable this hook, rename this file to "pre-merge-commit".

. git-sh-setup
test -x "$GIT_DIR/hooks/pre-commit" &&
        exec "$GIT_DIR/hooks/pre-commit"
:

```

### .git/hooks/pre-push.sample

```
#!/bin/sh

# An example hook script to verify what is about to be pushed.  Called by "git
# push" after it has checked the remote status, but before anything has been
# pushed.  If this script exits with a non-zero status nothing will be pushed.
#
# This hook is called with the following parameters:
#
# $1 -- Name of the remote to which the push is being done
# $2 -- URL to which the push is being done
#
# If pushing without using a named remote those arguments will be equal.
#
# Information about the commits which are being pushed is supplied as lines to
# the standard input in the form:
#
#   <local ref> <local oid> <remote ref> <remote oid>
#
# This sample shows how to prevent push of commits where the log message starts
# with "WIP" (work in progress).

remote="$1"
url="$2"

zero=$(git hash-object --stdin </dev/null | tr '[0-9a-f]' '0')

while read local_ref local_oid remote_ref remote_oid
do
	if test "$local_oid" = "$zero"
	then
		# Handle delete
		:
	else
		if test "$remote_oid" = "$zero"
		then
			# New branch, examine all commits
			range="$local_oid"
		else
			# Update to existing branch, examine new commits
			range="$remote_oid..$local_oid"
		fi

		# Check for WIP commit
		commit=$(git rev-list -n 1 --grep '^WIP' "$range")
		if test -n "$commit"
		then
			echo >&2 "Found WIP commit in $local_ref, not pushing"
			exit 1
		fi
	fi
done

exit 0

```

### .git/hooks/pre-rebase.sample

```
#!/bin/sh
#
# Copyright (c) 2006, 2008 Junio C Hamano
#
# The "pre-rebase" hook is run just before "git rebase" starts doing
# its job, and can prevent the command from running by exiting with
# non-zero status.
#
# The hook is called with the following parameters:
#
# $1 -- the upstream the series was forked from.
# $2 -- the branch being rebased (or empty when rebasing the current branch).
#
# This sample shows how to prevent topic branches that are already
# merged to 'next' branch from getting rebased, because allowing it
# would result in rebasing already published history.

publish=next
basebranch="$1"
if test "$#" = 2
then
	topic="refs/heads/$2"
else
	topic=`git symbolic-ref HEAD` ||
	exit 0 ;# we do not interrupt rebasing detached HEAD
fi

case "$topic" in
refs/heads/??/*)
	;;
*)
	exit 0 ;# we do not interrupt others.
	;;
esac

# Now we are dealing with a topic branch being rebased
# on top of master.  Is it OK to rebase it?

# Does the topic really exist?
git show-ref -q "$topic" || {
	echo >&2 "No such branch $topic"
	exit 1
}

# Is topic fully merged to master?
not_in_master=`git rev-list --pretty=oneline ^master "$topic"`
if test -z "$not_in_master"
then
	echo >&2 "$topic is fully merged to master; better remove it."
	exit 1 ;# we could allow it, but there is no point.
fi

# Is topic ever merged to next?  If so you should not be rebasing it.
only_next_1=`git rev-list ^master "^$topic" ${publish} | sort`
only_next_2=`git rev-list ^master           ${publish} | sort`
if test "$only_next_1" = "$only_next_2"
then
	not_in_topic=`git rev-list "^$topic" master`
	if test -z "$not_in_topic"
	then
		echo >&2 "$topic is already up to date with master"
		exit 1 ;# we could allow it, but there is no point.
	else
		exit 0
	fi
else
	not_in_next=`git rev-list --pretty=oneline ^${publish} "$topic"`
	/usr/bin/perl -e '
		my $topic = $ARGV[0];
		my $msg = "* $topic has commits already merged to public branch:\n";
		my (%not_in_next) = map {
			/^([0-9a-f]+) /;
			($1 => 1);
		} split(/\n/, $ARGV[1]);
		for my $elem (map {
				/^([0-9a-f]+) (.*)$/;
				[$1 => $2];
			} split(/\n/, $ARGV[2])) {
			if (!exists $not_in_next{$elem->[0]}) {
				if ($msg) {
					print STDERR $msg;
					undef $msg;
				}
				print STDERR " $elem->[1]\n";
			}
		}
	' "$topic" "$not_in_next" "$not_in_master"
	exit 1
fi

<<\DOC_END

This sample hook safeguards topic branches that have been
published from being rewound.

The workflow assumed here is:

 * Once a topic branch forks from "master", "master" is never
   merged into it again (either directly or indirectly).

 * Once a topic branch is fully cooked and merged into "master",
   it is deleted.  If you need to build on top of it to correct
   earlier mistakes, a new topic branch is created by forking at
   the tip of the "master".  This is not strictly necessary, but
   it makes it easier to keep your history simple.

 * Whenever you need to test or publish your changes to topic
   branches, merge them into "next" branch.

The script, being an example, hardcodes the publish branch name
to be "next", but it is trivial to make it configurable via
$GIT_DIR/config mechanism.

With this workflow, you would want to know:

(1) ... if a topic branch has ever been merged to "next".  Young
    topic branches can have stupid mistakes you would rather
    clean up before publishing, and things that have not been
    merged into other branches can be easily rebased without
    affecting other people.  But once it is published, you would
    not want to rewind it.

(2) ... if a topic branch has been fully merged to "master".
    Then you can delete it.  More importantly, you should not
    build on top of it -- other people may already want to
    change things related to the topic as patches against your
    "master", so if you need further changes, it is better to
    fork the topic (perhaps with the same name) afresh from the
    tip of "master".

Let's look at this example:

		   o---o---o---o---o---o---o---o---o---o "next"
		  /       /           /           /
		 /   a---a---b A     /           /
		/   /               /           /
	       /   /   c---c---c---c B         /
	      /   /   /             \         /
	     /   /   /   b---b C     \       /
	    /   /   /   /             \     /
    ---o---o---o---o---o---o---o---o---o---o---o "master"


A, B and C are topic branches.

 * A has one fix since it was merged up to "next".

 * B has finished.  It has been fully merged up to "master" and "next",
   and is ready to be deleted.

 * C has not merged to "next" at all.

We would want to allow C to be rebased, refuse A, and encourage
B to be deleted.

To compute (1):

	git rev-list ^master ^topic next
	git rev-list ^master        next

	if these match, topic has not merged in next at all.

To compute (2):

	git rev-list master..topic

	if this is empty, it is fully merged to "master".

DOC_END

```

### .git/hooks/pre-receive.sample

```
#!/bin/sh
#
# An example hook script to make use of push options.
# The example simply echoes all push options that start with 'echoback='
# and rejects all pushes when the "reject" push option is used.
#
# To enable this hook, rename this file to "pre-receive".

if test -n "$GIT_PUSH_OPTION_COUNT"
then
	i=0
	while test "$i" -lt "$GIT_PUSH_OPTION_COUNT"
	do
		eval "value=\$GIT_PUSH_OPTION_$i"
		case "$value" in
		echoback=*)
			echo "echo from the pre-receive-hook: ${value#*=}" >&2
			;;
		reject)
			exit 1
		esac
		i=$((i + 1))
	done
fi

```

### .git/hooks/prepare-commit-msg.sample

```
#!/bin/sh
#
# An example hook script to prepare the commit log message.
# Called by "git commit" with the name of the file that has the
# commit message, followed by the description of the commit
# message's source.  The hook's purpose is to edit the commit
# message file.  If the hook fails with a non-zero status,
# the commit is aborted.
#
# To enable this hook, rename this file to "prepare-commit-msg".

# This hook includes three examples. The first one removes the
# "# Please enter the commit message..." help message.
#
# The second includes the output of "git diff --name-status -r"
# into the message, just before the "git status" output.  It is
# commented because it doesn't cope with --amend or with squashed
# commits.
#
# The third example adds a Signed-off-by line to the message, that can
# still be edited.  This is rarely a good idea.

COMMIT_MSG_FILE=$1
COMMIT_SOURCE=$2
SHA1=$3

/usr/bin/perl -i.bak -ne 'print unless(m/^. Please enter the commit message/..m/^#$/)' "$COMMIT_MSG_FILE"

# case "$COMMIT_SOURCE,$SHA1" in
#  ,|template,)
#    /usr/bin/perl -i.bak -pe '
#       print "\n" . `git diff --cached --name-status -r`
# 	 if /^#/ && $first++ == 0' "$COMMIT_MSG_FILE" ;;
#  *) ;;
# esac

# SOB=$(git var GIT_COMMITTER_IDENT | sed -n 's/^\(.*>\).*$/Signed-off-by: \1/p')
# git interpret-trailers --in-place --trailer "$SOB" "$COMMIT_MSG_FILE"
# if test -z "$COMMIT_SOURCE"
# then
#   /usr/bin/perl -i.bak -pe 'print "\n" if !$first_line++' "$COMMIT_MSG_FILE"
# fi

```

### .git/hooks/push-to-checkout.sample

```
#!/bin/sh

# An example hook script to update a checked-out tree on a git push.
#
# This hook is invoked by git-receive-pack(1) when it reacts to git
# push and updates reference(s) in its repository, and when the push
# tries to update the branch that is currently checked out and the
# receive.denyCurrentBranch configuration variable is set to
# updateInstead.
#
# By default, such a push is refused if the working tree and the index
# of the remote repository has any difference from the currently
# checked out commit; when both the working tree and the index match
# the current commit, they are updated to match the newly pushed tip
# of the branch. This hook is to be used to override the default
# behaviour; however the code below reimplements the default behaviour
# as a starting point for convenient modification.
#
# The hook receives the commit with which the tip of the current
# branch is going to be updated:
commit=$1

# It can exit with a non-zero status to refuse the push (when it does
# so, it must not modify the index or the working tree).
die () {
	echo >&2 "$*"
	exit 1
}

# Or it can make any necessary changes to the working tree and to the
# index to bring them to the desired state when the tip of the current
# branch is updated to the new commit, and exit with a zero status.
#
# For example, the hook can simply run git read-tree -u -m HEAD "$1"
# in order to emulate git fetch that is run in the reverse direction
# with git push, as the two-tree form of git read-tree -u -m is
# essentially the same as git switch or git checkout that switches
# branches while keeping the local changes in the working tree that do
# not interfere with the difference between the branches.

# The below is a more-or-less exact translation to shell of the C code
# for the default behaviour for git's push-to-checkout hook defined in
# the push_to_deploy() function in builtin/receive-pack.c.
#
# Note that the hook will be executed from the repository directory,
# not from the working tree, so if you want to perform operations on
# the working tree, you will have to adapt your code accordingly, e.g.
# by adding "cd .." or using relative paths.

if ! git update-index -q --ignore-submodules --refresh
then
	die "Up-to-date check failed"
fi

if ! git diff-files --quiet --ignore-submodules --
then
	die "Working directory has unstaged changes"
fi

# This is a rough translation of:
#
#   head_has_history() ? "HEAD" : EMPTY_TREE_SHA1_HEX
if git cat-file -e HEAD 2>/dev/null
then
	head=HEAD
else
	head=$(git hash-object -t tree --stdin </dev/null)
fi

if ! git diff-index --quiet --cached --ignore-submodules $head --
then
	die "Working directory has staged changes"
fi

if ! git read-tree -u -m "$commit"
then
	die "Could not update working tree to new HEAD"
fi

```

### .git/hooks/sendemail-validate.sample

```
#!/bin/sh

# An example hook script to validate a patch (and/or patch series) before
# sending it via email.
#
# The hook should exit with non-zero status after issuing an appropriate
# message if it wants to prevent the email(s) from being sent.
#
# To enable this hook, rename this file to "sendemail-validate".
#
# By default, it will only check that the patch(es) can be applied on top of
# the default upstream branch without conflicts in a secondary worktree. After
# validation (successful or not) of the last patch of a series, the worktree
# will be deleted.
#
# The following config variables can be set to change the default remote and
# remote ref that are used to apply the patches against:
#
#   sendemail.validateRemote (default: origin)
#   sendemail.validateRemoteRef (default: HEAD)
#
# Replace the TODO placeholders with appropriate checks according to your
# needs.

validate_cover_letter () {
	file="$1"
	# TODO: Replace with appropriate checks (e.g. spell checking).
	true
}

validate_patch () {
	file="$1"
	# Ensure that the patch applies without conflicts.
	git am -3 "$file" || return
	# TODO: Replace with appropriate checks for this patch
	# (e.g. checkpatch.pl).
	true
}

validate_series () {
	# TODO: Replace with appropriate checks for the whole series
	# (e.g. quick build, coding style checks, etc.).
	true
}

# main -------------------------------------------------------------------------

if test "$GIT_SENDEMAIL_FILE_COUNTER" = 1
then
	remote=$(git config --default origin --get sendemail.validateRemote) &&
	ref=$(git config --default HEAD --get sendemail.validateRemoteRef) &&
	worktree=$(mktemp --tmpdir -d sendemail-validate.XXXXXXX) &&
	git worktree add -fd --checkout "$worktree" "refs/remotes/$remote/$ref" &&
	git config --replace-all sendemail.validateWorktree "$worktree"
else
	worktree=$(git config --get sendemail.validateWorktree)
fi || {
	echo "sendemail-validate: error: failed to prepare worktree" >&2
	exit 1
}

unset GIT_DIR GIT_WORK_TREE
cd "$worktree" &&

if grep -q "^diff --git " "$1"
then
	validate_patch "$1"
else
	validate_cover_letter "$1"
fi &&

if test "$GIT_SENDEMAIL_FILE_COUNTER" = "$GIT_SENDEMAIL_FILE_TOTAL"
then
	git config --unset-all sendemail.validateWorktree &&
	trap 'git worktree remove -ff "$worktree"' EXIT &&
	validate_series
fi

```

### .git/hooks/update.sample

```
#!/bin/sh
#
# An example hook script to block unannotated tags from entering.
# Called by "git receive-pack" with arguments: refname sha1-old sha1-new
#
# To enable this hook, rename this file to "update".
#
# Config
# ------
# hooks.allowunannotated
#   This boolean sets whether unannotated tags will be allowed into the
#   repository.  By default they won't be.
# hooks.allowdeletetag
#   This boolean sets whether deleting tags will be allowed in the
#   repository.  By default they won't be.
# hooks.allowmodifytag
#   This boolean sets whether a tag may be modified after creation. By default
#   it won't be.
# hooks.allowdeletebranch
#   This boolean sets whether deleting branches will be allowed in the
#   repository.  By default they won't be.
# hooks.denycreatebranch
#   This boolean sets whether remotely creating branches will be denied
#   in the repository.  By default this is allowed.
#

# --- Command line
refname="$1"
oldrev="$2"
newrev="$3"

# --- Safety check
if [ -z "$GIT_DIR" ]; then
	echo "Don't run this script from the command line." >&2
	echo " (if you want, you could supply GIT_DIR then run" >&2
	echo "  $0 <ref> <oldrev> <newrev>)" >&2
	exit 1
fi

if [ -z "$refname" -o -z "$oldrev" -o -z "$newrev" ]; then
	echo "usage: $0 <ref> <oldrev> <newrev>" >&2
	exit 1
fi

# --- Config
allowunannotated=$(git config --type=bool hooks.allowunannotated)
allowdeletebranch=$(git config --type=bool hooks.allowdeletebranch)
denycreatebranch=$(git config --type=bool hooks.denycreatebranch)
allowdeletetag=$(git config --type=bool hooks.allowdeletetag)
allowmodifytag=$(git config --type=bool hooks.allowmodifytag)

# check for no description
projectdesc=$(sed -e '1q' "$GIT_DIR/description")
case "$projectdesc" in
"Unnamed repository"* | "")
	echo "*** Project description file hasn't been set" >&2
	exit 1
	;;
esac

# --- Check types
# if $newrev is 0000...0000, it's a commit to delete a ref.
zero=$(git hash-object --stdin </dev/null | tr '[0-9a-f]' '0')
if [ "$newrev" = "$zero" ]; then
	newrev_type=delete
else
	newrev_type=$(git cat-file -t $newrev)
fi

case "$refname","$newrev_type" in
	refs/tags/*,commit)
		# un-annotated tag
		short_refname=${refname##refs/tags/}
		if [ "$allowunannotated" != "true" ]; then
			echo "*** The un-annotated tag, $short_refname, is not allowed in this repository" >&2
			echo "*** Use 'git tag [ -a | -s ]' for tags you want to propagate." >&2
			exit 1
		fi
		;;
	refs/tags/*,delete)
		# delete tag
		if [ "$allowdeletetag" != "true" ]; then
			echo "*** Deleting a tag is not allowed in this repository" >&2
			exit 1
		fi
		;;
	refs/tags/*,tag)
		# annotated tag
		if [ "$allowmodifytag" != "true" ] && git rev-parse $refname > /dev/null 2>&1
		then
			echo "*** Tag '$refname' already exists." >&2
			echo "*** Modifying a tag is not allowed in this repository." >&2
			exit 1
		fi
		;;
	refs/heads/*,commit)
		# branch
		if [ "$oldrev" = "$zero" -a "$denycreatebranch" = "true" ]; then
			echo "*** Creating a branch is not allowed in this repository" >&2
			exit 1
		fi
		;;
	refs/heads/*,delete)
		# delete branch
		if [ "$allowdeletebranch" != "true" ]; then
			echo "*** Deleting a branch is not allowed in this repository" >&2
			exit 1
		fi
		;;
	refs/remotes/*,commit)
		# tracking branch
		;;
	refs/remotes/*,delete)
		# delete tracking branch
		if [ "$allowdeletebranch" != "true" ]; then
			echo "*** Deleting a tracking branch is not allowed in this repository" >&2
			exit 1
		fi
		;;
	*)
		# Anything else (is there anything else?)
		echo "*** Update hook: unknown type of update to ref $refname of type $newrev_type" >&2
		exit 1
		;;
esac

# --- Finished
exit 0

```

### codebase_prompt_gen/__init__.py

```
"""Codebase AI Prompt Generator.

A tool to scan Git repositories and generate comprehensive prompts for AI models.
"""

__version__ = "0.1.0" 
```

### codebase_prompt_gen/core.py

```
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
```

### codebase_prompt_gen/__pycache__/__init__.cpython-313.pyc

```
�

    ���g�   �                   �   � S r Srg)zqCodebase AI Prompt Generator.

A tool to scan Git repositories and generate comprehensive prompts for AI models.
z0.1.0N)�__doc__�__version__� �    �M/Users/ydeng/src/codebase-ai-prompt-generator/codebase_prompt_gen/__init__.py�<module>r      s   ���
 �r   
```

### codebase_prompt_gen/__pycache__/core.cpython-313.pyc

```
�

    ���g@  �                   �8   � S r SSKrSSKrSSKJr  SS jrSS jrg)z8Core functionality for the Codebase AI Prompt Generator.�    N)�Pathc           	      ��  ^	^� Uc  / SQn/ n/ n/ n[         R                  " U 5       GH  u  pgnU V	^	s/ s H!  m	[        U	4S jU 5       5      (       a  M  T	PM#     sn	USS& [         R                  R	                  X`5      n
U
S:X  a  Sn
U
(       a  UR                  SU
 S35        [
        U5       H�  m[        U4S jU 5       5      (       a  M  U(       a  [        U4S	 jU 5       5      (       d  MB  U
(       a   [         R                  R                  U
T5      OTnUR                  S
U 35        UR                  U5        M�     GM     U H\  n[         R                  R                  X5      n [        USSS
S9 n
U
R                  5       nUR                  UUS.5        SSS5        M^     X44$ s  sn	f ! , (       d  f       Mw  = f! [         a,  nUR                  US[        U5       S3S.5         SnAM�  SnAff = f)a�  Generate a file tree structure for a given directory.

Args:
    root_dir: The root directory to scan
    exclude_patterns: List of glob patterns to exclude
    include_patterns: List of glob patterns to include
    
Returns:
    Tuple of (file_tree, files_content) where file_tree is a list of 
    formatted strings and files_content is a list of dictionaries with 
    path and content keys
N)z.git�__pycache__z*.pyc�node_modulesz	.DS_Storec              3   �R   >#   � U  H  n[         R                   " TU5      v �  M     g 7f�N��fnmatch)�.0�pattern�ds     ��I/Users/ydeng/src/codebase-ai-prompt-generator/codebase_prompt_gen/core.py�	<genexpr>�%generate_file_tree.<locals>.<genexpr>   s"   �� � �5r�aq�V]�g�o�o�a��6Q�6Q�aq��   �$'�.� u   📁 �/c              3   �R   >#   � U  H  n[         R                   " TU5      v �  M     g 7fr   r	   �r   r   �filenames     �r   r   r   -   s!   �� � �V�EU�'�7�?�?�8�W�5�5�EU�r   c              3   �R   >#   � U  H  n[         R                   " TU5      v �  M     g 7fr   r	   r   s     �r   r   r   1   s"   �� � �+o�^n�SZ�G�O�O�H�g�,N�,N�^n�r   u   📄 �r�utf-8�replace)�encoding�errors)�path�contentz[Error reading file: �])�os�walk�anyr   �relpath�append�sorted�join�open�read�	Exception�str)�root_dir�exclude_patterns�include_patterns�	file_tree�
files_content�	all_files�dirpath�dirnames�	filenamesr
   �rel_path�	file_path�abs_path�fr   �er   s            `      @r   �generate_file_treer:      s�  �� � ��X���I��M� �I�(*����(9�$��9�"*�s�(�Q�#�5r�aq�5r�2r�q�(�s���� �7�7�?�?�7�5���s�?��H� ����u�X�J�a�0�1� �y�)�H��V�EU�V�V�V��  ��+o�^n�+o�(o�(o��<D������X�x�8�(�I����u�Y�K�0�1����Y�'� *� ):�8 �	��7�7�<�<��4��	��h��g�i�H�A��&�&�(���$�$�%�&�&� � I�H� � �#�#��S t�: I�H�� � 	�� � �!�2�3�q�6�(�!�<�"� 
� 
��	�sA   �F,�F,�,G�8%F1�G�1
G 	�;G� G�
G9�
!G4�4G9c                 ��  � [         R                  R                  U 5      n [         R                  R                  U 5      n[	        XU5      u  pVSU S3nUS-
  nUSR                  U5      -
  nUS-
  nUS-
  nU H   nUSUS    S3-
  nUS-
  nXxS	   -
  nUS
-
  nM"     U(       a3  [
        USSS
9 n	U	R                  U5        SSS5        [        SU 35        U$ ! , (       d  f       N= f)aY  Generate a prompt for AI models containing the file tree and file contents.

Args:
    repo_path: Path to the Git repository
    exclude_patterns: List of glob patterns to exclude
    include_patterns: List of glob patterns to include
    output_file: Optional file path to write the prompt to
    
Returns:
    The generated prompt as a string
z# Repository: z

z## File Tree Structure

�
z## File Contents

z### r   z```
r   z
```

�wr   )r   NzPrompt written to )	r!   r   �abspath�basenamer:   r'   r(   �write�print)
�	repo_pathr-   r.   �output_file�	repo_namer/   r0   �prompt�	file_infor8   s
             r   �generate_promptrG   K   s  � � �����	�*�I���� � ��+�I�1�)�O_�`��I� �i�[��
-�F� �*�*�F�
�d�i�i�	�"�"�F�
�f��F� �$�$�F�"�	��D��6�*�+�4�0�0���'����I�&�&���+���	 #� �
�+�s�W�
5��
�G�G�F�O� 6�
�"�;�-�0�1��M�	 6�
5�s   �.C�
C&)NN)NNN)�__doc__r!   r
   �pathlibr   r:   rG   � �    r   �<module>rL      s   �� >� 	� � �@$�F'rK   
```

### codebase_prompt_gen/cli/__init__.py

```
"""Command-line interface for Codebase AI Prompt Generator.""" 
```

### codebase_prompt_gen/cli/main.py

```
"""Command-line interface for Codebase AI Prompt Generator."""

import argparse
import sys
from codebase_prompt_gen.core import generate_prompt


def main():
    """Main entry point for the CLI."""
    parser = argparse.ArgumentParser(description='Generate AI prompts from Git repositories')
    parser.add_argument('repo_path', type=str, nargs='?', default='.', 
                        help='Path to the Git repository (default: current directory)')
    parser.add_argument('--exclude', type=str, nargs='+', 
                        help='Patterns of files/directories to exclude (e.g., *.log)')
    parser.add_argument('--include', type=str, nargs='+', 
                        help='Patterns of files to include (e.g., *.py)')
    parser.add_argument('--output', type=str, 
                        help='Output file to write the prompt to')
    parser.add_argument('--version', action='store_true',
                        help='Show version information and exit')
    
    args = parser.parse_args()
    
    if args.version:
        from codebase_prompt_gen import __version__
        print(f"Codebase AI Prompt Generator v{__version__}")
        return 0
    
    try:
        prompt = generate_prompt(args.repo_path, args.exclude, args.include, args.output)
        if not args.output:
            print(prompt)
        return 0
    except Exception as e:
        print(f"Error: {str(e)}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main()) 
```

### codebase_prompt_gen/cli/__pycache__/__init__.cpython-313.pyc

```
�

    ���g?   �                   �   � S r g)z8Command-line interface for Codebase AI Prompt Generator.N)�__doc__� �    �Q/Users/ydeng/src/codebase-ai-prompt-generator/codebase_prompt_gen/cli/__init__.py�<module>r      s   �� >r   
```

### codebase_prompt_gen/cli/__pycache__/main.cpython-313.pyc

```
�

    ���g�  �                   �f   � S r SSKrSSKrSSKJr  S r\S:X  a  \R                  " \" 5       5        gg)z8Command-line interface for Codebase AI Prompt Generator.�    N)�generate_promptc                  �  � [         R                  " SS9n U R                  S[        SSSS9  U R                  S[        S	S
S9  U R                  S[        S	S
S9  U R                  S[        SS9  U R                  SSSS9  U R	                  5       nUR
                  (       a  SSKJn  [        SU 35        g [        UR                  UR                  UR                  UR                  5      nUR                  (       d  [        U5        g! [         a.  n[        S[        U5       3[        R                   S9   SnAgSnAff = f)zMain entry point for the CLI.z)Generate AI prompts from Git repositories)�description�	repo_path�?�.z7Path to the Git repository (default: current directory))�type�nargs�default�helpz	--exclude�+z6Patterns of files/directories to exclude (e.g., *.log))r	   r
   r   z	--includez)Patterns of files to include (e.g., *.py)z--outputz"Output file to write the prompt to)r	   r   z	--version�
store_truez!Show version information and exit)�actionr   r   )�__version__zCodebase AI Prompt Generator vzError: )�fileN�   )�argparse�ArgumentParser�add_argument�str�
parse_args�version�codebase_prompt_genr   �printr   r   �exclude�include�output�	Exception�sys�stderr)�parser�argsr   �prompt�es        �M/Users/ydeng/src/codebase-ai-prompt-generator/codebase_prompt_gen/cli/main.py�mainr&      s1  � �
�
$�
$�1\�
]�F�
����#�S�#�V� � X�
����#�S�U� � W�
����#�S�H� � J�
���
��A� � C�
����L�@� � B� ����D��|�|�3�
�.�{�m�<�=��� �������t�|�|�T�[�[�Y���{�{��&�M���� �
���A��x� �s�z�z�2����s   �5AD �
E �$D;�;E �__main__)�__doc__r   r   �codebase_prompt_gen.corer   r&   �__name__�exit� �    r%   �<module>r.      s3   �� >� � 
� 4��> �z���H�H�T�V�� r-   
```

### codebase_ai_prompt_generator.egg-info/PKG-INFO

```
Metadata-Version: 2.1
Name: codebase-ai-prompt-generator
Version: 0.1.0
Summary: Generate AI prompts from Git repositories with file tree structures and content
Author-email: Your Name <your.email@example.com>
License: MIT
Project-URL: Homepage, https://github.com/yourusername/codebase-ai-prompt-generator
Project-URL: Bug Tracker, https://github.com/yourusername/codebase-ai-prompt-generator/issues
Keywords: ai,prompt,git,code,repository
Classifier: Development Status :: 3 - Alpha
Classifier: Intended Audience :: Developers
Classifier: Topic :: Software Development :: Libraries :: Python Modules
Classifier: License :: OSI Approved :: MIT License
Classifier: Programming Language :: Python :: 3
Classifier: Programming Language :: Python :: 3.8
Classifier: Programming Language :: Python :: 3.9
Classifier: Programming Language :: Python :: 3.10
Classifier: Programming Language :: Python :: 3.11
Requires-Python: >=3.8
Description-Content-Type: text/markdown
License-File: LICENSE

# Codebase AI Prompt Generator

A tool to scan a Git repository and generate a comprehensive prompt for AI models, including file tree structure, file paths, and content.

## Features

- Creates a hierarchical file tree representation of a repository
- Includes file contents formatted for AI prompts
- Customizable file inclusion/exclusion via patterns
- Option to save output to a file or print to console
- Installable CLI tool

## Installation

```bash
# From PyPI (recommended)
pip install codebase-ai-prompt-generator

# From source
git clone https://github.com/yourusername/codebase-ai-prompt-generator.git
cd codebase-ai-prompt-generator
pip install -e .
```

## Usage

After installation, you can use the `codebase-prompt` command directly from your terminal:

```bash
# Basic usage (scans current directory)
codebase-prompt

# Scan a specific repository
codebase-prompt /path/to/repository

# Exclude specific file patterns
codebase-prompt --exclude "*.log" "*.tmp" ".env"

# Include only specific file patterns
codebase-prompt --include "*.py" "*.js" "*.html"

# Write output to a file
codebase-prompt --output prompt.md

# Show version information
codebase-prompt --version

# Combine options
codebase-prompt /path/to/repository --exclude "node_modules" "*.pyc" --include "*.py" "*.js" --output prompt.md
```

## Example Output

The generated prompt will have the following structure:

```
# Repository: repo-name

## File Tree Structure

📁 src/
📄 src/main.py
📄 src/utils.py
📁 tests/
📄 tests/test_main.py
📄 README.md

## File Contents

### src/main.py

```python
def main():
    print("Hello World")
```

### src/utils.py

```python
def helper():
    return "Helper function"
```

...
```

## Use Cases

- Generate prompts for AI code assistants to understand your entire codebase
- Create documentation snapshots of your repository
- Share codebase context with AI models for better assistance
- Provide comprehensive context to LLMs for code-related questions

## Development

To set up the development environment:

```bash
# Clone the repository
git clone https://github.com/yourusername/codebase-ai-prompt-generator.git
cd codebase-ai-prompt-generator

# Create and activate a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install in development mode
pip install -e .
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

```

### codebase_ai_prompt_generator.egg-info/SOURCES.txt

```
LICENSE
README.md
pyproject.toml
codebase_ai_prompt_generator.egg-info/PKG-INFO
codebase_ai_prompt_generator.egg-info/SOURCES.txt
codebase_ai_prompt_generator.egg-info/dependency_links.txt
codebase_ai_prompt_generator.egg-info/entry_points.txt
codebase_ai_prompt_generator.egg-info/top_level.txt
codebase_prompt_gen/__init__.py
codebase_prompt_gen/core.py
codebase_prompt_gen/cli/__init__.py
codebase_prompt_gen/cli/main.py
```

### codebase_ai_prompt_generator.egg-info/dependency_links.txt

```


```

### codebase_ai_prompt_generator.egg-info/entry_points.txt

```
[console_scripts]
codebase-prompt = codebase_prompt_gen.cli.main:main

```

### codebase_ai_prompt_generator.egg-info/top_level.txt

```
codebase_prompt_gen

```


```

### pyproject.toml

```
[build-system]
requires = ["setuptools>=61.0", "wheel"]
build-backend = "setuptools.build_meta"

[project]
name = "codebase-ai-prompt-generator"
version = "0.1.0"
description = "Generate AI prompts from Git repositories with file tree structures and content"
readme = "README.md"
requires-python = ">=3.8"
license = {text = "MIT"}
keywords = ["ai", "prompt", "git", "code", "repository"]
authors = [
    {name = "Your Name", email = "your.email@example.com"}
]
classifiers = [
    "Development Status :: 3 - Alpha",
    "Intended Audience :: Developers",
    "Topic :: Software Development :: Libraries :: Python Modules",
    "License :: OSI Approved :: MIT License",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.8",
    "Programming Language :: Python :: 3.9",
    "Programming Language :: Python :: 3.10",
    "Programming Language :: Python :: 3.11",
]

[project.urls]
"Homepage" = "https://github.com/yourusername/codebase-ai-prompt-generator"
"Bug Tracker" = "https://github.com/yourusername/codebase-ai-prompt-generator/issues"

[project.scripts]
codebase-prompt = "codebase_prompt_gen.cli.main:main"

[tool.setuptools]
packages = ["codebase_prompt_gen", "codebase_prompt_gen.cli"]

```

### test_output.md

```
# Repository: codebase-ai-prompt-generator

## File Tree Structure

📄 .gitignore
📄 .python-version
📄 LICENSE
📄 README.md
📄 main.py
📄 pyproject.toml

## File Contents

### .gitignore

```
# Python-generated files
__pycache__/
*.py[oc]
build/
dist/
wheels/
*.egg-info

# Virtual environments
.venv

```

### .python-version

```
3.10

```

### LICENSE

```
MIT License

Copyright (c) 2023 

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE. 
```

### README.md

```
# Codebase AI Prompt Generator

A tool to scan a Git repository and generate a comprehensive prompt for AI models, including file tree structure, file paths, and content.

## Features

- Creates a hierarchical file tree representation of a repository
- Includes file contents formatted for AI prompts
- Customizable file inclusion/exclusion via patterns
- Option to save output to a file or print to console

## Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/codebase-ai-prompt-generator.git
cd codebase-ai-prompt-generator

# Optional: Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -e .
```

## Usage

```bash
# Basic usage (scans current directory)
python main.py

# Scan a specific repository
python main.py /path/to/repository

# Exclude specific file patterns
python main.py --exclude "*.log" "*.tmp" ".env"

# Include only specific file patterns
python main.py --include "*.py" "*.js" "*.html"

# Write output to a file
python main.py --output prompt.md

# Combine options
python main.py /path/to/repository --exclude "node_modules" "*.pyc" --include "*.py" "*.js" --output prompt.md
```

## Example Output

The generated prompt will have the following structure:

```
# Repository: repo-name

## File Tree Structure

📁 src/
📄 src/main.py
📄 src/utils.py
📁 tests/
📄 tests/test_main.py
📄 README.md

## File Contents

### src/main.py

```python
def main():
    print("Hello World")
```

### src/utils.py

```python
def helper():
    return "Helper function"
```

...
```

## Use Cases

- Generate prompts for AI code assistants to understand your entire codebase
- Create documentation snapshots of your repository
- Share codebase context with AI models for better assistance

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

```

### main.py

```
import os
import argparse
from pathlib import Path
import fnmatch


def generate_file_tree(root_dir, exclude_patterns=None, include_patterns=None):
    """Generate a file tree structure for a given directory."""
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
    """Generate a prompt for AI models containing the file tree and file contents."""
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
    else:
        print(prompt)
    
    return prompt


def main():
    parser = argparse.ArgumentParser(description='Generate AI prompts from Git repositories')
    parser.add_argument('repo_path', type=str, nargs='?', default='.', 
                        help='Path to the Git repository (default: current directory)')
    parser.add_argument('--exclude', type=str, nargs='+', 
                        help='Patterns of files/directories to exclude (e.g., *.log)')
    parser.add_argument('--include', type=str, nargs='+', 
                        help='Patterns of files to include (e.g., *.py)')
    parser.add_argument('--output', type=str, 
                        help='Output file to write the prompt to')
    
    args = parser.parse_args()
    
    generate_prompt(args.repo_path, args.exclude, args.include, args.output)


if __name__ == "__main__":
    main()

```

### pyproject.toml

```
[project]
name = "codebase-ai-prompt-generator"
version = "0.1.0"
description = "Generate AI prompts from Git repositories with file tree structures and content"
readme = "README.md"
requires-python = ">=3.8"
dependencies = []
authors = [
    {name = "Your Name", email = "your.email@example.com"}
]
license = {text = "MIT"}
classifiers = [
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
]

[project.scripts]
codebase-ai-prompt = "main:main"

[build-system]
requires = ["setuptools>=61.0"]
build-backend = "setuptools.build_meta"

[tool.setuptools]
packages = [""]

```


```

### with_gitignore.md

```
# Repository: codebase-ai-prompt-generator

## File Tree Structure

📄 .gitignore
📄 LICENSE
📄 README.md
📄 pyproject.toml
📁 codebase_prompt_gen/
📄 codebase_prompt_gen/__init__.py
📄 codebase_prompt_gen/core.py
📁 codebase_prompt_gen/cli/
📄 codebase_prompt_gen/cli/__init__.py
📄 codebase_prompt_gen/cli/main.py

## File Contents

### .gitignore

```
# Python-generated files
__pycache__/
*.py[oc]
build/
dist/
wheels/
*.egg-info

# Virtual environments
.venv
venv/
ENV/

# Testing and output files
test_output.md
cli_test_output.md

# IDEs and editors
.vscode/
.idea/
*.swp
*~
.DS_Store

```

### LICENSE

```
MIT License

Copyright (c) 2023 

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE. 
```

### README.md

```
# Codebase AI Prompt Generator

A tool to scan a Git repository and generate a comprehensive prompt for AI models, including file tree structure, file paths, and content.

## Features

- Creates a hierarchical file tree representation of a repository
- Includes file contents formatted for AI prompts
- Customizable file inclusion/exclusion via patterns
- Option to save output to a file or print to console
- Automatically respects local and global .gitignore files
- Installable CLI tool

## Installation

```bash
# From PyPI (recommended)
pip install codebase-ai-prompt-generator

# From source
git clone https://github.com/yourusername/codebase-ai-prompt-generator.git
cd codebase-ai-prompt-generator
pip install -e .
```

## Usage

After installation, you can use the `codebase-prompt` command directly from your terminal:

```bash
# Basic usage (scans current directory)
codebase-prompt

# Scan a specific repository
codebase-prompt /path/to/repository

# Exclude specific file patterns
codebase-prompt --exclude "*.log" "*.tmp" ".env"

# Include only specific file patterns
codebase-prompt --include "*.py" "*.js" "*.html"

# Write output to a file
codebase-prompt --output prompt.md

# Show version information
codebase-prompt --version

# Ignore .gitignore files (both local and global)
codebase-prompt --no-gitignore

# Combine options
codebase-prompt /path/to/repository --exclude "node_modules" "*.pyc" --include "*.py" "*.js" --output prompt.md
```

## .gitignore Support

By default, the tool respects both:
- The repository's local `.gitignore` file
- The user's global gitignore file (found via `git config --global --get core.excludesfile`)

Files matching any pattern in these files will be excluded from the output. To disable this feature, use the `--no-gitignore` flag.

## Example Output

The generated prompt will have the following structure:

```
# Repository: repo-name

## File Tree Structure

📁 src/
📄 src/main.py
📄 src/utils.py
📁 tests/
📄 tests/test_main.py
📄 README.md

## File Contents

### src/main.py

```python
def main():
    print("Hello World")
```

### src/utils.py

```python
def helper():
    return "Helper function"
```

...
```

## Use Cases

- Generate prompts for AI code assistants to understand your entire codebase
- Create documentation snapshots of your repository
- Share codebase context with AI models for better assistance
- Provide comprehensive context to LLMs for code-related questions

## Development

To set up the development environment:

```bash
# Clone the repository
git clone https://github.com/yourusername/codebase-ai-prompt-generator.git
cd codebase-ai-prompt-generator

# Create and activate a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install in development mode
pip install -e .
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

```

### pyproject.toml

```
[build-system]
requires = ["setuptools>=61.0", "wheel"]
build-backend = "setuptools.build_meta"

[project]
name = "codebase-ai-prompt-generator"
version = "0.1.0"
description = "Generate AI prompts from Git repositories with file tree structures and content"
readme = "README.md"
requires-python = ">=3.8"
license = {text = "MIT"}
keywords = ["ai", "prompt", "git", "code", "repository"]
authors = [
    {name = "Your Name", email = "your.email@example.com"}
]
classifiers = [
    "Development Status :: 3 - Alpha",
    "Intended Audience :: Developers",
    "Topic :: Software Development :: Libraries :: Python Modules",
    "License :: OSI Approved :: MIT License",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.8",
    "Programming Language :: Python :: 3.9",
    "Programming Language :: Python :: 3.10",
    "Programming Language :: Python :: 3.11",
]

[project.urls]
"Homepage" = "https://github.com/yourusername/codebase-ai-prompt-generator"
"Bug Tracker" = "https://github.com/yourusername/codebase-ai-prompt-generator/issues"

[project.scripts]
codebase-prompt = "codebase_prompt_gen.cli.main:main"

[tool.setuptools]
packages = ["codebase_prompt_gen", "codebase_prompt_gen.cli"]

```

### codebase_prompt_gen/__init__.py

```
"""Codebase AI Prompt Generator.

A tool to scan Git repositories and generate comprehensive prompts for AI models.
"""

__version__ = "0.1.0" 
```

### codebase_prompt_gen/core.py

```
"""Core functionality for the Codebase AI Prompt Generator."""

import os
import fnmatch
from pathlib import Path
import subprocess


def read_gitignore_file(file_path):
    """Read a .gitignore file and return a list of patterns.
    
    Args:
        file_path: Path to the .gitignore file
        
    Returns:
        List of gitignore patterns
    """
    patterns = []
    if os.path.exists(file_path):
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                for line in f:
                    line = line.strip()
                    # Skip empty lines and comments
                    if line and not line.startswith('#'):
                        patterns.append(line)
        except Exception:
            # Silently fail if the file can't be read
            pass
    return patterns


def get_global_gitignore_patterns():
    """Get global gitignore patterns.
    
    Returns:
        List of global gitignore patterns
    """
    try:
        # Try to get the global gitignore file path
        result = subprocess.run(
            ["git", "config", "--global", "--get", "core.excludesfile"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            check=False
        )
        
        if result.returncode == 0 and result.stdout.strip():
            global_gitignore_path = os.path.expanduser(result.stdout.strip())
            return read_gitignore_file(global_gitignore_path)
    except (subprocess.SubprocessError, FileNotFoundError):
        # Git not installed or other error
        pass
    
    return []


def gitignore_to_pattern(gitignore_pattern):
    """Convert a gitignore pattern to a glob pattern.
    
    Args:
        gitignore_pattern: A pattern from a .gitignore file
        
    Returns:
        A glob pattern compatible with fnmatch
    """
    # Handle negation (patterns that start with !)
    if gitignore_pattern.startswith('!'):
        # Negation is not directly supported in fnmatch
        # Just return the pattern without the negation for now
        gitignore_pattern = gitignore_pattern[1:]
    
    # Handle directory-specific patterns (ending with /)
    if gitignore_pattern.endswith('/'):
        gitignore_pattern = gitignore_pattern[:-1]
    
    # Convert ** to match any number of directories
    if '**' in gitignore_pattern:
        gitignore_pattern = gitignore_pattern.replace('**/', '**/').replace('/**', '/**')
    
    return gitignore_pattern


def generate_file_tree(root_dir, exclude_patterns=None, include_patterns=None, respect_gitignore=True):
    """Generate a file tree structure for a given directory.
    
    Args:
        root_dir: The root directory to scan
        exclude_patterns: List of glob patterns to exclude
        include_patterns: List of glob patterns to include
        respect_gitignore: Whether to respect .gitignore files
        
    Returns:
        Tuple of (file_tree, files_content) where file_tree is a list of 
        formatted strings and files_content is a list of dictionaries with 
        path and content keys
    """
    if exclude_patterns is None:
        exclude_patterns = [".git", "__pycache__", "*.pyc", "node_modules", ".DS_Store"]
    else:
        # Make a copy to avoid modifying the original list
        exclude_patterns = exclude_patterns.copy()
    
    # Add gitignore patterns if requested
    if respect_gitignore:
        # Add global gitignore patterns
        global_patterns = get_global_gitignore_patterns()
        for pattern in global_patterns:
            glob_pattern = gitignore_to_pattern(pattern)
            if glob_pattern and glob_pattern not in exclude_patterns:
                exclude_patterns.append(glob_pattern)
        
        # Add local gitignore patterns
        local_gitignore_path = os.path.join(root_dir, '.gitignore')
        local_patterns = read_gitignore_file(local_gitignore_path)
        for pattern in local_patterns:
            glob_pattern = gitignore_to_pattern(pattern)
            if glob_pattern and glob_pattern not in exclude_patterns:
                exclude_patterns.append(glob_pattern)
    
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
            # Check if full path matches any exclude pattern
            file_path = os.path.join(rel_path, filename) if rel_path else filename
            if any(fnmatch.fnmatch(file_path, pattern) for pattern in exclude_patterns) or \
               any(fnmatch.fnmatch(filename, pattern) for pattern in exclude_patterns):
                continue
                
            # Apply include patterns if specified
            if include_patterns and not any(fnmatch.fnmatch(filename, pattern) for pattern in include_patterns) and \
               not any(fnmatch.fnmatch(file_path, pattern) for pattern in include_patterns):
                continue
                
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


def generate_prompt(repo_path, exclude_patterns=None, include_patterns=None, output_file=None, respect_gitignore=True):
    """Generate a prompt for AI models containing the file tree and file contents.
    
    Args:
        repo_path: Path to the Git repository
        exclude_patterns: List of glob patterns to exclude
        include_patterns: List of glob patterns to include
        output_file: Optional file path to write the prompt to
        respect_gitignore: Whether to respect .gitignore files
        
    Returns:
        The generated prompt as a string
    """
    repo_path = os.path.abspath(repo_path)
    repo_name = os.path.basename(repo_path)
    
    file_tree, files_content = generate_file_tree(repo_path, exclude_patterns, include_patterns, respect_gitignore)
    
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
```

### codebase_prompt_gen/cli/__init__.py

```
"""Command-line interface for Codebase AI Prompt Generator.""" 
```

### codebase_prompt_gen/cli/main.py

```
"""Command-line interface for Codebase AI Prompt Generator."""

import argparse
import sys
from codebase_prompt_gen.core import generate_prompt


def main():
    """Main entry point for the CLI."""
    parser = argparse.ArgumentParser(description='Generate AI prompts from Git repositories')
    parser.add_argument('repo_path', type=str, nargs='?', default='.', 
                        help='Path to the Git repository (default: current directory)')
    parser.add_argument('--exclude', type=str, nargs='+', 
                        help='Patterns of files/directories to exclude (e.g., *.log)')
    parser.add_argument('--include', type=str, nargs='+', 
                        help='Patterns of files to include (e.g., *.py)')
    parser.add_argument('--output', type=str, 
                        help='Output file to write the prompt to')
    parser.add_argument('--no-gitignore', action='store_true',
                        help='Ignore .gitignore files (both local and global)')
    parser.add_argument('--version', action='store_true',
                        help='Show version information and exit')
    
    args = parser.parse_args()
    
    if args.version:
        from codebase_prompt_gen import __version__
        print(f"Codebase AI Prompt Generator v{__version__}")
        return 0
    
    try:
        prompt = generate_prompt(
            args.repo_path, 
            args.exclude, 
            args.include, 
            args.output,
            respect_gitignore=not args.no_gitignore
        )
        if not args.output:
            print(prompt)
        return 0
    except Exception as e:
        print(f"Error: {str(e)}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main()) 
```


```

### codebase_prompt_gen/__init__.py

```
"""Codebase AI Prompt Generator.

A tool to scan Git repositories and generate comprehensive prompts for AI models.
"""

__version__ = "0.1.0" 
```

### codebase_prompt_gen/core.py

```
"""Core functionality for the Codebase AI Prompt Generator."""

import os
import fnmatch
from pathlib import Path
import subprocess


def read_gitignore_file(file_path):
    """Read a .gitignore file and return a list of patterns.
    
    Args:
        file_path: Path to the .gitignore file
        
    Returns:
        List of gitignore patterns
    """
    patterns = []
    if os.path.exists(file_path):
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                for line in f:
                    line = line.strip()
                    # Skip empty lines and comments
                    if line and not line.startswith('#'):
                        patterns.append(line)
        except Exception:
            # Silently fail if the file can't be read
            pass
    return patterns


def get_global_gitignore_patterns():
    """Get global gitignore patterns.
    
    Returns:
        List of global gitignore patterns
    """
    try:
        # Try to get the global gitignore file path
        result = subprocess.run(
            ["git", "config", "--global", "--get", "core.excludesfile"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            check=False
        )
        
        if result.returncode == 0 and result.stdout.strip():
            global_gitignore_path = os.path.expanduser(result.stdout.strip())
            return read_gitignore_file(global_gitignore_path)
    except (subprocess.SubprocessError, FileNotFoundError):
        # Git not installed or other error
        pass
    
    return []


def gitignore_to_pattern(gitignore_pattern):
    """Convert a gitignore pattern to a glob pattern.
    
    Args:
        gitignore_pattern: A pattern from a .gitignore file
        
    Returns:
        A glob pattern compatible with fnmatch
    """
    # Handle negation (patterns that start with !)
    if gitignore_pattern.startswith('!'):
        # Negation is not directly supported in fnmatch
        # Just return the pattern without the negation for now
        gitignore_pattern = gitignore_pattern[1:]
    
    # Handle directory-specific patterns (ending with /)
    if gitignore_pattern.endswith('/'):
        gitignore_pattern = gitignore_pattern[:-1]
    
    # Convert ** to match any number of directories
    if '**' in gitignore_pattern:
        gitignore_pattern = gitignore_pattern.replace('**/', '**/').replace('/**', '/**')
    
    return gitignore_pattern


def generate_file_tree(root_dir, exclude_patterns=None, include_patterns=None, respect_gitignore=True):
    """Generate a file tree structure for a given directory.
    
    Args:
        root_dir: The root directory to scan
        exclude_patterns: List of glob patterns to exclude
        include_patterns: List of glob patterns to include
        respect_gitignore: Whether to respect .gitignore files
        
    Returns:
        Tuple of (file_tree, files_content) where file_tree is a list of 
        formatted strings and files_content is a list of dictionaries with 
        path and content keys
    """
    if exclude_patterns is None:
        exclude_patterns = [".git", "__pycache__", "*.pyc", "node_modules", ".DS_Store"]
    else:
        # Make a copy to avoid modifying the original list
        exclude_patterns = exclude_patterns.copy()
    
    # Add gitignore patterns if requested
    if respect_gitignore:
        # Add global gitignore patterns
        global_patterns = get_global_gitignore_patterns()
        for pattern in global_patterns:
            glob_pattern = gitignore_to_pattern(pattern)
            if glob_pattern and glob_pattern not in exclude_patterns:
                exclude_patterns.append(glob_pattern)
        
        # Add local gitignore patterns
        local_gitignore_path = os.path.join(root_dir, '.gitignore')
        local_patterns = read_gitignore_file(local_gitignore_path)
        for pattern in local_patterns:
            glob_pattern = gitignore_to_pattern(pattern)
            if glob_pattern and glob_pattern not in exclude_patterns:
                exclude_patterns.append(glob_pattern)
    
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
            # Check if full path matches any exclude pattern
            file_path = os.path.join(rel_path, filename) if rel_path else filename
            if any(fnmatch.fnmatch(file_path, pattern) for pattern in exclude_patterns) or \
               any(fnmatch.fnmatch(filename, pattern) for pattern in exclude_patterns):
                continue
                
            # Apply include patterns if specified
            if include_patterns and not any(fnmatch.fnmatch(filename, pattern) for pattern in include_patterns) and \
               not any(fnmatch.fnmatch(file_path, pattern) for pattern in include_patterns):
                continue
                
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


def generate_prompt(repo_path, exclude_patterns=None, include_patterns=None, output_file=None, respect_gitignore=True):
    """Generate a prompt for AI models containing the file tree and file contents.
    
    Args:
        repo_path: Path to the Git repository
        exclude_patterns: List of glob patterns to exclude
        include_patterns: List of glob patterns to include
        output_file: Optional file path to write the prompt to
        respect_gitignore: Whether to respect .gitignore files
        
    Returns:
        The generated prompt as a string
    """
    repo_path = os.path.abspath(repo_path)
    repo_name = os.path.basename(repo_path)
    
    file_tree, files_content = generate_file_tree(repo_path, exclude_patterns, include_patterns, respect_gitignore)
    
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
```

### codebase_prompt_gen/cli/__init__.py

```
"""Command-line interface for Codebase AI Prompt Generator.""" 
```

### codebase_prompt_gen/cli/main.py

```
"""Command-line interface for Codebase AI Prompt Generator."""

import argparse
import sys
from codebase_prompt_gen.core import generate_prompt


def main():
    """Main entry point for the CLI."""
    parser = argparse.ArgumentParser(description='Generate AI prompts from Git repositories')
    parser.add_argument('repo_path', type=str, nargs='?', default='.', 
                        help='Path to the Git repository (default: current directory)')
    parser.add_argument('--exclude', type=str, nargs='+', 
                        help='Patterns of files/directories to exclude (e.g., *.log)')
    parser.add_argument('--include', type=str, nargs='+', 
                        help='Patterns of files to include (e.g., *.py)')
    parser.add_argument('--output', type=str, 
                        help='Output file to write the prompt to')
    parser.add_argument('--no-gitignore', action='store_true',
                        help='Ignore .gitignore files (both local and global)')
    parser.add_argument('--version', action='store_true',
                        help='Show version information and exit')
    
    args = parser.parse_args()
    
    if args.version:
        from codebase_prompt_gen import __version__
        print(f"Codebase AI Prompt Generator v{__version__}")
        return 0
    
    try:
        prompt = generate_prompt(
            args.repo_path, 
            args.exclude, 
            args.include, 
            args.output,
            respect_gitignore=not args.no_gitignore
        )
        if not args.output:
            print(prompt)
        return 0
    except Exception as e:
        print(f"Error: {str(e)}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main()) 
```

### codebase_ai_prompt_generator.egg-info/PKG-INFO

```
Metadata-Version: 2.1
Name: codebase-ai-prompt-generator
Version: 0.1.0
Summary: Generate AI prompts from Git repositories with file tree structures and content
Author-email: Your Name <your.email@example.com>
License: MIT
Project-URL: Homepage, https://github.com/yourusername/codebase-ai-prompt-generator
Project-URL: Bug Tracker, https://github.com/yourusername/codebase-ai-prompt-generator/issues
Keywords: ai,prompt,git,code,repository
Classifier: Development Status :: 3 - Alpha
Classifier: Intended Audience :: Developers
Classifier: Topic :: Software Development :: Libraries :: Python Modules
Classifier: License :: OSI Approved :: MIT License
Classifier: Programming Language :: Python :: 3
Classifier: Programming Language :: Python :: 3.8
Classifier: Programming Language :: Python :: 3.9
Classifier: Programming Language :: Python :: 3.10
Classifier: Programming Language :: Python :: 3.11
Requires-Python: >=3.8
Description-Content-Type: text/markdown
License-File: LICENSE

# Codebase AI Prompt Generator

A tool to scan a Git repository and generate a comprehensive prompt for AI models, including file tree structure, file paths, and content.

## Features

- Creates a hierarchical file tree representation of a repository
- Includes file contents formatted for AI prompts
- Customizable file inclusion/exclusion via patterns
- Option to save output to a file or print to console
- Automatically respects local and global .gitignore files
- Installable CLI tool

## Installation

```bash
# From PyPI (recommended)
pip install codebase-ai-prompt-generator

# From source
git clone https://github.com/yourusername/codebase-ai-prompt-generator.git
cd codebase-ai-prompt-generator
pip install -e .
```

## Usage

After installation, you can use the `codebase-prompt` command directly from your terminal:

```bash
# Basic usage (scans current directory)
codebase-prompt

# Scan a specific repository
codebase-prompt /path/to/repository

# Exclude specific file patterns
codebase-prompt --exclude "*.log" "*.tmp" ".env"

# Include only specific file patterns
codebase-prompt --include "*.py" "*.js" "*.html"

# Write output to a file
codebase-prompt --output prompt.md

# Show version information
codebase-prompt --version

# Ignore .gitignore files (both local and global)
codebase-prompt --no-gitignore

# Combine options
codebase-prompt /path/to/repository --exclude "node_modules" "*.pyc" --include "*.py" "*.js" --output prompt.md
```

## .gitignore Support

By default, the tool respects both:
- The repository's local `.gitignore` file
- The user's global gitignore file (found via `git config --global --get core.excludesfile`)

Files matching any pattern in these files will be excluded from the output. To disable this feature, use the `--no-gitignore` flag.

## Example Output

The generated prompt will have the following structure:

```
# Repository: repo-name

## File Tree Structure

📁 src/
📄 src/main.py
📄 src/utils.py
📁 tests/
📄 tests/test_main.py
📄 README.md

## File Contents

### src/main.py

```python
def main():
    print("Hello World")
```

### src/utils.py

```python
def helper():
    return "Helper function"
```

...
```

## Use Cases

- Generate prompts for AI code assistants to understand your entire codebase
- Create documentation snapshots of your repository
- Share codebase context with AI models for better assistance
- Provide comprehensive context to LLMs for code-related questions

## Development

To set up the development environment:

```bash
# Clone the repository
git clone https://github.com/yourusername/codebase-ai-prompt-generator.git
cd codebase-ai-prompt-generator

# Create and activate a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install in development mode
pip install -e .
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

```

### codebase_ai_prompt_generator.egg-info/SOURCES.txt

```
LICENSE
README.md
pyproject.toml
codebase_ai_prompt_generator.egg-info/PKG-INFO
codebase_ai_prompt_generator.egg-info/SOURCES.txt
codebase_ai_prompt_generator.egg-info/dependency_links.txt
codebase_ai_prompt_generator.egg-info/entry_points.txt
codebase_ai_prompt_generator.egg-info/top_level.txt
codebase_prompt_gen/__init__.py
codebase_prompt_gen/core.py
codebase_prompt_gen/cli/__init__.py
codebase_prompt_gen/cli/main.py
```

### codebase_ai_prompt_generator.egg-info/dependency_links.txt

```


```

### codebase_ai_prompt_generator.egg-info/entry_points.txt

```
[console_scripts]
codebase-prompt = codebase_prompt_gen.cli.main:main

```

### codebase_ai_prompt_generator.egg-info/top_level.txt

```
codebase_prompt_gen

```

