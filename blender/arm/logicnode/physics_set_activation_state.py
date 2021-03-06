import bpy
from bpy.props import *
from bpy.types import Node, NodeSocket
from arm.logicnode.arm_nodes import *

class SetActivationStateNode(Node, ArmLogicTreeNode):
    '''Set Activation State Node'''
    bl_idname = 'LNSetActivationStateNode'
    bl_label = 'Set Activation State'
    bl_icon = 'NONE'
    property0: EnumProperty(
        items = [('Inactive', 'Inactive', 'Inactive'),
                 ('Active', 'Active', 'Active'),
                 ('Always Active', 'Always Active', 'Always Active'),
                 ('Always Inactive', 'Always Inactive', 'Always Inactive'),
                 ],
        name='', default='Inactive')

    def init(self, context):
        self.inputs.new('ArmNodeSocketAction', 'In')
        self.inputs.new('ArmNodeSocketObject', 'Object')
        self.outputs.new('ArmNodeSocketAction', 'Out')

    def draw_buttons(self, context, layout):
        layout.prop(self, 'property0')

add_node(SetActivationStateNode, category='Physics')
