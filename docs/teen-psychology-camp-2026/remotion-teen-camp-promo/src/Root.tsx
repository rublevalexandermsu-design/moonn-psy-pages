import React from 'react';
import {Composition} from 'remotion';
import {TeenCampPromo} from './TeenCampPromo';

export const Root: React.FC = () => {
  return (
    <Composition
      id="TeenCampPromo"
      component={TeenCampPromo}
      durationInFrames={300}
      fps={30}
      width={1080}
      height={1920}
    />
  );
};
