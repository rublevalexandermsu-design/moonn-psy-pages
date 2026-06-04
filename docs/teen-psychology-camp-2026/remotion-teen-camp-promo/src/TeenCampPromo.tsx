import React from 'react';
import {
  AbsoluteFill,
  Easing,
  Img,
  interpolate,
  Sequence,
  staticFile,
  useCurrentFrame,
  useVideoConfig,
} from 'remotion';

const colors = {
  ink: '#181713',
  paper: '#fff8ec',
  blue: '#2f5ee9',
  mint: '#52c7a7',
  yellow: '#ffd166',
  red: '#ef5a5f',
  charcoal: '#2c2922',
};

const poster = staticFile('media/teen-psychology-camp-tatyana-moonn-poster-2026.jpg');

const smooth = (frame: number, start: number, end: number, from: number, to: number) =>
  interpolate(frame, [start, end], [from, to], {
    extrapolateLeft: 'clamp',
    extrapolateRight: 'clamp',
    easing: Easing.out(Easing.cubic),
  });

const appear = (frame: number, start: number, end = start + 18) =>
  smooth(frame, start, end, 0, 1);

const leave = (frame: number, start: number, end = start + 16) =>
  interpolate(frame, [start, end], [1, 0], {
    extrapolateLeft: 'clamp',
    extrapolateRight: 'clamp',
    easing: Easing.in(Easing.cubic),
  });

const TopBar: React.FC = () => {
  const frame = useCurrentFrame();
  const opacity = appear(frame, 6, 24);

  return (
    <div
      style={{
        position: 'absolute',
        left: 64,
        right: 64,
        top: 74,
        opacity,
        display: 'flex',
        justifyContent: 'space-between',
        alignItems: 'center',
        color: colors.paper,
        fontSize: 30,
        fontWeight: 800,
        letterSpacing: 0,
      }}
    >
      <span>Татьяна Мунн</span>
      <span>6-10 июля</span>
    </div>
  );
};

const MovingBands: React.FC = () => {
  const frame = useCurrentFrame();
  const slow = interpolate(frame, [0, 300], [0, 1]);

  return (
    <AbsoluteFill style={{background: colors.ink, overflow: 'hidden'}}>
      <div
        style={{
          position: 'absolute',
          inset: 0,
          background:
            'linear-gradient(150deg, #1b1a16 0%, #2b342f 34%, #214766 58%, #483739 100%)',
        }}
      />
      <div
        style={{
          position: 'absolute',
          width: 1540,
          height: 420,
          left: -260 + slow * 110,
          top: 210,
          transform: 'rotate(-18deg)',
          background: colors.blue,
          opacity: 0.62,
        }}
      />
      <div
        style={{
          position: 'absolute',
          width: 1380,
          height: 340,
          left: -120 - slow * 90,
          top: 760,
          transform: 'rotate(14deg)',
          background: colors.mint,
          opacity: 0.54,
        }}
      />
      <div
        style={{
          position: 'absolute',
          width: 1260,
          height: 300,
          left: 20 + slow * 130,
          top: 1260,
          transform: 'rotate(-11deg)',
          background: colors.yellow,
          opacity: 0.72,
        }}
      />
      <div
        style={{
          position: 'absolute',
          inset: 0,
          background:
            'linear-gradient(180deg, rgba(24,23,19,0.10) 0%, rgba(24,23,19,0.34) 48%, rgba(24,23,19,0.80) 100%)',
        }}
      />
    </AbsoluteFill>
  );
};

const SceneText: React.FC<{
  start: number;
  end: number;
  eyebrow: string;
  title: string;
  body: string;
  accent: string;
}> = ({start, end, eyebrow, title, body, accent}) => {
  const frame = useCurrentFrame();
  const opacity = appear(frame, start) * leave(frame, end - 18, end);
  const y = interpolate(opacity, [0, 1], [40, 0]);

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
          padding: '13px 19px',
          borderRadius: 999,
          background: 'rgba(255, 248, 236, 0.94)',
          color: colors.ink,
          fontSize: 30,
          fontWeight: 900,
          lineHeight: 1,
          marginBottom: 28,
        }}
      >
        <span style={{width: 18, height: 18, borderRadius: 99, background: accent}} />
        {eyebrow}
      </div>
      <div
        style={{
          color: colors.paper,
          fontSize: 78,
          fontWeight: 950,
          lineHeight: 0.94,
          letterSpacing: 0,
          maxWidth: 900,
          textShadow: '0 12px 42px rgba(0,0,0,0.35)',
        }}
      >
        {title}
      </div>
      <div
        style={{
          color: 'rgba(255, 248, 236, 0.95)',
          fontSize: 36,
          fontWeight: 700,
          lineHeight: 1.14,
          marginTop: 28,
          maxWidth: 850,
          textShadow: '0 10px 34px rgba(0,0,0,0.34)',
        }}
      >
        {body}
      </div>
    </div>
  );
};

