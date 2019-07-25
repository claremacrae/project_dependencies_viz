<a id="top"></a>

# project_dependencies_viz

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->


- [Introduction](#introduction)
  - [Feedback welcome](#feedback-welcome)
- [Why SVG output?](#why-svg-output)
- [Generating your own interactive dependency images](#generating-your-own-interactive-dependency-images)
  - [The 'sample' project](#the-sample-project)
  - [Viewing the dependencies](#viewing-the-dependencies)
  - [Creating the .svg files from .dot files](#creating-the-svg-files-from-dot-files)
  - [Future exercises](#future-exercises)
    - [Generate .dot files to represent dependencies of your projects](#generate-dot-files-to-represent-dependencies-of-your-projects)
    - [What depends on a particular library?](#what-depends-on-a-particular-library)
    - [Showing more information](#showing-more-information)
- [Alternative approaches - if you use CMake](#alternative-approaches---if-you-use-cmake)
  - [Details of the CMake mechanism](#details-of-the-cmake-mechanism)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

## Introduction

This is a quick demo of how to use [graphviz](https://www.graphviz.org/) to make interactive SVG files to show dependencies between projects, to help answer a question asked on the [#include <C++> Discord server](https://www.includecpp.org/).

The graphviz .dot files here show a technique of adding [URLs](https://www.graphviz.org/doc/info/attrs.html#d:URL) to nodes in a graph. When the output is .svg, the nodes are then hyper-linked, and provided easy navigation.

A second section shows how you can achieve a similar effect more easily, if your builds are driven by CMake.

### Feedback welcome

I'd love to have feedback on this - feel free to use the Issues system in this repo, or [Twitter](https://twitter.com/ClareMacraeUK).
 
Are there any better mechanisms that already exist to show project dependencies in large bodies of C++ code?

Has anyone already done the work of adding URLs to make the CMake output `--graphviz` output files interactive?

## Why SVG output?

Aside from the hyperlinking benefits I describe below, I found these benefits of using the [SVG format](https://en.wikipedia.org/wiki/Scalable_Vector_Graphics) to visualise complex dependencies:

* The files are text, and load very quickly into browsers like Chrome and Vivaldi - much quicker than corresponding bitmap images
* Because the SVG files are text, you can use the Browser's Search feature (`Ctrl + F`) to easily search for text in the image
* The images scale very nicely when zooming in and out of large files
* Some browsers allow you to hold down the shift key and then drag with the mouse to pan in all directions around the image 

## Generating your own interactive dependency images

### The 'sample' project

The images here represent the dependencies in a fictional, simple system, consisting of:
 
* two libraries ('lib1' and 'lib2') - drawn as ovals 
* two programs ('exe1' and 'exe2') - drawn as rectangles

![](all-targets.svg)

* the arrows show project dependencies 
* 'all-targets' is a special link that loads the full dependency image - which is what is shown above. This will make more sense after reading the next section.

### Viewing the dependencies

1. Download [this repo](https://github.com/claremacrae/project_dependencies_viz)
2. Load the file 'all-targets.svg into a modern browser - Chrome, for example
3. Click on  'exe1'
4. The file 'exe1-uses.svg' will load - showing only things that 'exe1' uses:

![](exe1-uses.svg)

You can click on 'all-targets' to get back to the initial view.

### Creating the .svg files from .dot files

Example command to create the file `all-targets.svg` from `all-targets.dot`

```bash
dot -Tsvg all-targets.dot -o all-targets.svg
```
The Python 3 script [dot_convert.py](dot_convert.py) does this conversion for all .dot files in the current directory. It requires graphvis'z `dot` command to be in the path.

### Future exercises

#### Generate .dot files to represent dependencies of your projects

These .dot files were hand-edited, for demo purposes. The intention here is to show how information in one's own build system could be presented in an easily navigable way.

#### What depends on a particular library? 

At a previous job, I wrote scripts to generate files like this from information in the project build system. It had one really useful extra feature, which is that you could also see what targets depended on a given library.

This was really helpful in understanding what code would have to be rebuilt, if a particular library was modified.

It also made the images much easier to navigate, as you could easily drill down to lower level libraries, and then navigate back up again.

In my first implementation, clicking repeatedly on a library node alternated between:

1. showing what the library used
2. showing what used the library

This was a bit non-obvious to users, so I then switched to adding extra nodes near the 'all-targets' node that hyper-linked to the two related images. 

#### Showing more information

I also added colour-coding to the images, for different types of libraries, with categories such as:

* targets that depended on Qt
* 3rd-party libraries
* targets that depended on libraries that they should not have done

I then added a colour-key link to each image. 

## Alternative approaches - if you use CMake

If you use CMake to drive your builds, and you just want to see a single image of all your project dependencies, you can use CMake's own option `--graphviz`.

Taking [ApprovalTests.cpp](https://github.com/claremacrae/ApprovalTests.cpp/) as an example:

```bash
cd ApprovalTests.cpp
mkdir cmake-build-dot
cd    cmake-build-dot
cmake --graphviz=test.dot ..
dot -Tsvg test.dot -o test.svg
```

The generated .dot file can be seen here

And the generated .svg file looks like this:

![](cmake-generated-files/test.svg)

### Details of the CMake mechanism

There is an [overview of the CMake graphviz output mechanism](https://gitlab.kitware.com/cmake/community/wikis/doc/cmake/Graphviz) on the Cmake wiki.

And there is much [more detail in the the CMake documentation](https://cmake.org/cmake/help/latest/module/CMakeGraphVizOptions.html), showing how you can control what types of targets are included in the output, and how to control the node and edge styles.

This documentation page describes the many separate files that CMake writes out.

It says:

> When CMake is run with the --graphviz=foo.dot option, it will produce:
> * a foo.dot file showing all dependencies in the project
> * a foo.dot.<target> file for each target, file showing on which other targets the respective target depends
> * a foo.dot.<target>.dependers file, showing which other targets depend on the respective target

This means that if you use CMake, and if you spend time post-processing the CMake graphviz output to add URLs, you could probable answer my "What depends on a particular library?" question above, for your projects, really quite quickly.
