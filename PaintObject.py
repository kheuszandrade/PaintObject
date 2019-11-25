from bge import *
from mathutils import Vector
import random

class PaintObject(types.KX_PythonComponent):
    args = {
        "Instance Object": "Cube",
        "Random Instance": False,
        "Destroy This Object": False
    }
    
    def start(self, args):
        self.scene = logic.getCurrentScene()
        self.instance_object = args["Instance Object"]
        self.random_instance = args["Random Instance"]
        self.destroy_this_object = args["Destroy This Object"]
        
        self.place_color = Vector()
        self.place_color.x = 0
        self.place_color.y = 0
        self.place_color.z = 0
        
        self.mesh = self.object.meshes[0]

        for i in range(0, self.mesh.getVertexArrayLength(0)):
            vertex = self.mesh.getVertex(0, i)
            color = Vector()
            color[0], color[1], color[2] = vertex.color[0], vertex.color[1], vertex.color[2]
            
            if color == self.place_color:
                if self.random_instance == True:
                    place = random.randint(0,1)
                    if place == 1:
                        self.PlaceObject(vertex)
                else:
                    self.PlaceObject(vertex)
                    
        if self.destroy_this_object == True:
            self.object.endObject()
                
    def PlaceObject(self, vertex):
        position = Vector()
        position[0] = (vertex.x * self.object.localScale.x) + self.object.worldPosition.x
        position[1] = (vertex.y * self.object.localScale.y) + self.object.worldPosition.y
        position[2] = (vertex.z * self.object.localScale.z) + self.object.worldPosition.z
    
        obj = self.scene.addObject(self.instance_object)
        obj.worldPosition = position
        
    def update(self):
        pass