const PosterPanel: React.FC = () => {
  const frame = useCurrentFrame();
  const opacity = appear(frame, 116, 140) * leave(frame, 232, 252);
  const scale = smooth(frame, 116, 252, 0.92, 1.03);
  const rotate = smooth(frame, 116, 252, -2, 1);

  return (
    <AbsoluteFill
      style={{
        opacity,
        alignItems: 'center',
        justifyContent: 'center',
        padding: 76,
      }}
    >
      <div
        style={{
          width: 720,
          padding: 22,
          borderRadius: 34,
          background: 'rgba(255, 248, 236, 0.96)',
          boxShadow: '0 34px 90px rgba(0,0,0,0.34)',
          transform: `scale(${scale}) rotate(${rotate}deg)`,
        }}
      >
        <Img
          src={poster}
          style={{
            width: '100%',
            display: 'block',
            borderRadius: 24,
          }}
        />
      </div>
    </AbsoluteFill>
  );
};

const InfoCard: React.FC<{
  from: number;
  left: number;
  top: number;
  label: string;
  value: string;
  color: string;
}> = ({from, left, top, label, value, color}) => {
  const frame = useCurrentFrame();
  const opacity = appear(frame, from, from + 14) * leave(frame, 238, 252);
  const x = interpolate(opacity, [0, 1], [30, 0]);

  return (
    <div
      style={{
        position: 'absolute',
        left,
        top,
        width: 380,
        opacity,
        transform: `translateX(${x}px)`,
        padding: '24px 26px',
        borderRadius: 22,
        background: 'rgba(255, 248, 236, 0.95)',
        boxShadow: '0 18px 52px rgba(0,0,0,0.22)',
      }}
    >
      <div style={{fontSize: 23, fontWeight: 850, color, marginBottom: 8}}>{label}</div>
      <div style={{fontSize: 34, fontWeight: 950, color: colors.ink, lineHeight: 1.04}}>{value}</div>
    </div>
  );
};

const FinalScreen: React.FC = () => {
  const frame = useCurrentFrame();
  const opacity = appear(frame, 244, 270);
  const y = interpolate(opacity, [0, 1], [36, 0]);

  return (
    <AbsoluteFill
      style={{
        opacity,
        justifyContent: 'flex-end',
        padding: '0 64px 86px',
        color: colors.paper,
      }}
    >
      <div style={{transform: `translateY(${y}px)`}}>
        <div
          style={{
            fontSize: 86,
            fontWeight: 950,
            lineHeight: 0.94,
            letterSpacing: 0,
            marginBottom: 28,
            maxWidth: 920,
          }}
        >
          Запись на подростковый интенсив открыта
        </div>
        <div
          style={{
            display: 'flex',
            alignItems: 'center',
            justifyContent: 'space-between',
            gap: 30,
            paddingTop: 30,
            borderTop: '3px solid rgba(255,248,236,0.42)',
            fontSize: 34,
            fontWeight: 850,
          }}
        >
          <span>мунн.рф</span>
          <span>Москва, Сущёвский Вал, 56</span>
        </div>
      </div>
    </AbsoluteFill>
  );
};

export const TeenCampPromo: React.FC = () => {
  const frame = useCurrentFrame();
  const {durationInFrames} = useVideoConfig();
  const grainOpacity = interpolate(frame % 18, [0, 9, 18], [0.07, 0.13, 0.07]);
  const sweep = interpolate(frame, [0, durationInFrames], [-420, 1180]);

  return (
    <AbsoluteFill style={{background: colors.ink, fontFamily: 'Arial, sans-serif'}}>
      <MovingBands />
      <TopBar />

      <div
        style={{
          position: 'absolute',
          left: 64,
          right: 64,
          bottom: 330,
        }}
      >
        <Sequence from={0} durationInFrames={96}>
          <SceneText
            start={8}
            end={92}
            eyebrow="12-19 лет"
            title="Интенсив для подростков"
            body="Психология общения, эмоции, уверенность и работа в группе"
            accent={colors.mint}
          />
        </Sequence>
        <Sequence from={88} durationInFrames={96}>
          <SceneText
            start={8}
            end={88}
            eyebrow="5 дней"
            title="Практика вместо лекций"
            body="Игры, задания, мини-проекты, разбор конфликтов и навыки самостоятельности"
            accent={colors.yellow}
          />
        </Sequence>
        <Sequence from={184} durationInFrames={86}>
          <SceneText
            start={6}
            end={80}
            eyebrow="Москва"
            title="Небольшая группа"
            body="Бережная среда, понятная программа и живой контакт с ведущей"
            accent={colors.red}
          />
        </Sequence>
      </div>

      <PosterPanel />

      <InfoCard from={142} left={70} top={1180} label="Когда" value="6-10 июля" color={colors.blue} />
      <InfoCard from={156} left={630} top={1180} label="Возраст" value="12-19 лет" color={colors.red} />
      <InfoCard from={170} left={70} top={1364} label="Формат" value="очно, Москва" color={colors.mint} />
      <InfoCard from={184} left={630} top={1364} label="Фокус" value="soft skills" color={colors.charcoal} />

      <div
        style={{
          position: 'absolute',
          left: sweep,
          top: 0,
          width: 160,
          height: 1920,
          transform: 'skewX(-14deg)',
          background: 'rgba(255, 248, 236, 0.12)',
        }}
      />
      <AbsoluteFill
        style={{
          opacity: grainOpacity,
          backgroundImage:
            'linear-gradient(90deg, rgba(255,255,255,0.08) 1px, transparent 1px), linear-gradient(180deg, rgba(255,255,255,0.05) 1px, transparent 1px)',
          backgroundSize: '46px 46px',
        }}
      />
      <FinalScreen />
    </AbsoluteFill>
  );
};
