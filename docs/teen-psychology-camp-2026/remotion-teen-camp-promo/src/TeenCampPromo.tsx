import React from 'react';
import {
  AbsoluteFill,
  Easing,
  Img,
  interpolate,
  OffthreadVideo,
  Sequence,
  staticFile,
  useCurrentFrame,
  useVideoConfig,
} from 'remotion';

const colors = {
  ink: '#151515',
  paper: '#fff8ec',
  blue: '#3d65f5',
  mint: '#69d9b4',
  yellow: '#ffd166',
  red: '#f45b69',
};

const sourceVideo = staticFile('media/teen-camp-source-video-2026-06-04.mp4');
const poster = staticFile('media/teen-psychology-camp-tatyana-moonn-poster-2026.jpg');

const appear = (frame: number, start: number, end = start + 18) =>
  interpolate(frame, [start, end], [0, 1], {
    extrapolateLeft: 'clamp',
    extrapolateRight: 'clamp',
    easing: Easing.out(Easing.cubic),
  });

const disappear = (frame: number, start: number, end = start + 15) =>
  interpolate(frame, [start, end], [1, 0], {
    extrapolateLeft: 'clamp',
    extrapolateRight: 'clamp',
    easing: Easing.in(Easing.cubic),
  });

const TextBlock: React.FC<{
  start: number;
  end?: number;
  eyebrow: string;
  title: string;
  body: string;
  accent?: string;
}> = ({start, end = 300, eyebrow, title, body, accent = colors.yellow}) => {
  const frame = useCurrentFrame();
  const opacity = appear(frame, start) * disappear(frame, end - 18, end);
  const y = interpolate(opacity, [0, 1], [36, 0]);

  return (
    <div
      style={{
        opacity,
        transform: `translateY(${y}px)`,
        width: '100%',
      }}
    >
      <div
        style={{
          display: 'inline-flex',
          alignItems: 'center',
          gap: 14,
          padding: '12px 18px',
          borderRadius: 999,
          background: 'rgba(255, 248, 236, 0.92)',
          color: colors.ink,
          fontSize: 30,
          fontWeight: 800,
          lineHeight: 1,
          marginBottom: 26,
        }}
      >
        <span
          style={{
            width: 18,
            height: 18,
            borderRadius: 99,
            background: accent,
          }}
        />
        {eyebrow}
      </div>
      <div
        style={{
          color: colors.paper,
          fontSize: 68,
          fontWeight: 900,
          lineHeight: 0.96,
          letterSpacing: 0,
          textShadow: '0 8px 34px rgba(0,0,0,0.36)',
          maxWidth: 880,
        }}
      >
        {title}
      </div>
      <div
        style={{
          color: 'rgba(255, 248, 236, 0.94)',
          fontSize: 34,
          fontWeight: 650,
          lineHeight: 1.18,
          marginTop: 28,
          maxWidth: 820,
          textShadow: '0 6px 24px rgba(0,0,0,0.38)',
        }}
      >
        {body}
      </div>
    </div>
  );
};

export const TeenCampPromo: React.FC = () => {
  const frame = useCurrentFrame();
  const {durationInFrames} = useVideoConfig();
  const zoom = interpolate(frame, [0, durationInFrames], [1.02, 1.09]);
  const posterOpacity = interpolate(frame, [222, 252], [0, 1], {
    extrapolateLeft: 'clamp',
    extrapolateRight: 'clamp',
  });
  const finalOpacity = interpolate(frame, [248, 276], [0, 1], {
    extrapolateLeft: 'clamp',
    extrapolateRight: 'clamp',
  });

  return (
    <AbsoluteFill style={{background: colors.ink, fontFamily: 'Arial, sans-serif'}}>
      <AbsoluteFill>
        <OffthreadVideo
          src={sourceVideo}
          style={{
            width: '100%',
            height: '100%',
            objectFit: 'cover',
            transform: `scale(${zoom})`,
            filter: 'saturate(1.1) contrast(1.04)',
          }}
          volume={0.35}
        />
      </AbsoluteFill>

      <AbsoluteFill
        style={{
          background:
            'linear-gradient(180deg, rgba(12,16,30,0.25) 0%, rgba(12,16,30,0.46) 45%, rgba(12,16,30,0.78) 100%)',
        }}
      />
      <AbsoluteFill
        style={{
          background: 'linear-gradient(135deg, rgba(61,101,245,0.18), rgba(105,217,180,0.1) 54%, transparent)',
          mixBlendMode: 'screen',
        }}
      />

      <div
        style={{
          position: 'absolute',
          left: 74,
          right: 74,
          top: 116,
        }}
      >
        <div
          style={{
            display: 'flex',
            alignItems: 'center',
            justifyContent: 'space-between',
            color: colors.paper,
            fontSize: 30,
            fontWeight: 800,
            opacity: 0.94,
          }}
        >
          <span>Татьяна Мунн</span>
          <span>Москва</span>
        </div>
      </div>

      <div
        style={{
          position: 'absolute',
          left: 74,
          right: 74,
          bottom: 380,
        }}
      >
        <Sequence from={0} durationInFrames={104}>
          <TextBlock
            start={8}
            end={104}
            eyebrow="12-19 лет"
            title="Подростковый лагерь"
            body="Психология, общение, уверенность и soft skills в живой группе"
            accent={colors.mint}
          />
        </Sequence>

        <Sequence from={104} durationInFrames={92}>
          <TextBlock
            start={8}
            end={92}
            eyebrow="6-10 июля"
            title="Пять дней практики"
            body="Эмоции, конфликты, самостоятельность, мини-проекты и работа с ИИ"
            accent={colors.yellow}
          />
        </Sequence>

        <Sequence from={196} durationInFrames={104}>
          <TextBlock
            start={8}
            end={100}
            eyebrow="Цветной бульвар"
            title="Запись открыта"
            body="Небольшая группа. Понятная программа. Бережная среда для подростков"
            accent={colors.red}
          />
        </Sequence>
      </div>

      <AbsoluteFill
        style={{
          opacity: posterOpacity,
          background: 'rgba(21,21,21,0.72)',
          display: 'flex',
          alignItems: 'center',
          justifyContent: 'center',
          padding: 76,
        }}
      >
        <Img
          src={poster}
          style={{
            width: 690,
            maxHeight: 1040,
            objectFit: 'contain',
            borderRadius: 28,
            boxShadow: '0 34px 90px rgba(0,0,0,0.36)',
          }}
        />
      </AbsoluteFill>

      <AbsoluteFill
        style={{
          opacity: finalOpacity,
          justifyContent: 'flex-end',
          padding: '0 74px 74px',
          color: colors.paper,
        }}
      >
        <div
          style={{
            display: 'flex',
            justifyContent: 'space-between',
            alignItems: 'flex-end',
            fontWeight: 850,
            fontSize: 34,
          }}
        >
          <span>мунн.рф</span>
          <span>Написать и уточнить участие</span>
        </div>
      </AbsoluteFill>
    </AbsoluteFill>
  );
};
