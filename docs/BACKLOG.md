# BabyHealth — Prioritized Backlog & Release Plan

## Document Overview

This document outlines the complete backlog for BabyHealth, organized by release phases, epics, and priority. It provides a roadmap from MVP through future ecosystem expansion.

---

## Release Strategy

### MVP Phase (Weeks 1-7) — ~50 business days
**Goal:** Launch core baby tracking app with 6 essential trackers, shared caregiver visibility, and beautiful daily dashboard.

**Release target:** Public beta or closed launch to 50-100 families

### Phase 2 (Weeks 8-10) — ~15 business days
**Goal:** Add reporting, insights, routines library, and baby profile/growth tracking.

**Release target:** General availability; gather user feedback; optimize engagement

### Phase 3 (Weeks 11+) — TBD
**Goal:** Health ecosystem (medications, health events), integrations, advanced features.

**Release target:** Health-focused features; prepare for ecosystem partnerships

---

## MVP Release Backlog

### Phase 1: Foundation & Core Logging (Weeks 1-5)

#### Epic EP-01: Fundação do Produto (P0)
- **Duration:** 10 business days
- **Owner:** Design Lead + Frontend Lead
- **Dependency:** None (blocks all others)
- **Features:**
  - IA and navigation structure
  - Design system (colors, typography, components)
  - App shell (bottom nav, headers, FAB)
  - Responsive layout (mobile-first)
  - Accessibility (WCAG AA)
- **Milestones:**
  - Day 2: IA finalized, design system in Figma
  - Day 6: Icon library complete
  - Day 10: Shell built, QA sign-off
- **Success Criteria:**
  - Design review pass
  - Home load < 1s
  - All components accessible
  - 60fps interactions

#### Epic EP-02: Modelo de Dados e Motor de Logs (P0)
- **Duration:** 10 business days
- **Owner:** Backend Lead + Frontend Lead
- **Dependency:** EP-01 (non-critical, but design context helpful)
- **Features:**
  - Generic event entity schema
  - Persistence layer (JSON, SQLite, abstraction)
  - Local storage (localStorage/IndexedDB)
  - Quick log engine
  - CRUD operations
  - Seed data for demo
- **Milestones:**
  - Day 2: Schema approved
  - Day 5: Data layer implemented
  - Day 8: Quick log engine working
  - Day 12: QA sign-off
- **Success Criteria:**
  - Event create < 500ms
  - 100% data persistence
  - Timeline renders 30 events in < 2s
  - All CRUD operations tested

#### Epic EP-03: Home "Hoje" (P0)
- **Duration:** 10 business days
- **Owner:** Frontend Lead
- **Dependency:** EP-01, EP-02
- **Features:**
  - Hero card with daily summary
  - 6 tracker cards (Feeding, Hydration, Sleep, Awake, Diapers, Activities)
  - Daily timeline (chronological)
  - Inline quick logging
  - Empty states and loading states
- **Milestones:**
  - Day 3: Hero card complete
  - Day 5: 6 cards done
  - Day 7: Timeline functional
  - Day 10: Inline logging working
  - Day 12: QA sign-off
- **Success Criteria:**
  - Home load < 1s
  - Inline log < 500ms
  - All card metrics update after new log
  - Responsive on 320px-768px

#### Epic EP-04: Alimentação e Hidratação (P0)
- **Duration:** 10 business days
- **Owner:** Frontend Lead + Backend Lead
- **Dependency:** EP-02, EP-03
- **Features:**
  - Bottle feeding (type, quantity, time)
  - Breastfeeding (simple and advanced modes, timer, sides)
  - Solids/food (type, quantity, acceptance, first exposure)
  - Hydration (quick presets, liquid types, progress)
  - Daily totals and last-logged display
- **Milestones:**
  - Day 3: Bottle feeding complete
  - Day 6: Breastfeeding (basic + advanced) done
  - Day 8: Solids complete
  - Day 9: Hydration complete
  - Day 10: QA sign-off
- **Success Criteria:**
  - Feeding log < 500ms
  - Quick presets < 300ms
  - Timer persists across navigation
  - All data types save correctly

#### Epic EP-05: Sono e Tempo Acordado (P0)
- **Duration:** 10 business days
- **Owner:** Frontend Lead + Backend Lead
- **Dependency:** EP-02, EP-03
- **Features:**
  - Sleep start/end logging
  - Duration calculation
  - Awake window counter (real-time)
  - Daily sleep summary (naps + overnight)
  - Sleep editing capability
