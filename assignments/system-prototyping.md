`---
title: System Manufacturing
subtitle: Team Assignment
week: "13"
points: 200
type: assignment
module: manufacturing
---

# System Manufacturing

## Introduction

The purpose of this assignment is to plan for the manufacturing of the full system, test the output, and produce a prototype

<!--hide-->

## Steps

1. Create a quick paper mockup of your final prototype design(You may use a prior prototype if it still applies, but you may destroy it.).  Once you have arrived at your desired architecture, proceed to unfold the prototype in a way that makes sense from the perspective of optimizing material usage, staying within any boundary limitations (size of a piece of posterboard, size of the cutter you will be using).
1. Design the geometry of your robot in .dxf format

      Alternative 1: Use the solidworks tutorial to generate design geometry (suggested).

      a. Convert the flattened pattern to _dimensioned_ a Solidworks sketch.  Include any mounting holes for motors, springs, or connectors.
      a. Use the Solidworks tutorial to create a hinged assembly of all parts of the design
      a. Take a screenshot of the robot in its folded & assembled state
      a. Flatten the assembly back to its original flattened state
      a. Create a drawing from the assembly and use the solidworks export macro to export a yaml file (generic).
      a. Use the solidworks support functionality in foldable robotics to convert to a dxf

      Alternative 2: Directly draw a .dxf using your favorite tool (not suggested as each tool can implement different versions of .dxf standard)
      
      a. Make two sets of geometry on two distinct layers: a body layer and a joint layer.
      a. The body layer should be a closed LWPoly type of the outline of your geometry.  Include any holes as separate lwpolylines.  Name the layer "body"
      a. The joints layer should be an consist of one LWPoly or line type for each joint, each consisting of a single, two-vertex line segment.  Name the layer "joints"
      
1. Using a single-layer design approach, compute the design of your device in one layer, plotting each step along the way.  This should include:
    1. a one-layer hinge design that fits your team's need (with justification for material used, rotational needs, manufacturing method used, etc)
    1. mapping the hinge design to each joint in your joints layer of the dxf
    1. subtracting the one layer hinge design from your body layer
    1. holes computed for any vertices
1. Using a **5-layer** design approach, compute the same design of your device in **five** layers, plotting each step along the way.  This should include:
    1. a five-layer hinge design that fits your team's need (with justification for material used, rotational needs, manufacturing method used, etc)
    1. mapping the hinge design to each joint in your joints layer of the dxf
    1. subtracting the 5-layer hinge design from the body laminate
    1. holes computed for any vertices
1. Using the full design pipeline found on the website and discussed in class, compute the manufacturing geometry for a five-layer laminate, plotting each step along the way.  This should include:
    1. Web design
    1. Support design
    1. Non-removable scrap
    1. Connection check of all parts that result from the second-pass cut.
    1. Similarity check between design and removed final part.

1. Export your final cut files to .dxf or .pdf, depending on your need.  You should export one file per layer as well as one final cut file(if using a laminate process).
      
## Submission

Please include:

1. The picture of your paper mockup in its 
    a. folded and 
    a. flattened state
1. A Solidworks screenshot of your robot in its 
    a. folded and 
    a. flattened state
1. The dxf of your body and joint layers output by solidworks or designed by you.
1. Your jupyter notebook script consisting of the following elements, clearly labeled.
    a. 1-Layer Robot Design
    a. 5-Layer Robot Design
    a. 5-Layer Manufacturing Design
1. Final .dxf files

The report should be submitted as a jupyter notebook.  Supporting files should accompany the jupyter notebook in a .zip file of the entire folder.


<!--unhide-->

## Rubric

| Description | Points |
|:------------|:-------|
| 1a          | 15     |
| 1b          | 15     |
| 2a          | 15     |
| 2b          | 15     |
| 3           | 30     |
| 4a          | 30     |
| 4b          | 30     |
| 4c          | 40     |
| 5           | 10     |
| total       | 200    |
