# math-teacher-skills-ko

수학 교사를 위한 AI 에이전트 스킬 모음 (한국어 번역·정리본).

공개된 오픈소스 스킬 중 **수학 수업 자료를 만들거나 풀이를 검증하는 데 쓸 수 있는 것**을 골라, 설명 문서를 한국어로 옮기고 교사 입장의 활용법을 덧붙였습니다. Claude Code 같은 에이전트의 `skills` 폴더에 넣어 쓰는 형식(`SKILL.md`)입니다.

> 번역은 AI(Claude)가 했고 사람이 전부 검수하지는 못했습니다. 의미가 어긋난 곳은 `SKILL.en.md` / `SKILL.zh.md` 원문과 대조해 주세요. 이슈로 알려 주시면 고치겠습니다.

## 들어 있는 스킬

| 스킬 | 이런 때 쓴다 (교사용) | 원본 | 라이선스 | 번역 범위 |
|---|---|---|---|---|
| [`manim-video-teacher`](skills/manim-video-teacher) | 개념 설명 애니메이션 영상 만들기: 대본 → 장면 → Manim 코드 → 음성·자막·썸네일 합성까지 | [lispking/video-skills](https://github.com/lispking/video-skills) | Apache-2.0 | `SKILL.md` 전문 (중국어 → 한국어). `scripts/`는 원본 그대로 |
| [`manim-composer`](skills/manim-composer) | "3Blue1Brown처럼" 설명하는 영상을 코드 쓰기 전에 장면별로 기획하기 (`scenes.md`) | [adithya-s-k/manim_skill](https://github.com/adithya-s-k/manim_skill) | MIT | `SKILL.md` 전문. `references/`·`templates/`는 영어 원문 |
| [`manimce-best-practices`](skills/manimce-best-practices) | Manim Community 코드를 쓸 때의 규칙·템플릿 (수식, 그래프, 3D, 카메라) | 위와 같음 | MIT | `SKILL.md` 전문. `rules/`·`templates/`는 영어 원문 |
| [`math-skill`](skills/math-skill) | 풀이·증명을 11가지 방법으로 검증하고, 문제와 채점 기준을 출제하고, 학생 풀이의 오류를 찾기 | [Wholiver/Math.Skill](https://github.com/Wholiver/Math.Skill) | MIT | `README.ko.md` 전문. `SKILL.md`·`modules/`는 영어 원문 그대로(사용자 언어에 맞춰 답하도록 되어 있어 한국어로 질문하면 한국어로 답함) |

### 교사가 이렇게 쓸 수 있습니다

- **수업용 애니메이션**: "이차함수 꼭짓점 꼴을 중3 학생에게 설명하는 60초 영상" → `manim-composer`로 장면을 기획하고 `manim-video-teacher`로 대본·코드·음성까지.
- **정답·해설 검산**: 직접 만든 문제와 해설을 붙여 넣고 `math-skill`로 "풀이 검토"를 요청. 최종 판단은 교사가 합니다.
- **문제 은행 만들기**: `math-skill`의 문제 출제 모드로 풀이와 채점 기준이 있는 문제를 만들고, 숫자는 코드로 한 번 더 검산하기를 권합니다.

## 설치

원하는 스킬 폴더를 에이전트의 skills 폴더로 복사합니다. Claude Code의 경우:

```bash
git clone https://github.com/dschloe/math-teacher-skills-ko.git
mkdir -p ~/.claude/skills
cp -R math-teacher-skills-ko/skills/math-skill ~/.claude/skills/
```

`manim-video-teacher`의 스크립트는 Python 3.10 이상, ffmpeg, `edge-tts`, Pillow가 필요합니다(해당 스킬 문서 참고).

## 제외한 것과 이유

- **`manimgl-best-practices`** (원 저장소 `adithya-s-k/manim_skill`): 예제가 3Blue1Brown의 영상 저장소(CC BY-NC-SA 4.0, 비영리·동일조건 라이선스)에서 가져온 코드라, 이 저장소의 MIT·Apache 라이선스와 섞어 재배포하기 어려워 제외했습니다. 원 저장소에서 직접 받아 쓰세요.
- **`manimce-best-practices/examples/`**: 일부 파일이 "3b1b ManimGL에서 변환"했다고 적혀 있어 같은 이유로 제외했습니다. `rules/`와 `templates/`는 포함합니다.
- **`math-skill`의 `examples/`, `tests/`, `rubrics/`**: 분량 때문에 넣지 않았습니다(원 저장소에서 확인).
- `Aaryan-Kapoor/video-production-skill`, `flysheep-ai/education-skills`(중국 수능 전용) 등은 이번 범위에서 다루지 않았습니다.

## 번역 정책

- 에이전트가 읽는 `SKILL.md`는 한국어로, 원문은 `SKILL.en.md`(영어) / `SKILL.zh.md`(중국어)로 함께 둡니다.
- 코드, 명령어, 파일 경로, 함수 이름은 번역하지 않습니다.
- 번역자가 덧붙인 내용은 문서 안에서 "번역자 주" 또는 "번역자 메모"로 표시했습니다.
- 바꾼 내용은 [`NOTICE.md`](NOTICE.md)에 정리했습니다.

## 출처와 라이선스

이 저장소의 모든 스킬은 원저작자의 라이선스(MIT 또는 Apache-2.0)를 따릅니다. 원 저작권 표기와 라이선스 전문은 [`licenses/`](licenses)에 있습니다. 원저작자들께 감사드리며, 이 저장소는 원저작자와 무관한 비공식 번역본입니다.
