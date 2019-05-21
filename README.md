# BlenderCity
A small random generator of city models in Bledner via bpy

The code generates a city (lots of resized cubes) such that small buildings "grow" towards the center and the skyscrapers just spawn randomly in the middle

Here are the variables:
  - roadlen1 - the length of two main roads. It is also a diameter of a circle
  - elevationcoef - growth coefficient of small buildings
  - houseconstant - constant to lower/lif all the houses at once
  
  - roadwidth1 - width of the main roads. recommended to use even numbers
  
  Secondary always have one end in a main road
  - MINroadlen2 
  - MAXroadlen2 - minimal and maximal length of secondary roads 
  - roadwidth2 - width of secondary roads
  - roadgap2 - minimum distance between two collinear secondary roads
  - roadsection2 - multiplied by roadgap2 is maximum distance from center
  - axialroads2 - amount of roads on an axis (roads can overlap, so it is a maximal possible amount)
  
  Tertiary roads always start and end in one halfplane 
  - MINstartlen3
  - MAXstartlen3 - minimum and maximum distance from closest end to the main road
  - MINendlen3
  - MAXendlen3 - minimum and maximum distance from furthest end to the main road
  - roadwidth3 
  - roadgap3
  - roadsection3 
  - axialroads3 - same as for secondary roads
  
  - roofchance - chance of getting triangle roof on top of house 
  - divcoef - randomness coefficient of small building
  
  - radius - radius of circle where skyscrapers can spawn
  - MINdim 
  - MAXdim - minimum and maximum dimensions of skyscrapers
  - MINheight
  - MAXheight - minimum and maximum heights of skyscrapers. multiplied by two in the code (ie MAXheight=10 will spawn building with height up to 20)
  - MINvert
  - MAXvert - minimum and maximum amount of vertices of skyscrapers
  - amount - amont of skyscrapers to be spawned (note that two shyskrapers can spawn in one place and look like one) 




