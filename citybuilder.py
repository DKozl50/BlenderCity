import bpy 
import bpy.ops as o
import numpy as np
from mathutils import Vector

#variables

roadlen1 = 30 
elevationcoef = 10
arr = np.ones((roadlen1,roadlen1))
houseconstant = -5

roadwidth1 = 2

MINroadlen2 = 9
MAXroadlen2 = 15
roadwidth2 = 1
roadgap2 = 3 
roadsection2 = 5
axialroads2 = 10

MINstartlen3 = 0
MAXstartlen3 = 6
MINendlen3 = 8
MAXendlen3 = 15
roadwidth3 = 1
roadgap3 = 3
roadsection3 = 5
axialroads3 = 8

roofchance = 3/10
divcoef = 1.5

radius = 6
MINdim = 1
MAXdim = 2.5
MINheight = 3  #*2
MAXheight = 10 #*2
MINvert = 3
MAXvert = 7
amount = 9 



#clears everything
def objclear():
  for obj in bpy.context.scene.objects:
    if obj.type == 'MESH':
      obj.select = True
    else:
      obj.select = False
      o.object.delete()

#random shortcut
def rand():
  return (np.random.rand()-0.5)*2
def randsq():
  return (np.random.rand()**2-0.5)*2

#cube shortcut
def cube(loc, resize):
  o.mesh.primitive_cube_add(location = loc)
  o.transform.resize(value = resize)
  
#prism shortcut
def prism(loc, resize, vert, angle, angle2):
  o.mesh.primitive_cylinder_add(vertices = vert, location = loc)
  ob = bpy.context.object
  ob.rotation_euler=(0, 0, angle)
  o.transform.resize(value = resize)
  ob.rotation_euler=(0, 0, angle2)


objclear()

#base
bpy.ops.mesh.primitive_torus_add(location = (0,0,0), major_radius=16, minor_radius = 0.5, major_segments = 256)
bpy.ops.mesh.primitive_cone_add(radius1 = 17, radius2 = 16.5, location = (0,0, -1), vertices = 1000)

#random small houses
for x in range(roadlen1):
  for y in range(roadlen1):
    arr[x,y] = (x-roadlen1/2)**2 + (y-roadlen1/2)**2
    arr[x,y]/=2*(roadlen1/2)**2/elevationcoef

arrmax = arr.max()
for x in range(roadlen1):
  for y in range(roadlen1):
    arr[x,y] = arrmax - arr[x,y]
    arr[x,y] += houseconstant


#roads

#road1
for i in range(roadlen1):
  for w in range(roadwidth1):
    arr[int(roadlen1/2-roadwidth1/2+w), i] = -1
    arr[i, int(roadlen1/2-roadwidth1/2+w)] = -1

#road2
for i in range(axialroads2):
  end = np.random.randint(MINroadlen2, MAXroadlen2)
  if(np.random.rand()-0.5<0):
    end = -end
  end+=roadlen1/2
  perpcoord = roadgap2*np.random.randint(-roadsection2,roadsection2)+roadlen1/2

  tmp = [int(roadlen1/2), int(end)]
  tmp.sort()

  for y in range(tmp[0],tmp[1]):
    arr[int(perpcoord), y] = -1


for i in range(axialroads2):
  end = np.random.randint(MINroadlen2, MAXroadlen2)
  if(np.random.rand()-0.5<0):
    end = -end
  end+=roadlen1/2
  perpcoord = roadgap2*np.random.randint(-roadsection2,roadsection2)+roadlen1/2

  tmp = [int(roadlen1/2), int(end)]
  tmp.sort()

  for x in range(tmp[0],tmp[1]):
    arr[x, int(perpcoord)] = -1

#road3
for i in range(axialroads3):
  start = np.random.randint(MINstartlen3, MAXstartlen3)
  end = np.random.randint(MINendlen3, MAXendlen3)
  if(np.random.rand()-0.5<0):
    start = -start
    end = -end
  start+=roadlen1/2
  end+=roadlen1/2
  perpcoord = roadgap3*np.random.randint(-roadsection3,roadsection3)+roadlen1/2
  
  tmp = [int(start), int(end)]
  tmp.sort()
  
  for x in range(tmp[0], tmp[1]):
    arr[x, int(perpcoord)] = -1


for i in range(axialroads3):
  start = np.random.randint(MINstartlen3, MAXstartlen3)
  end = np.random.randint(MINendlen3, MAXendlen3)
  if(np.random.rand()-0.5<0):
    start = -start
    end = -end
  start+=roadlen1/2
  end+=roadlen1/2
  perpcoord = roadgap3*np.random.randint(-roadsection3,roadsection3)+roadlen1/2
  
  tmp = [int(start), int(end)]
  tmp.sort()
  
  for y in range(tmp[0], tmp[1]):
    arr[int(perpcoord), y] = -1

#citylow
for i in range (roadlen1):
  for n in range (roadlen1):
    if (arr[i,n]!=-1) & ((i-roadlen1/2)**2+(n-roadlen1/2)**2+1<(roadlen1/2)**2):
        h = arr[i,n]+np.random.rand()*divcoef
        cube((i-roadlen1/2, n-roadlen1/2, h/2), (1/2, 1/2, h/2))
        if np.random.rand()<=roofchance:
            o.mesh.primitive_cylinder_add(vertices=3, location = (i-roadlen1/2,n-roadlen1/2,h))
            ob = bpy.context.object
            ob.rotation_euler=(np.pi/2, 0, 0)
            ob.location+=Vector((0,0,1/4 ))
            o.transform.resize(value=(1/(3**0.5), 1/2, 1/2))
            ob.rotation_euler =(np.pi/2, 0, np.random.randint(2)*np.pi/2)

#random skyscrapers
meandim = (MINdim+MAXdim)/2
deltadim = meandim-MINdim
meanheight = (MINheight+MAXheight)/2
deltaheight = meanheight-MINheight

built = 0
while built<=amount:
  x = rand()*(radius-1)
  y = rand()*(radius-1)
  if(x**2+y**2<=radius**2):
    h = randsq()*deltaheight+meanheight
    prism((x,y,h), (rand()*deltadim+meandim, rand()*deltadim+meandim, h), np.random.randint(MINvert, MAXvert+1), rand()*np.pi, rand()*np.pi)
    built+=1

prism((0,0, MAXheight+0.5),(2,2,MAXheight+0.5), 3, 3, 1) 

#for i in range(amount):
#  y = rand()*radius
#  x = rand()*((radius**2-y**2)**0.5)
#  h = rand()*deltaheight+meanheight
  
#  prism((x,y,h), (rand()*deltadim+meandim, rand()*deltadim+meandim, h), np.random.randint(MINvert, MAXvert+1), rand()*np.pi, rand()*np.pi)
  
  
  

bpy.ops.object.select_all(action='TOGGLE')
bpy.ops.text.save()
