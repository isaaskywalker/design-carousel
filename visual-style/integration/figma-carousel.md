# figma-carousel 연동 가이드

`visual-style`은 `figma-carousel`과 독립적으로 유지한다.

## visual-style 역할
- Pinterest / Instagram / 업로드 이미지 분석
- 소스 커버리지와 신뢰도 기록
- 관찰 → 규칙 변환
- 재사용 가능한 style profile 생성
- 스타일 일치도 평가
- 사용자-facing 결과를 한국어로 제공
- 이미지 생성기용 영문 키워드는 내부 필드로 유지

## figma-carousel 역할
- 캐러셀 구조
- 슬라이드별 콘텐츠
- 레이아웃 실행
- Figma 생성

## 입력 계약

```yaml
style_input:
  profile: .style-profiles/dori-editorial.yaml
  strictness: 0.75
  language:
    user_facing_language: ko-KR
  dimensions:
    typography: true
    layout: true
    imagery: true
    copy: true
```

## 권장 전체 흐름

```text
Pinterest board / Instagram account
                ↓
          visual-style
                ↓
       style-profile.yaml
                ↓
         figma-carousel
                ↓
          Figma output
                ↓
          Style Critic
                ↓
       필요 시 1회 수정
```

## 언어 규칙

- 캐러셀 본문/분석/설명은 기본적으로 한국어를 사용한다.
- 프로필의 `generation_keywords`는 이미지 생성기 또는 디자인 엔진으로 전달할 때만 사용한다.
- `generation_keywords`를 캐러셀 사용자-facing 카피에 그대로 노출하지 않는다.

## 소스 커버리지 가드레일
- `complete` 또는 `partial` + 분석 항목 10개 이상: 정상 사용
- 6~9개: 중간 신뢰도
- 6개 미만: provisional
- `blocked`: 스크린샷/이미지가 추가될 때까지 추론 규칙을 적용하지 않음

## 규칙 충돌 시 우선순위
1. 사용자의 명시적 지시
2. 브랜드/제품 제약
3. 저장된 style profile
4. carousel 기본값

레퍼런스 스타일 때문에 접근성, 가독성, 필수 콘텐츠가 훼손되면 안 된다.