- **Milestones:**
  - Day 3: Sleep start/end done
  - Day 4: Duration calculation working
  - Day 6: Awake window counter done
  - Day 8: Daily summary working
  - Day 10: QA sign-off
- **Success Criteria:**
  - Sleep log < 500ms
  - Awake counter ±1 min accuracy
  - Cross-midnight sleeps handled correctly
  - Real-time counter no battery drain

#### Epic EP-06: Fraldas e Atividades (P0)
- **Duration:** 10 business days
- **Owner:** Frontend Lead + Backend Lead
- **Dependency:** EP-02, EP-03
- **Features:**
  - Diaper logging (wet, soiled, mixed)
  - Diaper quick presets
  - Activity logging (tummy time, reading, play, outdoor, bath)
  - Activity timer option
  - Activity and diaper summaries
  - Daily totals and last logged
- **Milestones:**
  - Day 2: Diaper types and presets done
  - Day 3: Diaper card working
  - Day 4: Activity logging done
  - Day 6: Activity timer working
  - Day 8: Summary cards done
  - Day 10: QA sign-off
- **Success Criteria:**
  - Diaper preset < 300ms
  - Activity log < 500ms
  - Activity timer persists across nav
  - All aggregations accurate

#### Epic EP-07: Cuidadores (P0)
- **Duration:** 10 business days
- **Owner:** Frontend Lead + Backend Lead
- **Dependency:** EP-01, EP-02, EP-03
- **Features:**
  - Caregiver entity and identity
  - First-run setup flow
  - Caregiver selector
  - Event attribution (all logs tagged with caregiver)
  - Shared feed in Caregivers tab
  - (P1) Filtering by caregiver
- **Milestones:**
  - Day 3: Setup flow and selector done
  - Day 5: Event attribution working
  - Day 7: Shared feed visible
  - Day 8: (Optional) Filter chips done
  - Day 10: QA sign-off
- **Success Criteria:**
  - Setup completes without errors
  - All events have correct caregiver attribution
  - Feed displays events from all caregivers
  - Caregiver switching instant and persistent

### Phase 1.5: Reporting & Insights (Week 6)

#### Epic EP-08: Relatórios e Insights (P0/P1)
- **Duration:** 10 business days
- **Owner:** Frontend Lead + Data Lead
- **Dependency:** EP-04, EP-05, EP-06, EP-07
- **Features:**
  - Daily summary KPIs on home (update hero card)
  - Contextual daily messaging
  - Week-over-week comparison
  - Weekly report view with charts
  - (P1) Automatic insights (pattern detection)
  - (P1) Highlights and opportunities
- **Milestones:**
  - Day 2: KPIs defined, calculations ready
  - Day 4: Daily summary calculated
  - Day 5: Weekly report design done
  - Day 7: Weekly metrics and comparisons ready
  - Day 9: (Optional P1) Insights generated
  - Day 10: QA sign-off
- **Success Criteria:**
  - KPI calculations 100% accurate
  - Daily summary updates instantly after log
  - Weekly report loads < 2s
  - Insight accuracy > 90%
  - Messaging warm and non-judgmental

---

## Post-MVP Backlog (Phase 2-3)

### Phase 2: Features & Content (Weeks 8-10)

#### Epic EP-09: Rotinas e Conteúdo (P1)
- **Duration:** 12 business days
- **Owner:** Content Lead + Frontend Lead
- **Dependency:** EP-01
- **Features:**
  - Content library (20+ articles by theme and age)
  - Rotinas tab with carousels
  - Large content cards
  - 3 guided routines (tummy time, reading, bedtime)
  - Step-by-step routine UI
  - (P2) External resource links
- **Milestones:**
  - Day 3: Content curated
  - Day 5: Rotinas tab built
  - Day 7: Offline content caching done
  - Day 9: 3 guided routines implemented
  - Day 10: (Optional P2) External links
  - Day 12: QA sign-off
- **Success Criteria:**
  - Carousel smooth 60fps
  - 20+ articles available
  - Guided routines engaging and complete
  - Offline content accessible without network

