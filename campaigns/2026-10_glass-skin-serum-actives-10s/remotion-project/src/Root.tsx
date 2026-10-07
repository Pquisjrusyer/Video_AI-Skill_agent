import React from 'react';
import {Composition} from 'remotion';
import {Assembly, TOTAL} from './Assembly';

export const RemotionRoot: React.FC = () => (
  <Composition id="FinalAssembly" component={Assembly} durationInFrames={TOTAL} fps={30} width={1080} height={1920} />
);
