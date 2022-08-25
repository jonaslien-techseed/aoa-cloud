import * as React from 'react';
import { useFrame } from 'react-three-fiber';

const MyCylinder = ({}) => {
    const myMesh = React.useRef();
    let counter = 0;

    useFrame(() => {
        if(myMesh.current) {
            myMesh.current.rotation.x += 0.01;
            myMesh.current.rotation.y += 0.01;

            if(counter < 100) {
                //myMesh.current.position.x += 0.1;
                //myMesh.current.position.y += 0.1;
                myMesh.current.position.z += 0.1;
                counter++;
            } else if (counter >= 100 && counter < 200) {
                //myMesh.current.position.x -= 0.1;
                //myMesh.current.position.y -= 0.1;
                myMesh.current.position.z -= 0.1;
                counter++;
            } else {
                counter = 0;
            }
        }
    });

    return (
            <mesh 
                ref={myMesh} 
                position={[0, 0, -5]} 
                rotation={[Math.PI * 0.5, 0, 0]} >
                <cylinderBufferGeometry attach="geometry" args={[0.5, 0.5, 0.15, 32]} />
                <meshStandardMaterial attach="material" color="#fff" />
            </mesh>
    );
};

export default MyCylinder;