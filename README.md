Paper Model Tools
=================

The Paper Model Tools is a set of tools to create 2D paper model sheets from 3D
mesh geometry. They are currently implemented as a plugin for Autodesk Maya.

![showcase](https://raw.github.com/mjleehh/paper-model-tools/master/doc/images/showcase.png)

Two objects and paper models of these objects that were created using the Paper
Model Tools.

Installation
------------

Currently there are no packaged release versions of the plugin available for
download. To install the tools download the contents of this repo from

https://github.com/mjleehh/paper-model-tools

and unpack it to a folder of your choice.

In maya go to `Window -> Settings/Preferences -> Plug-in Manager`. In the
Plug-in manager click the `Browse` button and from the Paper Model Tools folder
pick

`paper_model_tools_plugin.py`

Now at the bottom of the list you should see

![loaded plugin in plug-in browser](https://raw.github.com/mjleehh/paper-model-tools/master/doc/images/plugin_loaded.png)

If you wish to load the plugin on startup check the `Auto load` box.

Create Paper Model Tool
-----------------------

This interactive tool lets the user create a paper model from a mesh geometry
controlling the layout of that paper model.

### Single Strip Paper Model ###

We want to convert the following geometry to a paper model:

![to be converted](https://raw.github.com/mjleehh/paper-model-tools/master/doc/images/create-paper-model-tool/initial.png)

* Select the `Create Paper Model Tool` and click on the object:

![selected](https://raw.github.com/mjleehh/paper-model-tools/master/doc/images/create-paper-model-tool/selected.png)

* Now the object is highlighted and we can select the first face:

![step 1](https://raw.github.com/mjleehh/paper-model-tools/master/doc/images/create-paper-model-tool/one-strip/step_01.png)

* The first section of the paper model has been created from the selected face.
Those faces directly connected to the face are highlighted. These faces can be
selected next. Select the face *above* the current one:

![step 2](https://raw.github.com/mjleehh/paper-model-tools/master/doc/images/create-paper-model-tool/one-strip/step_02.png)

* The face has been added to the paper model and the next selection options are
highlighted. Now continue selecting faces in the following order:

![selection order](https://raw.github.com/mjleehh/paper-model-tools/master/doc/images/create-paper-model-tool/one-strip/selection_order.png)

* Finally you end up with a paper model of the whole geometry:

![result](https://raw.github.com/mjleehh/paper-model-tools/master/doc/images/create-paper-model-tool/one-strip/done.png)

### Paper Model with multiple Strips ###

The paper model in the previous does represent the original geometry, but for
tree reasons creating a paper model as a single strip doesn't suffice:

1. The resulting model may be tedious to cut or waste large amounts of paper.
2. It may be that the single strip version of the model has overlapping surfaces
whereas other solutions to the problem do not. Thus you do not want to be
limited to single strip paper models.
3. Not all geometry may can be represented as a single strip model.

Below we have the example of the single strip paper model from the previous
section (left) and a paper model consisting of multiple strips that we want to
create in this section.

![comparison](https://raw.github.com/mjleehh/paper-model-tools/master/doc/images/create-paper-model-tool/multiple-strips/comparison.png)

Create Paper Model Command
--------------------------

This tool given a selected mesh object or a set of mesh faces generates a paper
model for that selection.

Copyright and License
---------------------

Copyright for Paper Model Tools *Michael Jonathan Lee*. Paper Model Tools is
released under the [GPL V3](http://choosealicense.com/licenses/gpl-v3/).