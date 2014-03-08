import maya.OpenMayaMPx as omp
import sys

from unfolder.select_facetree.select_facetree_context import SelectFacetreeContext


class FacetreeSelectionCommand(omp.MPxContextCommand):
    def __init__(self):
        omp.MPxContextCommand.__init__(self)

    def makeObj(self):
        return omp.asMPxPtr(SelectFacetreeContext())


# Creator
def createCommand():
    return omp.asMPxPtr(FacetreeSelectionCommand())

kPluginCmdName = "selectFacetree"


# Initialize the script plug-in
def initializePlugin(mobject):
    print('Loading facetree selection plugin.')

    mplugin = omp.MFnPlugin(mobject)
    try:
        mplugin.registerContextCommand(kPluginCmdName, createCommand)
    except:
        sys.stderr.write("Failed to register command: %s\n" % kPluginCmdName)
        raise


# Uninitialize the script plug-in
def uninitializePlugin(mobject):
    mplugin = omp.MFnPlugin(mobject)
    try:
        mplugin.deregisterContextCommand(kPluginCmdName)
    except:
        sys.stderr.write("Failed to unregister command: %s\n" % kPluginCmdName)