#### Epic EP-10: Meu Bebê e Crescimento (P1)
- **Duration:** 8 business days
- **Owner:** Frontend Lead + Data Lead
- **Dependency:** EP-01, EP-02
- **Features:**
  - Baby profile (name, age, caregivers, active modules)
  - Growth measurement form
  - Measurement history (chronological)
  - Growth charts (weight, height, head circumference)
  - Latest measurement highlight
  - (P2) Observations and milestones
- **Milestones:**
  - Day 2: Profile screen done
  - Day 3: Measurement form complete
  - Day 4: History list done
  - Day 6: Charts rendered
  - Day 7: Latest measurement card done
  - Day 8: QA sign-off
- **Success Criteria:**
  - Age calculation accurate
  - Charts render < 1s with 10+ measurements
  - Growth data persists across refresh
  - Responsive on mobile and tablet

#### Epic EP-11: Saúde, Vitaminas e Remédios (P1)
- **Duration:** 7 business days
- **Owner:** Frontend Lead + Data Lead
- **Dependency:** EP-02, EP-10
- **Features:**
  - Medication/supplement logging (dose, unit, time)
  - Medication presets (common vitamins)
  - Confirmation of administration
  - Medication history
  - (P2) Simple health events (temperature, symptom, consultation)
  - (P2) Health event history
- **Milestones:**
  - Day 2: Medication schema and form done
  - Day 3: Medication history done
  - Day 4: (Optional P2) Health event schema
  - Day 5: (Optional P2) Health event forms
  - Day 6: (Optional P2) Health event history
  - Day 7: QA sign-off
- **Success Criteria:**
  - Medication log < 500ms
  - Presets available and quick
  - Confirmation state persists
  - Health events displayed clearly (no medical recommendations)

---

## Backlog by Priority & Timeline

### P0 Epics (MVP Foundation — Must Have)
1. **EP-01** (Weeks 1-2): Fundação do Produto — Design system, shell, navigation
2. **EP-02** (Weeks 2-3): Modelo de Dados — Event entity, persistence, quick log engine
3. **EP-03** (Weeks 3-4): Home "Hoje" — Dashboard, hero card, timeline
4. **EP-04** (Weeks 4-5): Alimentação e Hidratação — Feeding (bottle, breast, solids), hydration
5. **EP-05** (Weeks 4-5): Sono e Tempo Acordado — Sleep logging, awake window
6. **EP-06** (Week 5): Fraldas e Atividades — Diaper and activity tracking
7. **EP-07** (Week 5-6): Cuidadores — Multi-caregiver support, shared feed
8. **EP-08** (Week 6): Relatórios e Insights — Daily summary, weekly report, insights

**MVP total: ~50 business days (10 weeks)**

### P1 Epics (Phase 2 — High Priority)
1. **EP-09** (Weeks 8-10): Rotinas e Conteúdo — Content library, guided routines
2. **EP-10** (Week 8): Meu Bebê e Crescimento — Baby profile, growth tracking
3. **EP-11** (Week 9): Saúde, Vitaminas e Remédios — Medication and health tracking

**Phase 2 total: ~27 business days (5-6 weeks)**

### P2 Epics (Phase 3 — Future)
- Health event tracking (EP-11.2)
- Guided routine filtering and bookmarking
- External resource links (EP-09.3)
- Observations and milestones (EP-10.3)
- And many more...

---

## Dependencies & Critical Path

### Critical Path to MVP
```
EP-01 (Design System)
  ↓
EP-02 (Data Model) ← [also depends on EP-01 context]
  ↓
├─ EP-03 (Home Dashboard)
│   ├─ Feeds EP-04, EP-05, EP-06, EP-07
│   └─ Feeds EP-08
├─ EP-04 (Feeding)
│   └─ Feeds EP-08
├─ EP-05 (Sleep)
│   └─ Feeds EP-08
├─ EP-06 (Diapers & Activities)
│   └─ Feeds EP-08
└─ EP-07 (Caregivers)
    └─ Feeds EP-08

EP-08 (Reports & Insights)
  Depends on all trackers (EP-04, EP-05, EP-06, EP-07)
  Final epic before MVP close
```

### Post-MVP Dependencies
```
EP-09, EP-10, EP-11
  Depend on EP-01, EP-02 (design and data foundations)
  Can be done in parallel after MVP
  EP-11 also has soft dependency on EP-10 (baby profile context)
```

---

## Sprint Planning Template

### MVP Sprint Structure (Recommended: 2-week sprints)

