import bpy
from bpy.props import *
from bpy.types import Node, NodeSocket
from arm.logicnode.arm_nodes import *

class RotateObjectNode(Node, ArmLogicTreeNode):
    '''Rotate object node'''
    bl_idname = 'LNRotateObjectNode'
    bl_label = 'Rotate Object'
    bl_icon = 'NONE'

    def init(self, context):
        self.inputs.new('ArmNodeSocketAction', 'In')
        self.inputs.new('ArmNodeSocketObject', 'Object')
        self.inputs.new('NodeSocketVector', 'Euler Angles')
        self.inputs.new('NodeSocketFloat', 'Angle / W')
        self.outputs.new('ArmNodeSocketAction', 'Out')
        
    def on_property_update(self, context):
        """ called by the EnumProperty, used to update the node socket labels"""
        if self.property0 == "Quaternion":
            self.inputs[2].name = "Quaternion XYZ"
            self.inputs[3].name = "Quaternion W"
        elif self.property0 == "Euler Angles":
            self.inputs[2].name = "Euler Angles"
            self.inputs[3].name = "[unused for Euler input]"
        elif self.property0.startswith("Angle Axies"):
            self.inputs[2].name = "Axis"
            self.inputs[3].name = "Angle"
        else:
            raise ValueError('No nodesocket labels for current input mode: check self-consistancy of action_set_rotation.py')
        
    def draw_buttons(self, context, layout):
        # this block is here to ensure backwards compatibility and warn the user.
        # delete it (only keep the "else" part) when the 'old version' of the node will be considered removed.
        # (note: please also update the corresponding haxe file when doing so)
        if len(self.inputs) < 4:
            row = layout.row(align=True)
            row.label(text="Node has been updated with armory 2020.09. Please consider deleting and recreating it.")
        else:
            layout.prop(self, 'property0')
            
    property0: EnumProperty(
        items = [('Euler Angles', 'Euler Angles', 'Euler Angles'),
                 ('Angle Axies (Radians)', 'Angle Axies (Radians)', 'Angle Axies (Radians)'),
                 ('Angle Axies (Degrees)', 'Angle Axies (Degrees)', 'Angle Axies (Degrees)'),
                 ('Quaternion', 'Quaternion', 'Quaternion')],
        name='', default='Euler Angles',
        update = on_property_update)

add_node(RotateObjectNode, category='Action')
