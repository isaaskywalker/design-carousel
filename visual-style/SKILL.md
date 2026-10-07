---
name: visual-style
description: Pinterest·Instagram·업로드 레퍼런스에서 타이포·색·여백·레이아웃 등 형식적 Style DNA를 추출하고 평가한다. 문화적 인물·밈 선정은 visual-culture에 맡긴다.
---

# visual-style

한국인 사용자를 기본 대상으로 하는 재사용 가능한 Visual Style Intelligence 스킬이다. Pinterest 보드, Instagram 계정/게시물, 업로드 이미지, 스크린샷, 무드보드, 저장된 스타일 프로필을 분석해 캐러셀 카피·레이아웃·이미지 생성에 재사용 가능한 디자인 규칙으로 변환한다.

## 기본 언어 정책

기본 사용자 언어는 `ko-KR`이다.

- 사용자에게 보여주는 분석, 설명, 관찰, 규칙, 평가, 수정 제안은 **한국어로 출력한다.**
- 이미지 생성기나 디자인 시스템에 전달할 필요가 있을 때만 **내부용 영문 생성 키워드**를 별도 필드로 유지한다.
- 사용자가 명시적으로 다른 언어를 요청하면 그 언어를 우선한다.
- 한국어 설명과 영문 생성 키워드를 섞어서 사용자에게 불필요하게 노출하지 않는다.

권장 설정:

```yaml
language:
  user_facing_language: ko-KR
  analysis_language: ko-KR
  generation_keyword_language: en-US
```

## 목적

사용자가 하나 이상의 시각 레퍼런스를 제공하고, 이후 생성물에 그 레퍼런스의 시각 언어를 반영하고 싶을 때 사용한다.

이 스킬은 `미니멀`, `클린`, `에디토리얼`, `모던` 같은 추상 키워드만 뽑고 끝내면 안 된다. 반드시 **관찰 가능한 근거 → 실행 가능한 디자인 규칙**으로 변환해야 한다.

## 핵심 기능

1. **Reference Analyzer** — Pinterest/Instagram URL, 스크린샷, 업로드 이미지, 폴더를 분석해 반복되는 시각 패턴을 찾는다.
2. **Style Distiller** — 관찰 내용을 재사용 가능한 디자인 규칙과 토큰으로 변환한다.
3. **Reference Weighting** — 타이포, 레이아웃, 이미지, 카피 등 항목별로 어떤 레퍼런스를 얼마나 반영할지 조절한다.
4. **Style Memory** — 이름을 붙인 스타일 프로필을 저장하고 재사용한다.
5. **Style Critic** — 생성 결과가 스타일 프로필을 얼마나 잘 따랐는지 평가하고 수정안을 제시한다.

## 지원 입력

다음 입력을 단독 또는 조합해서 받을 수 있다.

- Pinterest 보드 URL
- Pinterest 핀 URL
- Instagram 계정 URL
- 시각적으로 접근 가능한 Instagram 게시물/Reel URL
- 업로드 스크린샷
- 업로드 이미지
- 로컬 레퍼런스 폴더
- 이전에 저장한 스타일 프로필
- `A의 타이포를 많이 쓰고 B의 이미지 구성을 참고해줘` 같은 자연어 선호

## URL 우선 분석 정책

Pinterest와 Instagram URL은 보조 정보가 아니라 **1차 입력**이다.

URL이 들어오면:

1. 공개적으로 접근 가능한 시각 콘텐츠를 먼저 확인한다.
2. 실제로 발견한 항목과 실제 분석한 항목 수를 기록한다.
3. 화면에서 확인 가능한 근거만으로 관찰을 작성한다.
4. 일부만 접근 가능하면 그 범위 안에서 분석하고 신뢰도를 낮춘다.
5. 로그인, anti-bot, 동적 로딩, 비공개 계정 등으로 막히면 전체를 분석한 것처럼 말하지 않는다.
6. 다음 순서로 fallback한다.
   - 공개 프리뷰/썸네일
   - 사용자 업로드 스크린샷
   - 사용자 업로드 이미지/로컬 폴더

```yaml
source_status: complete | partial | blocked
```

권장 메타데이터:

```yaml
source:
  type: pinterest_board
  url: https://www.pinterest.com/example/board/
  source_status: partial
  discovered_items: 42
  analyzed_items: 18
  notes:
    - "로그인 없이 공개 프리뷰로 확인 가능한 핀만 분석함"
```

## 워크플로우

### 1. 레퍼런스 수집

```yaml
references:
  - id: ref_a
    source: instagram
    url: https://www.instagram.com/account_a/
    label: account_a
  - id: ref_b
    source: pinterest
    url: https://www.pinterest.com/user/board_b/
    label: board_b
```

### 2. URL 및 미디어 확인

URL 입력은 스크린샷을 먼저 요구하지 말고 공개 시각 콘텐츠를 먼저 분석한다.

계정 소개, 보드 제목, 캡션, 해시태그만으로 시각 스타일을 판단하지 않는다. 시각 자산이 핵심 근거다.