**Sprint 1 & 2 (Weeks 1-2):** Foundation
- EP-01 (Design & Shell): 80% complete
- EP-02 (Data Model): 50% complete
- **Deliverables:** Figma design file, app shell, basic data layer

**Sprint 2 & 3 (Weeks 3-4):** Home & Core Trackers Pt. 1
- EP-01: 100% complete
- EP-02: 100% complete
- EP-03 (Home): 100% complete
- EP-04 (Feeding): 50% complete
- **Deliverables:** Home dashboard with hero card, feeding tracker 50%

**Sprint 3 & 4 (Weeks 4-5):** Core Trackers Pt. 2
- EP-04 (Feeding): 100% complete
- EP-05 (Sleep): 100% complete
- EP-06 (Diapers & Activities): 100% complete
- **Deliverables:** All 6 trackers functional, timeline working

**Sprint 5 (Week 5-6):** Caregivers & Daily Summary
- EP-07 (Caregivers): 100% complete
- EP-08 (Reports): 50% complete (daily summary)
- **Deliverables:** Multi-caregiver support, shared feed, daily summary

**Sprint 6 (Week 6):** Insights & Testing
- EP-08 (Reports): 100% complete
- Beta testing, bug fixes, polish
- **Deliverables:** Weekly reports, insights, MVP ready for beta

### Post-MVP Sprint Structure

**Sprint 7 & 8 (Weeks 8-9):** Content & Profile
- EP-09 (Routines): 100% complete
- EP-10 (Baby Profile & Growth): 100% complete
- **Deliverables:** Content library, baby profile, growth tracking

**Sprint 9 (Week 9):** Health Tracking
- EP-11 (Health & Meds): 100% complete
- **Deliverables:** Medication logging, health events

---

## Feature Prioritization Matrix

### By Impact vs. Effort

| Epic | Impact | Effort | Ratio | Priority |
|------|--------|--------|-------|----------|
| EP-01 | Critical (blocks all) | High | N/A | P0 |
| EP-02 | Critical (enables tracking) | High | N/A | P0 |
| EP-03 | High (home engagement) | Medium | 3:1 | P0 |
| EP-04 | High (most important tracker) | High | 1:1 | P0 |
| EP-05 | High (sleep critical for parents) | High | 1:1 | P0 |
| EP-06 | Medium (quick wins) | Medium | 2:1 | P0 |
| EP-07 | High (core value: shared) | Medium | 2:1 | P0 |
| EP-08 | Medium-High (engagement) | Medium | 2:1 | P0/P1 |
| EP-09 | Medium (content value) | High | 1:2 | P1 |
| EP-10 | Medium (profile completeness) | Low-Medium | 2:1 | P1 |
| EP-11 | Medium (health ecosystem) | Low | 3:1 | P1 |

---

## Risk & Mitigation by Epic

| Epic | Risk | Mitigation |
|------|------|-----------|
| EP-01 | Design delays block everything | Start design in parallel; use UI kit template; agile iteration |
| EP-02 | Schema changes late | Lock schema early; get stakeholder buy-in; use versioning |
| EP-03 | Metrics calculation wrong | Unit test all logic; manual verification; stakeholder review |
| EP-04 | Timer doesn't persist | Use service worker + state management; test thoroughly |
| EP-05 | Cross-midnight sleeps fail | Unit tests with dates spanning midnight; handle timezone |
| EP-06 | Activity timer drains battery | Test battery impact; update only when in foreground |
| EP-07 | No auth confuses users | Clear onboarding; device pairing explanation; future upgrade path |
| EP-08 | Insights too pushy | Tone review by non-technical person; user testing |
| EP-09 | Content outdated | Pediatrician review; update schedule; user feedback loop |
| EP-10 | Charts slow with many measurements | Optimize queries; virtualization; test on low-end device |
| EP-11 | Users confuse with medical advice | Clear disclaimer; no recommendations; informational only |

---

## Metrics & Success Definition

### MVP Success Criteria
- 100+ active families in closed beta
- 10+ logs per family per day (average)
- 3+ caregivers per family minimum
- 7-day retention > 85%
- NPS > 50
- App rating > 4.5 stars
- < 5% critical bugs reported

### Phase 2 Success Criteria
- 500+ active families
- Content library engagement > 30% of users
- Growth tracking adoption > 60%
- User-generated feedback > 100 reviews/month
- NPS > 60

