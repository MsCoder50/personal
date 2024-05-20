import TrackballControls from 'https://cdn.jsdelivr.net/npm/three-trackballcontrols@0.9/index.min.js'
// Create a scene


var scene = new THREE.Scene();
// Load planet models
var planets = [];
var loader = new THREE.GLTFLoader();
// let distanceFactor = 550;
loader.load('models/sun' + '.glb', function (gltf){
    var planet = gltf.scene;
    planets.push(planet);
// planet.scale.set(0.1,0.1,0.1)

scene.add(planet);
planet.position.set( 0,0,0);
})

loader.load('models/mercury' + '.glb', function (gltf) {
    var planet = gltf.scene;
    planets.push(planet);
planet.scale.set(0.05,0.05,0.05)

scene.add(planet);
planet.position.set( 750,0,0);
})
loader.load('models/venus' + '.glb', function (gltf) {
    var planet = gltf.scene;
    planets.push(planet);
planet.scale.set(0.07,0.07,0.07)

scene.add(planet);
planet.position.set( 1100,0,0);
})
loader.load('models/earth' + '.gltf', function (gltf) {
    var planet = gltf.scene;
    planets.push(planet);
planet.scale.set(0.1,0.1,0.1)

scene.add(planet);
planet.position.set( 1300,0,0);
})
loader.load('models/mars' + '.glb', function (gltf) {
    var planet = gltf.scene;
    planets.push(planet);
planet.scale.set(0.08,0.08,0.08)

scene.add(planet);
planet.position.set( 1600,0,0);
})
loader.load('models/jupiter' + '.glb', function (gltf) {
    var planet = gltf.scene;
    planets.push(planet);
planet.scale.set(0.2,0.2,0.2)

scene.add(planet);
planet.position.set( 2200,0,0);
})
loader.load('models/saturn' + '.glb', function (gltf) {
    var planet = gltf.scene;
    planets.push(planet);
planet.scale.set(0.15,0.15,0.15)

scene.add(planet);
planet.position.set( 2800,0,0);
})
loader.load('models/uranus' + '.glb', function (gltf) {
    var planet = gltf.scene;
    planets.push(planet);
planet.scale.set(0.06,0.06,0.06)

scene.add(planet);
planet.position.set( 3200,0,0);
})
loader.load('models/neptune' + '.glb', function (gltf) {
    var planet = gltf.scene;
    planets.push(planet);
planet.scale.set(0.05,0.05,0.05)

scene.add(planet);
planet.position.set( 3700,0,0);
})
function addPlanetLabels() {
    planets.forEach(function (planet) {
        var planetName = planet.name;
        var labelDiv = document.createElement('div');
        labelDiv.className = 'planet-label';
        labelDiv.textContent = planetName;
        var label = new THREE.CSS2DObject(labelDiv);
        label.position.copy(planet.position);
        label.position.y += 450; // Adjust vertical position as needed
        scene.add(label);
    });
}

// Call the function to add planet labels
addPlanetLabels();

var directionalLight = new THREE.DirectionalLight(0xffffff, 1);
directionalLight.position.set(50, 0, 0).normalize(); // Set light position
scene.add(directionalLight);
var directionalLightt = new THREE.DirectionalLight(0xffffff, 1);
directionalLightt.position.set(-50, 0, 0).normalize(); // Set light position
scene.add(directionalLightt);
var directionalLighttt = new THREE.DirectionalLight(0xffffff, 1);
directionalLighttt.position.set(0, -50, 0).normalize(); // Set light position
scene.add(directionalLighttt);
var directionalLightttt = new THREE.DirectionalLight(0xffffff, 1);
directionalLightttt.position.set(0, 50, 0).normalize(); // Set light position
scene.add(directionalLightttt);

// Add light to the scene
var sunLight = new THREE.PointLight(0xffffff, 1); // Creating a point light with white color
sunLight.position.set(0, 0, 0); // Positioning the light at the center of the scene (where the sun is)
scene.add(sunLight);

// Set up camera, renderer, and controls
var renderer = new THREE.WebGLRenderer();
renderer.setSize(window.innerWidth, window.innerHeight);
document.body.appendChild(renderer.domElement);
var camera = new THREE.PerspectiveCamera(90, window.innerWidth / window.innerHeight, 0.1, 10000);
camera.position.set(-1000, 0, 0); 
scene.add(camera);

const controls = new TrackballControls(camera, renderer.domElement);
controls.noRotate = true;
controls.noPan = true;
controls.noZoom = false;
controls.zoomSpeed = 1.5;

const controls2 = new THREE.OrbitControls( camera, renderer.domElement );
// Load the panoramic image
var loader = new THREE.TextureLoader();
var texture = loader.load('models/panorami.jpg');

// Create a sphere geometry for the skybox
var geometry = new THREE.SphereGeometry(10000, 60, 40); // Adjust the radius as needed

// Map the texture to the inner faces of the sphere
var material = new THREE.MeshBasicMaterial({ map: texture, side: THREE.BackSide });

// Create a mesh using the sphere geometry and skybox material
var skybox = new THREE.Mesh(geometry, material);

// Add the skybox to the scene
scene.add(skybox);

// Adjust the camera's far clipping plane to accommodate the larger skybox
camera.far = 20000; // Adjust as needed based on the size of the skybox
camera.updateProjectionMatrix();

// Function to handle click events on planets
function onDocumentMouseDown(event) {
    const raycaster = new THREE.Raycaster();
    const mouse = new THREE.Vector2();
    mouse.x = (event.clientX / window.innerWidth) * 2 - 1;
    mouse.y = - (event.clientY / window.innerHeight) * 2 + 1;
    raycaster.setFromCamera(mouse, camera);

    const intersects = raycaster.intersectObjects(planets, true);
    if (intersects.length > 0) {
        const clickedPlanet = intersects[0].object;
        console.log('Clicked planet:', clickedPlanet.name);
        // Do something with the clicked planet
    }
}

// Add mouse down event listener to the document
// document.addEventListener('mousedown', onDocumentMouseDown);
const hello = document.getElementById("hello");
const boxPos = new THREE.Vector3();

function animate() {
    boxPos.setFromMatrixPosition(planets[0].matrixWorld)
    TWEEN.update();
    controls.target.set(controls.target.x, controls.target.y, controls.target.z);
    controls.update();
    requestAnimationFrame(animate);
    renderer.render(scene, camera);
    
}
animate();
