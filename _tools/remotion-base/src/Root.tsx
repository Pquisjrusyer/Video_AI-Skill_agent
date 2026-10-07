import React from 'react';
import {Composition} from 'remotion';
import {Main, Timeline, totalSeconds} from './Main';

// Dữ liệu dựng (timeline.json của campaign) đi vào qua inputProps — Claude chỉ sửa timeline.json, không sửa code.
const fallback: Timeline = {fps: 30, width: 1080, height: 1920, scenes: []};

export const Root: React.FC = () => (
  <Composition
    id="Main"
    component={Main}
    defaultProps={fallback}
    fps={30}
    width={1080}
    height={1920}
    durationInFrames={30}
    calculateMetadata={({props}) => {
      const fps = props.fps || 30;
      return {
        fps,
        width: props.width || 1080,
        height: props.height || 1920,
        durationInFrames: Math.max(1, Math.round(totalSeconds(props) * fps)),
      };
    }}
  />
);
