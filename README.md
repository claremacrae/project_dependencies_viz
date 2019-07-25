# project_dependencies_viz

This is a quick demo of how to use [graphviz](https://www.graphviz.org/) to make interactive svg files to show dependencies between projects, to help answer a question asked on the [#include <C++> Discord server](https://www.includecpp.org/).

The graphviz .dot files here show a technique of adding [URLs](https://www.graphviz.org/doc/info/attrs.html#d:URL) to nodes in a graph. When the output is .svg, the nodes are then hyper-linked, and provided easy navigation.

## The 'sample' project

The images here represent the dependencies in a fictional, simple system, consisting of two libraries (lib1 and lib2) and two programs (exe1 and exe2)

![](all-targets.svg)

'all-targets' is a special link that loads the full dependency image - which is what is shown above.

## Viewing the dependencies

1. Download the repo
2. Load the file 'all-targets.svg into a modern browser - Chrome, for example
3. Click on  'exe1'
4. The file 'exe1-uses.svg' will load - showing only things that 'exe1' uses:

![](exe1-uses.svg)

You can click on 'all-targets' to get back to the initial view.

## Creating the .svg files from .dot files

Example command to create the file `all-targets.svg` from `all-targets.dot`

```bash
dot -Tsvg all-targets.dot -o all-targets.svg
```
The Python 3 script [dot_convert.py](dot_convert.py) does this conversion for all .dot files in the current directory. It requires graphvis'z `dot` command to be in the path.

## Future exercises

### What depends on a particular library? 

At a previous job, I wrote scripts to generate files like this from information in the project build system. It had one really useful extra feature, which is that you could also see what targets depended on a given library.

This was really helpful in understanding what code would have to be rebuilt, if a particular library was modified.

It also made the images much easier to navigate, as you could easily drill down to lower level libraries, and then navigate back up again.

In my first implementation, clicking repeatedly on a library node alternated between:

1. showing what the library used
2. showing what used the library

This was a bit non-obvious to users, so I then switched to adding extra nodes near the 'all-targets' node that hyper-linked to the two related images. 


### Showing more information

I also added colour-coding to the images, for different types of libraries, with categories such as:

* targets that depended on Qt
* 3rd-party libraries
* targets that depended on libraries that they should not have done

I then added a colour-key link to each image. 