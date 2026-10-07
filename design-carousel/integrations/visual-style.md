# visual-style upstream 계약

설치된 `visual-style`의 SKILL.md와 실제 입력·출력 규격을 먼저 읽는다. 요청에는 레퍼런스 파일/URL, 사용 목적, 분석 범위와 한국어 설명 선호를 전달한다. 프로필을 복제 설치하거나 분석 스킬에 카피·레이아웃의 최종 결정을 맡기지 않는다.

필요한 정보는 palette, typography, spacing, composition, imagery, mood, 근거와 confidence다. 실제 프로필의 필드명이 다르면 별도의 normalized profile로 대응시키고 원본 프로필 경로를 보존한다. 정보가 없으면 unknown으로 남긴다. style_profile_ref는 URI 또는 로컬 경로이며 이 스킬 자체가 프로필 형식을 강제하지 않는다.

프로필이 이미 있으면 재사용한다. 스킬이 없으면 사용자가 제공한 프로필을 받아 진행한다. 프로필도 없으면 관찰 가능한 레퍼런스에서 임시 분석을 만들고 “visual-style 미실행·임시 프로필”이라고 표시한다. 레퍼런스에 접근할 수 없으면 입력을 요청하거나 사용자가 허용한 일반 방향을 assumptions에 기록한다. 링크를 봤다고 주장하지 않는다.