```yaml
inspection:
  source_status: partial
  discovered_items: 20
  analyzed_items: 14
  evidence_types:
    - image
    - visible_text
    - layout
```

서로 다른 시각 항목이 6개 미만이면 신뢰도를 명시적으로 낮추고 스크린샷/이미지 추가를 권장한다.

### 3. 관찰 가능한 근거 분석

나쁜 예:

```yaml
관찰: "모던하고 에디토리얼하다"
```

좋은 예:

```yaml
관찰: "분석한 게시물 12개 중 9개가 화면 폭의 약 1/3을 차지하는 큰 좌측 정렬 제목을 사용한다"
신뢰도: 높음
```

분석 분류 기준은 `references/reference-analysis.md`를 따른다.

### 4. 관찰 → 규칙 변환

`prompts/extract-style.md`를 사용한다.

```yaml
- 관찰: "12개 중 8개가 좌측 상단에 하나의 대형 제목을 배치한다"
  디자인_규칙: "슬라이드마다 핵심 제목은 하나만 두고 좌측 정렬한다. 제목 영역은 슬라이드 폭의 약 25~40%를 사용한다."
  적용_영역: layout
  신뢰도: 높음
  근거_수: 8
  generation_keywords:
    - "single oversized left-aligned headline"
    - "editorial negative space"
```

근거 없이 규칙을 만들지 않는다.

### 5. 레퍼런스 가중치 적용

사용자가 가중치를 직접 말하면 그대로 따른다. 없으면 균형 잡힌 기본값을 만들고 사용자에게 보이게 한다.

```yaml
reference_weights:
  ref_a:
    typography: 0.6
    layout: 0.2
    imagery: 0.2
  ref_b:
    typography: 0.1
    layout: 0.6
    imagery: 0.3
```

### 6. Style Profile 생성

`schemas/style-profile.schema.json` 형식을 따른다.

포함 항목:

- 언어 설정
- 소스 커버리지/접근 상태
- Visual DNA
- 타이포 규칙
- 레이아웃 규칙
- 이미지 방향
- 시각 모티프
- 카피 방향
- 피해야 할 패턴
- 신뢰도 메모
- 레퍼런스 가중치
- 내부용 영문 생성 키워드

### 7. Style Memory 저장/재사용

```text
.style-profiles/<style-name>.yaml
```

기존 프로필을 사용자 지시 없이 덮어쓰지 않는다. 교체 요청이 없으면 버전 파일을 만든다.

### 8. 다운스트림 적용

```yaml
style_input:
  profile: .style-profiles/dori-editorial.yaml
  strictness: 0.75
  dimensions:
    typography: true
    layout: true
    imagery: true
    copy: true
```

이미지 생성 시에는 이미지 관련 규칙과 `generation_keywords`만 전달한다. 전체 프로필을 이미지 프롬프트에 덤프하지 않는다.

카피 생성 시에는 카피/편집 리듬 관련 규칙만 사용한다.

자세한 내용은 `integration/figma-carousel.md`를 참고한다.

### 9. Style Critic 평가

생성 결과가 있으면 `prompts/style-critic.md`로 평가한다.

사용자-facing 결과는 한국어로 제공한다.

```yaml
스타일_일치도:
  타이포그래피: 91
  레이아웃: 74
  이미지: 86
  카피: 68
  종합: 79
수정_제안:
  - "보조 문구 길이를 약 30% 줄인다."
  - "제목 크기를 키우고 좌측 여백을 더 확보한다."
```

종합 점수가 80 미만이고 호출 환경이 반복 개선을 허용하면 한 번 자동 수정할 수 있다.

## 권장 명령 패턴

```text
/style analyze <pinterest-board-url>
/style analyze <instagram-account-url>
/style analyze <url-1> <url-2> <image-folder>
/style save <name>
/style apply <name>
/style critique <output>
/style compare <style-a> <style-b>
```

명령어는 개념적 패턴이며 호스트 에이전트 프레임워크에 맞게 조정한다.

## 사용자 응답 원칙

URL 분석 성공 시:
- 먼저 스크린샷 업로드를 요구하지 않는다.
- 분석한 항목 수를 알려준다.
- 샘플링 한계와 신뢰도를 한국어로 설명한다.

URL 분석이 일부만 가능할 때:
- provisional style profile을 만든다.
- 분석 범위를 명확히 밝힌다.

URL이 차단됐을 때:
- 전체 스타일을 추정하지 않는다.
- 대표 스크린샷 또는 이미지 업로드를 요청한다.

## 출력 언어 우선순위

1. 사용자가 명시한 언어
2. 저장된 스타일 프로필의 `language.user_facing_language`
3. 기본값 `ko-KR`

생성 시스템과 연결하기 위한 영문 키워드는 `generation_keywords` 내부에서만 유지한다.


## 문화 분석과의 경계
인물·밈의 정체성, 최신성, 댓글의 맥락과 자산 선정은 독립 `visual-culture`의 책임이다. 이 스킬은 크롭·색·질감·구도 등 형식적 이미지 처리만 정의한다. 단독 사용 시 문화 자산을 임의로 선정하지 않는다.