### Phase 3 Success Criteria
- 2000+ active families
- Health ecosystem ready for partnerships
- Pediatrician integration pilots in place
- Revenue model validated (freemium or premium)

---

## Technical Debt & Future Optimization

### Known Debt (To Address Post-MVP)
1. **State Management:** Switch from prop drilling to Context or Redux
2. **Testing:** Increase coverage to > 90%; add more E2E tests
3. **Performance:** Optimize timeline virtualization; chunk uploads
4. **Accessibility:** Full WCAG AAA audit; screen reader testing
5. **Offline-First:** Implement proper service worker strategies; conflict resolution for multi-device
6. **Real-time Sync:** Add cloud backend; conflict-free sync (CRDTs if needed)

### Scalability Considerations
- Database indexing on frequently queried fields (timestamp, type, caregiver)
- Caching strategy for reports and insights
- CDN for content/images
- API rate limiting and throttling
- Analytics pipeline for behavioral insights

---

## Go-To-Market & Launch Plan

### Closed Beta (Weeks 1-4, end of Sprint 2)
- **Audience:** 10-15 trusted families, friends of founders
- **Goal:** Validate MVP, gather feedback, squash major bugs
- **Cadence:** Daily check-ins, weekly feedback sessions
- **Deployment:** TestFlight (iOS) or Firebase App Distribution (Android)

### Soft Launch (Weeks 5-8, Sprints 3-4)
- **Audience:** 50-100 families via referral
- **Goal:** Test retention, identify missing features
- **Channels:** Parenting forums, Instagram, word-of-mouth
- **Deployment:** Beta tracks on Google Play and TestFlight

### Public Launch (Week 9+, Post-MVP)
- **Audience:** General public
- **Channels:** App stores, press release, parenting influencers, pediatrician outreach
- **Deployment:** Google Play and App Store production releases
- **Marketing:** Content marketing (blog), community building (Discord)

---

## Budget & Resource Allocation

### MVP Phase (50 business days)
- **Design:** 1 designer (part-time initially, full-time weeks 1-2)
- **Frontend:** 2 engineers
- **Backend:** 1 engineer
- **Product:** 1 product manager
- **QA:** 0.5 engineer (shift from dev as features land)
- **Estimated cost:** Depends on geography; ~$80-150k for MVP in US

### Phase 2 (27 business days)
- **Content:** 1 content creator/medical reviewer
- **Design:** 0.5 designer (refinement)
- **Frontend:** 2 engineers
- **Backend:** 1 engineer
- **Product:** 1 product manager
- **Estimated cost:** ~$40-60k

### Phase 3 (TBD)
- **Growth:** 1 marketing specialist
- **Partnerships:** Business dev (if integrations planned)
- **Estimated cost:** ~$30-50k/month ongoing

---

## Key Dates & Milestones

| Date | Milestone | Status |
|------|-----------|--------|
| Week 2, Day 10 | EP-01 & EP-02 Done | Pending |
| Week 4, Day 20 | Home & EP-03 Done; Feeders Pt. 1 | Pending |
| Week 5, Day 25 | All Core Trackers Done (EP-04-06) | Pending |
| Week 6, Day 30 | EP-07 & Daily Summary Done | Pending |
| Week 7, Day 35 | MVP Complete, Beta Ready | Pending |
| Week 8, Day 40 | Soft Launch (50-100 families) | Pending |
| Week 10, Day 50 | Phase 2 Done (Content, Growth, Health) | Pending |
| Week 12, Day 60 | Public Launch | Pending |

---

## Glossary

| Term | Definition |
|------|-----------|
| **MVP** | Minimum Viable Product; core features (8 epics, 6 trackers, shared feed) |
| **P0** | Highest priority; required for MVP |
| **P1** | High priority; post-MVP but soon |
| **P2** | Lower priority; future phases |
| **Closed Beta** | Limited release to trusted users for validation |
| **Soft Launch** | Limited release for early adopters and feedback |
| **Public Launch** | General availability on app stores |
| **Epic** | Large feature grouping; multiple stories and tasks |
| **Sprint** | 2-week development cycle |
| **NPS** | Net Promoter Score (customer satisfaction metric) |

---

## Document Control

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2026-04-04 | Product | Initial backlog and release plan |


## Integrações e assistentes (2026-11-11)

[EP-16/EP-17: features, user stories e sequência de entrega](INTEGRATIONS_PLAN.md).
