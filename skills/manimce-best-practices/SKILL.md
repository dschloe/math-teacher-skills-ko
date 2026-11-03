---
name: manimce-best-practices
description: |
  다음과 같을 때 사용한다. (1) 사용자가 "manim", "Manim Community", "ManimCE"를 언급할 때, (2) 코드에 `from manim import *`가 있을 때, (3) 사용자가 `manim` CLI 명령을 실행할 때, (4) Scene, MathTex, Create() 등 ManimCE 전용 클래스를 다룰 때.

  Manim Community Edition(커뮤니티가 유지하는 파이썬 애니메이션 엔진)의 모범 사례. Scene 구조, 애니메이션, LaTeX/MathTex, ThreeDScene을 이용한 3D, 카메라 제어, 스타일, CLI 사용법을 다룬다.

  ManimGL/3b1b 버전(`manimlib` import와 `manimgl` CLI를 쓰는 것)에는 쓰지 않는다.
---

<!--
번역본 안내
- 원본: adithya-s-k/manim_skill 의 skills/manimce-best-practices/SKILL.md (영어), MIT License
- 원문은 SKILL.en.md 입니다(원문에는 examples/ 안내가 있으나 이 저장소에는 examples/ 를 넣지 않았습니다). rules/, templates/ 는 원문(영어) 그대로 두었습니다.
-->

## 사용 방법

자세한 설명과 코드 예시는 개별 규칙 파일을 읽는다.

### 핵심 개념
- [rules/scenes.md](rules/scenes.md) - Scene 구조, construct 메서드, Scene 종류
- [rules/mobjects.md](rules/mobjects.md) - Mobject 종류, VMobject, Group, 위치 지정
- [rules/animations.md](rules/animations.md) - Animation 클래스, 애니메이션 재생, 타이밍

### 생성과 변형
- [rules/creation-animations.md](rules/creation-animations.md) - Create, Write, FadeIn, DrawBorderThenFill
- [rules/transform-animations.md](rules/transform-animations.md) - Transform, ReplacementTransform, 모핑
- [rules/animation-groups.md](rules/animation-groups.md) - AnimationGroup, LaggedStart, Succession

### 글자와 수식
- [rules/text.md](rules/text.md) - Text mobject, 글꼴, 스타일
- [rules/latex.md](rules/latex.md) - MathTex, Tex, LaTeX 렌더링, 수식 색칠
- [rules/text-animations.md](rules/text-animations.md) - Write, AddTextLetterByLetter, TypeWithCursor

### 스타일과 모양
- [rules/colors.md](rules/colors.md) - 색 상수, 그러데이션, 색 조작
- [rules/styling.md](rules/styling.md) - 채우기, 선, 불투명도, 시각 속성

### 위치와 배치
- [rules/positioning.md](rules/positioning.md) - move_to, next_to, align_to, shift 메서드
- [rules/grouping.md](rules/grouping.md) - VGroup, Group, arrange, 배치 패턴

### 좌표계와 그래프
- [rules/axes.md](rules/axes.md) - Axes, NumberPlane, 좌표계
- [rules/graphing.md](rules/graphing.md) - 함수 그래프, 매개변수 곡선
- [rules/3d.md](rules/3d.md) - ThreeDScene, 3D 축, 곡면, 카메라 방향

### 애니메이션 제어
- [rules/timing.md](rules/timing.md) - 속도 함수(rate function), 이징, run_time, lag_ratio
- [rules/updaters.md](rules/updaters.md) - Updater, ValueTracker, 동적 애니메이션
- [rules/camera.md](rules/camera.md) - MovingCameraScene, 확대, 이동, 프레임 조작

### 설정과 CLI
- [rules/cli.md](rules/cli.md) - 명령줄 인터페이스, 렌더 옵션, 화질 플래그
- [rules/config.md](rules/config.md) - 설정 체계, manim.cfg, 설정값

### 도형과 기하
- [rules/shapes.md](rules/shapes.md) - Circle, Square, Rectangle, Polygon 등 기본 도형
- [rules/lines.md](rules/lines.md) - Line, Arrow, Vector, DashedLine, 연결선

## 동작하는 예제 (이 저장소에는 넣지 않음)

원 저장소의 `examples/` 파일 일부는 3Blue1Brown의 ManimGL 코드를 변환한 것이라고 적혀 있어(저작권 조건이 불분명), 이 저장소에는 넣지 않았다. 필요하면 원 저장소(adithya-s-k/manim_skill)의 `skills/manimce-best-practices/examples/`를 직접 확인한다. 자세한 이유는 저장소 최상위 README의 "제외한 것" 항목을 본다.

## 장면 템플릿

복사해서 고쳐 쓰며 새 프로젝트를 시작한다.

- [templates/basic_scene.py](templates/basic_scene.py) - 기본 2D 장면 템플릿
- [templates/camera_scene.py](templates/camera_scene.py) - 확대·이동이 있는 MovingCameraScene
- [templates/threed_scene.py](templates/threed_scene.py) - 곡면과 카메라 회전이 있는 3D 장면

## 빠른 참조

### 기본 Scene 구조
```python
from manim import *

class MyScene(Scene):
    def construct(self):
        # mobject 만들기
        circle = Circle()

        # 장면에 추가 (정지 상태)
        self.add(circle)

        # 또는 애니메이션으로
        self.play(Create(circle))

        # 대기
        self.wait(1)
```

### 렌더 명령
```bash
# 미리보기와 함께 기본 렌더
manim -pql scene.py MyScene

# 화질 플래그: -ql(낮음), -qm(중간), -qh(높음), -qk(4k)
manim -pqh scene.py MyScene
```

### 3b1b/ManimGL과의 주요 차이

| 항목 | Manim Community | 3b1b/ManimGL |
|---------|-----------------|--------------|
| import | `from manim import *` | `from manimlib import *` |
| CLI | `manim` | `manimgl` |
| 수식 글자 | `MathTex(r"\pi")` | `Tex(R"\pi")` |
| Scene | `Scene` | `InteractiveScene` |
| 패키지 | `manim` (PyPI) | `manimgl` (PyPI) |

### Jupyter 노트북 지원

`%%manim` 셀 매직을 쓴다.

```python
%%manim -qm MyScene
class MyScene(Scene):
    def construct(self):
        self.play(Create(Circle()))
```

### 피해야 할 흔한 함정

1. **버전 혼동**: `manimgl`(3b1b 버전)이 아니라 `manim`(Community)을 쓰고 있는지 확인한다.
2. **import 확인**: `from manim import *`는 ManimCE, `from manimlib import *`는 ManimGL이다.
3. **오래된 튜토리얼**: 영상 튜토리얼은 옛날 것일 수 있으니 공식 문서를 우선한다.
4. **manimpango 문제**: 글자 렌더링이 실패하면 manimpango 설치 요건을 확인한다.
5. **PATH 문제(Windows)**: `manim` 명령을 찾지 못하면 `python -m manim`을 쓰거나 PATH를 확인한다.

### 설치

```bash
# Manim Community 설치
pip install manim

# 설치 확인
manim checkhealth
```

### 유용한 명령

```bash
manim -pql scene.py Scene    # 낮은 화질 미리보기 (개발용)
manim -pqh scene.py Scene    # 높은 화질 미리보기
manim --format gif scene.py  # GIF로 출력
manim checkhealth            # 설치 확인
manim plugins -l             # 플러그인 목록
```
