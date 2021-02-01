from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController





class Voxel(Button):
	def __init__(self, position = (0,0,0), texture = 'white_cube'):
		super().__init__(
			parent = scene,
			position = position,
			model = 'cube',
			origin_y = 0.5,
			texture = texture,
			color = color.color(0,0,random.uniform(0.9,1)),
			scale = 1,
			highlight_color = color.lime)

	def input(self,key):
		if self.hovered:
			if key =='left mouse down':
				voxel = Voxel(position = self.position + mouse.normal)	
			if key == 'right mouse down':
				destroy(self)
		

app = Ursina()

sky_texture = load_texture('assets/skybox.png')

window.fps_counter.enabled = False
window.exit_button.visible = False

for z in range(30):
	for x in range(30):
		voxel = Voxel(position = (x,0,z))

player = FirstPersonController()
sky = Sky()
app.run()