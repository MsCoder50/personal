import TrackballControls from 'https://cdn.jsdelivr.net/npm/three-trackballcontrols@0.9/index.min.js'

// Create a scene
const scene = new THREE.Scene();

// Load the sun model
const sunLoader = new GLTFLoader();
sunLoader.load('./models/sun.glb', function (gltf) {
    const sun = gltf.scene;
    scene.add(sun);
});

// Load planet models
const planets = [];
const planetNames = ['mercury', 'venus', 'earth', 'mars', 'jupiter', 'saturn', 'uranus', 'neptune'];
const loader = new GLTFLoader();
let distanceFactor = 50;
planetNames.forEach(function (name, index) {
    loader.load(`models/${name}.glb`, function (gltf) {
        const planet = gltf.scene;
        planets.push(planet);
        planet.scale.set(2, 2, 2);
        scene.add(planet);
        const ran = Math.random();
        if (ran > 0.5) {
            planet.position.set((index + 1) * distanceFactor, (index + 1) * distanceFactor, (index + 1) * distanceFactor);
        } else {
            distanceFactor = -50;
            planet.position.set((index + 1) * distanceFactor, (index + 1) * distanceFactor, (index + 1) * distanceFactor);
        }
    });
});

// Lights
const directionalLight = new THREE.DirectionalLight(0xffffff, 1);
directionalLight.position.set(50, 0, 0).normalize();
scene.add(directionalLight);

const sunLight = new THREE.PointLight(0xffffff, 1);
sunLight.position.set(0, 0, 0);
scene.add(sunLight);

// Set up camera, renderer, and controls
const renderer = new THREE.WebGLRenderer();
renderer.setSize(window.innerWidth, window.innerHeight);
document.body.appendChild(renderer.domElement);

const camera = new THREE.PerspectiveCamera(90, window.innerWidth / window.innerHeight, 0.1, 10000);
camera.position.set(50, 0, 0);
scene.add(camera);

const controls = new TrackballControls(camera, renderer.domElement);
controls.noRotate = true;
controls.noPan = true;
controls.zoomSpeed = 1.0; // Adjust the zoom speed as needed

// Load the panoramic image
const loaderTexture = new THREE.TextureLoader();
const texture = loaderTexture.load('models/panorami.jpg');

const geometry = new THREE.SphereGeometry(5000, 60, 40);
const material = new THREE.MeshBasicMaterial({ map: texture, side: THREE.BackSide });
const skybox = new THREE.Mesh(geometry, material);
scene.add(skybox);

// Handle window resizing
window.addEventListener('resize', onWindowResize);

function onWindowResize() {
    camera.aspect = window.innerWidth / window.innerHeight;
    camera.updateProjectionMatrix();
    renderer.setSize(window.innerWidth, window.innerHeight);
}

// Handle mouse scroll wheel for zooming
document.addEventListener('wheel', onDocumentMouseWheel);

function onDocumentMouseWheel(event) {
    const deltaY = event.deltaY;
    controls.zoomCamera(deltaY); // Call zoomCamera method from TrackballControls
}

// Animation loop
function animate() {
    requestAnimationFrame(animate);
    controls.update();
    renderer.render(scene, camera);
}

animate();